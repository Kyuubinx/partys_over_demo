label int_jane:

    #variaveis temporarias que vao ser definidas na etapa de cena do crime, que e mais chata de programar, entao deixei declaradas aqui por enquanto
    #elas se ativam conforme o jogador clica no xerife (1 ou 2 vezes)

    python:
        
        talk_sheriff_1 = False
        talk_sheriff_2 = False

        curr_sus = "Jane M. Doyle"
        tolerance = 5

        jane_ques_1 = False
        jane_ques_2 = False
        jane_ques_3 = False
        jane_ques_4 = False
        jane_ques_5 = False

        know_angela = False

    centered "Rainbow Building - 2nd Floor"

    pause 2

    $ first_line = False
    $ line = "Oh, thank god you're here!! I was so scared..."

    while tolerance > 0:
        if first_line:
            $ line = ""
        menu:
            sus "[line]"
            "What did you hear?" if not jane_ques_1:
                if not first_line:
                    $ first_line = True
                $ tolerance -= 1
                sus "Lots of painful screams, and then, after a while, a male singing... I could also hear some fingerstyled guitar playing... All from the same direction..."
                $ jane_ques_1 = True
            "Were you alone?" if not jane_ques_2:
                if not first_line:
                    $ first_line = True
                $ tolerance -= 1
                sus "Actually, no..."
                sus "My friend was here..."
                $ jane_ques_2 = True
                if not jane_ques_3:
                    sus "Her name is Angela..."
                    sus "It might be good to have a chat with her."
                    $ know_angela = True
                $ jane_ques_2 = True
            "Did you see anyone suspicious?" if not jane_ques_3:
                if not first_line:
                    $ first_line = True
                $ tolerance -= 1
                sus "I was too scared to look through the window, but my friend might have seen something..."
                if not jane_ques_2:
                    sus "Her name is Angela..."
                    sus "It might be good to have a chat with her."
                    $ know_angela = True
                $ jane_ques_3 = True
            "Did you know the victim?" if not jane_ques_4:
                if not first_line:
                    $ first_line = True
                $ tolerance -= 1
                sus "I wouldn't say I knew him, but I've seen him through this alley sometimes..."
                sus "Bonkers..."
                $ jane_ques_4 = True
            "Do you have anyone suspicious in mind?" if not jane_ques_5:
                if not first_line:
                    $ first_line = True
                $ tolerance -= 1
                sus "No, sorry..."
                sus "But it's curious, considering last years incidents..."
                sus "Never thought Halloween season would scare me this much..."
                $ jane_ques_5 = True
            "--Finish Interrogation--":
                $ tolerance = 0
        

label int_sheriff:
    
    python:

        curr_sus = "Sheriff Salice"
        tolerance = 4

        sheriff_ques_1 = False
        sheriff_ques_2 = False
        sheriff_ques_3 = False
        sheriff_ques_4 = False
        sheriff_ques_5 = False

        coll_vinyl = False

    centered "Police Station - Sheriff's Office"

    pause 2

    $ first_line = False
    $ line = "So... Did you find out something interesting?"

    while tolerance > 0:
        if first_line:
            $ line = ""
        menu:
            sus "[line]"
            "Where does Angela live?" if (jane_ques_2 or jane_ques_3) and not sheriff_ques_1:
                if not first_line:
                    $ first_line = True
                sus "Angela Gracie Reeds..."
                sus "Surely a strange girl..."
                sus "I want to say she was just in the wrong place at the wrong time…"
                sus "But this is starting to happen kinda often…"
                sus "Anyways, she lives about two miles away from the crime scene."
                python:
                    tolerance -= 1
                    sheriff_ques_1 = True
            "What exactly happened last year?" if (talk_sheriff_2 or jane_ques_5) and not sheriff_ques_2:
                if not first_line:
                    $ first_line = True
                if talk_sheriff_2:
                    sus "Like I said..."
                sus "Same time of the year, two teenagers disappeared and one died in a mysterious car crash."
                sus "The thing is…"
                sus "It all happened in the same place, and the same night."
                sus "It was October 31st."
                sus "Thomas Tinley and Ariana Marsh disappeared, and Frederich Hayes crashed his car with Faith Coombs sitting in the passenger's seat."
                sus "Faith survived, and it's curious how everything happened around the Coomb's house."
                python:
                    tolerance -= 1
                    sheriff_ques_2 = True
            "What did you mean by \"Mysterious car accident\"?" if (talk_sheriff_2 or sheriff_ques_2) and not sheriff_ques_3:
                if not first_line:
                    $ first_line = True
                sus "Well, Frederich sure hit something REALLY hard."
                sus "His car was devastated."
                sus "But we never found the other car."
                sus "And every single person who was close to the accident said they never saw any other car."
                sus "It's like the boy hit the vacuum."
                python:
                    tolerance -= 1
                    sheriff_ques_3 = True
            "What is \"Dehydrate Division\"?" if coll_vinyl and not sheriff_ques_4:
                if not first_line:
                    $ first_line = True
                if sheriff_ques_2:
                    sus "Speaking of the Devil..."
                sus "An indie rock duo."
                sus "They played at some bars in the town."
                if sheriff_ques_2:
                    "Wanna know the best part?"
                    "Thomas Tinley was the singer and guitarist and Frederich Hayes was the drummer."
                python:
                    tolerance -= 1
                    sheriff_ques_4 = True
            "Were you shocked by the crime scene?" if not sheriff_ques_5:
                if not first_line:
                    $ first_line = True
                "Nah, it's actually pretty common."
                python:
                    tolerance -= 1
                    sheriff_ques_5 = True
            "--Finish Interrogation--":
                $ tolerance = 0
    
    sus "You know, it's getting late."
    sus "Got work to do tomorrow."
    if sheriff_ques_1:
        "You can go check out on Angela if you want to."

label int_angela:

    python:
        
        curr_sus = "Angela Gracie Reeds"
        tolerance = 6

        angela_ques_1 = False
        angela_ques_2 = False
        angela_ques_3 = False
        angela_ques_4 = False
        angela_ques_5 = False
        angela_ques_6 = False

        know_faith = False

    centered "Angela's House"

    pause 2

    $ first_line = False
    $ line = "A police officer? Did I do something wrong?"

    while tolerance > 0:
        if first_line:
            $ line = ""
        menu:
            sus "[line]"
            "Do you like to film things?" if not angela_ques_1:
                if not first_line:
                    $ first_line = True
                sus "Yeah... I'm like an ambulant cassette recorder..."
                sus "Got some pretty weird stuff recorded too..."
                python:
                    tolerance -= 1
                    angela_ques_1 = True
            "What do you remember from yesterday?" if not angela_ques_2:
                if not first_line:
                    $ first_line = True
                sus "Well, it scared the hell out of me..."
                sus "I recorded some audio, if it's useful..."
                centered "Obtained \033[1;31mAngela's Cassette #1"
                python:
                    tolerance -= 1
                    angela_ques_2 = True
            "Do you have anyone suspicious in mind?" if not angela_ques_3:
                if not first_line:
                    $ first_line = True
                sus "No one at all... But I think this dead guy was at Faith Coombs' house last year's Halloween."
                sus "I wasn't at the party, but it's literally the house in front to mine."
                python:
                    tolerance -= 1
                    know_faith = True
                    angela_ques_3 = True
            "What's your relation with Jane M. Doyle?" if not angela_ques_4:
                if not first_line:
                    $ first_line = True
                sus "A childhood friend."
                sus "We still hang out once in a while."
                python:
                    tolerance -= 1
                    angela_ques_4 = True
            "What do you know about last year's event?" if not angela_ques_5:
                if not first_line:
                    $ first_line = True
                sus "Not much concrete stuff, but it all happened here, right?"
                if not angela_ques_3:
                    sus "Faith Coombs lives at the other side of the street."
                sus "People call me crazy, but I could swear I saw a girl falling from the house's roof."
                sus "Also, I've never seen any car hitting Freddie Hayes..."
                python:
                    tolerance -= 1
                    angela_ques_5 = True
            "How do you feel about living here?" if not angela_ques_6:
                if not first_line:
                    $ first_line = True
                sus "It's quiet, but... Kinda scary sometimes..."
                python:
                    tolerance -= 1
                    angela_ques_6 = True
            "--Finish Interrogation--":
                $ tolerance = 0

label int_faith:

    python:

        curr_sus = "Faith Coombs"
        tolerance = 7

        faith_ques_1 = False
        faith_ques_2 = False
        faith_ques_3 = False
        faith_ques_4 = False
        faith_ques_5 = False
        faith_ques_6 = False
        faith_ques_7 = False
        faith_ques_8 = False
        faith_ques_9 = False
        faith_ques_10 = False

        know_faith = True

        know_rowan = False
        know_seth = False
        know_melvin = False
        know_kimberlyn = False
        know_sarah = False
        know_finn = False

    centered "Coombs' House"

    pause 2

    $ first_line = False
    $ line = "Oh, great. Again."

    while tolerance > 0:
        if first_line:
            $ line = ""
        menu:
            sus "[line]"
            "Do you live alone?" if not faith_ques_1:
                if not first_line:
                    $ first_line = True
                sus "I live with my older brother."
                sus "He might know something interesting, but be careful."
                sus "He barely talks to me, I don't think he'll enjoy talking to you."
                sus "My parents left us the house and moved with my younger brother."
                python:
                    tolerance -= 1
                    faith_ques_1 = True
                    know_seth = True
            "Whose car is that on your garage?" if not faith_ques_2:
                if not first_line:
                    $ first_line = True
                sus "Oh, it's Rowan's."
                python:
                    tolerance -= 1
                    faith_ques_2 = True
                    know_rowan = True
            "Do you know someone who was close to any of the missing people from last year?" if not faith_ques_3 and (talk_sheriff_2 or sheriff_ques_2 or faith_ques_5):
                if not first_line:
                    $ first_line = True
                sus "Me, I guess..."
                sus "But if it's not enough..."
                sus "Well, there's Finn..."
                sus "Finneas Copeland."
                sus "I don't think he'll cooperate, though."
                sus "You should try Melvin, even though I didn't invite him to the party."
                sus "He lives 3 blocks away."
                sus "Melvin M. Tores."
                python:
                    tolerance -= 2
                    faith_ques_3 = True
                    know_melvin = True
            "Do you know someone who was close to Freddie Hayes and I could interrogate?" if not faith_ques_4 and sheriff_ques_3:
                if not first_line:
                    $ first_line = True
                sus "Well, there's Kimberlyn, her girlfriend at the time."
                sus "She lives in another state, so you can try calling her."
                sus "Here, I'll give you her number."
                python:
                    tolerance -= 2
                    faith_ques_4 = True
                    know_kimberlyn = True
            "What exactly happened at the party a year ago?" if not faith_ques_5 and (talk_sheriff_2 or sheriff_ques_2):
                if not first_line:
                    $ first_line = True
                sus "And here we go again..."
                sus "It was an ordinary Halloween party, to celebrate my 18th birthday."
                sus "Had a heartbreak, got so fucking pissed with some people, and of course things wouldn't end well."
                sus "The midnight game started."
                sus "Some people were still smoking weed, others still drinking."
                sus "Then when it all ended, Tommy and Ari went missing, and Freddie... {p=1} Yeah..."
                python:
                    tolerance -= 3
                    faith_ques_5 = True
            "How do you know Angela G. Reeds?" if not faith_ques_6:
                if not first_line:
                    $ first_line = True
                sus "Who?"
                python:
                    tolerance += 2
                    faith_ques_6 = True
            "Who planned the games you were playing?" if not faith_ques_7 and faith_ques_5:
                if not first_line:
                    $ first_line = True
                sus "The midnight game?"
                sus "It was Sarah."
                sus "Sarah Barber."
                sus "She is... {p=1} Was... {p=1} My friend."
                sus "Now she's just my brother's girlfriend."
                python:
                    tolerance += 1
                    faith_ques_7 = True
                    know_sarah = True
            "What kind of relation did you have with the missing people?" if not faith_ques_8 and (talk_sheriff_2 or sheriff_ques_2 or faith_ques_5):
                if not first_line:
                    $ first_line = True
                    sus "I was a very close friend of them both."
                    sus "They started dating because I was the one to introduce them."
                    python:
                        tolerance -= 2
                        faith_ques_8 = True
            "Tell me about Finneas Copeland" if not faith_ques_9 and faith_ques_3:
                if not first_line:
                    $ first_line = True
                sus "I mean, don't get me wrong, he's a nice guy..."
                sus "But Tommy is a delicate subject to him, so be patient..."
                python:
                    tolerance += 2
                    faith_ques_9 = True
                    know_finn = True
            "What were you doing in Frederich's car's passenger's seat?" if not faith_ques_10 and faith_ques_5:
                if not first_line:
                    $ first_line = True
                sus "Let's say the midnight game went kinda wrong."
                sus "Some people were too high too."
                sus "He tried to take me out of the house with him."
                sus "I don't remember anything after getting in the car."
                python:
                    tolerance -= 1
                    faith_ques_10 = True
            "--Finish Interrogation--":
                $ tolerance = 0

label int_rowan:

    python:

        curr_sus = "Rowan Long"
        tolerance = 3

        rowan_ques_1 = False
        rowan_ques_2 = False
        rowan_ques_3 = False
        rowan_ques_4 = False

        if know_faith == None:
            know_faith = False
        
    centered "Coombs' House"

    pause 2.0

    $ first_line = False
    $ line = "Oh, can I help you?"

    while tolerance > 0:
        if first_line:
            $ line = ""
        menu:
            sus "[line]"
            "Does Faith Coombs live here?" if not rowan_ques_1 and know_faith:
                if not first_line:
                    $ first_line = True
                sus "Oh, yes, she's watching TV on the couch right now."
                python:
                    tolerance -= 1
                    rowan_ques_1 = True
            "Did you notice anything weird yesterday?" if not rowan_ques_2:
                if not first_line:
                    $ first_line = True
                sus "Well, my guitar was gone..."
                sus "That got me pissed off."
                python:
                    tolerance -= 1
                    rowan_ques_2 = True
            "Tell me about your guitar." if not rowan_ques_3 and rowan_ques_2:
                if not first_line:
                    $ first_line = True
                sus "Oh, it's a black Les Paul."
                sus "It sounds like a freakshow."
                sus "I bought it at Prism Music Store."
                python:
                    tolerance += 1
                    rowan_ques_3 = True
            "What do you think about Dehydrate Division?" if not rowan_ques_4 and coll_vinyl and rowan_ques_2:
                if not first_line:
                    $ first_line = True
                sus "Rest in peace, Freddie..."
                sus "I wonder what happened to Tommy..."
                sus "The band was absurdly good."
                sus "I always felt insecure to ask them if I could join."
                sus "Do you think The Midnight Man took Tommy and Ari?"
                python:
                    tolerance -= 2
                    rowan_ques_4 = True
            "--Finish Interrogation--":
                $ tolerance = 0

label int_seth:

    python:
        
        curr_sus = "Seth Coombs"
        tolerance = 2

        seth_ques_1 = False
        seth_ques_2 = False
        seth_ques_3 = False
        seth_ques_4 = False

    centered "Seth's Bedroom"
        
    pause 2

    $ first_line = False
    $ line = "What?"

    while tolerance > 0:
        if first_line:
            $ line = ""
        menu:
            sus "[line]"
            "Did you notice anything weird yesterday?" if not seth_ques_1:
                if not first_line:
                    $ first_line = True
                sus "Some weird noises like someone was here."
                sus "Tried to check but didn't see a thing."
                sus "Also, for some reason, a piece of the lawn outside died."
                sus "I think it was just the place that..."
                sus "Nevermind..."
                python:
                    tolerance -= 1
                    seth_ques_1 = True
            "What do you think about Dehydrate Division?" if not seth_ques_2 and coll_vinyl:
                if not first_line:
                    $ first_line = True
                sus "Shitty band."
                python:
                    tolerance -= 1
                    seth_ques_2 = True
            "Do you know Angela G. Reeds?" if not seth_ques_3 and faith_ques_6:
                if not first_line:
                    $ first_line = True
                sus "The freak that lives in front of us?"
                sus "I don't, but Kian may know something."
                sus "Name's Kian Hayden."
                python:
                    tolerance -= 1
                    seth_ques_3 = True
            "Tell me about Sarah Barber" if not seth_ques_4 and faith_ques_7:
                if not first_line:
                    $ first_line = True
                sus "Why should I?"
                sus "It's my girlfriend."
                sus "What do you want?"
                python:
                    tolerance -= 1
                    seth_ques_4 = True
            "--Finish Interrogation--":
                $ tolerance = 0

label int_ruben:
    
    python:
        
        curr_sus = "Ruben J. Waters"
        tolerance = 3

        ruben_ques_1 = False
        ruben_ques_2 = False
        ruben_ques_3 = False
        ruben_ques_4 = False
        ruben_ques_5 = False

    centered "Prism Music Store"
        
    pause 2

    $ first_line = False
    $ line = "How can I help you?"

    while tolerance > 0:
        if first_line:
            $ line = ""
        menu:
            sus "[line]"
            "Did you ever sell to Dehydrate Division?" if not ruben_ques_1 and coll_vinyl:
                if not first_line:
                    $ first_line = True
                sus "Yeah, I'd say all their gear comes from here."
                sus "Instruments, amplifiers, pedals, everything."
                sus "Those boys spent four years working to get everything they had from here."
                sus "I was so happy to see them growing."
                sus "It's really sad that things turned out this way..."
                python:
                    tolerance -= 1
                    ruben_ques_1 = True
            "What kind of people were they?" if not ruben_ques_2 and ruben_ques_1:
                if not first_line:
                    $ first_line = True
                sus "They were really serene people."
                sus "Never seen any of them passing off the limits."
                sus "Not the kind of rock band who would get in toruble."
                python:
                    tolerance -= 1
                    ruben_ques_2 = True
            "Show me the model you sold to Rowan" if not ruben_ques_3:
                if not first_line:
                    $ first_line = True
                sus "Rowan Long?"
                sus "Good kid."
                sus "Sure, I think I still have that model."
                python:
                    tolerance -= 1
                    seth_ques_3 = True
            "What's your relation with Joel Chatham?" if not ruben_ques_4:
                if not first_line:
                    $ first_line = True
                sus "Well, the D.D. kids talked about him..."
                sus "Never actually seen him."
                sus "He was the only member who already had his gear, if you can actually call him a member."
                python:
                    tolerance -= 1
                    ruben_ques_4 = True
            "Where were the places Dehydrate Division used to play at?" if not ruben_ques_5:
                if not first_line:
                    $ first_line = True
                sus "They used to play at Richardon's Bar."
                python:
                    tolerance -= 1
                    seth_ques_4 = True
            "--Finish Interrogation--":
                $ tolerance = 0

label int_kevin:
        
    python:
        
        curr_sus = "Kevin E. Richardson"
        tolerance = 3

        kevin_ques_1 = False
        kevin_ques_2 = False
        kevin_ques_3 = False
        kevin_ques_4 = False
        kevin_ques_5 = False

    centered "Richardson's Bar"
        
    pause 2

    $ first_line = False
    $ line = "Welcome."

    while tolerance > 0:
        if first_line:
            $ line = ""
        menu:
            sus "[line]"
            "What kind of people come to this bar?" if not kevin_ques_1:
                if not first_line:
                    $ first_line = True
                sus "All sorts, friend."
                sus "There's not really an answer."
                python:
                    tolerance -= 1
                    kevin_ques_1 = True
            "Did Dehydrate Division play here before?" if not kevin_ques_2 and coll_vinyl:
                if not first_line:
                    $ first_line = True
                sus "They were the most popular band of this bar."
                sus "Almost every Saturday night they would come."
                sus "It's sad that those nights had to end."
                python:
                    tolerance -= 1
                    kevin_ques_2 = True
            "How did people act when Dehydrate Division played here?" if not kevin_ques_3 and kevin_ques_2:
                if not first_line:
                    $ first_line = True
                sus "Never seen them more energetic."
                sus "They surely had a future waiting for them."
                python:
                    tolerance -= 1
                    kevin_ques_3 = True
            "What do you know about Joel Chatham?" if not kevin_ques_4:
                if not first_line:
                    $ first_line = True
                sus "Lazy bass player."
                sus "Never liked him."
                python:
                    tolerance -= 1
                    kevin_ques_4 = True
            "How long is the bar working?" if not kevin_ques_5:
                if not first_line:
                    $ first_line = True
                sus "Since the start of the 90's"
                python:
                    tolerance -= 1
                    kevin_ques_5 = True
            "--Finish Interrogation--":
                $ tolerance = 0

label int_kimberlyn:
    
    python:
        
        curr_sus = "Kimberlyn G. Buffington"
        tolerance = 3

        kimberlyn_ques_1 = False
        kimberlyn_ques_2 = False
        kimberlyn_ques_3 = False
        kimberlyn_ques_4 = False
        kimberlyn_ques_5 = False
        kimberlyn_ques_6 = False

    centered "CALLING..."
        
    pause 2

    $ first_line = False
    $ line = "Hello?"

    while tolerance > 0:
        if first_line:
            $ line = ""
        menu:
            sus "[line]"
            "How was your relation with Frederich?" if not kimberlyn_ques_1:
                if not first_line:
                    $ first_line = True
                sus "It was cool."
                sus "But I had to move on, right?"
                sus "Guess I knew exactly how to move on."
                python:
                    tolerance -= 1
                    kimberlyn_ques_1 = True
            "What kind of interaction did you have with Thomas Tinley?" if not kimberlyn_ques_2:
                if not first_line:
                    $ first_line = True
                sus "..."
                sus "Why is he important?"
                python:
                    tolerance -= 1
                    kimberlyn_ques_2 = True
            "Where were you at the night of the party?" if not kimberlyn_ques_3:
                if not first_line:
                    $ first_line = True
                sus "Well, I live in another state."
                sus "Obviously, I was at my hometown."
                python:
                    tolerance -= 1
                    kimberlyn_ques_3 = True
            "Are you dating someone now?" if not kimberlyn_ques_4:
                if not first_line:
                    $ first_line = True
                sus "Yes."
                sus "Clearence is just a cutie."
                python:
                    tolerance -= 1
                    kimberlyn_ques_4 = True
            "How did you meet Frederich?" if not kimberlyn_ques_5:
                if not first_line:
                    $ first_line = True
                sus "We met when he travelled to my hometown."
                sus "We hung out and started talking."
                python:
                    tolerance -= 1
                    kimberlyn_ques_5 = True
            "What do you know about Joel Chatham?" if not kimberlyn_ques_6:
                if not first_line:
                    $ first_line = True
                sus "I didn't meet him actually."
                sus "But Freddie never gave me a good impression of him."

                python:
                    tolerance -= 1
                    kimberlyn_ques_6 = True
            "--Finish Interrogation--":
                $ tolerance = 0

label int_melvin:
    
    python:
        
        curr_sus = "Melvin M. Torres"
        tolerance = 4

        melvin_ques_1 = False
        melvin_ques_2 = False
        melvin_ques_3 = False
        melvin_ques_4 = False
        melvin_ques_5 = False

    centered "Melvin's House"
        
    pause 2

    $ first_line = False
    $ line = "Good evening..."

    while tolerance > 0:
        if first_line:
            $ line = ""
        menu:
            sus "[line]"
            "" if not []_ques_1:
                if not first_line:
                    $ first_line = True
                sus "Why should I?"
                sus "It's my girlfriend."
                sus "What do you want?"
                python:
                    tolerance -= 1
                    seth_ques_4 = True
            "" if not []_ques_1:
                if not first_line:
                    $ first_line = True
                sus "Why should I?"
                sus "It's my girlfriend."
                sus "What do you want?"
                python:
                    tolerance -= 1
                    seth_ques_4 = True
            "" if not []_ques_1:
                if not first_line:
                    $ first_line = True
                sus "Why should I?"
                sus "It's my girlfriend."
                sus "What do you want?"
                python:
                    tolerance -= 1
                    seth_ques_4 = True
            "" if not []_ques_1:
                if not first_line:
                    $ first_line = True
                sus "Why should I?"
                sus "It's my girlfriend."
                sus "What do you want?"
                python:
                    tolerance -= 1
                    seth_ques_4 = True
            "" if not []_ques_1:
                if not first_line:
                    $ first_line = True
                sus "Why should I?"
                sus "It's my girlfriend."
                sus "What do you want?"
                python:
                    tolerance -= 1
                    seth_ques_4 = True
            "--Finish Interrogation--":
                $ tolerance = 0
                
    