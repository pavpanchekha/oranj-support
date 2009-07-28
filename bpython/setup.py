from distutils.core import setup

import os, sys
sys.path.remove(os.path.abspath(""))

try:
    import oranj.core.objects.about
    import bpython
except ImportError, e:
    print "oranj and bpython must be installed to install bpython/oranj"
    print "Aborting installation"
    exit()

oranjpath = oranj.core.objects.about.mainpath[:-5]
files = [(os.path.join(oranjpath, "support"), ["ishell.py"])]

bpythonpath = os.path.join(bpython.__path__[0], "languages")
files.append((bpythonpath, ["oranj.py"]))

setup(name="bpython/oranj",
      version="1.0",
      description="Oranj Programming Language Supporting Libraries for bpython",
      author="Pavel Panchekha",
      author_email="pavpanchekha@gmail.com",
      url="http://panchekha.no-ip.com:8080/pavpan/oranj/",
      data_files=files,
      requires=["oranj (>=0.5)", "bpython"], #TODO: give version number
      )
