from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('applications.account.urls')),
    path('api/v1/category/', include('applications.category.urls')),
    path('api/v1/movie/', include('applications.movie.urls')),
    path('api/v1/review/', include('applications.review.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)