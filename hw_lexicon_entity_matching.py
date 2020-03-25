from emora_stdm import KnowledgeBase, DialogueFlow, Macro
from enum import Enum, auto
import requests
import json
from sportsreference.nba.schedule import Schedule
from sportsreference.nba.roster import Player


# TODO: Update the State enum as needed
class State(Enum):
    START = auto()
    TURN0 = auto()
    TURN0ERR = auto()
    TURNTRADE1S = auto()
    TURNTRADE1U = auto()
    TURNTRADE1ERR = auto()
    TURNTRADE2S = auto()
    TURNTRADE2U = auto()
    TURNTRADE2AS = auto()
    TURNTRADE2AU = auto()
    TURNTRADE2ERR = auto()
    TURNTRADE3S = auto()
    TURNTRADE3U = auto()
    TURNTRADE3ERR = auto()
    TURNTRADE4S = auto()
    TURNTRADE4U = auto()
    TURNTRADE4ERR = auto()
    TURNTRADE5U = auto()
    TURNTRADE5S = auto()
    END = auto()
    EARLYEND = auto()


# ONTOLOGY IS LOADED FROM teams.json
ontology = {
    "ontology": {

        }
}

#GLOBAL VARS????
receivingTeam = str()
givingTeam = str()
player = str()

class news(Macro):
    def run (self, ngrams, vars, args):
        #andrew- im just gonna assume that the input is the team name and only the team name, eg "Atlanta Hawks"

        endpoint = "Lakers sign guard dion waiters".replace(" ", "%20")
        endpoint = "http://newsapi.org/v2/everything?q="+endpoint+"&apiKey=d50b19bb1c7445b588bb694ecc2a119f"
        news = requests.get(endpoint)
        formatted_news = news.json()
        formatted_news = formatted_news['articles']

        ## THINGS TO RETURN #####
        title = formatted_news[0]['title']
        description = formatted_news[0]['description']
        #########################

        return "{}".format(description)

class newsPlayer(Macro):
    def run (self, ngrams, vars, args):
        #andrew- im just gonna assume that the input is the team name and only the team name, eg "Atlanta Hawks"

        endpoint = vars['player'].replace(" ", "%20")
        endpoint = "http://newsapi.org/v2/everything?q="+endpoint+"&apiKey=d50b19bb1c7445b588bb694ecc2a119f"
        news = requests.get(endpoint)
        formatted_news = news.json()
        formatted_news = formatted_news['articles']

        ## THINGS TO RETURN #####
        title = formatted_news[0]['title']
        description = formatted_news[0]['description']
        #########################

        return "I found this recent news headline. {}. It says that {}".format(title, description)

class newsTeam(Macro):
    def run (self, ngrams, vars, args):

        endpoint = vars['favoriteTeam'].replace(" ", "%20") +"%20basketball"
        endpoint = "http://newsapi.org/v2/everything?q="+endpoint+"&apiKey=d50b19bb1c7445b588bb694ecc2a119f"
        news = requests.get(endpoint)
        formatted_news = news.json()
        formatted_news = formatted_news['articles']

        ## THINGS TO RETURN #####
        title = formatted_news[0]['title']
        description = formatted_news[0]['description']
        #########################
        
        #is this line useful?
        result = ""

        return "I found this recent news headline about {}. {}. It says {}".format(vars['favoriteTeam'], title, description)

class teamStats(Macro):
    def run (self, ngrams, vars, args):
        #Assume input is team name, all lowercase

        if vars['favoriteTeam'] == "Atlanta Hawks" or "Atlanta" or "Hawks":
            team = 'ATL'
        elif vars['favoriteTeam'] == "Boston Celtics" or "Boston" or "Celtics":
            team = 'BOS'
        elif vars['favoriteTeam'] == "Brooklyn Nets" or "Brooklyn" or "Nets":
            team = 'BKN'
        elif vars['favoriteTeam'] =="Charlotte Hornets" or "Charlotte" or "Hornets":
            team = 'CHA'
        elif vars['favoriteTeam'] =="Chicago Bulls" or "Chicago" or "Bulls":
            team = 'CHI'
        elif vars['favoriteTeam'] =="Cleveland Cavaliers" or "Cleveland" or "Cavaliers":
            team = 'CLE'
        elif vars['favoriteTeam'] =="Dallas Mavericks" or "Dallas" or "Mavericks":
            team = 'DAL'
        elif vars['favoriteTeam'] =="Denver Nuggets" or "Denver" or "Nuggets":
            team = 'DEN'
        elif vars['favoriteTeam'] =="Detroit Pistons" or "Detroit" or "Pistons":
            team = 'DET'
        elif vars['favoriteTeam'] =="Golden State Warriors" or "GSW" or "Warriors":
            team = 'GSW'
        elif vars['favoriteTeam'] =="Houston Rockets" or "Houston" or "Rockets":
            team = 'HOU'
        elif vars['favoriteTeam'] =="Indiana Pacers" or "Indiana" or "Pacers":
            team = 'IND'
        elif vars['favoriteTeam'] =="LA Clippers" or "Clippers":
            team = 'LAC'
        elif vars['favoriteTeam'] =="Los Angeles Lakers" or "Lakers":
            team = 'LAL'
        elif vars['favoriteTeam'] =="Memphis Grizzlies" or "Memphis" or "Grizzlies":
            team = 'MEM'
        elif vars['favoriteTeam'] =="Miami Heat" or "Miami":
            team = 'MIA'
        elif vars['favoriteTeam'] =="Milwaukee Bucks" or "Milwaukee" or "Bucks":
            team = 'MIL'
        elif vars['favoriteTeam'] =="Minnesota Timberwolves" or "Minnesota" or "Timberwolves":
            team = 'MIN'
        elif vars['favoriteTeam'] =="New Orleans Pelicans" or "Pelicans" or "NoLa":
            team = 'NOP'
        elif vars['favoriteTeam'] =="New York Knicks" or "Knicks" or "NY":
            team = 'NYK'
        elif vars['favoriteTeam'] =="Oklahoma City Thunder" or "Thunder" or "OKC":
            team = 'OKC'
        elif vars['favoriteTeam'] =="Orlando Magic" or "Orlando" or "Magic":
            team = 'ORL'
        elif vars['favoriteTeam'] =="Philadelphia SeventySixers" or "Philly" or "SeventySixers" or "76ers":
            team = 'PHI'
        elif vars['favoriteTeam'] =="Phoenix Suns" or "Phoenix" or "Suns":
            team = 'PHX'
        elif vars['favoriteTeam'] =="Portland Trail Blazers" or "Portland" or "Trail Blazers":
            team = 'POR'
        elif vars['favoriteTeam'] =="Sacramento Kings" or "Sacramento" or "Kings":
            team = 'SAC'
        elif vars['favoriteTeam'] =="San Antonio Spurs" or "San Antonio" or "Spurs":
            team = 'SAS'
        elif vars['favoriteTeam'] =="Toronto Raptors" or "Toronto" or "Raptors":
            team = 'TOR'
        elif vars['favoriteTeam'] =="Utah Jazz" or "Utah" or "Jazz":
            team = 'UTA'
        elif vars['favoriteTeam'] =="Washington Wizards" or "Washington" or "Wizards":
            team = 'WAS'
        else:
            #error handling? idk if needed
            return "I didn't get that"

        wins = 0
        losses = 0
        teamSchedule = Schedule(team)
        for game in teamSchedule:
            if game.result == 'Win':
                wins += 1
            else:
                losses += 1

        return "The {} have a total of {} wins and {} losses".format(vars['favoriteTeam'], wins, losses)

class tradeNews(Macro):
    def run (self, ngrams, vars, args):
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
        print('recieving team', receivingTeam)
        print(givingTeam, givingTeam)
        print(player)
        print(role)

        return "I found this most recent trade for {} between the {} and {}".format(player, givingTeam, receivingTeam)

class playerRating(Macro):
    def run (self, ngrams, vars, args):
        n = vars['playername'].split()
        s = ""
        if (len(n[1]) >= 5):    #edge case for names with shorter than 5 characters/jr. resolved
            for i in range(5):
                s += n[1][i]
        else:
            for i in range(len(n[1])):
                s += n[1][i]
        for i in range(2):
            s += n[0][i]
        s += "01"
        playerid = s.lower()

        player = Player(playerid)
        PER = player.player_efficiency_rating
        if (PER > 18): return "good player"
        else: return "bad player"


#returns name of team which has better W/L ratio
class betterTeam(Macro):
    def run (self, ngrams, vars, args):
        if vars[receivingTeam] == "Atlanta Hawks" or "Atlanta" or "Hawks":
            teama = 'ATL'
        elif vars[receivingTeam] == "Boston Celtics" or "Boston" or "Celtics":
            teama = 'BOS'
        elif vars[receivingTeam] == "Brooklyn Nets" or "Brooklyn" or "Nets":
            teama = 'BKN'
        elif vars[receivingTeam] =="Charlotte Hornets" or "Charlotte" or "Hornets":
            teama = 'CHA'
        elif vars[receivingTeam] =="Chicago Bulls" or "Chicago" or "Bulls":
            teama = 'CHI'
        elif vars[receivingTeam] =="Cleveland Cavaliers" or "Cleveland" or "Cavaliers":
            teama = 'CLE'
        elif vars[receivingTeam] =="Dallas Mavericks" or "Dallas" or "Mavericks":
            teama = 'DAL'
        elif vars[receivingTeam] =="Denver Nuggets" or "Denver" or "Nuggets":
            teama = 'DEN'
        elif vars[receivingTeam] =="Detroit Pistons" or "Detroit" or "Pistons":
            teama = 'DET'
        elif vars[receivingTeam] =="Golden State Warriors" or "GSW" or "Warriors":
            teama = 'GSW'
        elif vars[receivingTeam] =="Houston Rockets" or "Houston" or "Rockets":
            teama = 'HOU'
        elif vars[receivingTeam] =="Indiana Pacers" or "Indiana" or "Pacers":
            teama = 'IND'
        elif vars[receivingTeam] =="LA Clippers" or "Clippers":
            teama = 'LAC'
        elif vars[receivingTeam] =="Los Angeles Lakers" or "Lakers":
            teama = 'LAL'
        elif vars[receivingTeam] =="Memphis Grizzlies" or "Memphis" or "Grizzlies":
            teama = 'MEM'
        elif vars[receivingTeam] =="Miami Heat" or "Miami":
            teama = 'MIA'
        elif vars[receivingTeam] =="Milwaukee Bucks" or "Milwaukee" or "Bucks":
            teama = 'MIL'
        elif vars[receivingTeam] =="Minnesota Timberwolves" or "Minnesota" or "Timberwolves":
            teama = 'MIN'
        elif vars[receivingTeam] =="New Orleans Pelicans" or "Pelicans" or "NoLa":
            teama = 'NOP'
        elif vars[receivingTeam] =="New York Knicks" or "Knicks" or "NY":
            teama = 'NYK'
        elif vars[receivingTeam] =="Oklahoma City Thunder" or "Thunder" or "OKC":
            teama = 'OKC'
        elif vars[receivingTeam] =="Orlando Magic" or "Orlando" or "Magic":
            teama = 'ORL'
        elif vars[receivingTeam] =="Philadelphia SeventySixers" or "Philly" or "SeventySixers" or "76ers":
            teama = 'PHI'
        elif vars[receivingTeam] =="Phoenix Suns" or "Phoenix" or "Suns":
            teama = 'PHX'
        elif vars[receivingTeam] =="Portland Trail Blazers" or "Portland" or "Trail Blazers":
            teama = 'POR'
        elif vars[receivingTeam] =="Sacramento Kings" or "Sacramento" or "Kings":
            teama = 'SAC'
        elif vars[receivingTeam] =="San Antonio Spurs" or "San Antonio" or "Spurs":
            teama = 'SAS'
        elif vars[receivingTeam] =="Toronto Raptors" or "Toronto" or "Raptors":
            teama = 'TOR'
        elif vars[receivingTeam] =="Utah Jazz" or "Utah" or "Jazz":
            teama = 'UTA'
        elif vars[receivingTeam] =="Washington Wizards" or "Washington" or "Wizards":
            teama = 'WAS'
        else:
            #error handling? idk if needed
            return "I didn't get that"

        teamAWins = 0
        teamALosses = 0
        teamSchedule = Schedule(teama)
        for game in teamSchedule:
            if game.result == 'Win':
                teamAWins += 1
            else:
                teamALosses += 1
        teamARatio = teamAWins/teamALosses

        if vars[givingTeam] == "Atlanta Hawks" or "Atlanta" or "Hawks":
            teamb = 'ATL'
        elif vars[givingTeam] == "Boston Celtics" or "Boston" or "Celtics":
            teamb = 'BOS'
        elif vars[givingTeam] == "Brooklyn Nets" or "Brooklyn" or "Nets":
            teamb = 'BKN'
        elif vars[givingTeam] =="Charlotte Hornets" or "Charlotte" or "Hornets":
            teamb = 'CHA'
        elif vars[givingTeam] =="Chicago Bulls" or "Chicago" or "Bulls":
            teamb = 'CHI'
        elif vars[givingTeam] =="Cleveland Cavaliers" or "Cleveland" or "Cavaliers":
            teamb = 'CLE'
        elif vars[givingTeam] =="Dallas Mavericks" or "Dallas" or "Mavericks":
            teamb = 'DAL'
        elif vars[givingTeam] =="Denver Nuggets" or "Denver" or "Nuggets":
            teamb = 'DEN'
        elif vars[givingTeam] =="Detroit Pistons" or "Detroit" or "Pistons":
            teamb = 'DET'
        elif vars[givingTeam] =="Golden State Warriors" or "GSW" or "Warriors":
            teamb = 'GSW'
        elif vars[givingTeam] =="Houston Rockets" or "Houston" or "Rockets":
            teamb = 'HOU'
        elif vars[givingTeam] =="Indiana Pacers" or "Indiana" or "Pacers":
            teamb = 'IND'
        elif vars[givingTeam] =="LA Clippers" or "Clippers":
            teamb = 'LAC'
        elif vars[givingTeam] =="Los Angeles Lakers" or "Lakers":
            teamb = 'LAL'
        elif vars[givingTeam] =="Memphis Grizzlies" or "Memphis" or "Grizzlies":
            teamb = 'MEM'
        elif vars[givingTeam] =="Miami Heat" or "Miami":
            teamb = 'MIA'
        elif vars[givingTeam] =="Milwaukee Bucks" or "Milwaukee" or "Bucks":
            teamb = 'MIL'
        elif vars[givingTeam] =="Minnesota Timberwolves" or "Minnesota" or "Timberwolves":
            teamb = 'MIN'
        elif vars[givingTeam] =="New Orleans Pelicans" or "Pelicans" or "NoLa":
            teamb = 'NOP'
        elif vars[givingTeam] =="New York Knicks" or "Knicks" or "NY":
            teamb = 'NYK'
        elif vars[givingTeam] =="Oklahoma City Thunder" or "Thunder" or "OKC":
            teamb = 'OKC'
        elif vars[givingTeam] =="Orlando Magic" or "Orlando" or "Magic":
            teamb = 'ORL'
        elif vars[givingTeam] =="Philadelphia SeventySixers" or "Philly" or "SeventySixers" or "76ers":
            teamb = 'PHI'
        elif vars[givingTeam] =="Phoenix Suns" or "Phoenix" or "Suns":
            teamb = 'PHX'
        elif vars[givingTeam] =="Portland Trail Blazers" or "Portland" or "Trail Blazers":
            teamb = 'POR'
        elif vars[givingTeam] =="Sacramento Kings" or "Sacramento" or "Kings":
            teamb = 'SAC'
        elif vars[givingTeam] =="San Antonio Spurs" or "San Antonio" or "Spurs":
            teamb = 'SAS'
        elif vars[givingTeam] =="Toronto Raptors" or "Toronto" or "Raptors":
            teamb = 'TOR'
        elif vars[givingTeam] =="Utah Jazz" or "Utah" or "Jazz":
            teamb = 'UTA'
        elif vars[givingTeam] =="Washington Wizards" or "Washington" or "Wizards":
            teamb = 'WAS'
        else:
            #error handling? idk if needed
            return "I didn't get that"

        teamBWins = 0
        teamBLosses = 0
        teamSchedule = Schedule(teamb)
        for game in teamSchedule:
            if game.result == 'Win':
                teamBWins += 1
            else:
                teamBLosses += 1
        teamBRatio = teamBWins/teamBLosses

        if teamBRatio >= teamARatio:
            return "The better team is {} ".format(vars[givingTeam])

        else:
            return "The better team is {} ".format(vars[receivingTeam]) #todo receivingTeams might need ''



#todo double check that Macros are declared in constructor

knowledge = KnowledgeBase()
knowledge.load_json_file("teams.json")
df = DialogueFlow(State.START, initial_speaker=DialogueFlow.Speaker.SYSTEM, kb=knowledge, macros={'news': news(), 'newsPlayer': newsPlayer(), 'newsTeam': newsTeam(), 'teamStats': teamStats(), 'playerRating' : playerRating(), 'tradeNews':tradeNews(), 'betterTeam': betterTeam()})

#########################
# THIS DOCUMENT IS THE SOURCE OF TRUTH FOR WHAT WE ARE DOING: https://docs.google.com/document/d/15N6Xo60IipqOknUGHxXt-A17JFOXOhMCZSMcOAyUEzo/edit
##########################

#turn 0
df.add_system_transition(State.START, State.TURN0, '"Hi I’m NBA chatbot. I can talk to you about trades, injuries, drafts, or all-stars. Which of these would you like to talk about?"')
df.add_user_transition(State.TURN0, State.TURNTRADE1S, '[#ONT(trades)]')
df.set_error_successor(State.TURN0, State.TURN0ERR)
df.add_system_transition(State.TURN0ERR, State.TURN0, r'[! "I do not know how to talk about that yet"]')
#df.add_system_transition(State.TURNTRADE1S2, State.EARLYEND, r'[! "Oh, thats a shame. I cant really talk about other news right now unfortunately. Maybe next time we can talk some more"]')


#turn 1
df.add_system_transition(State.TURNTRADE1S, State.TURNTRADE1U, r'[!{#tradeNews()} ". If this trade does not interest you we can also talk about all-stars, injuries, or the draft"]') #todo input news Macro here
df.add_user_transition(State.TURNTRADE1U, State.TURNTRADE2S, '[#ONT(agree)]')
df.add_user_transition(State.TURNTRADE1U, State.TURN0, '[#ONT(disagree)]')
df.set_error_successor(State.TURNTRADE1U, State.TURNTRADE1ERR)
df.add_system_transition(State.TURNTRADE1ERR, State.TURNTRADE2U, r'[! "Do not know if I want to talk about trades or about something else"]' )

#turn 2
df.add_system_transition(State.TURNTRADE2S, State.TURNTRADE2U, r'[! "Personally I think this will help" #betterTeam() ". Do you think it will?"]') #todo change this back to worseTeam
df.add_user_transition(State.TURNTRADE2U, State.TURNTRADE2AS, '[{#ONT(disagree)}]')
df.add_user_transition(State.TURNTRADE2U, State.TURNTRADE3S, '[{#ONT(agree)}]')
df.set_error_successor(State.TURNTRADE2U, State.TURNTRADE2ERR)
df.add_system_transition(State.TURNTRADE2ERR, State.TURNTRADE3U, r'[! "Do not know if it will help the worse team"]')

#turn 3
df.add_system_transition(State.TURNTRADE3S, State.TURNTRADE3U, r'[! #teamStats($worseTeam) ". But when I watch " $player ", I fell like they are a " $goodBadPlayer ". Hopefully this will boost the wins of " $worseTeam ". What do you think?"]')
df.add_user_transition(State.TURNTRADE3U, State.TURNTRADE4S, "[$response2=#POS(adj)]")
df.set_error_successor(State.TURNTRADE3U, State.TURNTRADE3ERR)
df.add_system_transition(State.TURNTRADE3ERR, State.TURNTRADE4U, "Do not know if it will boost W-L record.")

#turn 4
df.add_system_transition(State.TURNTRADE4S, State.TURNTRADE4U, r'[! "If this ends up being a good thing, it could change the playoff picture. Do you think it will? "]')
df.add_user_transition(State.TURNTRADE4U, State.TURNTRADE5S, "[$response3=/[a-z A-Z]+/]")
df.set_error_successor(State.TURNTRADE4U, State.TURNTRADE4ERR)
df.add_system_transition(State.TURNTRADE4ERR, State.TURNTRADE4S, "Do not have a playoff prediction")

df.add_system_transition(State.TURNTRADE5S, State.TURNTRADE5U, r'[! "I guess that is a possibility. We will not know until playoffs actually start. Do you want to chat about playoffs or another topic?"]')
df.add_user_transition(State.TURNTRADE5U, State.END, '[$watching={#ONT(agree)}]')




if __name__ == '__main__':
    df.run(debugging=True)