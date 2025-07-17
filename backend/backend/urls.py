
from django.contrib import admin
from django.urls import path, include
from loginapp.views import login_view  # Asegúrate de importar tu vista

from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
     path('login/', login_view, name='login'),
      path('', TemplateView.as_view(template_name='index.html')),
]
