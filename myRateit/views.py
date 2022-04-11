from email import message
from multiprocessing import AuthenticationError
from urllib import response
from django.shortcuts import redirect, render
from .models import Project, Profile,Likes
from django.contrib.auth import login, authenticate
from django.http import JsonResponse, Http404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, ProjectForm, CommentForm, SignUpForm
from .serializer import ProjectSerializer, ProfileSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.


def first_page(request):
    
    return redirect('/accounts/login/')

# @login_required(login_url='/accounts/login/')
def home(request):
    projects = Project.objects.all()
    message ="Welcome to my RateIt"
    

    return render(request,'index.html',{'projects':projects, 'message': message})

@login_required(login_url='/accounts/login/')
def profile_update(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile= Profile.objects.filter(username=current_user)
            print(profile)
            if profile:
                print('profile exist')
                username = current_user
                useremail=form.cleaned_data['useremail']
               
                userage=form.cleaned_data['userage']
                profile_image=form.cleaned_data['profile_image']
                AuthenticationError=form.cleaned_data['AuthenticationError']
                Profile.objects.filter(username=current_user).update(useremail=useremail, userage=userage,profile_image=profile_image,AuthenticationError=AuthenticationError)
            else:
                print('profile does not exist')
                profile=form.save(commit=False)
                profile.username= current_user
                profile.save()

            message='saved successfuly'
            # profile_display(request)
            return redirect(profile_display)
    
            
    else:
        form = ProfileForm()
        
    return render(request, 'profiledisplay.html',{'form':form})
       
       
@login_required(login_url='/accounts/login/')
def profile_display(request):

    current_user = request.user
    profile= Profile.objects.filter(username=current_user)
   

    return render(request, 'profile.html',{'profile':profile})

@login_required(login_url='/accounts/login/')
def add_post(request):
   
    current_user = request.user
    print(current_user)
    print('passed')
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            
            landing_page=form.cleaned_data['landing_page']
            
            title=form.cleaned_data['title']
            description=form.cleaned_data['description']
            author = current_user
            link= form.cleaned_data['link']

            project=Project(landing_page=landing_page, title=title,description=description,author=author, link=link)
            print(project.author)
            # new_post=form.save(commit=False)
            # new_post.author=current_user
            project.save()
            print('post saved')
            return redirect(home)
           
                        
    else:
        form = ProjectForm()
        
    return render(request, 'add_post.html',{'form':form})

def add_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            new_comment=form.save(commit=False)
            # new_post.profile=current_user
            new_comment.save()
            print('comment saved')
            return redirect(home)
        
    else:
        form = CommentForm()
            
        return render(request, 'add_comment.html',{'form':form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

# def project_like(request, id):
#     likes = Likes.objects.filter(id=id).first()
#     # check if the user has already liked the image
#     if Likes.objects.filter(id=id).exists():
#         # unlike the image
#         likes.delete()
#         # reduce the number of likes by 1 for the image
#         project = Project.objects.get(id=id)
#         # check if the image like_count is equal to 0
#         if project.like_count == 0:
#             project.like_count = 0
#             project.save()
#         else:
#             like =project.like_count
#             like= like -1 
#             project.save()
#         return redirect('/')
#     else:
#         likes = Likes(id=id)
#         likes.save()
#         # increase the number of likes by 1 for the image
#         image = Project.objects.get(id=id)
#         likes=image.like_count 
#         likes = likes +1
#         likes.save()
#         image.save()
#         return redirect('/')

def project_details(request, pk):
    project = Project.objects.filter(id=pk)
    print(project)

    return render(request,'project_details.html', {'projects':project})

def rate_project(request):
    if request.method =='POST':
        project_id =request.POST.get('project_id')
        val =request.POST.get('val_num')
        obj =Project.objects.get(id= project_id)
        current_votes=obj.score
        adding= (current_votes + int(val))/2
        obj.score =adding
        obj.save()
        
        return JsonResponse({'success':'true', 'score':adding}, safe =False)
    return JsonResponse({'success':'false'})


class ProjectList(APIView):
    def get(self, request, format=None):
        all_projects = Project.objects.all()
        serializers = ProjectSerializer(all_projects, many=True)
        return Response(serializers.data)

class ProfileDescription(APIView):
    
    def get_profile(self, pk):
        try:
            return ProfileSerializer.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        profile = self.get_profile(pk)
        serializers = ProfileSerializer(profile)
        return Response(serializers.data)


def search_results(request):

    if 'search_term' in request.GET and request.GET["search_term"]:
        search_term = request.GET.get("search_term")
        try:
            searched_result = Project.search(search_term)
            message = f"Found searched project by title {search_term}"
        except Project.DoesNotExist:
             message="No project with that title please try a different title."
             return render(request, 'NotFound.html',{'message':message})


        return render(request, 'search.html',{'message':message,"search_result": searched_result})

    else:
        message = "You haven't searched for any category"
        return render(request, 'search.html',{"message":message})