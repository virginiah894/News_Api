from os import link
from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    link = models.URLField(max_length=120)
    creation_date = models.DateField()
    upvote = models.IntegerField(null=True)
    author_name = models.CharField(max_length=50)

    @property
    def count_comments(self):
        comments = self.comments.count()
        return comments

    @property
    def count_upvotes(self):
        upvotes= self.upvote.count()
        return upvotes


    def __str__(self):
        return self.title

    class Meta:
         ordering = ['-upvote']

   

class Comments(models.Model):
    creation_date = models.DateField()
    author_name = models.CharField(max_length=50)
    content = models.CharField(max_length=50,null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')

    def __str__(self):
        return self.content


class UpVote(models.Model):
    Post = models.ForeignKey(Post ,on_delete=models.CASCADE, related_name='upvotes')

    def save_vote(self):
        self.save()

    def unvote(self):
        self.delete()

