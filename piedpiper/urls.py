from django.conf import settings
from django.urls import path, re_path, include, reverse_lazy
from django.conf.urls.static import static
from django.contrib import admin

from rest_framework.authtoken import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api-token-auth/', views.obtain_auth_token),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('rest-auth/', include('rest_auth.urls')),
    path('api/v1/user/', include('piedpiper.users.urls')),
     path('api/v1/tweet/', include('piedpiper.tweet.urls')),

    # the 'api-root' from django rest-frameworks default router
    # http://www.django-rest-framework.org/api-guide/routers/#defaultrouter
    re_path(r'^$',TemplateView.as_view(template_name='index.html'), name='home'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
