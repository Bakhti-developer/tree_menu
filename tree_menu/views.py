from django.shortcuts import render
from django.urls import resolve


def dynamic_view(request, path=None):
    try:
        match = resolve(request.path)
        view_name = match.view_name
    except:
        view_name = 'home'

    context = {
        'path': path,
        'view_name': view_name,
    }

    return render(request, 'base.html', context)
