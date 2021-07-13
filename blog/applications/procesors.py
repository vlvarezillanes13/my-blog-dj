from applications.home.models import Home


def home_contact(request):
    home = Home.objects.latest('created')

    return {
        'phone':home.phone,
        'email':home.about_emil,
    }