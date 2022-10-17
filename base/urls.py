from django.urls import path
from . import views

# Define your routes here
urlpatterns = [
   # Home route / landing page
   path('', views.index_page, name='home'),
   
   # ------------------------------------------------------------------------------------------------
   # Authentication related routes
   # ------------------------------------------------------------------------------------------------
   path('login/', views.login_page, name='login'),
   path('register/', views.register_page, name='register'),
   path('logout/', views.logout_page, name='logout'),
   
   # ------------------------------------------------------------------------------------------------
   # User related routes
   # ------------------------------------------------------------------------------------------------
   path('user/<str:pk>/', views.profile_page, name='profile'),
   
   # ------------------------------------------------------------------------------------------------
   # Event related routes
   # ------------------------------------------------------------------------------------------------
   path('event/<str:pk>/', views.event_page, name='event'),
   path('event-confirmation/<str:pk>/', views.confirm_registration_page, name='event-confirmation'),
   
   # ------------------------------------------------------------------------------------------------
   # Account related routes
   # ------------------------------------------------------------------------------------------------
   path('account/', views.account_page, name='account'),
   path('edit-account/', views.edit_account, name='edit-account'),
   
   # ------------------------------------------------------------------------------------------------
   # Project submission related routes
   # ------------------------------------------------------------------------------------------------
   path('project-submission/<str:pk>/', views.project_submission_page, name='project-submission'),
   path('update-submission/<str:pk>/', views.update_submission, name='update-submission'),
]