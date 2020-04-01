from django.urls import path
from . import views

urlpatterns = [
    path('',views.registration),
    path('home',views.home),
    path('forum', views.forum),
    path('comment/<int:id>',views.comment),
    path('like_message/<int:id>', views.like_message),
    path('like_comment/<int:id>', views.like_comment),
    path('videos', views.videos),

]
