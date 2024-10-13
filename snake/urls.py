from django.urls import path
from .views import SnakeList, SnakeDetail

urlpatterns = [
  path("", SnakeList.as_view(), name="snake_list"),
  path("<int:pk>/", SnakeDetail.as_view(), name="snake_detail"),
]
