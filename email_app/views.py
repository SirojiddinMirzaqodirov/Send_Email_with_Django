from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.core.mail import send_mail

@csrf_exempt
@require_http_methods(['GET', 'POST'])
def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')

        # Your send_mail function here
        send_mail(
            f'New message from {name}',
            f'{message}\n\nFrom: {name} ({email})',
            'perfectworldfrom2021@gmail.com',  # Replace with your email address
            ['perfectworldfrom2021@gmail.com'],  # Replace with your email address
            fail_silently=False,
        )

        return JsonResponse({'message': 'Email sent successfully.'})
    else:
        return render(request, 'contact.html')
