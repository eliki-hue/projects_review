from email import message
from django.shortcuts import redirect, render
from .models import Image, Profile,Likes
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, ImageForm, CommentForm, SignUpForm

# Create your views here.


def first_page(request):
    
    return redirect('/accounts/login/')

# @login_required(login_url='/accounts/login/')
def home(request):
    images = Image.objects.all()
    message ="Welcome to my Instagram clone"
    print(images)

    return render(request,'index.html',{'images':images, 'message': message})
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
                user_password=form.cleaned_data['user_password']
                Profile.objects.filter(username=current_user).update(useremail=useremail, userage=userage,profile_image=profile_image,user_password=user_password)
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
       
       

def profile_display(request):

    current_user = request.user
    profile= Profile.objects.filter(username=current_user)
   

    return render(request, 'profile.html',{'profile':profile})


def add_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            new_post=form.save(commit=False)
            # new_post.profile=current_user
            new_post.save()
            print('post saved')
            return redirect(home)
           
                        
    else:
        form = ImageForm()
        
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

def image_like(request, id):
    likes = Likes.objects.filter(id=id).first()
    # check if the user has already liked the image
    if Likes.objects.filter(id=id).exists():
        # unlike the image
        likes.delete()
        # reduce the number of likes by 1 for the image
        image = Image.objects.get(id=id)
        # check if the image like_count is equal to 0
        if image.like_count == 0:
            image.like_count = 0
            image.save()
        else:
            like =image.like_count
            like= like -1 
            image.save()
        return redirect('/')
    else:
        likes = Likes(id=id)
        likes.save()
        # increase the number of likes by 1 for the image
        image = Image.objects.get(id=id)
        likes=image.like_count 
        likes = likes +1
        likes.save()
        image.save()
        return redirect('/')
        