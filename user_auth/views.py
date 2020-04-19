from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileForm
from .models import Profile 


def signup(request):
    print ("signup------------------------------------------")
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.email = form.cleaned_data.get('email')
            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            #form = ProfileForm()
            #return render(request, 'registration/profile.html', {'form': profileForm})
            return redirect('/')
    else:
        form = ProfileForm()
    return render(request, 'registration/signup.html', {'form': form})

def profile(request):
    print ("profile-------------------------------------------------")
    print (request.method)
    if request.method == 'POST':
        username = request.user.username
        profiles = Profile.objects.filter(user__username=username)
        profile = profiles[0]
        print ("profile2222222222222")
        #form = ProfileForm(request.POST)
        fname = request.POST.get("fname", "")
        lname = request.POST.get("lname", "")
        email = request.POST.get("email", "")
        expertise = request.POST.get("expertise", "")
        major = request.POST.get("major", "")
        bio = request.POST.get("bio", "")
        print ('first name=' + fname)
        
        profile.first_name = fname
        profile.last_name = lname
        profile.email = email
        profile.expertise = expertise
        profile.major = major
        profile.bio = bio
        profile.save()
        return redirect('/')
    else:
        print ("eeelllllllllsssseeeeee")
        #data = Profile.objects.filter(first_name=='test101')
        username = request.user.username
        profile = Profile.objects.filter(user__username=username)
        #form = ProfileForm()
        #form.first_name = 'George'
    return render(request, 'registration/profile.html', {'profile': profile})
