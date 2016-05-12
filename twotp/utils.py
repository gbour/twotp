# -*- test-case-name: twotp.test.test_term -*-
# Copyright (c) 2007-2009 Thomas Herve <therve@free.fr>.
# See LICENSE for details.
#
# -*- coding: utf8 -*-

from twotp.term import *

"""
Define useful functions
"""

def to_python(Term):
    """
        - Atom() converted to string
        - Binary() converted to string
    """
    if hasattr(Term, 'to_python'):
        return Term.to_python()
    elif hasattr(Term, 'iteritems'):
        return dict([(to_python(k), to_python(v)) for (k,v) in Term.iteritems()])
    elif hasattr(Term, '__getitem__'):
        return [to_python(elt) for elt in Term]
    
    return Term

