from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Submission, User

# Define your forms here...
class SubmissionForm(ModelForm):
   class Meta:
      model = Submission
      fields = ['details']

class RegistrationForm(UserCreationForm):
   class Meta:
      model = User
      fields = ['username', 'email', 'name', 'password1', 'password2']

class EditAccountForm(ModelForm):
   class Meta:
      model = User
      fields = ['username', 'email', 'bio', 'avatar']