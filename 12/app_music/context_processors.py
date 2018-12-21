from django.conf import settings


def get_settings_value(request):
	return {'MEDIA_URL': settings.MEDIA_URL}