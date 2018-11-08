# -*- coding: utf-8 -*-
"""
a module for demonstrating exceptions
Created on Mon Jul 30 14:23:35 2018

@author: bhagu
"""

from math import log

def convert(s):
    '''Convert to an Integer. '''
    x = -1
    try:
        x = int(s)
        print('Conversion was Successful!')
    except (ValueError, TypeError):
        print('Conversion Failed!')
    return x


def string_log(s):
    v = convert(s)
    return log(v)


