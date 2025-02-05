"""
URL configuration for ecommerce_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products import views as product_views
from rest_framework_simplejwt import views as jwt_views
from django.http import HttpResponse

# Setting up the router for the API
router = DefaultRouter()
router.register(r'products', product_views.ProductViewSet, basename='product')
router.register(r'categories', product_views.CategoryList, basename='category')

# Root view for the homepage (to avoid 404 at '/')
def home(request):
    return HttpResponse("Welcome to the Ecommerce API!")

# Combined URL patterns
urlpatterns = [
    path('', home),  # Root URL path to home view
    path('admin/', admin.site.urls),  # Admin URL
    path('api/', include(router.urls)),  # API URLs
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),  # DRF auth URLs
]
