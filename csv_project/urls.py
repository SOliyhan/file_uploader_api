from django.contrib import admin
from django.urls import path, include
from csv_app.views import HomepageView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('csv_app.urls')),
    path('', HomepageView.as_view(), name='home'),
    path('api/token/', TokenObtainPairView.as_view(), name='access-token'),
    path('api/token/refresh/'\
         , TokenRefreshView.as_view(), name='refresh-token'),
]

