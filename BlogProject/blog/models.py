from django.contrib.auth.models import User
from django.db import models

# Create your models here.

# 帖子分类
class Category(models.Model):
    name = models.CharField('分类名', unique=True, max_length=20)
    slug = models.SlugField('URL标识', unique=True, max_length=50)
    
    class Meta:
        verbose_name = '分类'
        verbose_name_plural = '分类'
    def __str__(self):
        return self.name

# 博客帖子
class Post(models.Model):
    title = models.CharField('标题', max_length=50)
    slug = models.SlugField('URL标签', unique=True, 
        allow_unicode=True, max_length=50)
    summary = models.TextField('摘要', max_length=200)
    content = models.TextField('正文')
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name='分类',
        related_name='posts'
    )
    favorites = models.ManyToManyField(
        User,
        related_name='favorite_posts',
        verbose_name='收藏者',
        blank=True
    )
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('更新时间', auto_now=True)
    
    
    
    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'
        ordering = ['-created_at']  # noqa: RUF012
        
    def __str__(self):
        return self.title
        
    
    
    