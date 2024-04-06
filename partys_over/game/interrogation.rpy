label int_jane:

    #variaveis temporarias que vao ser definidas na etapa de cena do crime, que e mais chata de programar, entao deixei declaradas aqui por enquanto
    #elas se ativam conforme o jogador clica no xerife (1 ou 2 vezes)

    python:
        
        talk_sheriff_1 = False
        talk_sheriff_2 = False

        curr_sus = "Jane M. Doyle"
        toleration = 5

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
        toleration = 4

        sheriff_ques_1 = False
        sheriff_ques_2 = False
        sheriff_ques_3 = False
        sheriff_ques_4 = False
        sheriff_ques_5 = False

        coll_vynil = False

    centered "Police Station - Sheriff's Office"

    pause 2

    $ first_line = False
    $ line = "So… Did you find out something interesting?"

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
            "What is \"Dehydrate Division\"?" if coll_vynil and not sheriff_ques_4:
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
                sus "Yeah… I'm like an ambulant cassette recorder…"
                sus "Got some pretty weird stuff recorded too…"
                python:
                    tolerance -= 1
                    angela_ques_1 = True
            "What do you remember from yesterday?" if not angela_ques_2:
                if not first_line:
                    $ first_line = True
                sus "Well, it scared the hell out of me…"
                sus "I recorded some audio, if it's useful…"
                centered "Obtained \033[1;31mAngela's Cassette #1"
                python:
                    tolerance -= 1
                    angela_ques_2 = True
            "Do you have anyone suspicious in mind?" if not angela_ques_3:
                if not first_line:
                    $ first_line = True
                sus "No one at all… But I think this dead guy was at Faith Coombs' house last year's Halloween."
                sus "I wasn't at the party, but it's literally the house in front to mine."
                python:
                    tolerance -= 1
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
                sus "Also, I've never seen any car hitting Freddie Hayes…"
                python:
                    tolerance -= 1
                    angela_ques_5 = True
            "How do you feel about living here?" if not angela_ques_6:
                if not first_line:
                    $ first_line = True
                sus "It's quiet, but… Kinda scary sometimes…"
                python:
                    tolerance -= 1
                    angela_ques_6 = True
