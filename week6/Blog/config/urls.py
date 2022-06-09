"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls.conf import include
from django.contrib import admin
from django.urls import path
from blog.views_blog import BlogListView


urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Blog
    path('', BlogListView.as_view()),
    path('blog/', include('blog.urls_blog')),
    path('article/', include('blog.urls_article')),
]
