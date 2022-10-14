from django.urls import path
from . import views

# Define your routes here
urlpatterns = [
   path("", views.index_page, name="home"),
   
   # ------------------------------------------------------------------------------------------------
   # Authentication Routes
   # ------------------------------------------------------------------------------------------------
   path("login/", views.login_page, name="login"),
   path("register/", views.register_page, name="register"),
   path("logout/", views.logout_page, name="logout"),
   
   # ------------------------------------------------------------------------------------------------
   # User Routes
   # ------------------------------------------------------------------------------------------------
   path("user/<str:pk>/", views.profile_page, name="profile"),
   
   # ------------------------------------------------------------------------------------------------
   # Event Routes
   # ------------------------------------------------------------------------------------------------
   path("event/<str:pk>/", views.event_page, name="event"),
   path("event-confirmation/<str:pk>/", views.confirm_registration_page, name="event-confirmation"),
   
   # ------------------------------------------------------------------------------------------------
   # Account Routes
   # ------------------------------------------------------------------------------------------------
   path("account/", views.account_page, name="account"),
   
   # ------------------------------------------------------------------------------------------------
   # Project Submission Routes
   # ------------------------------------------------------------------------------------------------
   path("project-submission/<str:pk>/", views.project_submission_page, name="project-submission"),
   path("update-submission/<str:pk>/", views.update_submission, name="update-submission"),
]