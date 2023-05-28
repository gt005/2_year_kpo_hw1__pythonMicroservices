import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'Order_handler_service.settings')

app = Celery('Order_handler_service')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

from celery.schedules import crontab

app.conf.beat_schedule = {
    'switch-next-order-status-every-10-seconds': {
        'task': 'api_app.tasks.switch_next_order_status',  # обратите внимание на путь к задаче
        'schedule': 30.0
    }
}

