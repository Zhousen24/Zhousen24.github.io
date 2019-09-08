from django.shortcuts import render

# Create your views here.


# 基于函数或者基于类的视图
# 接受的参数第一个必须为request，并且需要返回一个response对象
def index(request):
    return render(request, 'news/index.html')