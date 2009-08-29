#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools

def setup():
	pass

def bulid():
	pass

def install():
    pythonmodules.install()
    pisitools.dodoc("README", "AUTHORS", "CHANGELOG", "LICENSE")
