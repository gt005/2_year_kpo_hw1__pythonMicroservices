# apps.py
from django.apps import AppConfig


class ApiAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api_app'


# class RunAsyncTasks(AppConfig):
#     name = 'api_app'
#
#     def ready(self):
#         from .async_tasks.order_status_switcher_task import switch_next_order_status
#         switch_next_order_status.apply_async(countdown=10)
