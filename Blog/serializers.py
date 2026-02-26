from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=Blog
        field=['id','title','content','created_at','updated_at']
        read_fields=['created_at', 'updated_at']