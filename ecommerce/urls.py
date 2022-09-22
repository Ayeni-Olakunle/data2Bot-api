from ecommerce import views
from django.urls import path


urlpatterns = [
    path('create/order', views.post_get, name="Create and Get"),
    path('order/editing/<int:id>', views.update_link, name="Edit Order and Delete Order"),
]

# from ecommerce import views
# from django.urls import path

# urlpatterns = [
#     path("create", views.CreateOrderAPIView.as_view(), name="orders"),
#     # path("login", views.LoginApiView.as_view(), name="login"),
# ]