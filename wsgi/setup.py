#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

import os, sys
sys.path.remove(os.path.abspath(""))

try:
    import oranj.core.objects.about
except ImportError, e:
    print "Oranj must be installed to install Oranj-Support"
    print "Aborting installation"
    exit()

def rec_files(path):
    return [os.path.join(dirpath, f) for dirpath, dirs, files in os.walk(path) for f in files]

oranjpath = oranj.core.objects.about.mainpath[:-5]
files = [(os.path.join(oranjpath, "support/wsgi/"), rec_files("wsgi/"))]
files += [(os.path.join(oranjpath, "sitelib/wsgi/"), rec_files("or-wsgi/*"))]

setup(name="wsgi/oranj",
      version="0.5",
      description="Oranj Programming Language WSGI Interface",
      author="Pavel Panchekha",
      author_email="pavpanchekha@gmail.com",
      data_files=files,
        # Nastiest hack EVER!!! RUN IN FEAR!!!
      requires=["oranj (>=0.5)"],
      )
