from django.contrib import admin

# Register your models here.
from .models import Post  # 导入我们刚刚创建的 Post 模型

admin.site.register(Post) # 把 Post 模型注册到 admin 后台