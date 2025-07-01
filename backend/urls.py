
from django.contrib import admin
from django.urls import path, include
from loginapp.views import login_view  # Asegúrate de importar tu vista

urlpatterns = [
    path('admin/', admin.site.urls),
     path('login/', login_view, name='login'),
]
