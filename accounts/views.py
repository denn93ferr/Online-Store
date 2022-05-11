from django.shortcuts import redirect, render
from .forms import SignUpForm
from django.contrib.auth import authenticate, login

from django.contrib.auth.views import LoginView, PasswordChangeView, LogoutView
from django.urls import reverse_lazy

# Create your views here.
# 1: try changing thiswith a form-specific class based view
# 2: try oberwriting the .save() method of the modelform and add there
#    the logic of keeping the user logged in after creation


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(user, request)
            #
            return redirect("properties")
    else:
        form = SignUpForm()
    return render(request, "signup.html", {"form": form})


# redirect ~ reverse_lazy"


class CustomLoginView(LoginView):
    template_name = "login.html"


class CustomLogoutView(LogoutView):
    template_name = None


class CustomPasswordChangeView(PasswordChangeView):
    template_name = "password_change.html"
    success_url = reverse_lazy("properties")
    # success_url = redirect('properties')
