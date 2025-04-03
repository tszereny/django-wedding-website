from django.conf import settings
from django.shortcuts import render
from guests.save_the_date import SAVE_THE_DATE_CONTEXT_MAP


def home(request):
    return render(request, 'home.html', context={
        'save_the_dates': SAVE_THE_DATE_CONTEXT_MAP,
        'support_tel_person_1': settings.SUPPORT_TEL_PERSON_1,
        'support_tel_person_2': settings.SUPPORT_TEL_PERSON_2,
        'support_fb_person_1': settings.SUPPORT_FB_PERSON_1,
        'support_fb_person_2': settings.SUPPORT_FB_PERSON_2,
        'website_url': settings.WEDDING_WEBSITE_URL,
        'couple_name': settings.BRIDE_AND_GROOM,
        'wedding_location': settings.WEDDING_LOCATION,
        'wedding_date': settings.WEDDING_DATE,
    })
