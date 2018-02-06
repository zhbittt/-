#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys
BASEPATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(BASEPATH)

from core import SpiderMan
if __name__ == '__main__':
    s=SpiderMan.SpiderMan()
    s.async()