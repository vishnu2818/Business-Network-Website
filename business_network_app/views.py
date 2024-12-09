from django.db.models.fields import return_None
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import *
from django.contrib import messages
from .models import *


# if request.method == 'POST':
#     email = request.POST.get('email')
#     password = request.POST.get('password')
#     return HttpResponse(f"Received: {email}, {password}")

def login(request):
    return render(request, 'login.html')

def index(request):
    companies = Company.objects.all()
    # Another way!
    # is_approved = Company.objects.POST.get('is_approved')
    # companies = Company.objects.get(is_approved = is_approved)

    filtered_companies = []
    for company in companies:
        #Adding filter Condition Approved companies !
        if company.is_approved:
            filtered_companies.append(company)

    return render(request, 'index.html', {'companies': filtered_companies})


def testmethod(request):
    return render(request, 'test.html')

def company_register(request):
    if request.method == 'POST':
        company_form = CompanyRegistrationForm(request.POST, request.FILES)
        if company_form.is_valid():
            username = company_form.cleaned_data.get('email')
            password = company_form.cleaned_data.get('password')
            print(username)
            print(password)
            company_form.save()
            company_name = company_form.cleaned_data.get('company_name')
            messages.success(request, f"Account created for {company_name}")
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        company_form = CompanyRegistrationForm()

    context = {'company_form': company_form}
    return render(request, 'register.html', context)

def company_login(request):
    if request.method == 'POST':
        print("hiiiiiiiiiiiii im innnnnn!!!")
        form = CompanyLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
        try:
            company = Company.objects.get(email=email)
            print("hiiiii", {company})
            # if company.check_password(password):
            if company.password == password:
                print("Password is correct!")
                # login(request, company)
                return redirect('index')
            else:
                print("wrong password")
            # email = form.cleaned_data.get('email')
            # password = form.cleaned_data.get('password')
            # user = authenticate(request, email=email, password=password)
            # message = messages.error(request, "Invalid username or password")
            # if user is not None:
            #     login(request, user)
            #       # Redirect to home page or another view after successful login
        except Company.DoesNotExist:
            return messages.error(request, "Company Not Found!")
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})