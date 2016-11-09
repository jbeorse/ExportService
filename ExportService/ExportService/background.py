from ExportService import app
from flask_apscheduler import APScheduler
import requests

API_NAME = 'kf-api-key'
API_KEY = ''

def refresh_live_data():
    print('Refreshing')
    url = 'https://app.klipfolio.com/api/1.0/datasource-instances/359209a9c0611518784c7f26ba2a34e1/@/refresh'
    headers = { API_NAME : API_KEY }
    r = requests.post(url=url, headers=headers)
    print('Finished refresh: ' + r.text)

class Config(object):
    JOBS = [
        {
            'id': 'refresh_live_data',
            'func': refresh_live_data,
            'trigger': 'interval',
            'seconds': 5
        }
    ]

    SCHEDULER_VIEWS_ENABLED = True

app.config.from_object(Config())

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()