from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, Http404
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.core.urlresolvers import reverse
from django.utils import timezone
from watson import search
from .models import Box, Activity, Category, SubZone, UserBookmark, UserRating, FeaturedActivity, UserReview
from .forms import FeedbackForm
from .decorators import require_user_authenticated, require_activity
from .utils import get_paginated_list

def handler404(request):
    return render(request, 'outingbox/404.html', {})

def handler500(request):
    return render(request, 'outingbox/500.html', {})

def index_view(request):
    boxes = Box.objects.all()
    featured_set = FeaturedActivity.objects.all()

    featured = []
    if featured_set.count() > 0:
        featured = featured_set[0]

    return render(request, 'outingbox/index.html', {'boxes': boxes, 'featured': featured})

def contact_us_view(request):
    if request.method == 'GET':
        form = FeedbackForm()
    else:
        form = FeedbackForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('feedback-thanks'))

    return render(request, 'outingbox/contact-us.html', {'form': form})

def contact_us_thanks(request):
    return render(request, 'outingbox/contact-us.html', {'thanks': True})

def about_us_view(request):
    return render(request, 'outingbox/about-us.html')

def box_view(request, id=None, title=None):
    try:
        id = int(id)
    except ValueError:
        raise Http404("Box doesn't exist")

    box = get_object_or_404(Box, pk=id)
    categories = box.category_set.all()

    # Create a set in order to have only distinct activities
    # This is required because multiple boxes can have the same activity
    activity_set = set()
    for category in categories:
        activity_set.update(category.activity_set.all())

    # Default to page 1
    page = request.GET.get('page', 1)
    activities = get_paginated_list(list(activity_set), 12, page)

    url_prev_page_number = None
    if activities.has_previous():
        url_prev_page_number = add_page_to_request_url(request, 'box', {'page': activities.previous_page_number()}, kwargs={'id':id, 'title':box.title})
    
    url_next_page_number = None
    if activities.has_next():
        url_next_page_number = add_page_to_request_url(request, 'box', {'page': activities.next_page_number()}, kwargs={'id':id, 'title':box.title})

    return render(request, 'box/box.html', {
        'box': box, 
        'activities': activities,
        'url_next_page_number': url_next_page_number,
        'url_prev_page_number': url_prev_page_number
    })

@login_required
def profile_bookmarks_view(request):
    try:
        user_bookmark_inst = UserBookmark.objects.get(user=request.user)
        bookmarks = user_bookmark_inst.bookmarks.all()
    except UserBookmark.DoesNotExist:
        bookmarks = []

    page = request.GET.get('page', 1)
    bookmarks = get_paginated_list(bookmarks, 12, page)

    url_prev_page_number = None
    if bookmarks.has_previous():
        url_prev_page_number = add_page_to_request_url(request, 'profile_bookmarks', {'page': bookmarks.previous_page_number()})
    
    url_next_page_number = None
    if bookmarks.has_next():
        url_next_page_number = add_page_to_request_url(request, 'profile_bookmarks', {'page': bookmarks.next_page_number()})

    return render(request, 'account/bookmarks.html', {
        'bookmarks': bookmarks,
        'url_next_page_number': url_next_page_number,
        'url_prev_page_number': url_prev_page_number
    })

def activity_view(request, id=None, title=None):
    try:
        id = int(id)
    except ValueError:
        raise Http404("Activity doesn't exist")

    activity = get_object_or_404(Activity, pk=id)

    user_bookmarks = None
    user_rating = 0
    user_review_inst = None
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

        try:
            user_review_inst = UserReview.objects.get(user=request.user, activity=activity)
            user_review = user_review_inst.review
        except UserReview.DoesNotExist:
            pass

    reviews = [review_inst for review_inst in UserReview.objects.filter(activity=activity)]

    context = {
        'activity': activity, 
        'bookmarks': user_bookmarks, 
        'photos': activity.photos.all(),
        'reviews': reviews,
        'user_rating': user_rating,
        'user_review': user_review_inst
    }

    return render(request, 'activity/activity.html', context)

@login_required
def profile_view(request):
    try:
        user_bookmark_inst = UserBookmark.objects.get(user=request.user)
        bookmarks = user_bookmark_inst.bookmarks.all()[:3]
    except UserBookmark.DoesNotExist:
        bookmarks = []

    return render(request, 'account/profile.html', {
        'bookmarks': bookmarks
    });

@csrf_protect
@require_POST
@require_user_authenticated
@require_activity
def rate_activity(request, activity):
    delete_rating = request.POST.get('delete', None)
    if delete_rating:
        try:
            user_rating_inst = UserRating.objects.get(user=request.user, activity=activity)
            old_rating = user_rating_inst.rating

            if activity.votes == 1:
                activity.rating = 0
            else:
                activity.rating = (activity.rating*activity.votes - old_rating)/(activity.votes-1)

            activity.votes = activity.votes - 1
            activity.save()
            user_rating_inst.delete()
        except UserRating.DoesNotExist:
            pass
        
        return JsonResponse({'msg': 'ok', 'status': '0'})

    rating = int(request.POST.get('new_rating', 0))
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
        activity.votes = activity.votes + 1
        activity.save()
    elif old_rating != rating:
        user_rating_inst.rating = rating
        user_rating_inst.save()

        activity.rating = (activity.rating*activity.votes - old_rating + rating)/(activity.votes)
        activity.save()

    return JsonResponse({'msg': 'ok', 'status': '0'})

@csrf_protect
@require_POST
@require_user_authenticated
@require_activity
def bookmark_activity(request, activity):
    user_bookmark_inst, created = UserBookmark.objects.get_or_create(user=request.user)

    delete_bookmark = request.POST.get('delete', None)
    if delete_bookmark:
        user_bookmark_inst.bookmarks.remove(activity)
    else:
        user_bookmark_inst.bookmarks.add(activity)
    
    return JsonResponse({'msg': 'ok', 'status': '0'})

@csrf_protect
@require_POST
@require_user_authenticated
@require_activity
def comment_activity(request, activity):
    delete_review = request.POST.get('delete', None)
    if delete_review:
        try:
            user_review_inst = UserReview.objects.get(user=request.user, activity=activity)
            user_review_inst.delete()
        except UserReview.DoesNotExist:
            pass

        return JsonResponse({
            'msg': 'ok',
            'status': '0'
        })

    review = request.POST.get('review', '')
    if not review or len(review) > 512:
        res = JsonResponse({'msg': 'comment too long/short', 'status': '1'})
        return res

    try:
        user_review_inst = UserReview.objects.get(user=request.user, activity=activity)
    except UserReview.DoesNotExist:
        user_review_inst = UserReview(user=request.user, activity=activity)

    user_review_inst.review = review
    user_review_inst.pub_date = timezone.now()
    user_review_inst.is_published = True
    user_review_inst.save()

    date_format = '%b. %d, %Y'
    return JsonResponse({
        'msg': 'ok',
        'status': '0',
        'date': user_review_inst.pub_date.strftime(date_format),
        'username': request.user.username
    })

# Ensure _new_params to be a dictionary
def add_page_to_request_url(request, view_name, _new_params, kwargs=None):
    _dict = request.GET.copy()

    # Django query dict update method appends instead of replacing the value if a key is present in both dicts
    # Therefore remove page from original dict
    try:
        _dict.pop('page')
    except KeyError:
        pass

    _dict.update(_new_params)
    return reverse(view_name, kwargs=kwargs)+'?'+_dict.urlencode()

def get_search_filter_urls(request, order_by):
    _dict = request.GET.copy()
    _dict['page'] = 1
    _dict['ob'] = order_by

    return reverse('search')+'?'+_dict.urlencode()

def search_view(request):
    query = request.GET.get('query', '')
    page  = request.GET.get('page', 1)
    order_by = request.GET.get('ob', '')
    sub_zones_selected_list = request.GET.getlist('sz', [])
    categories_selected_list = request.GET.getlist('c', [])

    sub_zone_list = SubZone.objects.all_name_value_list()
    category_list = Category.objects.all_name_value_list()

    activities = Activity.objects.all()

    int_sub_zones_selected_list = []
    if sub_zones_selected_list:
        for sub_zone in sub_zones_selected_list:
            try:
                int_sub_zone = int(sub_zone)
                int_sub_zones_selected_list.append(int_sub_zone)
            except ValueError:
                raise Http404("No results")

        activities = activities.filter(address__sub_zone__in=int_sub_zones_selected_list)
    
    int_categories_selected_list = []
    if categories_selected_list:
        for category in categories_selected_list:
            try:
                int_category = int(category)
                int_categories_selected_list.append(int_category)
            except ValueError:
                raise Http404("No results")

        activities = activities.filter(category__in=int_categories_selected_list)

    if query:
        activities = search.filter(activities, query)

    order_dict = {
        'raa': 'rating',   # Rating ascending
        'rad': '-rating',  # Rating descending
        'pra': 'cost',     # Price ascending
        'prd': '-cost'     # Price descending
    }
    if order_by:
        activities = activities.order_by(order_dict[order_by])

    results_paginator = Paginator(activities, 10)
    try:
        results_page = results_paginator.page(page)
    except PageNotAnInteger:
        results_page = results_paginator.page(1)
    except EmptyPage:
        results_page = results_paginator.page(results_paginator.num_pages)

    activities = results_page

    order_by_relevance_url = get_search_filter_urls(request, '')
    order_by_rating_url = get_search_filter_urls(request, 'rad')
    order_by_price_url = get_search_filter_urls(request, 'pra')

    url_prev_page_number = None
    url_next_page_number = None

    if activities.has_previous():
        url_prev_page_number = add_page_to_request_url(request, 'search', {'page': activities.previous_page_number()})

    if activities.has_next():
        url_next_page_number = add_page_to_request_url(request, 'search', {'page': activities.next_page_number()})

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
        'sub_zones_selected_list': int_sub_zones_selected_list,
        'categories_selected_list': int_categories_selected_list,
        'query': query,
        'page': page,
        'bookmarks': bookmarks
    }

    return render(request, 'search/search.html', context)
