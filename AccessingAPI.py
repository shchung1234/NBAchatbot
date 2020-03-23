import requests
import json
from sportsreference.nba.schedule import Schedule

response = requests.get("https://stats.nba.com/js/data/playermovement/NBA_Player_Movement.json")
test = response.json()
trades = [x for x in test['NBA_Player_Movement']['rows'] if x['Transaction_Type'] == 'Trade']
trade = trades[0]['TRANSACTION_DESCRIPTION']
receivingTeam = trade.split('received')[0]
givingTeam = trade.split('from ')[1]
givingTeam = givingTeam[:-1]
player = trade.split('received ')[1]
player = player.split('from')[0]

playerList = player.split(' ')
role = playerList[0]
playerList.pop(0)
player = ' '.join(playerList)

print(trade)
print(receivingTeam)
print(givingTeam)
print(player)
print(role)
print("I found this most recent trade for {} between the {} and {}".format(player, givingTeam, receivingTeam))

# wins = 0
# losses = 0
# teamSchedule = Schedule('HOU')
# for game in teamSchedule:
#     if game.result == 'Win':
#         wins += 1
#     else:
#         losses += 1

# print(wins)
# print(losses)

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
