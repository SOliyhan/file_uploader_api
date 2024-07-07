import os
import requests
from io import StringIO
import pandas as pd
from dateutil.parser import parse as date_parse
from rest_framework.views import APIView
from django.http import JsonResponse
from .models import Game
from .serializers import GameSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from django.db import models

from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny


file_dir = os.path.dirname(os.path.realpath('__file__'))
parent_dir = os.path.dirname(file_dir)
file_name = "demo.csv"
file_path = os.path.join(parent_dir, file_name)


class HomepageView(APIView):
    permission_classes= [AllowAny]
    def get(self, request):
        return JsonResponse({'message': 'Welcome to the File Uploader API. Read documentation on github for more details'}, status=200)


class UploadCSV(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        
        file_url = request.data.get("file_url")
     
        if not file_url:
            return JsonResponse({"error":"no file url provided"}, status=400)
        
        csv_url = file_url.replace("/edit?gid=","/export?format=csv&gid=")

        try:
            response = requests.get(csv_url)
            response.raise_for_status()

        except Exception as e:
            return JsonResponse({"error": e}, status=400)
        
        if response.status_code !=200:
                return JsonResponse({'message': 'Failed to download file'}, status=400)
        
        
        csv_data = StringIO(response.text)
        df = pd.read_csv(csv_data)

        Game.objects.all().delete()
        
        for _, row in df.iterrows():
            date_str = row['Release date']  
            date_obj = date_parse(date_str, fuzzy=True).date()
            print(date_str, date_obj)

            serializer = GameSerializer(data={
                "app_id": row["AppID"],
                "name": row["Name"],
                "release_date": date_obj,
                "required_age": row["Required age"],
                "price": row["Price"],
                "dlc_count": row["DLC count"],
                "about_the_game": row["About the game"],
                "supported_languages": row["Supported languages"],
                "on_windows": row["Windows"],
                "on_mac": row["Mac"],
                "on_linux": row["Linux"],
                "positive": row["Positive"],
                "negative": row["Negative"],
                "score_rank": row["Score rank"],
                "developers": row["Developers"],
                "publishers": row["Publishers"],
                "categories": row["Categories"],
                "genres": row["Genres"],
                "tags": row["Tags"],
            })

            if not serializer.is_valid(raise_exception=True):
                return JsonResponse({'Validation error': {serializer.errors}}, status=500)
            
            serializer.save()

        return JsonResponse({'message': 'File uploaded successfully'}, status=200)
    

class SearchCSV(APIView):
    permission_classes = [IsAuthenticated] 

    def get(self, request):
        field_name = request.data.get('field')
        field_value = request.data.get('value')

        if not field_name or not field_value:
            return JsonResponse({'error': 'Missing required parameters: field and value'}, status=400)

        try:
            field = Game._meta.get_field(field_name)
            
        except AttributeError:
            return JsonResponse({'error': f'Invalid field name: {field_name}'}, status=400)

        filters = Q()
        if isinstance(field, models.CharField):
            filters = Q(**{f"{field_name}__icontains": field_value})
        elif isinstance(field, (models.IntegerField, models.FloatField, models.DecimalField, models.DateField)):
            filters = Q(**{field_name: field_value}) 
        else:
            print(filters)
            return JsonResponse({'error': 'Unsupported field type'}, status=400)
            
        queryset = Game.objects.filter(filters)

        serializer = GameSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)
