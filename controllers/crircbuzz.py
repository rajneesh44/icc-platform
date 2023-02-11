import os
import requests
from dotenv import load_dotenv

load_dotenv()

CRICBUZZ_BASE_URL = "https://cricbuzz-cricket.p.rapidapi.com"

class CricbuzzController:

    @staticmethod
    def get_api_key():
        return os.getenv("CRICBUZZ_API_KEY_1")
    
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

