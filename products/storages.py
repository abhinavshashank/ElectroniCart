from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.exceptions import ImproperlyConfigured

PROTECTED_MEDIA = getattr(settings, 'PROTECTED_MEDIA', None)
if PROTECTED_MEDIA == None:
    raise ImproperlyConfigured("Protected media is not set in settings")

class ProtectedStorage(FileSystemStorage):
    location = PROTECTED_MEDIA