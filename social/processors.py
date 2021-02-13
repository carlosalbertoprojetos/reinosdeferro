from .models import Link


def context_processors_social(request):
    ctx_dict = {}
    links = Link.objects.all()
    for link in links:
        ctx_dict[link.chave] = link.url

    return ctx_dict
