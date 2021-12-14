
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from myapp import views
from .views import index
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),

    path('search/', include('myapp.urls'))
]
