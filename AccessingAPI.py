import requests
import json
from sportsreference.nba.schedule import Schedule
from random import randrange

with open('trades.json') as f:
    data = json.load(f)
trades = data['trades']
# print(trades)
trade = trades[randrange(55)]['TRANSACTION_DESCRIPTION']
receivingTeam = trade.split(' received')[0]
givingTeam = trade.split('from ')[1]
givingTeam = givingTeam[:-1]
player = trade.split('received ')[1]
player = player.split('from')[0]

playerList = player.split(' ')
role = playerList[0]
playerList.pop(0)
player = ' '.join(playerList)

# vars['receivingTeam'] = receivingTeam
# vars['givingTeam'] = givingTeam
# vars['player'] = player

print(trade)
print('recieving team', receivingTeam)
print('givingTeam', givingTeam)
print(player)
print(role)

# return "I found this most recent trade news that {} from {} is going to {}".format(player, givingTeam, receivingTeam)
