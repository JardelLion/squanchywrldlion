# my_app/views.py

from django.http import JsonResponse
from scraping.last_result import LastResult
from functions.process import process_and_save_data


def scrape_and_save_view(request):
    #url =  'file:///home/jardel-lion-studio/Documents/games/octuber/11/Novorizontino%20vs%20Sport%20Recife%20H2H%20stats%20preview%20and%20analysis,%202024.html'
    
    url = 'file:///home/jardel-lion-studio/Documents/games/octuber/18/Alaves%20vs%20Valladolid%20H2H%20stats%20preview%20and%20analysis,%202024-2025.html'
    try:
        last_result = LastResult(url)
        process_and_save_data(last_result.get_home)
        process_and_save_data(last_result.get_away)  # Salvando os dados de "away"
        return JsonResponse({'status': 'success', 'message': 'Data scraped and saved successfully'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})
