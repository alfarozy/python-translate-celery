from celery import Celery

def make_celery(app_name=__name__):
    return Celery(
        app_name,
        broker='pyamqp://guest@localhost//',  # Gunakan RabbitMQ sebagai broker
        backend='rpc://'  # Backend untuk mengambil hasil
    )

celery = make_celery()
