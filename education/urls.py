from django.urls import path
from .views import home_page, course_detail, add_course, user_login, user_register, log_out


urlpatterns = [
    path("", home_page, name="home_page"),
    path("detail/<int:pk>/", course_detail, name="detail"),
    path("add/", add_course, name="add_course"),
    path("login/", user_login, name="login"),
    path("register/", user_register, name="register"),
    path("logout/", log_out, name="logout"),
]
