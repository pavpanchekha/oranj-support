import oranj.core.interpreter as intp
from oranj.core.objects.function import Function

class Request(intp.OrObject):
    def __init__(self, environ):
        intp.OrObject.__init__(self, "req", Request)
        self.buffer = []
        self.environ = environ
        self.headers = {}

        self.set("$$getitem", self.__getitem__)
        self.set("$$setitem", self.__setitem__)
        self.set("$$delitem", self.__delitem__)
        self.set("$$output", self.write)
        self.set("write", Function(self.write))
        self.set("keys", Function(self.keys))
        self.set("GET", self.get_GET())

    def get_GET(self):
        import urlparse
        return intp.OrObject.from_py(urlparse.parse_qs(self.environ["QUERY_STRING"]))

    def __getitem__(self, key):
        if hasattr(key, "ispy") and key.ispy():
            key = key.topy()

        if key in self.headers:
            return self.headers[key]
        else:
            return self.environ[key]

    def __setitem__(self, key, value):
        if hasattr(key, "ispy") and key.ispy():
            key = key.topy()
        if hasattr(value, "ispy") and value.ispy():
            value = value.topy()

        if type(key) != type(""):
            raise TypeError("Cannot set non-string keys")

        self.headers[key] = value

    def __delitem__(self, key):
        if hasattr(key, "ispy") and key.ispy():
            key = key.topy()

        del self.headers[key]

    def keys(self):
        return list(self.headers.keys()) + list(self.environ.keys())

    def ispy(self): return False
    def topy(self): return NotImplemented
    
    def write(self, *strings):
        self.buffer += list(strings)
        return self

    def output(self):
        return "".join(map(str, self.buffer))
