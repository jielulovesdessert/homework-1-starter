# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 01:20:45 2018

@author: Jie Lu
"""

def test():
    utf8_text=open('task2/input.txt').read()
    unicode_data = utf8_text.strip().decode('utf8')
    assert len(unicode_data) == 6