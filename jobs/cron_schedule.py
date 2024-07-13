from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .job import schedule_fetch

def start():
	scheduler = BackgroundScheduler()
	scheduler.add_job(schedule_fetch, 'interval', minutes=360)
	scheduler.start()
