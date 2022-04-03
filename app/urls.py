from posixpath import basename
from django.urls import include, re_path
from django.urls import URLPattern,path,include
from rest_framework.routers import DefaultRouter
from.views import  CommentViewset, PostViewSet
from . import views


router = DefaultRouter()
router.register('app', PostViewSet)

urlpatterns = [
    path('api/',include(router.urls)),
    path('',views.home,name ='home'),
    path('api/comments', views.CommentViewset.as_view()),
    path('comment/<int:pk>/', views.comment, name = 'comment'),
    path('new_posts/',views.new_posts,name ='new'),
    path('past_posts/',views.past_posts,name ='past'),
    path('update/',views.post_update,name='update'),
    path('delete/<int:pk>/',views.post_delete,name='delete'),



    






]