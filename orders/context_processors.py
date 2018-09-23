from .models import ProductBasket

def getting_basket_info(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    products_in_basket = ProductBasket.objects.filter(session_key=session_key, is_active=True,order__isnull=True)
    products_total_nmb = products_in_basket.count()

    return locals()