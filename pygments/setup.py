from distutils.core import setup

import os, sys
sys.path.remove(os.path.abspath(""))

try:
    import oranj.core.objects.about
except ImportError, e:
    print "oranj and pygments must be installed to install bpython/oranj"
    print "Aborting installation"
    exit()

oranjpath = oranj.core.objects.about.mainpath[:-5]
files = [(os.path.join(oranjpath, "support"), ["pygments.py"])]

setup(name="pygments/oranj",
      version="1.0",
      description="Oranj Programming Language Supporting Libraries for pygments",
      author="Pavel Panchekha",
      author_email="pavpanchekha@gmail.com",
      url="http://panchekha.no-ip.com:8080/pavpan/oranj/",
      data_files=files,
      requires=["oranj (>=0.5)", "pygments"],
      )
