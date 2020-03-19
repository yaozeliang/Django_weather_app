from django.urls import path
from . import views

urlpatterns = [
    path('list/',views.book_list),
    path('detail/<book_id>/',views.book_detail),
    path('publisher/<int:pub_id>/',views.publish_detail),
    path('author/',views.author_detail)
]



