"""
Base Class for Windows
"""


##############################################################################
#  Sage Notebook: A Graphical User Interface for Sage
#  Copyright (C) 2013  Volker Braun <vbraun.name@gmail.com>
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
##############################################################################




class WindowABC(object):

    def __init__(self, object_id):
        """
        INPUT:
        
        - ``object_id`` -- anything that identifies the window
        """
        self._object_id = object_id

    def get_geometry(self):
        """
        Return the window geometry as a dictionary

        OUTPUT:

        A JSON-serializable dictionary. Usually contains width/height
        and so on. Must be valid input for :meth:`restore_geometry`.
        """
        return {}
        
    def restore_geometry(self, geometry_dict={}):
        """
        Set the window to previously-stored size.
        """
        pass

    def show(self):
        """
        Show the window. 

        If the window is already visible, nothing is done.
        """
        raise NotImplementedError

    def present(self):
        """
        Bring to the user's attention
        
        Implies :meth:`show`. If the window is already visible, this 
        method will deiconify / bring it to the foreground as necessary.
        """
        self.show()

    def hide(self):
        raise NotImplementedError

    def destroy(self):
        raise NotImplementedError





class ModalDialogABC(WindowABC):

    def __init__(self, parent_window, object_id):
        """
        INPUT:
        
         - ``parent_window`` -- A :class:`Window` instance. The dialog
          is displayed on top of its parent.

        - ``object_id`` -- anything that identifies the window
        """
        super().__init__(object_id)

    
