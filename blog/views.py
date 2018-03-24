from math import ceil

from django.shortcuts import render,redirect

from .models import Post


# 文章分页
def post_list(request):
	total= Post.objects.count()
	pages = ceil(total/5)
	page = int(request.GET.get('page',1))
	start = (page - 1)*5

	end = start + 5
	posts = Post.objects.all()[start:end]
	return render(request,'post_list.html',{'posts':posts,'pages':range(1,pages+1)})



# 修改文章
def edit_post(request):
	if request.method == 'POST':
		post_id = int(request.GET.get('post_id'))
		title = request.POST.get('title')
		content = request.POST.get('content')
		post = Post.objects.get(id=post_id)
		post.title = title
		post.content = content
		post.save()
		return redirect('/post/read/?post_id=%s'% post.id)
	else:
		post_id = int(request.GET.get('post_id'))
		post = Post.objects.get(id=post_id)
	return render(request,'edit_post.html',{'post':post})




# 创建文章
def create_post(request):
	if request.method == 'POST':
		title = request.POST.get('title')
		content = request.POST.get('content')
		post = Post.objects.create(title=title,content=content)
		return redirect('/post/read/?post_id=%s'% post.id)
	return render(request,'create_post.html',{})

# 阅读文章
def read_post(request):
	post_id = int(request.GET.get('post_id'))
	post = Post.objects.get(id=post_id)
	return render(request,'read_post.html',{'post':post})