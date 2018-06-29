from django.conf.urls import url
from assets import views
#from assets.views import ReportView
from .views import *
app_name = 'assets'

urlpatterns = [
    url(r'^report/', views.report, name='report'),
    url(r'^dashboard/', DashboardView.as_view(), name='dashboard'),
    url(r'^index/', IndexView.as_view(), name='index'),
    url(r'^detail/(?P<asset_id>[0-9]+)/$', DetailView.as_view(), name='detail'),
    url(r'^$', DashboardView.as_view())
]