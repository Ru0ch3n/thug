#!/usr/bin/env python
#
# MimeType.py
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA  02111-1307  USA


from .JSClass import JSClass


class MimeType(JSClass):
    def __init__(self, init = None):
        self._mimetype = dict()

        if init is None:
            return

        for k, v in init.items():
            self._mimetype[k] = v

    def __setitem__(self, key, value):
        self._mimetype[key] = value

    def __getitem__(self, name):
        return self._mimetype.get(name, None)

    def __delitem__(self, name):
        if name not in self._mimetype:
            return

        del self._mimetype[name]
