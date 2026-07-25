from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name='getRoutes'),
    path('products/', views.getProducts, name='getProducts'),
    path('product/<str:pk>/', views.getProduct, name='getProduct'),
    path('users/login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/profile/', views.getUserProfile, name='getUserProfile'),
    path('users/', views.getUsers, name='getUsers'),
    path('users/register/', views.registerUser, name='registerUser'),
    path('activate/<uidb64>/<token>',views.ActivateAccountView.as_view(),name='active'),
    path("cart/", views.get_cart),
    path("cart/add/", views.add_to_cart),
    path("cart/remove/<int:product_id>/", views.remove_from_cart),
]
