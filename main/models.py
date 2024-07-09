from django.db import models
from django.contrib.auth.models import User
 # Create your models here.
class News(models.Model):
    title= models.CharField('Заголовок', max_length=255)
    text= models.TextField('Текст')
    create_date= models.DateField('Дата')
    source=models.CharField('Источник', max_length=255, null=True, blank=True)
    def __str__(self):
        return self.title


class Blog(models.Model):
    title= models.CharField('Заголовок', max_length=255)
    text= models.TextField('Текст')
    create_date= models.DateField('Дата')
    image=models.ImageField('Картинка',upload_to='blog',null=True,  blank=True )
    def __str__(self):
        return self.title

class Comments(models.Model):
    blog = models.ForeignKey(Blog, verbose_name='Блог', on_delete=models.CASCADE)
    text = models.TextField('Текст коментария')
    user = models.ForeignKey(User, verbose_name='Автор',on_delete=models.CASCADE )
    create_date_comment= models.DateField('Дата', auto_now=True)
    def __str__(self):
        return self.user.username
