from Order_handler_service.celery import app  # импортируйте экземпляр Celery из celery.py

@app.task
def switch_next_order_status():
    from .models import Order  # убедитесь, что путь к модели Order верный
    Order.objects.filter(status='in_progress').update(status='done')
    Order.objects.filter(status='waiting').update(status='in_progress')