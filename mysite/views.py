import datetime

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

count = 0

user_list = [
    {'username':'雪之下雪乃','password':'5201314'},
    {'username':'雷格','password':'1314'},
    {'username':'堀北铃音','password':'520'},
]

def index(request):
    global count
    count += 1
    print(datetime.datetime.now(),'::第',count,'次有人访问了...')
    # return HttpResponse('hello!django!!!')
    if request.method == 'POST':
        if request.POST.get('username') is not '' and request.POST.get('password') is not '':
            user = {'username':request.POST.get('username'),'password':request.POST.get('password')}
            user_list.append(user)
    return render(request,'index.html',{'data':user_list})