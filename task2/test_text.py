# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 01:20:45 2018

@author: Jie Lu
"""

import io

def test():
    text= io.open('task2/input.txt')
    char=text.read().strip()
    assert len(char)==6