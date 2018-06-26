from django.conf.urls import url
from assets import views
#from assets.views import ReportView

app_name = 'assets'

urlpatterns = [
    url(r'^report/', views.report, name='report'),
]