from django.shortcuts import render
from coins.models import Coin
from coins.views import CoinViewSet
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.


# A dashboard to show users available coins 
# A search bar you can use to search for a specific coin
# Coin blocks with subscribe button 

def coin_list(request, *args, **kwargs):
    coins = CoinViewSet().get_queryset()
    paginator = Paginator(coins, 100) 
    page = request.GET.get('page')
    coins = paginator.get_page(page)
    try:
        coins = paginator.page(page)
    except PageNotAnInteger:
        coins = paginator.page(1)
    except EmptyPage:
        coins = paginator.page(paginator.num_pages)
    return render(request, 
                'frontpage/coin_list.html', 
                {'coins':coins})

    # return render(request, 'frontpage/coin_list.html', {"coins":coins})

def template(request):
    return render(request, 'frontpage/base.html', {})

def coin_list_interactive(request, *args, **kwargs):
    coin_list = CoinViewSet().get_queryset()
    # Show 40 contacts per page
    paginator = Paginator(coin_list, 40) 
    page = request.GET.get('page')
    coins = paginator.get_page(page)
    try:
        coins = paginator.page(page)
    except PageNotAnInteger:
        coins = paginator.page(1)
    except EmptyPage:
        coins = paginator.page(paginator.num_pages)
    return render(request, 
                'frontpage/test.html', 
                {'coins':coins})
