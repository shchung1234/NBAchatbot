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
    TURN0S = auto()
    TURN0DK1S = auto()
    TURN0DK1U = auto()
    TURN0ERR = auto()
    TURNTRADE1S = auto()
    TURNTRADE1U = auto()
    TURNTRADE1ERR = auto()
    TURNTRADE1BS = auto()
    TURNTRADE1BU = auto()
    TURNTRADE2S = auto()
    TURNTRADE2U = auto()
    TURNTRADE2AS = auto()
    TURNTRADE2AU = auto()
    TURNTRADE2DK1S = auto()
    TURNTRADE2ERR = auto()
    TURNTRADE3S1 = auto()
    TURNTRADE3S2 = auto()
    TURNTRADE3U = auto()
    TURNTRADE3DK1S = auto()
    TURNTRADE3ERR = auto()
    TURNTRADE4S = auto()
    TURNTRADE4S1 = auto()
    TURNTRADE4U = auto()
    TURNTRADE4DK1S = auto()
    TURNTRADE4ERR = auto()
    TURNTRADE5U = auto()
    TURNTRADE5S = auto()
    TURNTRADE5U_ERR = auto()
    TURNTRADE6AS = auto()
    TURNTRADE6BS = auto()
    TURNTRADE6BU = auto()
    TURNTRADE6BU_ERR = auto()
    TURNPF1S = auto()
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
        response = requests.get("https://stats.nba.com/js/data/playermovement/NBA_Player_Movement.json")
        test = response.json()
        trades = [x for x in test['NBA_Player_Movement']['rows'] if x['Transaction_Type'] == 'Trade']
        trade = trades[0]['TRANSACTION_DESCRIPTION']
        receivingTeam = trade.split(' received')[0]
        givingTeam = trade.split('from ')[1]
        givingTeam = givingTeam[:-1]
        player = trade.split('received ')[1]
        player = player.split('from')[0]

        playerList = player.split(' ')
        role = playerList[0]
        playerList.pop(0)
        player = ' '.join(playerList)
        #Assume input is team name, all lowercase

        if vars['receivingTeam'] == "Atlanta Hawks" or "Atlanta" or "Hawks":
            team = 'ATL'
        elif vars['receivingTeam'] == "Boston Celtics" or "Boston" or "Celtics":
            team = 'BOS'
        elif vars['receivingTeam'] == "Brooklyn Nets" or "Brooklyn" or "Nets":
            team = 'BKN'
        elif vars['receivingTeam'] =="Charlotte Hornets" or "Charlotte" or "Hornets":
            team = 'CHA'
        elif vars['receivingTeam'] =="Chicago Bulls" or "Chicago" or "Bulls":
            team = 'CHI'
        elif vars['receivingTeam'] =="Cleveland Cavaliers" or "Cleveland" or "Cavaliers":
            team = 'CLE'
        elif vars['receivingTeam'] =="Dallas Mavericks" or "Dallas" or "Mavericks":
            team = 'DAL'
        elif vars['receivingTeam'] =="Denver Nuggets" or "Denver" or "Nuggets":
            team = 'DEN'
        elif vars['receivingTeam'] =="Detroit Pistons" or "Detroit" or "Pistons":
            team = 'DET'
        elif vars['receivingTeam'] =="Golden State Warriors" or "GSW" or "Warriors":
            team = 'GSW'
        elif vars['receivingTeam'] =="Houston Rockets" or "Houston" or "Rockets":
            team = 'HOU'
        elif vars['receivingTeam'] =="Indiana Pacers" or "Indiana" or "Pacers":
            team = 'IND'
        elif vars['receivingTeam'] =="LA Clippers" or "Clippers":
            team = 'LAC'
        elif vars['receivingTeam'] =="Los Angeles Lakers" or "Lakers":
            team = 'LAL'
        elif vars['receivingTeam'] =="Memphis Grizzlies" or "Memphis" or "Grizzlies":
            team = 'MEM'
        elif vars['receivingTeam'] =="Miami Heat" or "Miami":
            team = 'MIA'
        elif vars['receivingTeam'] =="Milwaukee Bucks" or "Milwaukee" or "Bucks":
            team = 'MIL'
        elif vars['receivingTeam'] =="Minnesota Timberwolves" or "Minnesota" or "Timberwolves":
            team = 'MIN'
        elif vars['receivingTeam'] =="New Orleans Pelicans" or "Pelicans" or "NoLa":
            team = 'NOP'
        elif vars['receivingTeam'] =="New York Knicks" or "Knicks" or "NY":
            team = 'NYK'
        elif vars['receivingTeam'] =="Oklahoma City Thunder" or "Thunder" or "OKC":
            team = 'OKC'
        elif vars['receivingTeam'] =="Orlando Magic" or "Orlando" or "Magic":
            team = 'ORL'
        elif vars['receivingTeam'] =="Philadelphia SeventySixers" or "Philly" or "SeventySixers" or "76ers":
            team = 'PHI'
        elif vars['receivingTeam'] =="Phoenix Suns" or "Phoenix" or "Suns":
            team = 'PHX'
        elif vars['receivingTeam'] =="Portland Trail Blazers" or "Portland" or "Trail Blazers":
            team = 'POR'
        elif vars['receivingTeam'] =="Sacramento Kings" or "Sacramento" or "Kings":
            team = 'SAC'
        elif vars['receivingTeam'] =="San Antonio Spurs" or "San Antonio" or "Spurs":
            team = 'SAS'
        elif vars['receivingTeam'] =="Toronto Raptors" or "Toronto" or "Raptors":
            team = 'TOR'
        elif vars['receivingTeam'] =="Utah Jazz" or "Utah" or "Jazz":
            team = 'UTA'
        elif vars['receivingTeam'] =="Washington Wizards" or "Washington" or "Wizards":
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

        return "The {} are currently {} and {} ".format(vars['receivingTeam'], wins, losses)

class tradeNews(Macro):
    def run (self, ngrams, vars, args):
        response = requests.get("https://stats.nba.com/js/data/playermovement/NBA_Player_Movement.json")
        test = response.json()
        trades = [x for x in test['NBA_Player_Movement']['rows'] if x['Transaction_Type'] == 'Trade']
        trade = trades[0]['TRANSACTION_DESCRIPTION']
        receivingTeam = trade.split(' received')[0]
        givingTeam = trade.split('from ')[1]
        givingTeam = givingTeam[:-1]
        player = trade.split('received ')[1]
        player = player.split('from')[0]

        playerList = player.split(' ')
        role = playerList[0]
        playerList.pop(0)
        player = ' '.join(playerList)

        vars['receivingTeam'] = receivingTeam
        vars['givingTeam'] = givingTeam
        vars['player'] = player
        
        #print(trade)
        #print('recieving team', receivingTeam)
        #print('givingTeam', givingTeam)
        #print(player)
        #print(role)

        return "{} from {} is going to {}".format(player, givingTeam, receivingTeam)

class goodBadTrade(Macro):
    def run (self, ngrams, vars, args):
        if vars['goodBadPlayer'] == 'good':
            return "this is a good trade for the {}".format(vars['receivingTeam'])
        else:
            return "this is a bad trade for the {}".format(vars['receivingTeam'])



class playerRating(Macro):
    def run (self, ngrams, vars, args):
        n = vars['player'].split()
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
        DEF_REB = player.defensive_rebound_percentage
        OFF_REB = player.offensive_rebound_percentage
        BLK = player.block_percentage
        FLD_GOAL = player.field_goal_percentage
        STL = player.steal_percentage
        THR_PT = player.three_point_percentage

        print(PER)
        if (PER > 18):
            vars['goodBadPlayer'] = 'good'
            if DEF_REB > 5 or OFF_REB > 2:
                return "This trade will be good I think. He'll definitely be able to leverage his skills at rebounding the ball."
            elif BLK > 3.69 or STL >= 1.09:
                return "He is incredible on defense, and I think this trade will make him only better."
            elif FLD_GOAL > 50 or THR_PT > 39:
                return "He is a ridiculous shooter and I think {} can only benefit.".format(vars['receivingTeam'])
            else:
                return "I get the impression that he is efficient and good player. With more opportunities, he may be even better. I think this trade will go great."
        else:
            vars['goodBadPlayer'] = 'bad'
            return "I don't get the impression that he is good. This could just be me, but he doesn't seem too efficient."


knowledge = KnowledgeBase()
knowledge.load_json_file("teams.json")
df = DialogueFlow(State.START, initial_speaker=DialogueFlow.Speaker.SYSTEM, kb=knowledge, macros={'news': news(), 'newsPlayer': newsPlayer(), 'newsTeam': newsTeam(),
                                                                                                  'teamStats': teamStats(), 'playerRating' : playerRating(),
                                                                                                  'goodBadTrade' : goodBadTrade(), 'tradeNews':tradeNews()})




#########################
# THIS DOCUMENT IS THE SOURCE OF TRUTH FOR WHAT WE ARE DOING: https://docs.google.com/document/d/15N6Xo60IipqOknUGHxXt-A17JFOXOhMCZSMcOAyUEzo/edit
##########################

# natex expressions
dont_know = '[{' \
            'dont know,do not know,unsure,maybe,[not,{sure,certain}],hard to say,no idea,uncertain,i guess,[!no {opinion,opinions,idea,ideas,thought,thoughts,knowledge}],' \
            '[{dont,do not}, have, {opinion,opinions,idea,ideas,thought,thoughts,knowledge}],' \
            '[!{cant,cannot,dont} {think,remember,recall}]' \
            '}]'

possible_results = '[{' \
                   'win,lose,better,worse,obliterate,crush,destroy,change,effect,difference,improve,adjust,adapt,implications,good,bad,weird' \
                   '}]'

playoffs = '[{'\
        'playoff, playoffs''}]'

end = '[{'\
    'end, stop, terminate, cease''}]'

#turn 0

#df.add_system_transition(State.START, State.TURN0, '"Hi I’m NBA chatbot. I can talk to you about trades or playoffs. Which of these would you like to talk about?"')
#df.add_user_transition(State.TURN0, State.TURNTRADE1S, '[#ONT(trades)]')
#df.add_user_transition(State.TURN0, State.TURN0S, '[#ONT(offtopics)]')

#df.add_user_transition(State.TURN0, State.TURN0DK1S, dont_know) # dont knows section
#df.add_system_transition(State.TURN0DK1S, State.TURN0DK1U, r'[! "No worries, if you dont know, I can just talk about trades! Is that okay?"]')
#df.add_user_transition(State.TURN0DK1U, State.TURNTRADE1S, "[#ONT(agree)]")
#df.set_error_successor(State.TURN0DK1U, State.TURN0ERR)

#df.add_system_transition(State.TURN0S, State.TURN0, r'[! "I do not know how to talk about that yet"]')
#df.set_error_successor(State.TURN0, State.TURN0ERR)
#df.add_system_transition(State.TURN0ERR, State.TURNTRADE1U, r'[! "Honestly, Im only really good at talking about trades right now. If thats okay then listen to this! " #tradeNews() ". Doesnt that sound interesting?"]')
#df.add_system_transition(State.TURNTRADE1S2, State.EARLYEND, r'[! "Oh, thats a shame. I cant really talk about other news right now unfortunately. Maybe next time we can talk some more"]')


#turn 1
df.add_system_transition(State.START, State.TURNTRADE1U, r'[!"Hi I’m NBA chatbot." I found this interesting trade article that says that {#tradeNews()} ". Do you want to talk about this trade?"]')
df.add_user_transition(State.TURNTRADE1U, State.TURNTRADE2S, '[#ONT(agree)]')
df.add_user_transition(State.TURNTRADE1U, State.END, '[#ONT(disagree)]') #todo currently set up to end, maybe can let user select a different trade to discuss
#df.add_system_transition(State.TURNTRADE1BS, State.TURNTRADE1BU, r'[! "We can also talk about playoffs or stop talking. Which would you prefer?"]')
#df.add_user_transition(State.TURNTRADE1BU, State.TURNPF1S, playoffs)
#df.add_user_transition(State.TURNTRADE1BU, State.END, '[/[a-z A-Z]+/]')
df.set_error_successor(State.TURNTRADE1U, State.TURNTRADE1ERR)
df.add_system_transition(State.TURNTRADE1ERR, State.TURNTRADE2U, r'[! "Okay, I mean " $player " is really interesting, and I really want to talk about him. " #playerRating() " What do you think about him?"]' )

#turn 2

df.add_system_transition(State.TURNTRADE2S, State.TURNTRADE2U, r'[! "When I watch " $player ", " #playerRating() " What do you think about " $player "?"]')
df.add_user_transition(State.TURNTRADE2U, State.TURNTRADE3S1, "[$response2=#POS(adj)]")
df.add_user_transition(State.TURNTRADE2U, State.TURNTRADE3S2, "[$response2=#POS(verb)]")
df.add_user_transition(State.TURNTRADE2U, State.TURNTRADE2DK1S, dont_know) # dont knows
df.add_system_transition(State.TURNTRADE2DK1S, State.TURNTRADE3U, r'[! "Its okay if youre not sure! I actually think that " #goodBadTrade() ". Do you agree?"]')
df.set_error_successor(State.TURNTRADE2U, State.TURNTRADE2ERR)
df.add_system_transition(State.TURNTRADE2ERR, State.TURNTRADE3U, r'[! "I dont know why you made that comment about " $player ". I still think that " '
                                                                 r'#goodBadTrade() ". Do you agree?"]')

#turn 3

df.add_system_transition(State.TURNTRADE3S1, State.TURNTRADE3U, r'[! {My robot uncle thinks that,All my friends think that,My friend Seeree thinks that} $player " is " $response2 "too. But lets not forget about the teams" #teamStats() ", and I think that " #goodBadTrade() ". Do you agree?"]')
df.add_system_transition(State.TURNTRADE3S2, State.TURNTRADE3U, r'[! {My robot uncle thinks that,All my friends think that,My friend Seeree thinks that} $player $response2 "too. Ultimately, " #goodBadTrade() ". Do you agree?"]')
df.add_user_transition(State.TURNTRADE3U, State.TURNTRADE4S, '[#ONT(agree)]')
df.add_user_transition(State.TURNTRADE3U, State.TURNTRADE4S1, '[#ONT(disagree)]')

df.add_user_transition(State.TURNTRADE3U, State.TURNTRADE3DK1S, dont_know) # dont knows
df.add_system_transition(State.TURNTRADE3DK1S, State.TURNTRADE4U, r'[! "Youre not sure? Thats okay, since its hard to tell. How do you think this trade will affect the playoffs?"]')
df.set_error_successor(State.TURNTRADE3U, State.TURNTRADE3ERR)
df.add_system_transition(State.TURNTRADE3ERR, State.TURNTRADE4U, r'[! "That is certainly an opinion haha. Playoffs are happening soon though! How do you think this trade affects the playoff?"]')

#turn 4
df.add_system_transition(State.TURNTRADE4S1, State.TURNTRADE4U, r'[! "Interesting perspective! I cant say I agree with you though. Anyway, how do you think this affects the playoff?"]')
df.add_system_transition(State.TURNTRADE4S, State.TURNTRADE4U, r'[! "How do you think this trade will affect the playoffs? "]')
df.add_user_transition(State.TURNTRADE4U, State.TURNTRADE5S, possible_results)

df.add_user_transition(State.TURNTRADE4U, State.TURNTRADE4DK1S, dont_know)
df.add_system_transition(State.TURNTRADE4DK1S, State.TURNTRADE5U, r'[! "Honestly, youre probably right to be unsure as we wont know until playoffs actually start. Would you like to chat about another trade?"]')
df.set_error_successor(State.TURNTRADE4U, State.TURNTRADE4ERR)
df.add_system_transition(State.TURNTRADE4ERR, State.TURNTRADE5U, r'[! "Haha, youre funny, but ultimately I guess we wont know until later when playoffs start. Would you like to talk about another trade?"]')

df.add_system_transition(State.TURNTRADE5S, State.TURNTRADE5U, r'[! "I guess that is a possibility. We will not know until playoffs actually start." {Do you want to chat about another trade,Would you like to chat about another trade}"?"]')

df.add_user_transition(State.TURNTRADE5U, State.TURNTRADE6AS, "[#ONT(agree)]")
df.add_system_transition(State.TURNTRADE6AS, State.TURNTRADE1U, r'[! "Okay! I found" {another,this other,a new} {trade news, article} "that says that" #tradeNews() "Does that sound interesting?"]')

df.add_user_transition(State.TURNTRADE5U, State.TURNTRADE6BS, "[#ONT(disagree)]")
df.set_error_successor(State.TURNTRADE5U, State.TURNTRADE5U_ERR)
df.add_system_transition(State.TURNTRADE5U_ERR, State.TURNTRADE6BU, r'[! "Okay, in that case would you like to talk about playoffs or would you like to stop talking?"]')

df.add_system_transition(State.TURNTRADE6BS, State.TURNTRADE6BU, r'[! "Okay, in that case would you like to talk about playoffs or would you like to stop talking?"]')
df.set_error_successor(State.TURNTRADE6BU, State.TURNTRADE6BU_ERR)
df.add_system_transition(State.TURNTRADE6BU_ERR, State.END, r'[! "In that case, I will take my leave for now"]')
df.add_user_transition(State.TURNTRADE6BU, State.END, end)
df.add_user_transition(State.TURNTRADE6BU, State.TURNPF1S, playoffs)

df.add_system_transition(State.TURNPF1S, State.END, r'[!  "You are currently accessing a module which will be deployed as a part of the project. I cannot talk about playoffs right now."]')





if __name__ == '__main__':
    df.run(debugging=False)