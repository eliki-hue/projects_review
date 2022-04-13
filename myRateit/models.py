
from wsgiref.validate import validator
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User 
from cloudinary.models import CloudinaryField
# Create your models here.

class Profile(models.Model):
    username = models.CharField(max_length=20)
    useremail = models.EmailField(max_length=30)
    userage = models.CharField(max_length=2)
    bio = models.CharField(max_length=100)
    profile_image = CloudinaryField('images', null=True)
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


class Project(models.Model):
    landing_page = CloudinaryField('images', null=True)
    title = models.CharField(max_length =60)
    description= models.CharField(max_length=1000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    votes = models.ManyToManyField(User,related_name='projects',default=0) 
    link= models.CharField(max_length=100, default='/')
    score= models.IntegerField(default=0)
    validators=[
        MaxValueValidator(10),
        MinValueValidator(1)

        ]
    

    def __str__(self):
        return self.title

    def save_project(self):
        self.save()

    def delete_project(self,project_reff):
        to_delete= Project.objects.filter(name=project_reff).delete()

    def total_likes(self):
        return self.likes.count()

    @classmethod
    def search(cls,title):
        items = cls.objects.get(title=title)
        return items


class Likes(models.Model):
    likes=models.ForeignKey(Project, related_name='like_count',null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.likes

    
class Comment(models.Model):
    project= models.ForeignKey(Project, related_name='comments', on_delete=models.CASCADE)
    comments =models.CharField(max_length=100, blank=True, default='great')
    author = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.project.title, self.author)

class Rate(models.Model):
    RATE_CHOICES =[[1,'1'],[2,'2'],[3,'3'],[4,'4'],[5,'5'],[6,'6'],[6,'6'],[7,'7'],[8,'8'],[9,'9'],[10,'10']]

    project= models.ForeignKey(Project, related_name='rating', on_delete=models.CASCADE)
    design = models.IntegerField(choices=RATE_CHOICES,default=0)
    usability = models.IntegerField(choices=RATE_CHOICES,default=0)
    content = models.IntegerField(choices=RATE_CHOICES,default=0)

    def __str__(self):
        return self.project