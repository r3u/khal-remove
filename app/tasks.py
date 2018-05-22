import celery
from celery.result import AsyncResult
import sys
import time

@celery.task
def test():
    # XXX mock sleep
    time.sleep(30)
    return "Dummy result"

def state(id):
    # Note: res is 'PENDING' for jobs that don't exist
    res = AsyncResult(id)
    return res.state

def get(id):
    res = AsyncResult(id)
    if res.successful():
        return res.get()
    else:
        return None
