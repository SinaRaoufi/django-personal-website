from django.shortcuts import render, redirect
from .forms import ConatactMeForm
from django.contrib import messages
# from django.core.mail import send_mail


def about_me(request):
    return render(request, "about.html", {})


def resume(request):
    return render(request, "resume.html", {})


def contact_me(request):
    if request.method == 'POST':
        form = ConatactMeForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # send_mail('SinaRaoufi-Form', cd['message'],
            #           'mail.sinaraoufi.com', ['sinaraoufi@outlook.com', ])
            messages.success(request, 'پیام شما با موفقیت ارسال شد')
            return redirect('contact-me')
    else:
        form = ConatactMeForm()

    context = {
        'form': form,
    }
    return render(request, "contact-me.html", context)
