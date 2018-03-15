bot-run:
	python main.py

periodic-run:
	celery worker -A bot.celery_conf --beat -l info --purge
