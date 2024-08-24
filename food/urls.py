from . import views
from django.urls import path

app_name='food'
urlpatterns = [
    path('',views.IndexClassView.as_view(),name='index'),
    path('<int:pk>/',views.FoodDetails.as_view(),name='detail'),
    path('items/',views.items,name='item'),
    path('addfood/',views.CreateItem.as_view(),name='addfood'),
    path('update/<int:id>/',views.update_item,name='update_item'),
    path('delete/<int:id>/',views.delete_item,name='delete_item')
]
