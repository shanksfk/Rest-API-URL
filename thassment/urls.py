
from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('sorted', viewPosts.as_view()),
    path('sor/<int:input>', viewPostDetails.as_view(), name='sorted'),
    path('search/', filter_search, name='search'),
    path('post-top/', sort_top, name='top'),

    re_path('^sor/(?P<title>.+)/$', viewPostDetails.as_view()),
    #     path('s', list_posts),
]
