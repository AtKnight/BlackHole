#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 16:52:34 2018

@author: ed
"""

from Constants import *

class Stone:
    def __init__(self, color=EMPTY, value=0):
        self.color = color
        self.value = value
    
    def toString(self):
        return "(%s, %d)" % (COLOR_SHORT[self.color], self.value)
    
    def print(self):
        print(self.toString(), end='')
