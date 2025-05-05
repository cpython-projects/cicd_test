from .models import SocialNetwork


def social_networks(request):
    links = SocialNetwork.objects.all()
    context = {
        'social_network_links': links,
    }

    return context