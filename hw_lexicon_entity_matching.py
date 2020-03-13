from emora_stdm import KnowledgeBase, DialogueFlow, Macro
from enum import Enum, auto
from pip._vendor import requests
import json
from sportsreference.nba.schedule import Schedule


# TODO: Update the State enum as needed
class State(Enum):
    START = auto()
    TURN0 = auto()
    TURN0ERR = auto()
    TURN1S1 = auto()
    TURN1S2 = auto()
    TURN1U = auto()
    TURN1ERR = auto()
    TURN2S = auto()
    TURN2U = auto()
    TURN2ERR = auto()
    TURN3S = auto()
    TURN3U = auto()
    TURN3ERR = auto()
    TURN4S = auto()
    TURN4U = auto()
    TURN4ERR = auto()
    TURN5U = auto()
    TURN5S = auto()
    END = auto()


# ONTOLOGY IS LOADED FROM teams.json
ontology = {
    "ontology": {

        }
}

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

        if vars[0] == "Atlanta Hawks" or "Atlanta" or "Hawks":
            team = 'ATL'
        elif vars[0] == "Boston Celtics" or "Boston" or "Celtics":
            team = 'ATL'
        elif vars[0] == "Brooklyn Nets" or "Brooklyn" or "Nets":
            team = 'ATL'
        elif vars[0] =="Charlotte Hornets" or "Charlotte" or "Hornets":
            team = 'ATL'
        elif vars[0] =="Chicago Bulls" or "Chicago" or "Bulls":
            team = 'ATL'
        elif vars[0] =="Cleveland Cavaliers" or "Cleveland" or "Cavaliers":
            team = 'ATL'
        elif vars[0] =="Dallas Mavericks" or "Dallas" or "Mavericks":
            team = 'ATL'
        elif vars[0] =="Denver Nuggets" or "Denver" or "Nuggets":
            team = 'ATL'
        elif vars[0] =="Detroit Pistons" or "Detroit" or "Pistons":
            team = 'ATL'
        elif vars[0] =="Golden State Warriors" or "GSW" or "Warriors":
            team = 'ATL'
        elif vars[0] =="Houston Rockets" or "Houston" or "Rockets":
            team = 'ATL'
        elif vars[0] =="Indiana Pacers" or "Indiana" or "Pacers":
            team = 'ATL'
        elif vars[0] =="LA Clippers" or "Clippers":
            team = 'ATL'
        elif vars[0] =="Los Angeles Lakers" or "Lakers":
            team = 'ATL'
        elif vars[0] =="Memphis Grizzlies" or "Memphis" or "Grizzlies":
            team = 'ATL'
        elif vars[0] =="Miami Heat" or "Miami":
            team = 'ATL'
        elif vars[0] =="Milwaukee Bucks" or "Milwaukee" or "Bucks":
            team = 'ATL'
        elif vars[0] =="Minnesota Timberwolves" or "Minnesota" or "Timberwolves":
            team = 'ATL'
        elif vars[0] =="New Orleans Pelicans" or "Pelicans" or "NoLa":
            team = 'ATL'
        elif vars[0] =="New York Knicks" or "Knicks" or "NY":
            team = 'ATL'
        elif vars[0] =="Oklahoma City Thunder" or "Thunder" or "OKC":
            team = 'ATL'
        elif vars[0] =="Orlando Magic" or "Orlando" or "Magic":
            team = 'ATL'
        elif vars[0] =="Phoenix Suns" or "Phoenix" or "Suns":
            team = 'ATL'
        elif vars[0] =="Portland Trail Blazers" or "Portland" or "Trail Blazers":
            team = 'ATL'
        elif vars[0] =="Sacramento Kings" or "Sacramento" or "Kings":
            team = 'ATL'
        elif vars[0] =="San Antonio Spurs" or "San Antonio" or "Spurs":
            team = 'ATL'
        elif vars[0] =="Toronto Raptors" or "Toronto" or "Raptors":
            team = 'ATL'
        elif vars[0] =="Utah Jazz" or "Utah" or "Jazz":
            team = 'ATL'
        elif vars[0] =="Washington Wizards" or "Washington" or "Wizards":
            team = 'ATL'
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

        return "The {} have a total of {} wins and {} losses", vars[0], wins, losses

knowledge = KnowledgeBase()
knowledge.load_json_file("teams.json")
df = DialogueFlow(State.START, initial_speaker=DialogueFlow.Speaker.SYSTEM, kb=knowledge, macros={'newsPlayer': newsPlayer(), 'newsTeam': newsTeam()})

# THIS DOCUMENT IS THE SOURCE OF TRUTH FOR WHAT WE ARE DOING: https://docs.google.com/document/d/15N6Xo60IipqOknUGHxXt-A17JFOXOhMCZSMcOAyUEzo/edit

#turn 0
df.add_system_transition(State.START, State.TURN0, '"Hi, I am NBA chatbot. I can talk to you about NBA news. This includes topics such as trades, injuries, and community events?"')
df.add_user_transition(State.TURN0, State.TURN1S1, '[$player={#ONT(teams)}]') #todo change ontology here and in the one below too
df.add_user_transition(State.TURN0, State.TURN1S2, "[! -{#ONT(teams)} {$person=#NER(person)}]") #gives a name that's not currently in NBA
df.add_system_transition(State.TURN1S2, State.TURN0, r'[! "Oh I do not know how to talk about that topic yet. 'r'Do you have any current NBA player that you want to talk about?"]')


"""this is left over code, might not need error handling if POS works correctly"""
"""
df.set_error_successor(State.TURN0, State.TURN0ERR)
df.add_system_transition(State.TURN0ERR, State.TURN0, "I don't think that's a person. If you don't have a favorite player, we can also talk about teams") #todo this turn to, what state seems rather abrupt, see if there is a way to make it more smooth
"""


#turn 1
df.add_system_transition(State.TURN1S1, State.TURN1U, r'[!"Have you heard the news about", {#newsPlayer($player)}]') #todo need to change this to topic
df.add_user_transition(State.TURN1U, State.TURN2S, "[$response1=#POS(adj)]") #todo here user says whether or not they heard about the news
#df.add_user_transition(State.TURN1U, State.TURN1S1, "$player = #ONT(player)") #gets users opinion about headline 1 ##there might be an error here. trace a correct answer to turn1S1
df.set_error_successor(State.TURN1U, State.TURN1ERR)
df.add_system_transition(State.TURN1ERR, State.TURN2U, "Knowing news about trade", ) #todo this might be wrong

#turn 2

df.add_system_transition(State.TURN2S, State.TURN2U, r'[! "Which team do you think is benefitting more from this trade? "]')
df.add_user_transition(State.TURN2U, State.TURN3S, '[$favoriteTeam={#ONT(teams)}]')
df.set_error_successor(State.TURN2U, State.TURN2ERR) 
df.add_system_transition(State.TURN2ERR, State.TURN3U, "Do not know which team is benefiting more")

#turn3 df.add_system_transition(State.TURN1S1, State.TURN1U, '"Here is what I know about" $player "." #news($player) " What do you think about this situation?"')

df.add_system_transition(State.TURN3S, State.TURN3U, r'[! #newsTeam($favoriteTeam)"I agree. This will ruin $team for playoffs, they are already so close! Do you think they still have a chance?"]') #todo should call macro which predicts playoffs
df.add_user_transition(State.TURN3U, State.TURN4S, "[$response2=#POS(adj)]")
df.set_error_successor(State.TURN3U, State.TURN3ERR)
df.add_system_transition(State.TURN3ERR, State.TURN4U, "Cool opinion. I think you should say that at a party next time.") #todo need to fix this error handling, this is temporary

#turn 4
df.add_system_transition(State.TURN4S, State.TURN4U, r'[! "I really agree/disagree with you. This news has really changed my opinion on " $favoriteTeam] "What about the rest of the playoff picture? "') #todo fix the agree/disagree
df.add_user_transition(State.TURN4U, State.TURN5S, "[$response3=/[a-z A-Z]+/]")
df.set_error_successor(State.TURN4U, State.TURN4ERR)
df.add_system_transition(State.TURN4ERR, State.END, "Yea I guess youre right on that")

df.add_system_transition(State.TURN5S, State.END, 'I agree with you on that. But, ultimately, we will not know for sure until games start. We should chat once those games start. TTYL')





if __name__ == '__main__':
    df.run(debugging=False)