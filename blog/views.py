from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import ListView

# Create your views here.


class PostListView(ListView):
    queryset = Post.objects.published()
    # paginate_by = 8
    template_name = "blog/post-list.html"


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    context = {
        'post': post
    }
    return render(request, "blog/post_detail.html", context)
