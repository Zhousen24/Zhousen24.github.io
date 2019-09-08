from django.shortcuts import render
from django.views import View
from django_redis import get_redis_connection
from utils.captcha.captcha import captcha
from django.http import HttpResponse
from . import constants

class ImageCodeView(View):
    '''图片验证码'''
    # 因为参数校验放在url中的正则中了，所以接受参数之后不需要序列化器校验；并且整个过程是返回图片，没有转换字典的过程，所以只需要继承View就可以了
    def get(self, request, image_code_id):      # 调用View的方法
        # 使用第三方的captcha工具来生成验证码图片
        text, image = captcha.generate_captcha()    # 生成文本和图片
        # 连接redis数据库
        redis_conn = get_redis_connection('verify_codes')
        # 保存真实值到redis；三个参数为key，有效期，value
        redis_conn.setex('img{}'.format(image_code_id), constants.IMAGE_CODE_REDIS_EXPIRES, text)

        return HttpResponse(image, content_type='image/jpg')






