from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def get_paginated_list(lst, num_objects_on_page, page):
    paginator = Paginator(lst, num_objects_on_page)

    try:
        paginated_list = paginator.page(page)
    except PageNotAnInteger:
        paginated_list = paginator.page(1)
    except EmptyPage:
        paginated_list = paginator.page(paginator.num_pages)

    return paginated_list
