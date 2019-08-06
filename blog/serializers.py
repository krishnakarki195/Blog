from rest_framework import serializers
from blog.models import Blog, LANGUAGE_CHOICES, STYLE_CHOICES


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']