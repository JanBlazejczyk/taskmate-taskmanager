from django.contrib import admin
from django.urls import path, include
from todolist import views as todolist_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todolist_views.home, name='home'),
    path('task/', include('todolist.urls')),
    path('contact/', todolist_views.contact, name='contact'),
    path('about/', todolist_views.about, name='about')
]
