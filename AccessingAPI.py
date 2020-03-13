import requests
import json
from sportsreference.nba.schedule import Schedule

wins = 0
losses = 0
teamSchedule = Schedule('HOU')
for game in teamSchedule:
    if game.result == 'Win':
        wins += 1
    else:
        losses += 1

print(wins)
print(losses)

# input = "Atlanta Hawks"
# endpoint = input.replace(" ", "%20")
# print(endpoint)
# endpoint = "http://newsapi.org/v2/everything?q="+endpoint+"&domains=espn.com&apiKey=d50b19bb1c7445b588bb694ecc2a119f"
# print(endpoint)
# news = requests.get(endpoint)
# formatted_news = news.json()
# formatted_news = formatted_news['articles']
# print(formatted_news[0]['title'])

# # if __name__ == "__main__":
# #   print(news.status_code)
# #   print(json.dumps(news.json(), sort_keys=True, indent=4))
