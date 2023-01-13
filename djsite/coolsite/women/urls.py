from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', WomenHome.as_view(), name='home'),
    #path('', index, name='home'),#представление функция
    path('about/', about, name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
#    path('category/<int:cat_id', show_category, name='category'),
    path('category/<slug:cat_slug>/', WomenCategory.as_view(), name='category'),
    path('register/', login, name=login),
]
