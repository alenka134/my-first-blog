from django.core.paginator import Paginator
from django.shortcuts import render
from django.utils import timezone
from .models import Post

POSTS_PER_PAGE = 3


def post_list(request):
    qs = Post.objects.filter(
        published_date__lte=timezone.now()
    ).order_by('-published_date')
    paginator = Paginator(qs, POSTS_PER_PAGE)
    page_obj = paginator.get_page(request.GET.get('page'))
    elided_page_range = list(
        paginator.get_elided_page_range(
            page_obj.number,
            on_each_side=1,
            on_ends=1,
        )
    )
    return render(
        request,
        'blog/post_list.html',
        {
            'page_obj': page_obj,
            'elided_page_range': elided_page_range,
        },
    )