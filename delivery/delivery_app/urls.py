from django.urls import path
from .views import *


app_name = 'env_delivery'
urlpatterns = [
    path('medicine/', MedicineCreateView.as_view()),
    path('umedicine/<int:pk>', MedicineUpdateView.as_view()),
    path('order/', MakeOrderView.as_view()),
    path('list/', ListOrderView.as_view()),


]