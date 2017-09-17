from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, UserForm, ProfileForm
from django.contrib.auth.models import User
from .models import Profile

# Create your views here.
def main(request):
    skills = []
    for person in Profile.objects.all():
        for skill in person.fields_of_expertise.keys():
            if (not(skill in skills)):
                skills.append(skill)
    return render(request, 'main/main.html', {'skills': skills})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.first = form.cleaned_data.get('first')
            user.profile.last = form.cleaned_data.get('last')
            user.profile.email = form.cleaned_data.get('email')
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'main/signup.html', {'form': form})

def search(request, category, value):
    users_found_in_category = []
    category = category.upper()
    value = int(value)

    for person in Profile.objects.all():
        for skill in list(person.fields_of_expertise.keys()):
            print("Skill"+ skill)
            print("cat" +category)
            if (skill == category):
                users_found_in_category.append(person)
    users_found = []
    print(users_found_in_category)
    for person in users_found_in_category:
        level  = int(person.fields_of_expertise.get(category))
        if (level >= value):
            users_found.append(person)
    print(users_found)

    if request.method == 'POST':
        return redirect('search')
    return render(request, 'main/search.html', {'users_found': users_found, 'category': category,'value': value})

def profile(request, name):
    user = Profile.objects.filter(first=name)
    return render(request, 'main/profile.html', {'user': user})

def chat(request, name):
    user = Profile.objects.filter(first=name)[0]
    print(user)
    return render(request, 'main/chat.html', {'user': user})
