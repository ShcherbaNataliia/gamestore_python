"""
URL configuration for gamestore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls')
"""
from django.contrib import admin
from django.urls import path
from games import views
from django.conf.urls.static import static

from gamestore import settings

urlpatterns = [
                  path('', views.home, name='home'),
                  path('admin/', admin.site.urls),
                  path('add_publisher/', views.add_publisher, name='add_publisher'),
                  path('add_game/', views.add_game, name='add_game'),
                  path('game/<int:game_id>/', views.game_detail, name='game_detail'),
                  path('game/<int:game_id>/delete/', views.delete_game, name='delete_game'),
                  path('game/<int:game_id>/update/', views.update_game, name='update_game'),
                  path('publisher/<int:publisher_id>/', views.publisher_detail, name='publisher_detail'),
                  path('publisher/<int:publisher_id>/delete/', views.delete_publisher, name='delete_publisher'),
                  path('publisher/<int:publisher_id>/update/', views.update_publisher, name='update_publisher'),
                  path('publishers/', views.publishers, name='publishers'),
                  path('add_category/', views.add_category, name='add_category'),
                  path('categories/', views.categories, name='categories'),
                  path('category/<int:category_id>/', views.category_detail, name='category_detail'),
                  path('category/<int:category_id>/delete/', views.delete_category, name='delete_category'),
                  path('category/<int:category_id>/update/', views.update_category, name='update_category'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)