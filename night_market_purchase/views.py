from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from bought.models import item

# Create your views here.
def index(request):
    list = item.objects.all()
    context ={
        'list': list,}
    return render(request, 'bought/index.html', context)

def detail(request,id):
    itm = get_object_or_404(item, pk = id)
    context = {'item' : itm}
    return render(request,'bought/detail.html', context)
