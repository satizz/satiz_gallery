from django.shortcuts import render, loader, RequestContext
from django.http import HttpResponse
from bought.models import item

# Create your views here.
def index(request):
    list = item.objects.all()
    context ={
        'list': list,}
    return render(request, 'bought/index.html', context)