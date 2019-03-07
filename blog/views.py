from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog
from datetime import date

# Create your views here.

def home(request):
    blogs = Blog.objects    # 쿼리셋 # 메소드
    #print(type(blogs))
    return render(request,'blog.html',{'blogs' : blogs.order_by("id").reverse().all()[:3]})   # 객체를 역순으로 정렬하여 마지막 세개만 반환

def detail(request,blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)

    return render(request, 'detail.html', {'blog':blog_detail})

# new.html을 띄워주는 함수
def new(request):
    return render(request, 'new.html')

# 입력받은 내용을 DB에 insert
def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.id))    # 처리 후 blog+id 라는 url로 연결되도록

def allList(request):
    blogs = Blog.objects
    return render(request,'allList.html',{'blogs' : blogs.order_by("id").reverse()})    # 최신순(역순)으로 정렬

#def is_today(request, self):
#    print("checkkkkkkkkkkk")
#    print(date.today())
#    print(self.pub_date.date)
#    print(date.today()==self.pub_date.date)
#    return date.today()==self.pub_date.date