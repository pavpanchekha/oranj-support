import os
import sys
import oranj.core.interpreter as intp
from execute import execfile

def Application(f):
    sys.path.append(os.path.dirname(f))
    return application

def application(environ, start_response):
    script = environ["PATH_INFO"][1:] # [1:] removes first slash
    os.chdir(os.path.dirname(__file__))
    sys.path.append(os.path.dirname(__file__))
    import __config

    req, status, output = execfile(script, environ, __config)

    response_headers = [("Content-type", req.headers.get("Content-type", "text/plain")),
                        ("Content-Length", str(len(output)))]

    for i in req.headers:
        if i != "Content-type":
            response_headers.append((i, req.headers[i]))

    start_response(status, response_headers)

    return [output]
