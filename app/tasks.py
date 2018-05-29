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

import celery
from celery.result import AsyncResult
import sys
from logger import logger
import processor

@celery.task(bind=True)
def process(self, in_path, out_path, filename):
    logger = self.get_logger()
    for info, progress in processor.process(in_path, out_path, filename):
        self.update_state(state='PROGRESS', meta={
            'info': info,
            'progress': progress
        })
    return filename

def state(id):
    # Note: res is 'PENDING' for jobs that don't exist
    res = AsyncResult(id)
    if res.state == 'PROGRESS':
        return {
            "state": "PROCESSING",
            "progress": res.info['progress'],
            "info": res.info['info']
        }
    else:
        return {
            "state": res.state
        }

def get(id):
    res = AsyncResult(id)
    if res.successful():
        return res.get()
    else:
        return None
