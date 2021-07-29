import json

from django.db import models
from treebeard.ns_tree import NS_Node
from django.forms.models import model_to_dict


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статья'


class CommentQuerySet(models.query.QuerySet):
    def get(self, **kwargs):
        comment = super().get(**kwargs)
        comment['children'] = comment.get_children()
        return comment


class CommentManager(models.Manager.from_queryset(CommentQuerySet)):
    pass


class Comment(NS_Node):
    id = models.AutoField(primary_key=True)
    description = models.TextField(verbose_name='Описание')
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    parent_id = models.PositiveIntegerField(blank=True, db_index=True, null=True)
    tree_id = models.PositiveIntegerField(blank=True, db_index=True)
    lft = models.PositiveIntegerField(blank=True, db_index=True)
    rgt = models.PositiveIntegerField(blank=True, db_index=True)
    depth = models.PositiveIntegerField(blank=True, db_index=True)

    def __str__(self):
        return self.description

    def delete(self):
        self.description = 'Комментарий был удален'
        self.save()
        return self

    @property
    def children(self):
        result = []
        children = self.get_children()
        for item in children:
            result.append(model_to_dict(item))
        return result

    class Meta:
        verbose_name = 'Комментарий'
