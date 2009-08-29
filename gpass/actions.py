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
	shelltools.export("LDFLAGS", "-export-dynamic")
	autotools.configure()
def bulid():
	shelltools.export("LDFLAGS", "-export-dynamic")
	autotools.make()

def install():
	shelltools.export("LDFLAGS", "-export-dynamic")
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())
	pisitools.dodoc("AUTHORS", "INSTALL*", "NEWS", "README*")
