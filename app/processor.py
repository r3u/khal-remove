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
import argparse
import tempfile
from shutil import copyfile
import os.path

def process(in_file, work_dir, out_file):
    tmp_prefix = work_dir + os.path.sep

    with tempfile.TemporaryDirectory(prefix=tmp_prefix) as tmpdir:
        yield "Bitcrushing", 0.0
        tmp_file_1 = os.path.join(tmpdir, "tmp1.wav")
        tfm = sox.Transformer()
        tfm.gain(gain_db=-6.0, normalize=True)
        tfm.convert(bitdepth=8)
        tfm.build(in_file, tmp_file_1)
        tmp_file_2 = os.path.join(tmpdir, "tmp2.wav")
        tfm = sox.Transformer()
        tfm.gain(gain_db=-6.0, normalize=True)
        tfm.convert(bitdepth=16)
        tfm.build(tmp_file_1, tmp_file_2)

        yield "Reversing", 33.3
        tmp_file_3 = os.path.join(tmpdir, "tmp3.wav")
        tfm = sox.Transformer()
        tfm.reverse()
        tfm.build(tmp_file_2, tmp_file_3)

        yield "Normalizing", 66.6
        tfm = sox.Transformer()
        tfm.gain(gain_db=-1.0, normalize=True)
        tfm.build(tmp_file_3, out_file)
    yield "Finished", 100.0


# Standalone mode
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('in_file', help="File to process")
    parser.add_argument('out_file', help="Name of output file")
    parser.add_argument('--work_dir', help="Work directory (default: /tmp)")
    a = parser.parse_args()
    work_dir = a.work_dir if a.work_dir else "/tmp"
    for info, prgs in process(a.in_file, work_dir, a.out_file):
        print("Info={0}, Progress={1}".format(info, prgs))

