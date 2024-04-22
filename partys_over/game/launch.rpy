screen name_input:
    window:

        style "nvl_window"
        text prompt xalign 0.5 yalign 0.4
        input id "input" xalign 0.5 yalign 0.5

    use quick_menu

label start:

    centered "Greetings, Officer."
    $ playerName = renpy.call_screen("name_input", prompt="Could you please tell me your name?")
    centered "Great, Officer [playerName]"
    centered "Today is October 29th, 1995."
    centered "Well, as you may know, you were called to assist our police department on a case."
    centered "For starters, welcome to Moonland."
    centered "Our procedure is divided in three steps."
    centered "First, we'll take a look at the crime scene, search for items and other clues we may find along the way."
    centered "The second step is the interrogation, where we'll talk to some people that may know something about what we're trying to find out."
    centered "It's fair to remember that the city govenment does not like us to be violent, so if someone doesn't cooperate, unless they're a suspect, we unfortunately have nothing to do."
    centered "Keep that in mind when asking the questions."
    centered "Some people may not have the best tolerance."
    centered "Some of them will make it easy for you to understand how they're feeling just by looking at their face."
    centered "Although, some people may be a little harder to read."
    centered "To finish the procedure, we have the third and last step, the report."
    centered "That's the step where we'll reunite all our clues, analyze it deeply, and try to come to a conclusion."
    centered "However, for now, you will be designated only for the second step, the interrogations."
    centered "Our local officers will search the crime scene and Sheriff Hadwin Salice will assist you on the report step, so you don't have to worry about it."
    centered "Thanks for your help, Officer [playerName]."
