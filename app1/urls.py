from django.urls import path
from .views import AisatsuView

urlpatterns = [
    path("",AisatsuView.as_view(),name="aisatsu"),
]