from django.shortcuts import render
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator
from .models import DonationForm, NGO # Import your DonationForm model
from django.shortcuts import get_object_or_404

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
    ngos = NGO.objects.all()

    if query:
        ngos = ngos.filter(name__icontains=query)
    if location:
        ngos = ngos.filter(city=location)
    if category:
        ngos = ngos.filter(categories__name=category)

    cities = NGO.objects.values_list('city', flat=True).distinct()
    categories = NGO.objects.values_list('categories__name', flat=True).distinct()

    context = {
        'ngos': ngos,
        'cities': cities,
        'categories': categories,
        'query': query,
        'location': location,
        'category': category,
    }
    return render(request, 'ngo_list.html', context)

def ngo_detail(request, pk):
    ngo = get_object_or_404(NGO, pk=pk)
    return render(request, 'ngo_detail.html', {'ngo': ngo})

def contact(request):
    return render(request, 'contact.html')