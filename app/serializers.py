from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from .models import Post, Comments, UpVote        

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'

class UpVoteSerializer(ModelSerializer):
    class Meta:
        model = UpVote
        fields = "__all__"

class PostSerializer(ModelSerializer):
    upvote = UpVoteSerializer(read_only=True, many=False),
    comments = CommentSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = '__all__'


        