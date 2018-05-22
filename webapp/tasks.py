import celery
import sys

@celery.task
def test():
    return sys.version
