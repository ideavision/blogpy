from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from datetime import datetime

#file validator
def validate_file_extentions(value):
    import os
    from django.core.exceptions import ValidationError

    ext = os.path.splitext(value.name)[1]
    valid_extentions = ['.jpg','.png']
    if not ext.lower() in valid_extentions:
        raise ValidationError('Unsupported file extention')


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.FileField(upload_to='files/user_avatar/', null = False, blank=False, validators=[validate_file_extentions])
    description = models.CharField(max_length=512, null= False, blank=False)

    def __str__(self):
        return self.user.username

class Article(models.Model):
    title = models.CharField(max_length=512, null=False, blank =False)
    cover = models.FileField(upload_to='files/article_cover/', validators=[validate_file_extentions])
    content = RichTextField()
    created_at = models.DateTimeField(default = datetime.now, blank=False)
    category = models.ForeignKey('category', on_delete=models.CASCADE)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.title

class Category(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False)
    cover =models.FileField(upload_to='files/category_cover/', null=False, blank= False, validators=[validate_file_extentions])
    
    def __str__(self):
        return self.title