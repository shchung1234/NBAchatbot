Required Packages:
Emora-stdm
Enum
Requests
Sportsreference.nba.schedule
Sportsreference.nba.roster
Json
Random
Nltk - nltk.download(‘vader_lexicon’)


Required Jsons:
teams.json
trades.json
original_names.json




What we want to show off: 
1. Player specific rationale
        Our bot has two favorite players. Kawhi Leonard and Jimmy Butler. The bot is able to 
respond to critiques which are specific to the two players. E.g. for Kawhi Leonard, that 
he is injury prone, for Jimmy Butler that he has bad chemistry with other players
        
2. Nicknames
        We can capture how people naturally talk about players which may include nicknames.  
E.g. lbj for lebron james, aquaman for steven adams, or greek freak for Giannis                 Antetokounmpo


3. Opinion on each different player changes (player rating macro)
        Our bot will have different opinions about different players. These are not hardcoded 
beforehand but pull from the dataset about players and formulates an opinion based on 
their stats. This also changes in relation to the context the opinion is being sought in e.g. overall opinion vs opinion of how the player will perform in playoffs. E.g. in conversation #1 our bot has a different opinion for Giannis Antetokounmpo vs Jordan McRae


4. Engagement with users’ emotions even if sentence isn’t caught by ontology (sentiment analyzer)
        Bot will indicate to the user that we understand the sentiment of their opinion even if the 
bot isn’t able to respond to their specific comment e.g. in conversation #1 we see the user is neutral about Isaiah Thomas


5. Variation
No two conversations will ever be identical because of variation of responses based on opinions and players mentioned by user throughout the conversation, and also individual changes in each utterance 
Sample conversation #1: 
-greek freak is a player nickname (any famous nicknames will be recognized)


S: Hi I am NBA chatbot. The NBA season has been put on hold because of COVID-19.  If we had playoffs based off the current standings , which team do you think would win?
U: the bucks will win
S:  Why do you think the bucks will win?
U: they have greek freak # nickname recognition
S:    I see giannis antetokounmpo is having an exceptional season. Personally, I think Clippers will win because Kawhi Leonard is more clutch . Whats your opinion of Kawhi Leonard ?
U: he is too fragile # specific rationale catch for Kawhi Leonard
S: Even though he is fragile  he always  overperforms  in playoffs. Anyways, I saw that Isaiah Thomas  from Washington Wizards went to LA Clippers . What are your thoughts about  Isaiah Thomas  ?
U: i dont have much thoughts
S: Okay, I can tell youre pretty neutral about Isaiah Thomas  . I dont think he is too terrible but he doesnt seem to have a huge impact to the game.  Do you think that trade influenced how the  LA Clippers  performed this season? #Sentiment analyser used as fail-safe error handler for opinions
U: hes probably not going to affect
S: I agree, the trade was early in the season and he has not shown he was worth it . Do you think he will play a big role in getting the  LA Clippers to playoffs next year?
U: maybe
S: I do not think he will play a big role. I think he is past his prime. I am a little uncertain too. You can never account for randomness like injuries sidelining players.  do you want to chat about another trade ?
U: yes
S: Okay! I found a new trade news that says that Willie Cauley-Stein  from Golden State Warriors is going to Dallas Mavericks Does that sound interesting?
U: no
S: I found this other trade article. Jordan McRae  from Washington Wizards is going to Denver Nuggets
U: yes
S: Okay, then what do you think about Jordan McRae  ?
U: hes pretty good
S: So you think  Jordan McRae   is aight.  As an unexperienced player, I think Jordan McRaeHe has been making stable contribution to the team even though his stats don't stand out.And I think his contribution can get even better if playoff was to start.  Do you think that trade influenced how the  Denver Nuggets  performed this season? # player evaluation can change with the players




Sample Conversation #2: a scenario where the user starts the conversation with i don’t know (represents a less engaged user)


S: Hi I am NBA chatbot. The NBA season has been shutdown because of COVID-19.  If we had playoffs today , which team do you think would win?
U: i dont know
S:  Its okay to be unsure. I think that the Clippers can win if we were to play today. Do you agree?
U: no
S: Oh thats interesting! Why do you think the Clippers will not win?
U: i heard they dont have good players
S: What... I actually dont agree with you when you say that the Clippers are not good . In addition, I also think that the Clippers will win because of  Kawhi Leonard .  What do you think of Kawhi Leonard ?
U: ive heard he has bad stamina
S: Hmm... I mean I hear you when you say Kawhi Leonard has bad stamina , but hes also extremely clutch! . Lets go back to the teams for now though. Earlier in the season I heard that Marcus Morris Sr.  from New York Knicks went to LA Clippers . What do you think about  Marcus Morris Sr.  ?
U: he has mediocre shooting
S: So you think  Marcus Morris Sr.   is bad.  As a veteran player, I think Marcus Morris had a stable career.He has been scoring really well making a good contribution to LA ClippersAnd I think his contribution can get even better if playoff was to start.  Do you think that trade influenced how the  LA Clippers  performed this season?
U: oh in that case yea
S: he was traded quite recently before covid shutdown so I am wondering if he will continue to perform as well as he has so far . Do you think he will play a big role in getting the  LA Clippers to playoffs next year?
U: sure
S: So you are excited to see him play next year.  I do not think he will play a big role. I think he is past his prime. would you like to chat about another trade ?
U: no
S: Okay, well in that case we can talk again later. Bye!


Sample conversation #3: conversation when user picks the clippers as their favorite


S: Hi I am NBA chatbot. The NBA season has been suspended because of COVID-19.  If we had playoffs right now , which team do you think would win?
U: the clippers
S:  Why do you think the clippers will win?
U: they have kawhi
S:    I see kawhi leonard is having an exceptional season. Personally, I think Miami Heat will win because Jimmy Butler is more clutch . Whats your opinion of Jimmy Butler ?
U: he has bad chemistry with his team
S: You might think that he has bad chemistry but I think he always comes out clutch in playoffs. Speaking of playoffs, I heard that Isaiah Thomas  from Washington Wizards went to LA Clippers . What do you think about  Isaiah Thomas  ?
U: hes okay
S: So you think  Isaiah Thomas   is aight.  I dont think he is too terrible but he doesnt seem to have a huge impact to the game.  Do you think that trade influenced how the  LA Clippers  performed this season?
U: not really
S: actually though, i do not think he had enough time to impact the team because he was traded close to the covid shutdown . Do you think he will play a big role in getting the  LA Clippers to playoffs next year?
U: no
S: So you do not have high hopes  I do not think he will play a big role. I think he is past his prime. would you like to chat about another trade ?
U: yea sure
S: Okay! I found a new article that says that Gerald Green  from Houston Rockets is going to Denver Nuggets Does that sound interesting?
U: cool
S: Okay, then what do you think about Gerald Green  ?