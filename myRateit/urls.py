from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('', views.home, name ='home'),
    path('my_profile', views.profile_display, name='profile_display'),
    path('update_profile', views.profile_update, name='profile_update'),
    path('my_post', views.add_post, name='my_post'),
    path('add_comment', views.add_comment, name='add_comment'),
    path('', views.signup, name='signup'),
    path("like/<int:id>",views.image_like,name='image_like')
    
]