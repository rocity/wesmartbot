from celery import Celery
from celery.task import periodic_task
from datetime import timedelta
from decouple import config

from .bot import execute_master_plan

app = Celery('wesmart',
             broker=config('BROKER_URL'),
             backend=config('BROKER_URL'))

@periodic_task(run_every=timedelta(seconds=30))
def run_bot(*args):
    execute_master_plan()

if __name__ == '__main__':
    app.start()
