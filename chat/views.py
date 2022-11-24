from django.http import JsonResponse
from django.shortcuts import render


def index(request):
    return render(request, "chat/index.html")


def room(request, room_name):
    user_name = request.GET.get('user_name')
    if user_name is None:
        return JsonResponse('user_name not defined', status=400)
    return render(request, "chat/room.html", {
        "room_name": room_name,
        "user_name": user_name,
    })
