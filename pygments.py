# -*- coding: utf-8 -*-

from __future__ import absolute_import

from pygments.lexer import RegexLexer, bygroups, using
from pygments.token import *
from pygments.lexers import PythonLexer
from pygments.lexers.web import XmlLexer

class OranjLexer(RegexLexer):
    """
    For `Oranj <http://github.com/pavpanchekha/oranj/tree/master>`_ source
    code

    *New in Pygments 1.1.*
    """
    
    name = "Oranj"
    aliases = ["oranj", "or"]
    filenames = ["*.or"]

    tokens = {
        "root": [
            (r"[a-zA-Z0-9\$_]+(?=\s*=\s*fn)", Name.Function),
            (r"[a-zA-Z0-9\$_]+(?=\s*=\s*class)", Name.Class),
            (r"\s+|;+", Text),
            (r"\b((is\s+not)|aint|mod|and|or|not|in|is)\b", Operator.Word),
            (r"[\./\+\-\*\|\^]", Operator),
            (r"(?<![<>])(\+|\-|\^|\/|\/\/|\*|<<|>>)\=(?![=<>])", Operator),
            (r"(?<![<>])\=(?![=<>])", Operator),
            (r">=|=>", Operator),
            (r"[><!]|==", Operator),
            (r"\b(true|false|nil|inf)\b", Keyword.Constant),
            (r"\b(self|block|runtime)\b", Keyword.Psuedo),
            (r"[\[\{\(\)\}\]\,]", Punctuation),
            (r"\b(catch|class|else|elif|finally|for|fn|yield|if|return|throw"
             r"|try|while|with|del|extern|import|break|continue|assert|as)\b",
             Keyword.Reserved),
            (r"(?<![\.eE]|\d)(?:(?:[ \t]*[0-9])+)(?![ \t]*\.|\d|\w)",
             Number.Integer),
            (r"(?<![\.eE]|\d)(?:0(?:\w))(?:(?:[ \t]*[0-9a-zA-Z])+)"
             r"(?![ \t]*\.|\d|\w)", Number.Integer),
            (r"(?P<number>(?:(?:[ \t]*[0-9])+\.(?:[ \t]*[0-9])+)|"
             r"(?:\.(?:[ \t]*[0-9])+)|(?:(?:[ \t]*[0-9])+\.))"
             r"(?P<exponent>(?:[eE][+-]?(?:[ \t]*[0-9])*)?)", Number.Float),
            (r"(?P<value>[a-zA-Z0-9\$_]+)", Name.Variable),
            (r"\`(?P<value>[a-zA-Z0-9\$_]+)", String.Symbol),

            (r"#!", Comment.Preproc, "procdir"),
            (r"#.*", Comment),

            (r"'''", String, "tsstring"),
            (r'"""', String, "tdstring"),
            (r"'", String, "sstring"),
            (r'"', String, "dstring"),
        ],

        "procdir": [
            (r"python\s*{", Comment.Preproc, "python"),
            (r"xml\s*{", Comment.Preproc, "xml"),
            (r"[a-zA-Z0-9]+(\s.*)?\n", Comment.Preproc, "#pop"),
            (r".*", Comment, "#pop"),
        ],

        "sstring": [
            (r"\\.", String.Escape),
            (r"'", String, "#pop"),
            (r'[^\\\']+', String),
            (r'[\\\']', String),
        ],

        "dstring": [
            (r"\\.", String.Escape),
            (r'"', String, "#pop"),
            (r'[^\\"]+', String),
            (r'[\\"]', String),
        ],

        "tsstring": [
            (r"\\.", String.Escape),
            (r"'''", String, "#pop"),
            (r"[^\\\']+", String),
            (r'[\\\']', String),
        ],

        "tdstring": [
            (r"\\.", String.Escape),
            (r'"""', String, "#pop"),
            (r"[^\\\"]+", String),
            (r'[\\\"]', String),
        ],

        "python": [
            (r"\s*#!\s*}", Comment.Preproc, "#pop"),
            (r"(?s).*?(?=\s*#!\s*})", using(PythonLexer)),
        ],

        "xml": [
            (r"\s*#!\s*}", Comment.Preproc, "#pop"),
            (r"(?s).*?(?=\s*#!\s*})", using(XmlLexer)),
        ],
    }
