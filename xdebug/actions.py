#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "xdebug-2.0.5"

def setup():
    shelltools.system("phpize")
    autotools.configure("--enable-xdebug")

def build():
    autotools.make()

def install():
    autotools.rawInstall("INSTALL_ROOT=%s" % get.installDIR())

    extension = shelltools.ls("%s/usr/lib/php/extensions/*/xdebug.so" % get.installDIR())[0]

    pisitools.dosed("xdebug.ini", "EXTENSION_PATH", extension.replace(get.installDIR(), ""))
    pisitools.insinto("/etc/php/ext", "xdebug.ini")

    pisitools.dodoc("CREDITS", "LICENSE", "README*", "NEWS")
