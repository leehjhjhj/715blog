from django.shortcuts import get_object_or_404, render, redirect
from .models import Blog, Comment
from django.utils import timezone
from .forms import BlogForm
from django.core.paginator import Paginator

def home(request):
    blogs = Blog.objects.order_by('-pub_date')

    query = request.GET.get('query')
    if query:
        blogs = Blog.objects.filter(title__contains=query)

    paginator = Paginator(blogs, 5)
    page = request.GET.get('page')
    paginated_blogs = paginator.get_page(page)
    return render(request, 'home.html', {'blogs': paginated_blogs})

def detail(request,id):
    blog = get_object_or_404(Blog,pk=id)
    comments = Comment.objects.filter(post = id)
    if request.method == "POST":
        comment = Comment()
        comment.post = blog
        comment.body = request.POST['body']
        comment.date = timezone.now()
        if request.user.is_authenticated:
            comment.user = request.user
        comment.save()
    return render(request,'detail.html',{'blog':blog, 'comments':comments})

def delete(request, id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    return redirect('home')

def new(request):
    form = BlogForm()
    return render(request, 'new.html', {'form': form})

def create(request):
    form = BlogForm(request.POST, request.FILES) 
    if form.is_valid():
        new_blog = form.save(commit=False) 
        new_blog.pub_date = timezone.now()
        if request.user.is_authenticated:
            new_blog.user = request.user
        else:
            return redirect('blog:mustsign')
        new_blog.save()
        return redirect('blog:detail', new_blog.id)
    return redirect('home')

def mustsign(request):
    return render(request, 'mustsign.html')

def update(request, id):
    blog = get_object_or_404(Blog, pk = id)
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=blog) 
        if form.is_valid():
            blog = form.save(commit=False)
            blog.pub_date = timezone.now()
            blog.save()
            return redirect('blog:detail', blog.id)
        else:
            return redirect('home')
    else:
        form = BlogForm(instance=blog)
        return render(request, 'update.html', {'form': form})
