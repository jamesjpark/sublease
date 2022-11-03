from django.urls import include, path
from rest_framework import routers
from post import urls as post_urls
from auth import urls as auth_urls
router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('post/', include(post_urls)),
    path('auth/', include(auth_urls)),

]