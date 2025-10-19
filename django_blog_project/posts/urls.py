from django.urls import path
from . import views  # 从当前文件夹导入 views.py

urlpatterns = [
    path('', views.post_list_view, name='post_list'),
]