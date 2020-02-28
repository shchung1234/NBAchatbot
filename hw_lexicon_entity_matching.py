from emora_stdm import KnowledgeBase, DialogueFlow
from enum import Enum


# TODO: Update the State enum as needed
class State(Enum):
    START = 0
    PROMPT = 1
    TURN1S = 2
    TURN1U = 3
    TURN2S = 4
    TURN2U = 5
    END = 6


# TODO: create the ontology as needed
ontology = {
    "ontology": {

        }
}


knowledge = KnowledgeBase()
knowledge.load_json_file("teams.json")
df = DialogueFlow(State.START, initial_speaker=DialogueFlow.Speaker.SYSTEM, kb=knowledge)

df.add_system_transition(State.START, State.PROMPT, '"Hi, what do you want to talk about?"')
df.add_user_transition(State.PROMPT, State.Team, "#ONT(Atlanta Hawks)")
df.set_error_successor(State.PROMPT, State.ERR)
# TODO: create your own dialogue manager


if __name__ == '__main__':
    df.run(debugging=False)