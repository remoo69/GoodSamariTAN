from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.core.files.storage import FileSystemStorage
from .models import DonationForm, NGOApplication
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.hashers import make_password

def donation_view(request):
    if request.method == 'POST':
        # Extract form data from the POST request
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        item = request.POST.get('item')
        quantity = request.POST.get('quantity')
        category = request.POST.get('category')
        description = request.POST.get('description')
        height = request.POST.get('height')
        width = request.POST.get('width')
        weight = request.POST.get('weight')
        notes = request.POST.get('notes')

        # Handle image upload
        image = request.FILES.get('image')
        image_url = None
        if image:
            fs = FileSystemStorage()
            image_name = fs.save(image.name, image)
            image_url = fs.url(image_name)  # Get the URL of the uploaded image

        # Save the form data to the database
        try:
            donation = DonationForm.objects.create(
                name=name,
                phone=phone,
                email=email,
                item=item,
                quantity=int(quantity) if quantity else None,  # Ensure `quantity` is an integer
                category=category,
                description=description,
                height=int(height) if height else None,  # Ensure `height` is an integer
                width=int(width) if width else None,  # Ensure `width` is an integer
                weight=int(weight) if weight else None,  # Ensure `weight` is an integer
                notes=notes,
                image=image,  # Pass the image directly
            )
            # Return success response
            # return JsonResponse({'success': True, 'message': 'Donation successfully submitted!', 'image_url': image_url}),
            return render(request, 'ngo-donation-section.html', {'success': True, 'message': 'Donation successfully submitted!', 'image_url': image_url})
        except Exception as e:
            # Handle any errors during saving
            return JsonResponse({'success': False, 'message': str(e)})

    # Render the donation form page (for GET requests)
    
    #ayusin mo romeo @romeo
    return render(request, 'donation_form.html')

# def donation_form(request):
#     if request.method == 'GET':
#         return render(request, 'donation_form.html')

# Home View
def landingPage(request):
    return render(request, 'landingPage.html')

# Landing Page View for Donation Section
def landing_page(request):
    return render(request, 'ngo-donation-section.html')


# NGO Application Form View
def ngo_application(request):
    if request.method == 'GET':
        return render(request, 'ngo-application.html')


#ngo application submit
def ngo_application_submit(request):
    if request.method == 'POST':
        ein = request.POST['ein']
        name = request.POST['name']
        address = request.POST['address']
        contact_number = request.POST['contact_number']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        form_990 = request.FILES['form_990']

        # Check if EIN, name, or email already exists
        if NGOApplication.objects.filter(ein=ein).exists():
            return render(request, 'ngo-application.html', {'error': "This EIN is already registered."})
        
        if NGOApplication.objects.filter(name=name).exists():
            return render(request, 'ngo-application.html', {'error': "This organization name is already taken."})
        
        if NGOApplication.objects.filter(email=email).exists():
            return render(request, 'ngo-application.html', {'error': "This email address is already registered."})

        if password != confirm_password:
            return render(request, 'ngo-application.html', {'error': "Passwords do not match."})

        # Save the uploaded form file
        fs = FileSystemStorage()
        filename = fs.save(form_990.name, form_990)

        # Save the NGOApplication instance
        ngo_application = NGOApplication.objects.create(
            ein=ein,
            name=name,
            address=address,
            contact_number=contact_number,
            email=email,
            password=make_password(password),  # Hash password for security
            form_990=filename
        )

        # Create a corresponding User in the auth system if not exists
        if not User.objects.filter(username=email).exists():
            User.objects.create_user(
                username=email,
                email=email,
                password=password
            )

        # Automatically log in the user
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')

        return HttpResponse('Application submitted successfully but login failed')

    return HttpResponse('Invalid request')

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'success': True, 'message': 'Login successful'})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid login credentials'}, status=401)
    return render(request, 'login.html')

def check_unique(request):
    ein = request.GET.get('ein', '')
    name = request.GET.get('name', '')
    email = request.GET.get('email', '')
    
    response = {'ein_exists': False, 'name_exists': False, 'email_exists': False}
    
    if NGOApplication.objects.filter(ein=ein).exists():
        response['ein_exists'] = True
    if NGOApplication.objects.filter(name=name).exists():
        response['name_exists'] = True
    if NGOApplication.objects.filter(email=email).exists():
        response['email_exists'] = True
    
    return JsonResponse(response)

def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to home page
from django.shortcuts import render
from .models import NGOApplication

def ngos_view(request):
    ngos = NGOApplication.objects.all()  # Fetch all NGOs
    return render(request, 'ngo-donation-section.html', {'ngos': ngos})

def landing_page_view(request):
    ngos = NGOApplication.objects.all()  # Fetch all NGOs
    return render(request, 'landingPage.html', {'ngos': ngos})

def search_ngos(request):
    search = request.GET.get('search', '')    # Search term
    location = request.GET.get('location', '')  # Location filter
    category = request.GET.get('category', '')  # Category filter (optional, if you have it)

    ngos = NGOApplication.objects.all()

    # Apply search filter (name contains the search string)
    if search:
        ngos = ngos.filter(name__icontains=search)
    
    # Apply location filter (address contains the location)
    if location:
        ngos = ngos.filter(address__icontains=location)

    # Apply category filter (if needed)
    if category:
        ngos = ngos.filter(category__icontains=category)

    ngos_data = [{
        'name': ngo.name,
        'address': ngo.address,
        'email': ngo.email
    } for ngo in ngos]

    return JsonResponse({'ngos': ngos_data})