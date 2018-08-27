"""mysite URL Configuration

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
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # whenever django encounters an include() function it chops off whatever part of the URL matched up to that point and sends the remaining string to the included URLconf for further processing.
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),

    #  path() function is passed 4 arguments:
    # - (2 required) route and view
    # - kwargs and name
    # name - naming of URLs, allows them to be referred to unambiguously from elsewhere, especially within templates
]

"""
Another way is to include additional URL patterns - list of path() instances eg.

from django.urls import include, path

from apps.main import views as main_views
from credit import views as credit_views

extra_patterns = [
    path('reports/', credit_views.report),
    path('reports/<int:id>/', credit_views.report),
    path('charge/', credit_views.charge),
]

urlpatterns = [
    path('', main_views.homepage),
    path('help/', include('apps.help.urls')),
    path('credit/', include(extra_patterns)),
]

Here, /credit/reports will be handled by credit_views.report
"""
