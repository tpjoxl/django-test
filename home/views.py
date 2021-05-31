#home.views
from django.shortcuts import render,HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import messages
from datetime import datetime
from .models import Post,setting
import json




# Create your views here.
#render(request, template_name:要使用的 template, dictionary:包含要新增至 template 的變數)
def homepage(request):
    postlist=Post.objects.all()
    return render(request, 'home.html',{'postlist': postlist,})

def hello(request):
    return render(request, 'hello.html', {'current_time': str(datetime.now()),})

def gettopic(request):
    #status = list(setting.objects.all())


    k=setting.objects.count()
    print(k)
    data=[]
    for i in range(1,k+100):
        data += setting.objects.filter(pk=i).values()
        status= list(data)
    status = json.dumps(status)
    with open('topic/topic.json', 'w', encoding="UTF-8") as file:
        file.write(status)


        messages.success(request, "下載已完成")
        return HttpResponseRedirect("/admin/home/setting")







    
    
    
    

    
    


