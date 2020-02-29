from emora_stdm import KnowledgeBase, DialogueFlow
from enum import Enum


# TODO: Update the State enum as needed
class State(Enum):
    START = 0
    TURN0 = 1
    TURN1S = 2
    TURN1U = 3
    TURN2S = 4
    TURN2U = 5
    TURN3S = 6
    TURN3U = 7
    TURN4S = 8
    TURN4U = 9
    END = 99


# TODO: create the ontology as needed
ontology = {
    "ontology": {

        }
}


knowledge = KnowledgeBase()
knowledge.load_json_file("teams.json")
df = DialogueFlow(State.START, initial_speaker=DialogueFlow.Speaker.SYSTEM, kb=knowledge)

#turn 0
df.add_system_transition(State.START, State.TURN0, '"Hi, I am NBA chatbot. I can talk to you about NBA news. Do you have a favorite team or player?"')
df.add_user_transition(State.TURN0, State.TURN1S, "#ONT(Atlanta Hawks)") #todo change this to whatever the onto label is
df.set_error_successor(State.PROMPT, State.PROMPTERR)

#turn 1
df.add_system_transition(State.TURN1S, State.TURN1U, "Here is what I know about $player/team.", "<<insert macro here>>", "What do you think about this situation?")
df.add_user_transition(State.TURN1U, State.TURN2S, "[$response1]") #todo here we could have system detect if user thinks the idea is good or bad

#turn 2
df.add_system_transition(State.TURN2S, State.TURN2U, "[!I think that is ", "#macro()", "I also heard that " "[#macro2()] ", "What do you think of that?") #todo macro here would be hard coded to always be positive view of the news
df.add_system_transition(State.TURN2U, State.TURN3S, "[$response2]")

#turn 4
df.add_system_transition(State.TURN4S, END, "[! I actually have not made a decision about this myself. How about I talk to you in a couple of day about that?")



if __name__ == '__main__':
    df.run(debugging=False)