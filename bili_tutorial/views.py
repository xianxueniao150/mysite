from django.shortcuts import render
import datetime
from django.db.models import Sum
from django.utils import timezone
from blog.models import ReadDetail, Blog
from django.core.cache import cache


def home(request):
    hot_blogs_for_7_days = cache.get("hot_blogs_for_7_days")
    if hot_blogs_for_7_days is None:
        hot_blogs_for_7_days = get_7_days_hot_data()
        cache.set("hot_blogs_for_7_days", hot_blogs_for_7_days, 3600)


    dates, read_nums = get_seven_days_read_data()
    context = {}
    context["dates"] = dates
    context['read_nums'] = read_nums
    context["today_hot_data"] = get_today_hot_data()
    context["yesterday_hot_data"] = get_yesterday_hot_data()
    context["hot_blogs_for_7_days"] = hot_blogs_for_7_days
    return render(request, 'home.html', context)


def get_seven_days_read_data():
    today = timezone.now().date()
    read_nums = []
    dates = []
    for i in range(7, 0, -1):
        date = today - datetime.timedelta(days=i)
        dates.append(date.strftime("%m/%d"))
        read_details = ReadDetail.objects.filter(date=date)
        result = read_details.aggregate(read_num_sum=Sum('read_detail_num'))
        read_nums.append(result['read_num_sum'] or 0)
    return dates, read_nums


def get_today_hot_data():
    today = timezone.now().date()
    read_details = ReadDetail.objects.filter(date=today).order_by('-read_detail_num')
    return read_details[:7]

def get_yesterday_hot_data():
    today = timezone.now().date()
    yesterday = today - datetime.timedelta(days=1)
    read_details = ReadDetail.objects.filter(date=yesterday).order_by('-read_detail_num')
    return read_details[:7]


# def get_7_days_hot_data():
#     today = timezone.now().date()
#     date = today - datetime.timedelta(days=7)
#       read_details = ReadDetail.objects\
#                                .filter(date__lt=today, date__gte=date) \
#                                .values('blog') \
#                                .annotate(read_num_sum=Sum('read_detail_num')) \
#                                .order_by('-read_num_sum')
#     return read_details[:7]

def get_7_days_hot_data():
    today = timezone.now().date()
    date = today - datetime.timedelta(days=7)
    read_details = Blog.objects\
                       .filter(read_detail_num__date__lt=today, read_detail_num__date__gte=date) \
                       .annotate(read_num_sum=Sum('read_detail_num__read_detail_num')) \
                       .order_by('-read_num_sum')
    return read_details[:7]


