from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage,PageNotAnInteger, Paginator

from .models import Listing
from listings.choices import *

# Create your views here.
def index(request):
    listings=Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings,2)
    page=request.GET.get('page')
    paged_listings=paginator.get_page(page)
    context={
        'listings':paged_listings,
    }
    return render(request,'listings/listings.html', context)

def listing(request, listing_id):
    list_details=get_object_or_404(Listing, pk=listing_id)
    photos_check=(list_details.photo_1,list_details.photo_2,list_details.photo_3,list_details.photo_4,list_details.photo_5,list_details.photo_6)
    photo=[]
    for i in photos_check:
        if(i):
            photo.append(i.url)
    context={
        'list_details':list_details,
        'photo':photo,
    }
    return render(request,'listings/listing.html',context)

def search(request):
    query_listings=Listing.objects.order_by('-list_date')

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            query_listings=query_listings.filter(description__icontains=keywords)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            query_listings=query_listings.filter(city__iexact=city)

    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            query_listings=query_listings.filter(state__iexact=state)

    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            query_listings=query_listings.filter(bedrooms__lte=bedrooms)

    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            query_listings=query_listings.filter(price__lte=price)

    context={
        'listings': query_listings,
        'states': state_choices,
        'bedroom': bedroom_choices,
        'price': price_choices,
        'values':request.GET,
    }
    return render(request,'listings/search.html',context)