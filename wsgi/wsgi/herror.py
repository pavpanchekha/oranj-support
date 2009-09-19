import traceback
from oranj.core import libintp
import pagetemplate
import os

footer = ""

def handle500(e, intp):
    template = pagetemplate.template(type(e).__name__, ("EF2929", "CC0000", "A40000", "FF5656"), type(e).__name__ + ": " + str(e), footer)
    
    output = []
    output.append("""<h2>Traceback</h2>""")

    tb = libintp.str_exception(e, intp)
    tb = tb.replace("${RED}", "<span class='color'>")
    tb = tb.replace("${NORMAL}", "</span>")
    tb = tb.replace("\n", "<br />")
    output.append("<pre>" + tb + "</pre>")
    
    output.append("""<h2>Python Traceback</h2>""")
    output.append("""<div class="error"><pre>""" + traceback.format_exc(e) + """</pre></div>""")
    return template % "\n".join(output)

def handle404(path):
    template = pagetemplate.template("File not found", ("FCAF3E", "F57900", "CE5C00", "FFCB46"), "File not found: `" + path + "`", footer)
    return template % "<p>The page you are looking for could not be found. Perhaps you should <a href='./'> go to the directory index</a> and try again?</p>"

def handle403(path):
    template = pagetemplate.template("Forbidden", ("FCAF3E", "F57900", "CE5C00", "FFCB46"), "Forbidden: `" + path + "`", footer)
    return template % "<p>You are not allowed to access this page. Perhaps you should <a href='./'> go to the directory index</a> and try another?</p>"

def handle_index(path, forbidden=lambda x: False):
    template = pagetemplate.template("Directory Index", ("729FCF", "3456A4", "204A87", "94ACE3"), path[1:], footer)

    output = ["<ul>"]
    for i in os.listdir(path):
        if os.path.isdir(i):
            i += "/"

        if not forbidden(i):
            output.append("<li><a href='%s'>%s</a></li>" % (i, i))
    output.append("</ul>")

    return template % "\n".join(output)
