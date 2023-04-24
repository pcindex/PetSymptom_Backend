from django.urls import path

from . import views

#URL path to query the BERT Model. URL resolves to */machinelearning/query and takes URL arguments

urlpatterns = [path('',views.query.as_view(), name='query'),] #path to query ML model