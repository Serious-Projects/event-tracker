from django.urls import path
from . import views

# Define your routes here
urlpatterns = [
   # Home route / landing page
   path('', views.index_page, name='home'),
   
   # ------------------------------------------------------------------------------------------------
   # Authentication related routes
   # ------------------------------------------------------------------------------------------------
   path('auth/login/', views.login_page, name='login'),
   path('auth/register/', views.register_page, name='register'),
   path('auth/logout/', views.logout_page, name='logout'),
   
   # ------------------------------------------------------------------------------------------------
   # User related routes
   # ------------------------------------------------------------------------------------------------
   path('user/<str:pk>/', views.profile_page, name='profile'),
   
   # ------------------------------------------------------------------------------------------------
   # Account related routes
   # ------------------------------------------------------------------------------------------------
   path('account/', views.account_page, name='account'),
   path('account/edit/', views.edit_account, name='edit-account'),
   path('account/reset-password/', views.reset_password, name='reset-password'),
   
   # ------------------------------------------------------------------------------------------------
   # Event related routes
   # ------------------------------------------------------------------------------------------------
   path('event/<str:pk>/', views.event_page, name='event'),
   path('event/confirmation/<str:pk>/', views.confirm_registration_page, name='event-confirmation'),
   
   # ------------------------------------------------------------------------------------------------
   # Project related routes
   # ------------------------------------------------------------------------------------------------
   path('project/submission/<str:pk>/', views.project_submission_page, name='project-submission'),
   path('project/update/<str:pk>/', views.update_submission, name='update-submission'),
]