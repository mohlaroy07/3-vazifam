from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Lesson
from .forms import CourseForm, RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate


def home_page(request):
    course_list = Course.objects.all()
    context = {
        "courses": course_list,
    }

    return render(request, "components/index.html", context=context)


def add_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            user_id = request.user.id

            form.instance.user_id = user_id

            form.save()
            return redirect("home_page")

    else:
        form = CourseForm()
    return render(request, "components/add_course.html", {"form": form})


def course_detail(request, pk):
    course = get_object_or_404(Course, id=pk)

    context = {
        "course": course,
        "lesson": course.lesson.all(),
    }
    if request.method == "POST":

        lesson_list = request.POST.get("content")

        if lesson_list:

            lesson = course.comments.create(
                content=lesson_list, author=request.user, course=course
            )
            lesson.save()
            return redirect("detail", pk=pk)

        return render(request, "components/detail.html", context)


def user_login(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect("home_page")
    else:
        form = LoginForm()

    return render(request, "components/login.html", {"form": form})


def user_register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]

            if User.objects.filter(username=username).exists():
                form.add_error(
                    "username", "Bunday foydalanuvchi nomi allaqachon mavjud"
                )
            else:
                user = form.save(commit=False)
                user.set_password(form.cleaned_data["password"])
                user.save()
                login(request, user)
                return redirect("home_page")
    else:
        form = RegisterForm()

    return render(request, "components/register.html", {"form": form})


def log_out(request):
    logout(request)
    return redirect("home_page")
