from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import EmptyPage,PageNotAnInteger, Paginator
from .models import Listing
from .models import Realtor
from listings.choices import *



def index(request):
    listings=Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings,3)
    page=request.GET.get('page')
    paged_listings=paginator.get_page(page)
    context={
        'listings': paged_listings,
        'states': state_choices,
        'bedroom': bedroom_choices,
        'price': price_choices,
    }
    return render(request,'pages/index.html',context)


def about(request):
    realtors=Realtor.objects.all()
    mvp=Realtor.objects.filter(is_mvp=True)
    print(realtors,mvp)
    context={
        'realtors':realtors,
        'mvp': mvp,
    }
    return render(request,'pages/about.html',context)