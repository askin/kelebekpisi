#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
	autotools.configure()

def bulid():
	autotools.make()

def install():
	autotools.install()
        pisitools.dosym("/usr/share/gtodo2/gtodo.png", "/usr/share/pixmaps/gtodo.png")
