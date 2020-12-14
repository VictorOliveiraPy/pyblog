from django.shortcuts import render

from Pyblog.core.models import Publish


def home(request):
    publish = Publish.objects.all()
    return render(request, 'index.html', {'publish': publish})