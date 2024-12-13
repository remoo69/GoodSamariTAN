from django.shortcuts import render
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from .models import DonationForm  # Import your DonationForm model
from .models import Ngo, NgoDonationMethod, NgoImage, NgoNeeded

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

def landingPage(request):
    return render(request, 'landingPage.html', {})


def landing_page(request):
    return render(request, 'ngo-donation-section.html')


def about_page(request,):
    sample=Ngo(name="Aboitiz Foundation, Inc.",
                location="Manila",
                phone="1234454",
                email="random@gmail.com",
                about_us="Lorem ipsum dolor sit amet consectetur adipiscing eli mattis sit phasellus mollis sit aliquam sit nullam neque ultrices. Lorem ipsum dolor sit amet consectetur adipiscing eli mattis sit phasellus mollis sit aliquam sit nullam neque ultrices. Lorem ipsum dolor sit amet consectetur adipiscing eli mattis sit phasellus mollis sit aliquam sit nullam neque ultrices."
                )
    # NgoNeeded.objects.create(ngo=sample,
    #                name="Ewan")
    # NgoNeeded.objects.create(ngo=sample,
    #                name="Ewan2")
    # NgoNeeded.objects.create(ngo=sample,
    #                name="Ewan3")
    needed=["Ewan", "IDK"]
    contact_methods=["Globe", "Smart"]
    context={
        "ngo":sample,
        "needed_items":needed,
        "contact_methods":contact_methods
    }
    return render(request, "about_page.html", context=context)