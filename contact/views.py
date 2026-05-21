from django.shortcuts import render
from django.http import JsonResponse
from contact.forms import ContactForm
from contact.models import Message


def index(request):
    """Render the main index page."""
    return render(request, 'index.html')


def contact_form(request):
    """Handle contact form: validate, save to db, send email, and respond."""
    contact_form = ContactForm(request.POST or None)

    if request.method == 'POST':

        # is_valid() formdaki e-posta formatını ve boş alanları otomatik kontrol eder
        if contact_form.is_valid():

            # 1. VERİTABANINA KAYIT İŞLEMİ (Temizlenmiş verilerle)
            try:
                Message.objects.create(
                    name=contact_form.cleaned_data['name'],
                    last_name=contact_form.cleaned_data['last_name'],
                    email=contact_form.cleaned_data['email'],
                    subject=contact_form.cleaned_data['subject'],
                    message=contact_form.cleaned_data['message']
                )
            except Exception as e:
                print('DB create error:', e)
                return JsonResponse({'success': False, 'message': 'Veritabanına kaydedilirken bir hata oluştu.'},
                                    status=500)

            # 2. E-POSTA GÖNDERME İŞLEMİ
            # forms.py içine yazdığımız send_email fonksiyonunu burada çağırıyoruz
            try:
                contact_form.send_email()
            except Exception as e:
                print('Email send error:', e)
                return JsonResponse({'success': False, 'message': 'E-posta gönderilirken bir hata oluştu.'}, status=500)

            # HER İKİ İŞLEM DE BAŞARILIYSA
            data = {'success': True, 'message': 'Contact form sent successfully.'}
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse(data)
            return render(request, 'contact.html', data)

        else:
            # FORM HATALIYSA (Örn: Boş bırakılan yer varsa)
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'message': 'Lütfen formu eksiksiz doldurun.'}, status=400)

    # GET İSTEKLERİ İÇİN
    context = {
        'contact_form': contact_form,
    }
    return render(request, 'contact.html', context)