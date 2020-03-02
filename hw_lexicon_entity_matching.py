from emora_stdm import KnowledgeBase, DialogueFlow, Macro
from enum import Enum
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
    END = auto()


# ONTOLOGY IS LOADED FROM teams.json
ontology = {
    "ontology": {

        }
}

class news(Macro):
    def run (self, ngrams, vars, args):
        #andrew- im just gonna assume that the input is the team name and only the team name, eg "Atlanta Hawks"
        #THIS IS A PRIVATE REPO, BUT IDK IF GITHUB WILL LET THE KEY BE PUSHED, SO I'M GONNA PUT THE KEY INTO GOOGLE DOCS?
        endpoint = args[0].replace(" ", "%20")
        print(endpoint)
        endpoint = "http://newsapi.org/v2/everything?q="+endpoint+"&domains=espn.com&apiKey="
        print(endpoint)
        news = requests.get(endpoint)
        formatted_news = news.json()
        formatted_news = formatted_news['articles']

        ## THINGS TO RETURN #####
        title = formatted_news[0]['title']
        description = formatted_news[0]['description']
        #########################
        
        return title

knowledge = KnowledgeBase()
knowledge.load_json_file("teams.json")
df = DialogueFlow(State.START, initial_speaker=DialogueFlow.Speaker.SYSTEM, kb=knowledge, macros = {'news':news()})

# THIS DOCUMENT IS THE SOURCE OF TRUTH FOR WHAT WE ARE DOING: https://docs.google.com/document/d/15N6Xo60IipqOknUGHxXt-A17JFOXOhMCZSMcOAyUEzo/edit

#turn 0
df.add_system_transition(State.START, State.TURN0, '"Hi, I am NBA chatbot. I can talk to you about NBA news. Do you have a favorite player from NBA?"')
df.add_user_transition(State.TURN0, State.TURN1S1, "$player = #ONT(player)") #todo change this to player name
df.add_user_transition(State.TURN0, State.TURN1S2, "") #gives a name that's not currently in NBA
df.set_error_successor(State.TURN0, State.TURN0ERR)
df.add_system_transition(State.TURN0ERR, State.TURN0, "I have never heard of them. Please enter a current player") #todo this turn to, what state seems rather abrupt, see if there is a way to make it more smooth

#turn 1
df.add_system_transition(State.TURN1S1, State.TURN1U, '"Here is what I know about $player. #news($player) What do you think about this situation?"')
df.add_system_transition(State.TURN1S2, State.TURN1U, '"Oh this person is not in NBA right now. Do you have any current NBA player that you want to talk about?"')
df.add_user_transition(State.TURN1U, State.TURN1S1, "$player = #ONT(player)") # gives player name that is in ontology
df.add_user_transition(State.TURN1U, State.TURN2S, "[$response1]") #todo here we could have system detect if user thinks the idea is good or bad
df.set_error_successor(State.TURN1U, State.TURN1ERR, "I have heard that a lot of people have similar opinions to that")
df.set_system_transition(State.TURN1ERR, State.TURN2S) #todo this might be wrong

#turn 2
df.add_system_transition(State.TURN2S, State.TURN2U, "[!I think that is ", "#macro()", "I also heard that " "[#macro2()] ", "What do you think of that?") #todo macro here would be hard coded to always be positive view of the news
df.add_system_transition(State.TURN2U, State.TURN3S, "[$response2]")
df.set_error_successor(State.TURN2U, State.TURN2ERR, "That is a pretty interesting take, I have not heard that before")
df.add_system_transition(State.TURN2ERR, State.TURN3S)

#turn3
df.add_system_transition(State.TURN3S, State.TURN3U, "I agree with your take. This move also definetly impacts the ", "#macro, ", "how big of a change do you think this will be?")
df.add_user_transition(State.TURN3U, State.TURN4S, "[$response3]")
df.set_error_successor(State.TURN3U, State.TURN3ERR, "")

df.add_system_transition(State.TURN3ERR, State.TURN3S) #todo need to fix this error handling, this is temporary


#turn 4
df.add_system_transition(State.TURN4S, END, "[! I actually have not decided myself how important this move is. How about I talk to you in a couple of day about that?")



if __name__ == '__main__':
    df.run(debugging=False)