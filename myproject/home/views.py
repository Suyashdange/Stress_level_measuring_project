from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from home.models  import * 
from .forms import StressAssessmentForm
from .models import StressAssessmentResponse
from django.contrib.auth.models import User
import uuid

def home(request):
    return render(request, 'home.html')

def register_view(request):
    if request.method == 'POST':
        email = request.POST.get('email').strip()
        password = request.POST.get('password').strip()
        user_type = request.POST.get('type')

        if not email or not password or not user_type:
            messages.error(request, "All fields are required.")
            return render(request, 'register.html')

        # Create a new user instance
        user = registration_data(email=email, type=user_type)
        user.set_password(password)
        user.save()

        messages.success(request, "Registration successful! Please log in.")
        return redirect('login')

    return render(request, 'register.html')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')  
    
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()

        try:
            user = registration_data.objects.get(email=email)
            if user.check_password(password):
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                login(request, user)
                print(f"Logged in user: {user.email}")
                print(request.session.items())
                return redirect('dashboard')
            else:
                messages.error(request, "Invalid password.")
        except registration_data.DoesNotExist:
            messages.error(request, "User does not exist.")

    return render(request, 'login.html')

def dashboard_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    # Fetch all test records for the logged-in user
    user_tests = test_data.objects.filter(username=request.user.email).order_by('-date')  # Sort by latest date

    return render(request, 'home.html', {'tests': user_tests})

def counsellors_view(request):
    counsellors = counsellor_data.objects.all()

    return render(request, 'counsellors.html', {'counsellors': counsellors})
def counsellor_view(request):
    return render (request, 'counsellor.html')

def appointment_view(request):
    if request.method == 'POST':
        # appointmentid = ''
        # counsellorid =''
        # userid =''
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        date = request.POST.get('date')
        time = request.POST.get('time')
        address = request.POST.get('address')
        # result = ''
        status ='pending'
        frm = appointement_data(name=name,phone=phone,email=email,date=date,time=time,address=address,status=status)
        frm.save()
        return redirect('dashboard')
    else:
        return render (request, 'appointment.html')

def accept(request):
    return render (request, 'appointment.html')

def reject(request):
    return render (request, 'appointment.html')

def test_view(request):
     user_email = request.user.email
     if request.method == 'POST':
        form = StressAssessmentForm(request.POST)
        if form.is_valid():
            print("Form is valid")  # Debugging line
            
            # Collecting the form responses
            responses = {f"question_{i+1}": int(form.cleaned_data[f"question_{i+1}"]) for i in range(len(form.fields) - 2)}
            
            # Create and save the response
            response = StressAssessmentResponse.objects.create(responses=responses)
            
            # Calculate the stress level based on the response
            stress_level = response.stress_level()
            
            # Create a test ID
            testid = str(uuid.uuid4())
            
            # Save the activity with the user's email
            if user_email:  # Check if the user email is valid
                activity = test_data(username=user_email, date=timezone.now(), testid=testid, result=stress_level)
                print(f"Saving activity: {activity}")  # Debugging line
                activity.save()
            else:
                print("Error: User email not available")  # Debugging line

            # Render the counsellor's page with the response and stress level
            return redirect('counsellors')

def logout_view(request):
    logout(request)
    return redirect('login')

def stress_assessment_view(request):
    if not request.user.is_authenticated:
        print("user not authenticated")
        return redirect('login')
    
    # Debugging line to check if user is authenticated
    print(f"Authenticated user: {request.user.email}")  # Check if user is authenticated and email is available
    
    user_email = request.user.email
    if not user_email:
        print("Error: User email is empty")  # Debugging line
    
    if request.method == 'POST':
        form = StressAssessmentForm(request.POST)
        if form.is_valid():
            print("Form is valid")  # Debugging line
            
            # Collecting the form responses
            responses = {f"question_{i+1}": int(form.cleaned_data[f"question_{i+1}"]) for i in range(len(form.fields) - 2)}
            
            # Create and save the response
            response = StressAssessmentResponse.objects.create(responses=responses)
            
            # Calculate the stress level based on the response
            stress_level = response.stress_level()
            
            # Create a test ID
            testid = str(uuid.uuid4())
            
            # Save the activity with the user's email
            if user_email:  # Check if the user email is valid
                activity = test_data(username=user_email, date=timezone.now(), testid=testid, result=stress_level)
                print(f"Saving activity: {activity}")  # Debugging line
                activity.save()
            else:
                print("Error: User email not available")  # Debugging line

            # Render the counsellor's page with the response and stress level
            return render(request, 'result.html', {
                'response': response,
                'stress_level': stress_level,
            })
        else:
            print("Form is not valid")  # Debugging line
            print(form.errors)  # Debugging line to show form errors
    else:
        form = StressAssessmentForm()

    return render(request, 'assessment.html', {'form': form})