from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #path('', include("frontend.urls")),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('auth/', include('users.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('', include('values.urls'))
    # path('results/', include("results.urls")),
    # path('lists', include("lists.urls")),
    #path('', include("frontend.urls"))
]
