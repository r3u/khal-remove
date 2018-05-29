# KHAL | REMOVE | 2.0
# Copyright (C) 2018  Rachael Melanson
# Copyright (C) 2018  Henry Rodrick
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import sox
import time
from shutil import copyfile
import os.path

def process(in_path, out_path, filename):
    yield "Step 1", 0.0
    time.sleep(2)
    yield "Step 2", 25.0
    time.sleep(2)
    yield "Step 3", 50.0
    time.sleep(2)
    yield "Step 4", 75.0
    time.sleep(2)
    copyfile(os.path.join(in_path, filename),
             os.path.join(out_path, filename))
    yield "Finished", 100.0


# Standalone mode
if __name__ == '__main__':
    pass
