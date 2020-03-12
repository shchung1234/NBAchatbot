from emora_stdm import KnowledgeBase, DialogueFlow, Macro
from enum import Enum, auto
from pip._vendor import requests
import json


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
        #THIS IS A PRIVATE REPO, BUT IDK IF GITHUB WILL LET THE KEY BE PUSHED, SO I'M GONNA PUT THE KEY INTO GOOGLE DOCS?

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
        #andrew- im just gonna assume that the input is the team name and only the team name, eg "Atlanta Hawks"
        #THIS IS A PRIVATE REPO, BUT IDK IF GITHUB WILL LET THE KEY BE PUSHED, SO I'M GONNA PUT THE KEY INTO GOOGLE DOCS?

        endpoint = vars['favoriteTeam'].replace(" ", "%20") +"%20basketball"
        endpoint = "http://newsapi.org/v2/everything?q="+endpoint+"&apiKey=d50b19bb1c7445b588bb694ecc2a119f"
        news = requests.get(endpoint)
        formatted_news = news.json()
        formatted_news = formatted_news['articles']

        ## THINGS TO RETURN #####
        title = formatted_news[0]['title']
        description = formatted_news[0]['description']
        #########################
        result = ""

        return "I found this recent news headline about {}. {}. It says {}".format(vars['favoriteTeam'], title, description)

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

df.add_system_transition(State.TURN3S, State.TURN3U, r'[! #newsTeam($favoriteTeam)"I agree. This will ruin $team for playoffs, they are already so close!"]') #todo should call macro which predicts playoffs
df.add_user_transition(State.TURN3U, State.TURN4S, "[$response2=#POS(adj)]")
df.set_error_successor(State.TURN3U, State.TURN3ERR)
df.add_system_transition(State.TURN3ERR, State.TURN4U, "Cool opinion. I think you should say that at a party next time.") #todo need to fix this error handling, this is temporary

#turn 4
df.add_system_transition(State.TURN4S, State.TURN4U, r'[! "I really agree with you. This news has really changed my opinion on " $favoriteTeam " How do you think it will impact their playoff prospects?"]')
df.add_user_transition(State.TURN4U, State.TURN5S, "[$response3=/[a-z A-Z]+/]")
df.set_error_successor(State.TURN4U, State.TURN4ERR)
df.add_system_transition(State.TURN4ERR, State.END, "Yea I guess youre right on that")

df.add_system_transition(State.TURN5S, State.END, 'I agree with you on that. But, ultimately, we will not know for sure until games start. We should chat once those games start. TTYL')





if __name__ == '__main__':
    df.run(debugging=False)