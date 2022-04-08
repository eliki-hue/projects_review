
from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class Profile(models.Model):
    username = models.CharField(max_length=20)
    useremail = models.EmailField(max_length=30)
    userage = models.CharField(max_length=2)
    bio = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to = 'images/')
    user_password = models.CharField(max_length=15)
    def __str__(self):
        return self.username

    def save_profile(self):
        self.save()

    def delete_profile(self,username):
        to_delete= Profile.objects.filter(username=username).delete()
    
    def update_profile(self,old_user,new_user):
        Profile.objects.filter(username=old_user).update(name=new_user)
        self.save()


class Image(models.Model):
    image = models.ImageField(upload_to = 'images/', null=True)
    image_name = models.CharField(max_length =60)
    image_caption= models.CharField(max_length=100)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    likes_count = models.IntegerField(default=0) 
    # comments = models.CharField(null=True, max_length=100)
    videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")

    def __str__(self):
        return self.image_name+ ":"+str(self.videofile)

    def save_image(self):
        self.save()

    def delete_image(self,image_reff):
        to_delete= Image.objects.filter(name=image_reff).delete()

    def total_likes(self):
        return self.likes.count()


class Likes(models.Model):
    likes=models.ForeignKey(Image, related_name='like_count',null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.likes

    
class Comment(models.Model):
    image= models.ForeignKey(Image, related_name='comments', on_delete=models.CASCADE)
    comments =models.CharField(max_length=100, blank=True, default='great')
    author = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.image.image_name, self.author)