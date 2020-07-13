from django.http import HttpResponse
from django.shortcuts import render

# 表单
def search_form(request):
    return render(request, 'search_form.html')

# 接收请求数据
def search(request):
    request.encoding='utf-8'
    if '名称' in request.GET and request.GET['名称']:
        message = '你搜索的内容为: ' + request.GET['名称']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)

# 接收POST请求数据
def search_post(request):
    ctx ={}
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, "post.html", ctx)