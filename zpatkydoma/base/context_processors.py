from django.conf import settings # import the settings file

def custom_settings(request):
    return {'tracking_environment': settings.TRACKING_ENVIRONMENT}
