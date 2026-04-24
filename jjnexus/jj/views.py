from django.shortcuts import render, redirect
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


# def services(request):
#     return render(request, 'services.html')

def about(request):
    return render(request, 'about.html')


from .models import College

def courses(request):
    colleges = College.objects.all()
    return render(request, 'courses.html', {'colleges': colleges})

from django.shortcuts import render
from .models import Contact
from django.contrib import messages


def contact_view(request):

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print("DATA:", name, email, phone, message)
        #  # Prevent empty submission
        if name and email and message:
            Contact.objects.create(
                name=name,
                email=email,
                phone=phone,
                message=message
            )
            # print("SAVED SUCCESSFULLY")
            # Add a success message
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact') # Redirect to clear the form fields


        # return render(request, "contact.html", {"success": True})

    return render(request, "contact.html")


# def contact_view():
#     return None
