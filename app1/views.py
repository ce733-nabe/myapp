from django.shortcuts import render
from django.http import HttpResponse
from .models import Touroku
from .forms import IdKensaku

def index(request):

    params = {
        'title':'生活データ',
        'msg':'all records',
        'form':IdKensaku(),
        'data':[],
    }

    if (request.method =='POST'):
        number = request.POST['id']
        item = Touroku.objects.get(id = number)
        params['data'] = [item]
        params['form'] = IdKensaku(request.POST)
    else:
        params['data'] = Touroku.objects.all()
    return render(request, 'kenko/index.html', params)