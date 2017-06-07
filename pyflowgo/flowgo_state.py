# Copyright 2017 PyFLOWGO development team (Magdalena Oryaelle Chevrel and Jeremie Labroquere)
#
# This file is part of the PyFLOWGO library.
#
# The PyFLOWGO library is free software: you can redistribute it and/or modify
# it under the terms of the the GNU Lesser General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# The PyFLOWGO library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received copies of the GNU Lesser General Public License
# along with the PyFLOWGO library.  If not, see https://www.gnu.org/licenses/.

import math
import json

#
class FlowGoState:

    _crystal_fraction = 0.15
    _core_temperature = 1137 + 273.15
    _current_position = 0.
    _current_time = 0.
    _current_slope = 0.

    def get_core_temperature(self):
        return self._core_temperature

    def set_core_temperature(self, core_temperature):
        self._core_temperature = core_temperature

    def get_crystal_fraction(self):
        return self._crystal_fraction

    def set_crystal_fraction(self, crystal_fraction):
        self._crystal_fraction = crystal_fraction

    def get_current_position(self):
        return self._current_position

    def set_current_position(self, current_position):
        self._current_position = current_position

    def get_current_time(self):
        return self._current_time

    def set_current_time(self, current_time):
        self._current_time = current_time

    def read_initial_condition_from_json_file(self, filename):
        # read json parameters file
        with open(filename) as data_file:
            data = json.load(data_file)
            self._current_position = float(data['lava_state']['position'])
            self._current_time = float(data['lava_state']['time'])
