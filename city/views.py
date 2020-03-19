from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def book_list(request):
    return HttpResponse("书籍列表！")


def book_detail(request,book_id):
    text = f"您输入的书籍的id是:{book_id}" 
    return HttpResponse(text)


def author_detail(request):
    author_id = request.GET['id']
    # text = '作者的id是：%s' % author_id
    text = f'作者的id是:{author_id}'
    return HttpResponse(text)



def publish_detail(request,pub_id):
    # pub_id = request.GET['id']
    # text = '作者的id是：%s' % author_id
    text = f'chuban的id是:{pub_id}'
    return HttpResponse(text)