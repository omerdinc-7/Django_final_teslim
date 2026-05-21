from django.urls import path
from django.http import HttpResponseServerError


def _call_view(module_name, view_name):
    """Return a view callable that imports and calls the real view at runtime."""

    def _inner(request, *args, **kwargs):
        try:
            module = __import__(module_name, fromlist=[view_name])
            view = getattr(module, view_name)
            return view(request, *args, **kwargs)
        except Exception as e:
            return HttpResponseServerError(f'Error loading view {module_name}.{view_name}: {e}')

    return _inner


urlpatterns = [
    path('', _call_view('contact.views', 'index'), name='contact_index'),
    # BURAYI DEĞİŞTİRDİK: 'contact/' yerine 'form/' yazdık
    path('form/', _call_view('contact.views', 'contact_form'), name='contact'),

    # BURAYI DEĞİŞTİRDİK: 'contact/contact_form' yerine 'submit/' yazdık
    path('submit/', _call_view('contact.views', 'contact_form'), name='contact_form'),
]