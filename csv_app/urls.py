from django.urls import path
from .views import UploadCSV, SearchCSV

urlpatterns = [
    path('upload', UploadCSV.as_view(), name='upload-csv'),
    path('search', SearchCSV.as_view(), name='search'),

]
