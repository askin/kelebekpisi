#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import get
WorkDir = "."

def setup():
	pass

def bulid():
	pass

def install():
	pisitools.dobin("Kurtcuk.py")
	pisitools.rename("/usr/bin/Kurtcuk.py", "kurtcuk");
