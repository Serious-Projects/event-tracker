from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import User, Event, Submission
from .forms import SubmissionForm, RegistrationForm

# Create your views here.
def login_page(request):
   page = "login"
   if request.method == "POST":
      email = request.POST.get("email")
      password = request.POST.get("password")
      user = authenticate(email=email, password=password)
      if user is not None:
         login(request, user)
         return redirect("home")
      else:
         return redirect("login")
   return render(request, "login-register.html", { "page": page })

def register_page(request):
   page = "register"
   form = RegistrationForm()
   if request.method == "POST":
      form = RegistrationForm(request.POST)
      if form.is_valid():
         user = form.save(commit=False)
         user.save()
         login(request, user)
         return redirect("home")
      else:
         print("Errors:", form.errors.as_data())
   context = { "page": page, "form": form }
   return render(request, "login-register.html", context)

def logout_page(request):
   logout(request)
   return redirect("login")

def index_page(request):
   users = User.objects.filter(is_participant=True)
   events = Event.objects.all()
   context = { "users": users, "events": events }
   return render(request, "home.html", context)

def event_page(request, pk):
   event = Event.objects.get(id=pk)
   has_registered = False
   submitted = False
   if request.user.is_authenticated:
      has_registered = request.user.events.filter(id=event.id).exists()
      submitted = Submission.objects.filter(participant=request.user, event=event).exists()
   context = {
      "event": event,
      "has_registered": has_registered,
      "submitted": submitted,
   }
   return render(request, "event.html", context)

@login_required(login_url="/login")
def confirm_registration_page(request, pk):
   event = Event.objects.get(id=pk)
   if request.method == "POST":
      event.participants.add(request.user)
      return redirect("event", pk=event.id)
   return render(request, "event-confirmation.html", {"event": event})

def profile_page(request, pk):
   user = User.objects.get(id=pk)
   context = { "user": user }
   return render(request, "profile.html", context)

@login_required(login_url="login")
def account_page(request):
   context = { "user": request.user }
   return render(request, "account.html", context)

@login_required(login_url="/login")
def project_submission_page(request, pk):
   event = Event.objects.get(id=pk)
   if request.method == "POST":
      form = SubmissionForm(request.POST)
      if form.is_valid():
         submission = form.save(commit=False)
         submission.participant = request.user
         submission.event = event
         submission.save()
         return redirect("account")
   return render(request, "submit-form.html", { "event": event })

@login_required(login_url="/login")
def update_submission(request, pk):
   submission = Submission.objects.get(id=pk)
   if request.user != submission.participant:
      return HttpResponse("You can't be here...")
   event = submission.event
   if request.method == "POST":
      form = SubmissionForm(request.POST, instance=submission)
      form.save()
      return redirect("account")
   return render(request, "submit-form.html", { "event": event, "details": submission.details })
