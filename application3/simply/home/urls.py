from django.urls import path
from . views import *

urlpatterns = [
    path('', home, name = 'home'),

    # path('health/', health),

    path('health/startup/', startup),
    path('health/ready/', readiness),
    path('health/live/', liveness),

    path('register/', register, name = 'register'),
    path('login/', login, name = 'login'),
    path('logout/', logout, name = 'logout'),
]