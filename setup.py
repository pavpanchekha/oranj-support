#!/usr/bin/env python
# -*- coding: utf-8 -*-

# NOTE: Because distutils is annoying, the bpython support is in oranj.py

from distutils.core import setup

import os, sys
sys.path.remove(os.path.abspath(""))

try:
    import oranj.core.objects.about
except ImportError, e:
    print "Oranj must be installed to install Oranj-Support"
    print "Aborting installation"
    exit()

oranjpath = oranj.core.objects.about.mainpath[:-5]
files = [(os.path.join(oranjpath, "support"), ["pygments.py", "ishell.py"])]

try:
    import bpython
except ImportError, e:
    print "Not installing bpython support libs"
else:
    bpythonpath = os.path.join(bpython.__path__[0], "languages")
    files.append((bpythonpath, ["oranj.py"]))

setup(name="Oranj-Support",
      version="1.0",
      description="Oranj Programming Language Supporting Libraries",
      author="Pavel Panchekha",
      author_email="pavpanchekha@gmail.com",
      url="http://panchekha.no-ip.com:8080/pavpan/oranj/",
      data_files=files,
        # Nastiest hack EVER!!! RUN IN FEAR!!!
      requires=["oranj (>=0.5)"],
      )
