from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
import urllib.request, json 
import random


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)

print("IN VIEWSSSS")
the_url = 'http://acnhapi.com/v1/houseware'
#response = urllib.urlopen(url)
#data = json.loads(response.read())
with urllib.request.urlopen(the_url) as url:
    data = json.loads(url.read().decode(), encoding='utf-8')
    #print(data)

"""
for row in data:
    print(row)
    print(data[row].image_uri)
"""
images = []
for r in data.values():
    for row in r:
        images.append(row["image_uri"])
        #print(row["image_uri"])

random.shuffle(images)
context = {
    'images': images[:30],
    'images2': images[30:60],
    'images3': images[60:90]
}
#print(images)
@login_required
def trading(request):
    print("IN HERE!!!!")
    return render(request, 'users/trading.html', context)