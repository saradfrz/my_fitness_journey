from django.urls import path
from myFitnessJourney.views import home_view


urlpatterns = [
    path('', home_view),
]