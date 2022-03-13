from django.urls import path
from . import views  #引用這個資料夾中的views檔案
urlpatterns = [
    path('temp_search', views.TPS, name = "Temp_search"),
    path('temp_search/linechart',views.linechart,name="Linechart"),
    path('',views.home, name='Home'),
    path('piechart',views.piechart ,name='Piechart'),
    path('test',views.test,name='Timepick'),
    
]
 