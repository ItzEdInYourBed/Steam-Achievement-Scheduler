import time
import random
import requests
import steam_achievement_library

API_KEY = 'your_api_key_here'
STEAM_ID = 'your_steam_id_here'
GAME_ID = 'game_id_here'

def get_game_achievements(api_key, game_id):
    url = f"https://api.steampowered.com/ISteamUserStats/GetSchemaForGame/v2/?key={api_key}&appid={game_id}"
    response = requests.get(url)
    data = response.json()
    
    if 'game' not in data or 'availableGameStats' not in data['game'] or 'achievements' not in data['game']['availableGameStats']:
        return []

    achievements = data['game']['availableGameStats']['achievements']
    return [achievement['name'] for achievement in achievements.values()]

def unlock_achievement(steam_id, game_id, achievement_id):
    steam_achievement_library.unlock(steam_id, game_id, achievement_id, api_key=API_KEY)

def random_interval(min_seconds, max_seconds):
    return random.randint(min_seconds, max_seconds)

if __name__ == "__main__":
    achievements_to_unlock = get_game_achievements(API_KEY, GAME_ID)
    
    for achievement_id in achievements_to_unlock:
        unlock_achievement(STEAM_ID, GAME_ID, achievement_id)
        interval = random_interval(120, 300)
        time.sleep(interval)
