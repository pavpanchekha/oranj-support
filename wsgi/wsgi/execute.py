import os
import sys
import oranj.core.interpreter as intp
from request import Request
import herror

def forbidden(path, config):
    import fnmatch
    path = os.path.normpath(path)
    if path == ".":
        return False
    
    for i in config.AccessDeniedGlob:
        if fnmatch.fnmatch(path, i):
            return True
    for i in config.AccessDeniedRE:
        if i.match(path):
            return True
    return False

def rewrittenpath(path, config):
    for pattern, url in config.Rewrites:
        m = pattern.match(path)
        if m:
            return pattern.sub(url, path), list(m.groups()), m.groupdict()
    return path

def execfile(path, environ, config, rewrites=[]):
    environ["FilePath"] = path
    environ["Args"] = [] if not "Args" in environ else environ["Args"]
    
    if config.Handler and path != config.Handler:
        if os.path.isfile(config.Handler):
            return execfile(config.Handler, environ, config, rewrites)
        else:
            #TODO: Import module
            pass
    
    fname = os.path.split(path)[1]
    if "." in fname:
        ext = fname[fname.rfind(".")+1:]
    else:
        ext = ""

    if config.Rewrites and path not in rewrites and not config.Handler:
        newpath, environ["Args"], kwargs = rewrittenpath(path, config)
        environ.update(kwargs)
        return execfile(newpath, environ, config, rewrites=rewrites+[newpath])

    path = "./" + path
    
    if forbidden(path, config):
        req = Request(environ)
        req["Content-type"] = "text/html"
        return req, "403 Forbidden", herror.handle403(path)

    herror.footer = config.Footer
    if ext == "or" or ext == "" and os.path.isfile(path):
        return exec_or(path, environ)
    elif os.path.isdir(path):
        if not environ["REQUEST_URI"].endswith("/"):
            req = Request(environ)
            req["Location"] = req["REQUEST_URI"] + "/"
            return req, "301 Moved Permanently", ""

        for i in config.DirectoryDefault:
            if os.path.isfile(os.path.join(path, i)):
                return execfile(os.path.join(path, i), environ, config, rewrites)
        else:
            if config.DirectoryDefault:
                req = Request(environ)
                req["Content-type"] = "text/html"
                return req, "200 OK", herror.handle_index(path, lambda p: forbidden(p, config))
    elif os.path.isfile(path):
        req = Request(environ)
        if ext in config.ContentTypes:
            req["Content-type"] = config.ContentTypes[ext]
        return req, "200 OK", open(path).read()

    req = Request(environ)
    req["Content-type"] = "text/html"
    return req, "404 File Not Found", herror.handle404(path)
        
def exec_or(path, environ):
    environ["FilePath"] = path
    req = Request(environ)
    base_i = intp.Interpreter()
    base_i.curr["req"] = req
    base_i.curr["io"].register("http-stream", req)
    
    try:
        intp.run(open(path).read(), base_i)
        if "$$main" in base_i.curr:
            main = base_i.curr["$$main"]
            passargs = intp.OrObject.from_py([])
            main(passargs)
    except Exception, e:
        req["Content-type"] = "text/html"
        return req, "500 Internal Server Error", herror.handle500(e, base_i)
    else:
        return req, "200 OK", req.output()
