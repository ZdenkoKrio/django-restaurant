from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

from django.contrib.auth import login, authenticate
from ..forms import SignUpForm
from django.contrib.auth.decorators import login_required

def home_page(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render({}, request))


def signup(request):
    if request.method == 'POST':
      form = SignUpForm(request.POST)
      if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(request, user)
        return redirect('profile')
    else:
      form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required
def profile(request):
  template = loader.get_template('404.html')

  return HttpResponse(template.render({'user': request.user}, request))

