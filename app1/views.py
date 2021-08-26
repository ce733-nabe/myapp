from django.shortcuts import render
from django.http import HttpResponse
from .forms import AisatsuForm
from django.views.generic import TemplateView

class AisatsuView(TemplateView):

    def __init__(self):
        self.params = {
            'title':'Hello World',
            'msg':'ちゃんと挨拶したいので情報の登録をしてください:',
            'checkresult':"未設定",
            'form':AisatsuForm(),
        }

    def get(self,request):
        return render(request,'app1/index.html',self.params)

    def post(self,request):
        print(request.POST["check"])
        if request.POST["check"] == 'true':
            self.params['checkresult']='何かがOK'
        if request.POST["check"] == 'false':
            self.params['checkresult']='何かがNG'

        flag = self.params['checkresult']

        items = request.POST.getlist('choice')
        print(items)
        #itemlist = []
        #for item in items:
        #    itemlist.append(item)

        msg = 'こんにちは!'+request.POST['name']+'さん!<br>'\
            +request.POST['area']+'にお住まいで<br>年齢は'+request.POST['age']\
            +'歳なんですね!<br>今後の連絡先は'+request.POST['mail']\
            +'ですね<br>よろしくお願いします。<br>URL:'+request.POST['url']\
            +'<br>'+ request.POST['date'] + '<br>'+flag\
            +'<br>満足度:'+ items[0]
        self.params["msg"] = msg
        self.params['form'] = AisatsuForm(request.POST)
        return render(request,'app1/index.html',self.params)