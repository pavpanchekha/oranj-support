def template(title, colorscheme, h1, footer=""):
    output = []

    output.append("""<!DOCTYPE html><html><head><title>%s</title>""" % title)
    output.append("""
<style type="text/css">

* {
   margin: 0;
   padding: 0;
}

html, body{
   height: 100%%%%;
}

#container {
   min-height: 100%%%%;
   height: auto !important;
   height: 100%%%%;
   margin: 0 auto -3em;
}

#footer, #push {
   text-align: center;
   height: 1.1em;
}

h1 {
   border-bottom: 5px solid #%(l-1)s;
   background: #%(l1)s;
   padding: 10px;
   font-weight: 900;
   margin-bottom: 5px;
   height: 1em;
}

h2 {
   color: #%(l-1)s;
   padding: 5px;
   margin: 5px 0;
   border-bottom: 5px solid #%(l-1)s;
}

p {
    margin: 5px;
}

pre {
    margin: 5px;
    padding: 5px;
    background: #%(l2)s;
}

.color {
    font-weight: bold;
}

ul {
   margin: 10px;
}

li {
   list-style-position: inside;
   list-style-type: square;
}

a {
   color: #%(l-1)s;
   text-decoration: none;
}

a:hover {
   text-decoration: underline;
}

#footer {
   border-top: 5px solid #%(l-1)s;
   background: #%(l1)s;
   padding: 10px;
   margin-top: 5px;
}

</style>
""" % {"l1": colorscheme[0], "l0": colorscheme[1], "l-1": colorscheme[2], "l2": colorscheme[3]})

    output.append("""</head><body>""")
    output.append("<div id='container'><h1>%s</h1>%%s<div id='push'></div></div>" % h1)

    if footer:
        output.append("<div id='footer'>%s</div>" % footer)
    
    output.append("</body></html>")
    return "\n".join(output)
