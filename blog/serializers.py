from rest_framework import serializers
from django.contrib.auth.models import User
from blog.models import Blog, LANGUAGE_CHOICES, STYLE_CHOICES


class BlogSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='blog-highlight', format='html')

    class Meta:
        model = Blog
        fields = ['url', 'id', 'highlight', 'owner', 'title', 'code', 'linenos', 'language', 'style']


class UserSerializer(serializers.ModelSerializer):
    blog = serializers.HyperlinkedRelatedField(many=True, view_name='blog-detail', read_only=True)

    class Meta:
        model = User
        fields = ['Url', 'id', 'username', 'blog']