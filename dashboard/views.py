from datetime import datetime
from django.shortcuts import render
import requests
from django.conf import settings
from django.contrib.auth.decorators import login_required, permission_required

def format_spanish_ampm(dt):
    hour_12 = dt.strftime("%I").lstrip("0")  # hora en 12h sin 0 inicial
    ampm = "a. m." if dt.hour < 12 else "p. m."
    return dt.strftime(f"%d/%m/%Y, {hour_12}:%M:%S {ampm}")

# Create your views here.
@login_required
@permission_required('dashboard.index_viewer', raise_exception=True)
def index(request):
    response = requests.get(settings.API_URL)  # URL de la API 'https://matiasdeveloper.pythonanywhere.com/landing/api/index/?format=json'
    posts = response.json()  # Convertir la respuesta a JSON

    # Número total de respuestas
    total_responses = len(posts)
    total_product1 = 0
    total_product2 = 0
    total_product3 = 0

    for key, value in posts.items():
        if "date" in value:
            dt = datetime.fromisoformat(value["date"].replace("Z", "+00:00"))
            value["formatted_date"] = format_spanish_ampm(dt)
        
        product_id = value.get("productID")
        if product_id == "product1":
            total_product1 += 1
        elif product_id == "product2":
            total_product2 += 1
        elif product_id == "product3":
            total_product3 += 1

    data = {
        'title': "Landing Page' Dashboard",
        'total_responses': total_responses,
        'product1' : total_product1,
        'product2' : total_product2,
        'product3' : total_product3,
        'posts' : posts,
    }

    return render(request, 'dashboard/index.html', data)