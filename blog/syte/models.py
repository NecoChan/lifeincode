from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Создадим модель поста
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')
class Post(models.Model):
    STATUS_CHOICES=(
    ('draft', 'Draft'),
    ('published', 'Published'),
    )
    title = models.CharField('Заголовок',max_length=200)
    slug = models.SlugField('URL',max_length=200,unique_for_date='publish') # URL на наши публикации.
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    body = models.TextField('Текст')
    image = models.ImageField('Изображение',upload_to='products/%Y/%m/%d', blank=True)
    publish = models.DateTimeField("Дата публикации",default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField("Статус",max_length=50,choices=STATUS_CHOICES,default='draft')
    objects = models.Manager() # Менеджер по умолчанию.
    published = PublishedManager() # Наш новый менеджер.
    class Meta:
        ordering = ('-publish',)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[
        self.publish.year,self.publish.month, self.publish.day,
        self.slug])
# Комментарии
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField('Имя',max_length=80)
    email = models.EmailField()
    body = models.TextField('Сообщение')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    class Meta:
        ordering = ('created',)
    def __str__(self):
        return 'Коментарий от {} к {}'.format(self.name, self.post)
