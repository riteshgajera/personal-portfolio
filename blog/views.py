from django.shortcuts import render, get_object_or_404
from .models import Blog


def blogs(request):
    return render(request, 'blog/blogs.html', {'blogs': Blog.objects.order_by('-date')[:5] })


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})
