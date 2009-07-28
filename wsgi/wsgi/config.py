# This file contains defaults for all configuration options
import re

def rewrites(*l):
    return [(re.compile(i[0]) if type(i[0]) == type("") else i[0], i[1]) for i in l]

DirectoryDefault = ["$$main.or", "index.html"]
DirectoryIndex = True
Footer = ""
Handler = ""

AccessDeniedGlob = ["*.wsgi", "__config.py", ".*", "*~", "*.pyc"]
AccessDeniedRE = []

Rewrites = []

ContentTypes = {
    "png": "image/png",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "gif": "image/gif",
    "tiff": "image/tiff",

    "ogg": "audio/ogg",
    "mp4": "audio/mp4",
    "vorbis": "audio/vorbis",

    "css": "text/css",
    "csv": "text/csv",
    "html": "text/html",
    "htm": "text/html",
    "xhtml": "application/xml+xhtml",
    "xml": "xml",

    "mpeg": "video/mpeg",
    "h264": "video/h264"
    }
