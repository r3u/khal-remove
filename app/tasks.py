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
import time
from logger import logger

@celery.task(bind=True)
def process(self, filename):
    logger = self.get_logger()
    for n in range(10):
        progress = n / 10.0 * 100.0
        logger.info("Progress {0}".format(progress))
        self.update_state(state='PROGRESS', meta={'progress': progress})
        time.sleep(1)
    return "Dummy result for {0}".format(filename)

def state(id):
    # Note: res is 'PENDING' for jobs that don't exist
    res = AsyncResult(id)
    if res.state == 'PROGRESS':
        return {
            "state": "PROCESSING",
            "progress": res.info['progress']
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
