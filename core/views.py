from multiprocessing import context

from django.shortcuts import render, redirect, get_object_or_404
from core.models import GeneralSetting, ImageSetting, Skill, SocialMedia, Document


def layout(request):
    documents = Document.objects.all()
    site_title = GeneralSetting.objects.get(name='site_title').parameter
    site_keywords = GeneralSetting.objects.get(name='site_keywords').parameter
    site_description = GeneralSetting.objects.get(name='site_description').parameter
    site_author = GeneralSetting.objects.get(name='site_author').parameter
    footer = GeneralSetting.objects.get(name='footer').parameter
    phone_number = GeneralSetting.objects.get(name='phone_number').parameter
    email_address = GeneralSetting.objects.get(name='email_address').parameter
    address = GeneralSetting.objects.get(name='address').parameter


    # Images
    header_logo = ImageSetting.objects.get(name='header_logo').file
    home_banner_image = ImageSetting.objects.get(name='home_banner_image').file
    firstpage = ImageSetting.objects.get(name='firstpage').file
    site_favicon = ImageSetting.objects.get(name='site_favicon').file
    social_medias = SocialMedia.objects.all().order_by('order')
    secondpage = ImageSetting.objects.get(name='secondpage').file
    context = {
        'documents': documents,
        'site_title': site_title,
        'site_keywords': site_keywords,
        'site_description': site_description,
        'site_author': site_author,
        'footer': footer,
        'header_logo': header_logo,
        'home_banner_image': home_banner_image,
        'site_favicon': site_favicon,
        'social_medias': social_medias,
        'phone_number': phone_number,
        'email_address': email_address,
        'address': address,
        'firstpage': firstpage,
        'secondpage': secondpage,

    }
    return context


def index(request):
    # Documents

    # Skills
    skills = Skill.objects.all().order_by('order')

    # Social Media


    context = {
        'skills': skills,


    }

    return render(request, 'index.html', context=context)


def redirect_to_index(request, slug):
    doc = get_object_or_404(Document, slug=slug)

    return redirect(doc.file.url)

# Create your views here.
