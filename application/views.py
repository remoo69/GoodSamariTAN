from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator
from .models import DonationForm, NGO, Message, Subscriber # Import your DonationForm model
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .models import NGOCategory

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
            return JsonResponse({'success': True, 'message': 'Donation successfully submitted!', 'image_url': image_url})
        except Exception as e:
            # Handle any errors during saving
            return JsonResponse({'success': False, 'message': str(e)})

    # Render the donation form page (for GET requests)
    return render(request, 'donation_form.html')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def ngo_list(request):
    query = request.GET.get('q', '')
    location = request.GET.get('location')
    category = request.GET.get('category')
    
    # Only show verified NGOs
    ngos = NGO.objects.filter(verified=True)
    
    if query:
        ngos = ngos.filter(name__icontains=query)
    if location:
        ngos = ngos.filter(city=location)
    if category:
        ngos = ngos.filter(categories__name=category)

    paginator = Paginator(ngos, 6)  # Show 6 NGOs per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    cities = NGO.objects.values_list('city', flat=True).distinct()
    categories = NGO.objects.values_list('categories__name', flat=True).distinct()

    context = {
        'ngos': page_obj,
        'cities': cities,
        'categories': categories,
        'query': query,
        'location': location,
        'category': category,
        'page_obj': page_obj,
    }
    return render(request, 'ngo_list.html', context)

def ngo_detail(request, pk):
    ngo = get_object_or_404(NGO, pk=pk)
    return render(request, 'ngo_detail.html', {'ngo': ngo})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        Message.objects.create(name=name, email=email, message=message)
        return redirect('contact')  # Redirect to the same page or another page after submission

    return render(request, 'contact.html')

def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            if Subscriber.objects.filter(email=email).exists():
                messages.error(request, 'This email is already subscribed.')
            else:
                Subscriber.objects.create(email=email)
                messages.success(request, 'You have successfully subscribed.')
        return redirect('contact')  # Redirect to the contact page or another page after submission

    return render(request, 'contact.html')

def ngo_application(request):
    categories = NGOCategory.objects.all()  # Fetch all categories
    return render(request, 'ngo-application.html', {'categories': categories})

def ngo_application_submit(request):
    if request.method == 'POST':
        # Collect data from the form
        name = request.POST.get('name')
        cover_image = request.FILES.get('cover_image')
        about = request.POST.get('about')
        needs = request.POST.get('needs')
        city = request.POST.get('city')
        exact_address = request.POST.get('exact_address')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        other_donation_methods = request.POST.get('other_donation_methods')
        category_id = request.POST.get('category')

        # Fetch the category instance
        category = NGOCategory.objects.get(id=category_id)

        # Save to the NGO model
        ngo = NGO.objects.create(
            name=name,
            cover_image=cover_image,
            about=about,
            needs=needs,
            city=city,
            exact_address=exact_address,
            phone=phone,
            email=email,
            other_donation_methods=other_donation_methods,
        )
        # Assign the selected category
        ngo.categories.add(category)

        # Redirect to the home page
        return redirect('home')

    return redirect('ngo_application')