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
    path('signup', views.signup, name='signup'),
    # path("like/<int:id>",views.project_like,name='project_like'),
    path("details/<int:pk>",views.project_details,name='project_details'),
    path('rate/', views.rate_project, name='rate_project' ),
    path('api/projects', views.ProjectList.as_view()),
    path('api/project/project-id/<int:pk>[0-9]+)', views.ProfileDescription.as_view()),
    path('search/', views.search_results, name='search_results'),
    path('rate/<int:pk>', views.rate, name='rate')
]