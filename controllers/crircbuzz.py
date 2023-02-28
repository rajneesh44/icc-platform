import os
import requests
from dotenv import load_dotenv
import random

load_dotenv()

CRICBUZZ_BASE_URL = "https://cricbuzz-cricket.p.rapidapi.com"

class CricbuzzController:

    @staticmethod
    def get_api_key():
        api_keys = [os.getenv("CRICBUZZ_API_KEY_1"), os.getenv("CRICBUZZ_API_KEY_2"), os.getenv("CRICBUZZ_API_KEY_3")]
        selected_key = api_keys[random.randint(1,3)-1]
        return selected_key
    
    @staticmethod
    def get_headers():
        headers = {
            "X-RapidAPI-Key": "",
            "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
        }
        headers["X-RapidAPI-Key"] = CricbuzzController.get_api_key()
        return headers
    
    @staticmethod
    def get_matches_list(key=None):
        key = key or "recent"
        response = requests.request("GET", f'{CRICBUZZ_BASE_URL}/matches/v1/{key}', headers=CricbuzzController.get_headers())
        return response.json()
    
    @staticmethod
    def get_match_info(match_id):
        response = requests.get(f'{CRICBUZZ_BASE_URL}/mcenter/v1/{match_id}', headers=CricbuzzController.get_headers())
        return response.json()


    @staticmethod
    def get_icc_rankings(category: str, format: str):
        response = requests.get(f'{CRICBUZZ_BASE_URL}/stats/v1/rankings/{category}', {"formatType": format}, headers=CricbuzzController.get_headers())
        return response.json()
        

    @staticmethod
    def get_icc_news():
        response = requests.get(f'{CRICBUZZ_BASE_URL}/news/v1/index', headers=CricbuzzController.get_headers())
        return response.json()


    @staticmethod
    def get_player_info(player_id):
        response = requests.get(f'{CRICBUZZ_BASE_URL}/stats/v1/player/{player_id}', headers=CricbuzzController.get_headers())
        return response.json()


    @staticmethod
    def search_player(name: str):
        response = requests.get(f'{CRICBUZZ_BASE_URL}/stats/v1/player/search', {"plrN": name}, headers=CricbuzzController.get_headers())
        data: dict = response.json()["player"][0]
        
        info = CricbuzzController.get_player_info(data["id"])
        data.update(info)
        return data