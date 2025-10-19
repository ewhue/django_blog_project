from django.shortcuts import render
from .models import Post  # 导入我们的 Post 模型

def post_list_view(request):
    # 1. 从数据库中获取所有 Post 对象
    posts = Post.objects.all().order_by('-created_at') # 按创建时间倒序排列

    # 2. 定义一个 "上下文" 字典，用来传递数据给模板
    context = {
        'post_list': posts,
    }

    # 3. 渲染模板，并把上下文传递进去
    #    我们马上就会创建这个 post_list.html 文件
    return render(request, 'posts/post_list.html', context)
# Create your views here.
