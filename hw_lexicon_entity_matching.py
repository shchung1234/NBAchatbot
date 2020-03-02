from emora_stdm import KnowledgeBase, DialogueFlow, Macro
from enum import Enum
from pip._vendor import requests
import json


# TODO: Update the State enum as needed
class State(Enum):
    START = 0
    TURN0 = 1
    TURN0ERR = 101
    TURN1S = 2
    TURN1U = 3
    TURN1ERR = 201
    TURN2S = 4
    TURN2U = 5
    TURN2ERR = 401
    TURN3S = 6
    TURN3U = 7
    TURN3ERR = 601
    TURN4S = 8
    TURN4U = 9
    TURN4ERR = 801
    END = 99


# TODO: create the ontology as needed
# andrew- isn't ontology gonna be loaded from a json file?
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
        
        exit()
        return

knowledge = KnowledgeBase()
knowledge.load_json_file("teams.json")
df = DialogueFlow(State.START, initial_speaker=DialogueFlow.Speaker.SYSTEM, kb=knowledge, macros = {'news':news()})

# THIS DOCUMENT IS THE SOURCE OF TRUTH FOR WHAT WE ARE DOING: https://docs.google.com/document/d/15N6Xo60IipqOknUGHxXt-A17JFOXOhMCZSMcOAyUEzo/edit

#turn 0
df.add_system_transition(State.START, State.TURN0, '"Hi, I am NBA chatbot. I can talk to you about NBA news. Do you have a favorite player?"')
df.add_user_transition(State.TURN0, State.TURN1S, "#ONT(Atlanta Hawks)") #todo change this to whatever the onto label is
df.set_error_successor(State.TURN0, State.TURN0ERR)
df.add_system_transition(State.TURN0ERR, State.TURN0, "I have never heard of them. What home state are you from?") #todo this turn to, what state seems rather abrupt, see if there is a way to make it more smooth

#turn 1
df.add_system_transition(State.TURN1S, State.TURN1U, '"Here is what I know about $player/team. #news($player/team) What do you think about this situation?"')
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