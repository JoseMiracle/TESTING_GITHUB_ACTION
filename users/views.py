from django.shortcuts import render, redirect
from users.models import UserInformation


def collect_user_information(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        email = request.POST["email"]
        hobbies = request.POST["hobbies"]
        about_me = request.POST["about_me"]

        UserInformation.objects.create(
            first_name=first_name, email=email, hobbies=hobbies, about_me=about_me
        )
        return redirect("users:success")
    return render(request, "collect_user_information.html")


def success_page(request):
    return render(request, "success.html")
