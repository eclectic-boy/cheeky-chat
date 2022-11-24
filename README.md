# Cheeky Chat :smirk:

Chat server based on Django (ASGI) using WebSocket and Channels.

Based on the tutorial https://channels.readthedocs.io/en/stable/tutorial/part_1.html.

## Quick Start

Make sure you have Python3 installed and Docker.

Clone the repo, change to the root of the project and create a Python 3 virtualenv:
```bash
python -m virtualenv .venv -p python3.11
```

Start your Redis Docker container:
```bash
docker run -p 6379:6379 -d redis:5
```

Start your Django server
```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000/ to access the chat, there you can decide the name of the room and your username. If you open multiple tabs pointing to the same URL and you use the same room name, then you'll be able to communicate with all those tabs where the messages will be shared.

## Notes

Django Async capabilities:

[How to deploy with ASGI | Django documentation](https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/)

[Asynchronous support | Django documentation](https://docs.djangoproject.com/en/4.1/topics/async/)

[Class-based views | Django documentation](https://docs.djangoproject.com/en/4.1/topics/class-based-views/#asynchronous-class-based-views)

Apparently Django Rest Framework does not support Async views yet, here is the PR: [Async implementation by em1208 · Pull Request #8617 · encode/django-rest-framework · GitHub](https://github.com/encode/django-rest-framework/pull/8617)

Apparently this package Channels is the one to be used in Django when dealing with websockets hence Async web features: [Django Channels](https://channels.readthedocs.io/en/stable/index.html)

And there is exactly a tutorial for implementing a chat: [Tutorial Part 1: Basic Setup — Channels 4.0.0 documentation](https://channels.readthedocs.io/en/stable/tutorial/part_1.html#)

