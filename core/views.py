from django.shortcuts import render


def index(request):
    # context = {'teste'}
    return render(request, 'index.html')


