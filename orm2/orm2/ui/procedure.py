#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

##  This file is part of orm, The Object Relational Membrane Version 2.
##
##  Copyright 2002-2006 by Diedrich Vorberg <diedrich@tux4web.de>
##
##  All Rights Reserved
##
##  For more Information on orm see the README file.
##
##  This program is free software; you can redistribute it and/or modify
##  it under the terms of the GNU General Public License as published by
##  the Free Software Foundation; either version 2 of the License, or
##  (at your option) any later version.
##
##  This program is distributed in the hope that it will be useful,
##  but WITHOUT ANY WARRANTY; without even the implied warranty of
##  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##  GNU General Public License for more details.
##
##  You should have received a copy of the GNU General Public License
##  along with this program; if not, write to the Free Software
##  Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
##
##  I have added a copy of the GPL in the file gpl.txt.

class procedure:
    def __init__(self, context, formdata):
        self.__context__ = context
        self.__formdata__ = formdata
        
        for name, value in formdata.items():
            setattr(self, name, value)
        
    def __getattr__(self, name):
        """
        This will hook the procedure into Zope's acquisition mechanism.
        """
        return getattr(self.__context__, name)

# Local variables:
# mode: python
# ispell-local-dictionary: "english"
# End:

