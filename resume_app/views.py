from django.shortcuts import render, redirect
from .models import Portfolio, About, Service, Resume_work, Education
from .forms import ContactForm


# Create your views here.

def index(request):
    # education = Education.objeccts.all()
    resume_w = Resume_work.objects.all()
    about = About.objects.all()
    service = Service.objects.all()
    portfolio = Portfolio.objects.all()[::-1]
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(".")
    contex = {
        "portfolios": portfolio,
        "abouts": about,
        "servises": service,
        "works": resume_w,
        # "edu": education,
        "form": form
    }
    return render(request, "index.html", contex)
