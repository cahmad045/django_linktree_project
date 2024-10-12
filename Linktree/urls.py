from django.urls import path
from .views import Link_class_view, Link_create_view, Link_update_view, Link_delete_view, profile_view
urlpatterns = [
    path('', Link_class_view.as_view(), name='link_list'),
    path('link/create', Link_create_view.as_view(), name='link_create'),
    path('link/<int:pk>/update', Link_update_view.as_view(), name='link_update'),
    path('link/<int:pk>/delete', Link_delete_view.as_view(), name='link_delete'),
    path('<str:profile_slug>/', profile_view, name='profile'),
]