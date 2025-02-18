import random
import time

from django.shortcuts import render
from django.utils import timezone
from django.http import JsonResponse
from prometheus_client import Histogram

request_latency = Histogram(
    'django_request_latency_seconds',  # Название метрики
    'Latency of Django requests',  # Описание
    ['endpoint']  # Метрика будет раздельно считаться по эндпоинтам
)


def home(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    now = timezone.now()
    current_time = now.strftime("%d.%m.%Y %H:%M:%S")

    context = {
        'ip': ip,
        'current_time': current_time,
    }
    context = {'ip': ip, 'current_time': current_time}

    return render(request, 'web/index.html', context)


def slow_view(request):
    start_time = time.time()
    time.sleep(0.5)

    latency = time.time() - start_time
    request_latency.labels(endpoint='/slow').observe(latency)  # Сохраняем метрику

    return JsonResponse({
        "message": "OK",
        "latency": round(latency, 2)
    })


def usual_view(request):
    start_time = time.time()

    latency = time.time() - start_time
    request_latency.labels(endpoint='/usual').observe(latency)  # Сохраняем метрику

    return JsonResponse({
        "message": "OK",
        "latency": round(latency, 2)
    })


def random_view(request):
    start_time = time.time()
    time.sleep(round(random.uniform(0.1, 1.0), 1))  # случайное число от 0.1 до 1

    latency = time.time() - start_time
    request_latency.labels(endpoint='/random').observe(latency)  # Сохраняем метрику

    return JsonResponse({
        "message": "OK",
        "latency": round(latency, 2)
    })
