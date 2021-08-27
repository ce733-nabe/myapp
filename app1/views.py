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
    return render(request, 'app1/index.html', params)
'''
def index(request):

    params = {
        'title':'生活データ',
        'msg':'all records',
        'form':KenkoForm(),
        'data':[],
    }

    if (request.method =='POST'):
        nametxt = request.POST['name']
        item = Touroku.objects.get(name = nametxt)
        params['data'] = [item]
        params['form'] = KenkoForm(request.POST)
    else:
        params['data'] = Touroku.objects.values("id","name")#ここ
    return render(request, 'kenko/index.html', params)
'''