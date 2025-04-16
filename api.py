import requests

API_TOKEN = 'Nan2I47L22ujx5yx8DIfZO34xEePRrTAMwY09rZhYMvifbT60B9xWpMM55gS'
BASE_URL = 'https://api.sportmonks.com/v3/football/predictions/probabilities'

def get_detailed_predictions():
    url = f"{BASE_URL}?api_token={API_TOKEN}&include=fixture,localTeam,visitorTeam"

    response = requests.get(url)
    if response.status_code != 200:
        print("Error:", response.status_code)
        return

    predictions = response.json().get('data', [])
    
    for item in predictions:
        fixture = item.get('fixture', {})
        home_team = fixture.get('localTeam', {}).get('name', 'Home')
        away_team = fixture.get('visitorTeam', {}).get('name', 'Away')
        match_time = fixture.get('starting_at', {}).get('date', '')

        print(f"\n🏟️ {home_team} vs {away_team} — {match_time}")

        # 1X2 Market
        win_probs = item.get('win', {})
        print(f"🧠 1X2 Prediction:")
        print(f"   - {home_team} Win: {win_probs.get('localteam', 'N/A')}%")
        print(f"   - Draw: {item.get('draw', {}).get('draw', 'N/A')}%")
        print(f"   - {away_team} Win: {win_probs.get('visitorteam', 'N/A')}%")

        # Over/Under Prediction (example: Over 2.5 goals)
        over_under = item.get('over_under', {}).get('2_5', {})
        if over_under:
            print(f"📈 Over/Under 2.5 Goals:")
            print(f"   - Over: {over_under.get('over', 'N/A')}%")
            print(f"   - Under: {over_under.get('under', 'N/A')}%")

        # Both Teams To Score (BTTS)
        btts = item.get('btts', {})
        if btts:
            print(f"⚽ BTTS:")
            print(f"   - Yes: {btts.get('yes', 'N/A')}%")
            print(f"   - No: {btts.get('no', 'N/A')}%")

        # Correct Score Predictions (Top 3 guesses)
        correct_scores = item.get('correct_score', [])
        if correct_scores:
            print("🎯 Correct Score Predictions:")
            for cs in correct_scores[:3]:
                print(f"   - {cs.get('score', '')}: {cs.get('probability', '')}%")


get_detailed_predictions()

