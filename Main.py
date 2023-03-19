#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 19:23:24 2018

@author: ed
"""

from tkinter import *
from BordController import BordController

if __name__ == "__main__" :
    root = Tk()
    BordController(root, True)
    root.mainloop()  
