from django.urls import path, include
from .views import (
    PostListApiView,
    GetPostListView
)

urlpatterns = [
    path('new', PostListApiView.as_view()),
    path('get', GetPostListView.as_view(), name='get'),

]