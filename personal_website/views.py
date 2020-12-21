from django.shortcuts import render


def about_me(request):
    return render(request, "about.html", {})


def resume(request):
    return render(request, "resume.html", {})


def contact_me(request):
    return render(request, "contact-me.html", {})
