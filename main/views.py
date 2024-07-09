from django.shortcuts import render
from main import models
from main import forms
# Create your views here.
def index(request):
	about_site=''
	news=models.News.objects.all()
	return render(request,'index.html',{'about_site':about_site,'news':news})



def blogs(request):
	blogs=models.Blog.objects.all()
	return render(request,'blogs.html',{'blogs':blogs})
def blog(request,blog_id):
	blog=models.Blog.objects.get(id=blog_id)
	if request.method=="POST":
		form=forms.CommentForm(request.POST)
		if form.is_valid():
			comments=form.save(commit=False)
			comments.user=request.user
			comments.blog=blog
			comments.save()
	form=forms.CommentForm()
	comments=models.Comments.objects.filter(blog__id=blog_id)
	return render(request,'blog.html',{'blog':blog,'form':form,'comments':comments})
