from functools import reduce
import operator

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from watson import search
from .models import Box, Activity, Category, SubZone, UserBookmark, UserRating, FeaturedActivity, UserReview

def index_view(request):
    boxes = Box.objects.all()
    featured_set = FeaturedActivity.objects.all()

    if featured_set.count() > 0:
        featured = featured_set[0]

    return render(request, 'outingbox/index.html', {'boxes': boxes, 'featured': featured})

def get_nearby(request):
    lat = None
    lon = None
    if request.method == 'GET':
        lat = request.GET.get('lat', None)
        lon = request.GET.get('lon', None)

    return HttpResponse("OK")

def contact_us_view(request):
    return render(request, 'outingbox/contact-us.html')

def about_us_view(request):
    return render(request, 'outingbox/about-us.html')

def box_view(request):
    return render(request, 'outingbox/about-us.html')

def activity_view(request, id=None, title=None):
    activity = get_object_or_404(Activity, pk=id)

    user_bookmarks = None
    user_rating = 0
    if request.user.is_authenticated():
        try:
            user_bookmark_inst = UserBookmark.objects.get(user=request.user)
            user_bookmarks = user_bookmark_inst.bookmarks.all()
        except UserBookmark.DoesNotExist:
            pass

        try:
            user_rating_inst = UserRating.objects.get(user=request.user, activity=activity)
            user_rating = user_rating_inst.rating
        except UserRating.DoesNotExist:
            pass

    reviews = [review_inst.review for review_inst in UserReview.objects.filter(activity=activity)]

    context = {
        'activity': activity, 
        'bookmarks': user_bookmarks, 
        'photos': activity.photos.all(),
        'reviews': reviews,
        'user_rating': user_rating
    }

    return render(request, 'activity/activity.html', context)

@login_required
def profile_view(request):
    return render(request, 'account/profile.html', {});

@csrf_protect
@require_POST
def rate_activity(request):
    if not request.is_ajax():
        res = JsonResponse({'msg': 'not ajax request', 'status': '1'})
        res.status_code = 400
        return res

    if not request.user.is_authenticated():
        res = JsonResponse({'msg': 'not authenticated', 'status': '-1'})
        res.status_code = 400
        return res

    activity_id = request.POST.get("id", None)
    if activity_id is None:
        res = JsonResponse({'msg': 'invalid id', 'status': '1'})
        res.status_code = 400
        return res

    try:
        activity = Activity.objects.get(pk=activity_id)
    except Activity.DoesNotExist:
        res = JsonResponse({'msg': 'activity doesnt exist', 'status': '1'})
        res.status_code = 400
        return res

    rating = int(request.POST.get("new_rating", 0))
    if (rating > 5) or (rating <= 0):
        res = JsonResponse({'msg': 'invalid rating', 'status': '1'})
        res.status_code = 400
        return res

    old_rating = None
    try:
        user_rating_inst = UserRating.objects.get(user=request.user, activity=activity)
        old_rating = user_rating_inst.rating
    except UserRating.DoesNotExist:
        user_rating_inst = UserRating(user=request.user, activity=activity)

    if old_rating is None:
        user_rating_inst.rating = rating
        user_rating_inst.save()

        activity.rating = (activity.rating*activity.votes+rating)/(activity.votes+1)
        new_rating = activity.rating
        activity.votes = activity.votes + 1
        activity.save()
    elif old_rating != rating:
        user_rating_inst.rating = rating
        user_rating_inst.save()

        activity.rating = (activity.rating*activity.votes - old_rating + rating)/(activity.votes)
        new_rating = activity.rating
        activity.save()
    else:
        new_rating = old_rating

    return JsonResponse({'msg': 'ok', 'status': '0', 'new_rating': 'new_rating'})

@csrf_protect
@require_POST
def bookmark_activity(request):
    if not request.is_ajax():
        res = JsonResponse({'msg': 'not ajax request', 'status': '1'})
        res.status_code = 400
        return res

    if not request.user.is_authenticated():
        res = JsonResponse({'msg': 'not authenticated', 'status': '-1'})
        res.status_code = 400
        return res

    activity_id = request.POST.get("id", None)
    if activity_id is None:
        res = JsonResponse({'msg': 'invalid id', 'status': '1'})
        return res

    try:
        activity = Activity.objects.get(pk=activity_id)
    except Activity.DoesNotExist:
        res = JsonResponse({'msg': 'activity doesnt exist', 'status': '1'})
        return res

    user_bookmark_inst, created = UserBookmark.objects.get_or_create(user=request.user)

    delete_bookmark = request.POST.get('delete', None)
    if delete_bookmark:
        user_bookmark_inst.bookmarks.remove(activity)
    else:
        user_bookmark_inst.bookmarks.add(activity)
    
    return JsonResponse({'msg': 'ok', 'status': '0'})

@csrf_protect
@require_POST
def comment_activity(request):
    if not request.is_ajax():
        res = JsonResponse({'msg': 'not ajax request', 'status': '1'})
        res.status_code = 400
        return res

    if not request.user.is_authenticated():
        res = JsonResponse({'msg': 'not authenticated', 'status': '-1'})
        res.status_code = 400
        return res

    activity_id = request.POST.get("id", None)
    if activity_id is None:
        res = JsonResponse({'msg': 'invalid id', 'status': '1'})
        return res

    try:
        activity = Activity.objects.get(pk=activity_id)
    except Activity.DoesNotExist:
        res = JsonResponse({'msg': 'activity doesnt exist', 'status': '1'})
        return res

    try:
        user_review_inst = UserReview.objects.get(user=request.user, activity=activity)
        old_review = user_review_inst.review
    except UserReview.DoesNotExist:
        user_review_inst = UserReview(user=request.user, activity=activity)

    review = request.POST.get("review", None)
    if review is None:
        res = JsonResponse({'msg': 'invalid comment', 'status': '1'})
        return res

    user_review_inst.review = review
    user_review_inst.pub_date = timezone.now()
    user_review_inst.save()

    return JsonResponse({'msg': 'ok', 'status': '0'})


order_dict = {
    'raa': 'rating',    # Rating ascending
    'rad': '-rating',   # Rating descending
    'pra': 'cost',     # Price ascending
    'prd': '-cost'     # Price descending
}

# Ensure _new_params to be a dictionary
def add_param_to_request_url(request, _new_params):
    _dict = request.GET.copy()
    _dict.update(_new_params)

    return reverse('search')+'?'+_dict.urlencode()

def get_filter_url(request, order_by):
    _dict = request.GET.copy()
    _dict['page'] = 1
    _dict['ob'] = order_by

    return reverse('search')+'?'+_dict.urlencode()

def filter_list_in_model(query_set, filter_lst):
    Q_lst = [Q(id=id) for id in filter_lst]

    return query_set.filter(reduce(operator.or_, Q_lst))

def search_view(request):
    query = request.GET.get('query', '')
    page  = request.GET.get('page', 1)
    order_by = request.GET.get('ob', '')
    sub_zones_selected_list = request.GET.getlist('sz', '')
    categories_selected_list = request.GET.getlist('c', '')

    sub_zone_list = SubZone.objects.all_name_value_list()
    category_list = Category.objects.all_name_value_list()

    activities = Activity.objects.all()

    if sub_zones_selected_list:
        activities = filter_list_in_model(activities, map(int, sub_zones_selected_list))

    if categories_selected_list:
        activities = filter_list_in_model(activities, map(int, categories_selected_list))

    if query:
        activities = search.filter(activities, query)

    if order_by:
        activities = activities.order_by(order_dict[order_by])

    results_paginator = Paginator(activities, 10)
    try:
        results_page = results_paginator.page(page)
    except PageNotAnInteger:
        results_page = results_paginator.page(1)
    except:
        results_page = results_paginator.page(results_paginator.num_pages)

    activities = results_page

    order_by_relevance_url = get_filter_url(request, '')
    order_by_rating_url = get_filter_url(request, 'rad')
    order_by_price_url = get_filter_url(request, 'pra')

    url_prev_page_number = None
    url_next_page_number = None

    if activities.has_previous():
        url_prev_page_number = add_param_to_request_url(request, {'page': activities.previous_page_number()})

    if activities.has_next():
        url_next_page_number = add_param_to_request_url(request, {'page': activities.next_page_number()})

    bookmarks = None
    if request.user.is_authenticated():
        try:
            user_bookmark_inst = UserBookmark.objects.get(user=request.user)
            bookmarks = user_bookmark_inst.bookmarks.all()
        except UserBookmark.DoesNotExist:
            pass

    context = {
        'activities': activities,
        'order_by_relevance_url': order_by_relevance_url,
        'order_by_rating_url': order_by_rating_url,
        'order_by_price_url': order_by_price_url,
        'url_next_page_number': url_next_page_number,
        'url_prev_page_number': url_prev_page_number,
        'sub_zone_list': sub_zone_list,
        'category_list': category_list,
        'sub_zones_selected_list': sub_zones_selected_list,
        'categories_selected_list': categories_selected_list,
        'query': query,
        'page': page,
        'bookmarks': bookmarks
    }

    return render(request, 'search/search.html', context)
