from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
# swagger
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


from . import settings

# swagger
from .views import Home

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="movie site swagger",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('applications.user.urls')),
    path('api/v1/category/', include('applications.category.urls')),
    path('api/v1/movie/', include('applications.movie.urls')),
    path('api/v1/review/', include('applications.review.urls')),

    path('api/v1/swagger(.json|.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('api/v1/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # reset password
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('accounts/', include('allauth.urls')),
    path('google/', Home.as_view(), name='home'), # new
    path('', include('chat.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


    path('', include('chat.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

