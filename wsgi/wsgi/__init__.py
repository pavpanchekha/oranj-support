import os
import sys
import oranj.core.interpreter as intp
from execute import execfile

def Application(f):
    """
    To use, createa *.wsgi file containing:

    import oranj.support.wsgi
    application = oranj.support.wsgi.Application(__file__)
    
    """
    
    sys.path.append(os.path.dirname(f))
    return lambda e, s: application(e, s, path=os.path.dirname(f))

def application(environ, start_response, path=None):
    script = environ["PATH_INFO"][1:] # [1:] removes first slash
    
    if not path:
        path = os.path.dirname(__file__)
        sys.path.append(path)
    os.chdir(path)
    
    import __config

    req, status, output = execfile(script, environ, __config)

    response_headers = [("Content-type", req.headers.get("Content-type", "text/plain")),
                        ("Content-Length", str(len(output)))]

    for i in req.headers:
        if i != "Content-type":
            response_headers.append((i, req.headers[i]))

    start_response(status, response_headers)

    return [output]
