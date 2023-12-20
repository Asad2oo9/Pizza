from django.shortcuts import render
from .models import City
from home.forms import CityForm
import requests

from django.shortcuts import render
import requests




def index(request):
   
    search_history = request.session.get('search_history', [])

    if request.method == 'POST':
        city_name = request.POST.get('city_name', '')
   
        api_url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=e1408599974bfafd4add9fe2282cd73e'

        try:
            response = requests.get(api_url)
            data = response.json()

            weather_info = f"Температура: {data['main']['temp']}°C, {data['weather'][0]['description']}"
                 
                
            search_history.append(city_name)
            request.session['search_history'] = search_history

        except Exception as e:
            print(f"Ошибка при выполнении запроса: {e}")
            weather_info = 'Не удалось получить данные о погоде.'

        return render(request, 'weather_result.html', {'weather_info': weather_info, 'search_history': search_history})

    return render(request, 'home.html', {'search_history': search_history})

def history(request):
    # Retrieve the search history from the session
    search_history = request.session.get('search_history', [])
    return render(request, 'search_history.html', {'search_history': search_history})