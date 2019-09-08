from django.shortcuts import render

# Create your views here.

# 基于函数或者基于类的视图
# 接受的参数第一个必须为request，并且需要返回一个response对象
from django.views import View


def login(request):
    return render(request, 'users/login.html')

class RegisterView(View):
    """
    /users/register/
    """
    def get(self, request):

        return render(request, 'users/register.html')