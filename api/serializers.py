from rest_framework import serializers

from api.models import *


class CommentSerializer(serializers.ModelSerializer):
    comments = serializers.ReadOnlyField(source='children')

    def create(self, validated_data):
        if 'parent_id' not in validated_data:
            comment = Comment.add_root(**validated_data)
            comment.save()
            return comment
        else:
            parent = Comment.objects.get(id=validated_data['parent_id'])
            child = Comment(**validated_data)
            parent.add_child(instance=child)
            return child

    class Meta:
        model = Comment
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = ['name', 'description', 'comments']
