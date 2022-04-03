import datetime
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from rest_framework.viewsets import ModelViewSet
from rest_framework import status, serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from .forms import CommentForm, PostForm

from .models import Comments, Post, UpVote
from .serializers import PostSerializer, CommentSerializer,UpVoteSerializer
# Create your views here.

from rest_framework.permissions import SAFE_METHODS, BasePermission

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return request.user.is_staff


class PostViewSet(ModelViewSet):
    permission_classes = (IsAdminOrReadOnly,)

    serializer_class = PostSerializer
    queryset = Post.objects.all()
    def get_post(self, pk):
        try:
            return PostSerializer.objects.get(pk=pk)
        except PostSerializer.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        posts= Post.objects.all()
        posts = self.get_post(pk)
        serializers = PostSerializer(posts,many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = PostSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)



class CommentViewset(APIView):
    def get(self, request, format=None):
        comments = Comments.objects.all()
        serializers = CommentSerializer(comments, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = CommentSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
def home(request):
    posts = Post.objects.all()
    comments = Comments.objects.all()
    return render(request, 'index.html',locals())
def like(request, post_id):
    posts= Post.objects.get(id = post_id, user=request.user).first()
    print(upvoted)
    if upvoted:
        upvoted.delete()
        return redirect('home')
    else:
        new_like = UpVote(post = posts)
        likes = new_like.save_like()

        return redirect('home')


def is_liked(request):
    id = request.user.id
    liked_posts = UpVote.objects.filter(post_id=id)
    mylist = [i.post_id for i in liked_posts]
    print(mylist)
    return HttpResponse(liked_posts)

def comment(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(id=pk)
        form = CommentForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CommentForm()

    title = 'Comment'
    return render(request, 'comment.html', locals())
def new_posts(request):
    posts = Post.objects.all().filter(creation_date=datetime.date.today())
    comments = Comments.objects.all().filter(creation_date=datetime.date.today())
    return render(request, 'new.html',locals())

def past_posts(request):
    posts = Post.objects.all().exclude(creation_date=datetime.date.today())
    comments = Comments.objects.all().exclude(creation_date=datetime.date.today())

    return render(request, 'past.html',locals())


def post_update(request):
    if request.method =='POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form .save()
            return redirect('home')
        
         
    else:
        form = PostForm()
    return render(request,'post_form.html',locals())

def post_delete(request,pk):
    post = Post.objects.get(id=pk)
    if request.method=='POST':
        post.delete()
        return redirect('home')
    
    return render(request,'delete.html',locals())
