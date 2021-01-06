from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import CommentForm
from django.views.generic import ListView
from taggit.models import Tag

# Create your views here.


class PostListView(ListView):
    # paginate_by = 8
    template_name = "blog/post-list.html"

    def get_queryset(self):
        queryset = Post.objects.published()
        if bool(self.kwargs):
            tag = get_object_or_404(Tag, slug=self.kwargs['tag_slug'])
            queryset = queryset.filter(tags__in=[tag])
            print(self.kwargs)
        return queryset


class SearchPostList(ListView):
    template_name = "blog/post-list.html"

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q')
        if query is not None:
            return Post.objects.search(query)
        return Post.objects.published()


def post_detail(request, postID, post):
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             id=postID)

    comments = post.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            # return redirect('post_detail')
    else:
        comment_form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form
    }
    return render(request, "blog/post_detail.html", context)
