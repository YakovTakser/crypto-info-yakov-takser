web: gunicorn cryptoCoins.wsgi --log-file -
worker: celery -A cryptoCoins worker -l info --without-gossip --without-mingle --without-heartbeat -Ofair --pool=solo
beat: celery -A cryptoCoins beat