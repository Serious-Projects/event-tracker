from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages
from .models import User, Event, Submission
from .forms import SubmissionForm, RegistrationForm, EditAccountForm

# Create your views here.
def login_page(request):
   page = 'login'
   if request.method == 'POST':
      email = request.POST.get('email')
      password = request.POST.get('password')
      user = authenticate(email=email, password=password)
      if user is not None:
         login(request, user)
         return redirect('home')
      else:
         messages.error(request, 'Email OR Password is incorrect')
         return redirect('login')
   return render(request, 'login-register.html', {'page': page})

def register_page(request):
   page = 'register'
   form = RegistrationForm()
   if request.method == 'POST':
      form = RegistrationForm(request.POST)
      if form.is_valid():
         user = form.save(commit=False)
         user.save()
         login(request, user)
         return redirect('home')
   context = {'page': page, 'form': form}
   return render(request, 'login-register.html', context)

def logout_page(request):
   logout(request)
   return redirect('login')

@login_required(login_url='/login')
def reset_password(request):
   if request.method == 'POST':
      password = request.POST.get('password1')
      confirm_password = request.POST.get('password2')
      if password == confirm_password:
         request.user.set_password(password)
         request.user.save()
         return redirect('account')
      else:
         messages.error(request, 'Your passwords dont match :(')
   return render(request, 'reset-password.html')

def index_page(request):
   LIMIT = 5
   users_list = User.objects.get_queryset().order_by('id')
   # Getting query params for pagination
   page = int(request.GET.get('page') or 1)
   paginator = Paginator(users_list, LIMIT)
   try:
      users = paginator.page(page)
   except PageNotAnInteger:
      page = 1
      users = paginator.page(page)
   except EmptyPage:
      page = paginator.num_pages
      users = paginator.page(page)
   pages = list(range(1, (paginator.num_pages + 1)))
   events = Event.objects.all()
   context = {'users': users, 'events': events, 'paginator': paginator, 'pages': pages}
   return render(request, 'home.html', context)

def event_page(request, pk):
   event = Event.objects.get(id=pk)
   has_registered = False
   submitted = False
   if request.user.is_authenticated:
      has_registered = request.user.events.filter(id=event.id).exists()
      submitted = Submission.objects.filter(participant=request.user, event=event).exists()
   context = {'event': event, 'has_registered': has_registered, 'submitted': submitted}
   return render(request, 'event.html', context)

@login_required(login_url='/login')
def edit_account(request):
   form = EditAccountForm(instance=request.user)
   if request.method == 'POST':
      form = EditAccountForm(request.POST, request.FILES, instance=request.user)
      if form.is_valid():
         form.save()
         return redirect('account')
   context = {'form': form}
   return render(request, 'user-form.html', context)

@login_required(login_url='/login')
def confirm_registration_page(request, pk):
   event = Event.objects.get(id=pk)
   if request.method == 'POST':
      event.participants.add(request.user)
      return redirect('event', pk=event.id)
   return render(request, 'event-confirmation.html', {'event': event})

@login_required(login_url='/login')
def profile_page(request, pk):
   user = User.objects.get(id=pk)
   return render(request, 'profile.html', {'user': user})

@login_required(login_url='/login')
def account_page(request):
   context = {'user': request.user}
   return render(request, 'account.html', context)

@login_required(login_url='/login')
def project_submission_page(request, pk):
   event = Event.objects.get(id=pk)
   form = SubmissionForm(request.POST)
   if request.method == 'POST':
      form = SubmissionForm(request.POST)
      if form.is_valid():
         submission = form.save(commit=False)
         submission.participant = request.user
         submission.event = event
         submission.save()
         return redirect('account')
   return render(request, 'submit-form.html', {'event': event, 'form': form})

@login_required(login_url='/login')
def update_submission(request, pk):
   submission = Submission.objects.get(id=pk)
   form = SubmissionForm(instance=submission)
   if request.user != submission.participant:
      return HttpResponse("You can't be here...")
   event = submission.event
   if request.method == 'POST':
      form = SubmissionForm(request.POST, instance=submission)
      form.save()
      return redirect('account')
   context = {'event': event, 'form': form}
   return render(request, 'submit-form.html', context)