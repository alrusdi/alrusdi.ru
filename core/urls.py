"""alrusdi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
import os

from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static


from content.views import IndexView, PageView
from notes.views import NotesListView

urlpatterns = [
    path('tinymce/', include('tinymce.urls')),
    path('admin/', admin.site.urls),
    path('pwd/', NotesListView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static('/static/', document_root=os.path.join(settings.BASE_DIR, 'static'))

urlpatterns.append(path('<slug:slug>/', PageView.as_view()))
urlpatterns.append(path('', IndexView.as_view()))
