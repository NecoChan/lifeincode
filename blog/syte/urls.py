from django.urls import path
from . import views
app_name = 'syte'
urlpatterns = [
 # post views
 path('', views.post_list, name='post_list'),
 path('<int:year>/<int:month>/<int:day>/<slug:post>/',
 views.post_detail, name='post_detail'),
 path('book/',views.book, name='book_list'),
]
