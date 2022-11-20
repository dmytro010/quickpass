
from django.urls import path
from . import views
urlpatterns = [
    # path('', views.ContactView.as_view(), name="contact"),
    path('', views.send_secret_view, name="contact"),
]
