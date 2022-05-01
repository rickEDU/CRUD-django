from django.urls import path
from .views import list_cao, create_cao, update_cao, delete_cao

urlpatterns = [
    path('', list_cao, name='list_cao'),
    path('novo', create_cao, name='create_cao'),
    path('update/<int:id>/', update_cao, name='update_cao'),
    path('delete/<int:id>/', delete_cao, name='delete_cao'),
]