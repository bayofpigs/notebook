"""
The Data Model and Backend
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


import logging


from .config import Config
from .compute_service import ComputeService

from .worksheet import Cell, Worksheet


class Model:
    
    def __init__(self, presenter):
        self.presenter = presenter
        c = Config()
        self.config = c
        self.compute = ComputeService(presenter)
        self.worksheet = None

    def get_rpc_clients(self):
        return [self.compute.rpc_client]

    def terminate(self):
        # save
        pass

    def get_sage_installation(self, sage_root):
        """
        Return data about the Sage installation at ``sage_root``
    
        INPUT:

        - ``sage_root`` -- a directory name or ``None`` (default). The 
          path will be searched if not specified.
        """
        from .sage_installation import SageInstallation
        return SageInstallation(sage_root)

    # Worksheet data model

    def get_cell(self, cell_id):
        return self.worksheet.get_cell(cell_id)
        
    def insert_cell_at(self, pos, template_cell=None):
        ws = self.worksheet
        if template_cell is None:
            cell = Cell()
        else:
            cell = template_cell.copy()
        ws.insert(pos, cell)
        
    def load_worksheet(self):
        self.worksheet = ws = Worksheet.create_default()
        return ws

    # Evaluation of cells

    def eval_cell_init(self, cell_id, input_string):
        """
        Prepare the cell for evaluation
        """
        cell = self.get_cell(cell_id)
        cell.input = input_string
        cell.index = None
        self.compute.eval(cell)
        return cell

    def eval_cell_update(self, cell):
        """
        We got partial output for ``cell``.
        """
        pass

    def eval_cell_finished(self, cell):
        """
        Evaluation finished
        """
        pass
