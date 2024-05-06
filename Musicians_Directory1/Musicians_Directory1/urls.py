
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.HomeViewClass.as_view(),name="AddHome"),
    path("add/",include("album.urls")),
    path("add/",include("music.urls")),
    path("accounts/",include("author.urls")),
]
