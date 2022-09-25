

## This is a character file!
#### Read this carefully so that your character can work properly!

label char_yvonne:
    
    label .charsetup:
        $ y = Person(Character(
            "Yvonne",                                           # The Character's name, shown on screen.
            kind=defaultCharacter,                              # ----- Ignore -----
            image="yvonne",                                     # This character's images should all start with the word defined here, the prefix.
            window_background="gui/textbox_red.png",            # The image for this character's Chat Background
            namebox_background="gui/namebox.png",               # The image for this character's Nameplate Background
            callback=high_beep),                                # The voice tones when this character speaks: high_beep, mid_beep or low_beep
            "Yvonne",                                           # Due to coding shenanigans, you must add the Character's name, shown on screen, again.
            "yvonne")                                           # Due to coding shenanigans, you must add this character's images prefix here, again.
        
        return
    
    label .namejudge:
        if p_name == "Boobs":
            y.c c smug "Oh dear. Are you sure you wanna play the game with a silly name like that?"
        else:
            return
        
        menu:
            "Yes, stop name shaming!":
                y.c c wink "Ok, fine. I never got the appeal but you do you."
            
            "Actually no...":
                show yvonne c shock at bounce
                $ emote("yvonne","confused")
                y.c "T-then why did you pick it?"

                $ p_name = "Sandbag"
                y.c "I fixed it, so enjoy your new name, [p_name]!"

        return

    label .decideclass(forMain=False):
        show yvonne c shock
        $ emote("yvonne","notice")

        y.c "Oh, uhh, sure."
        show yvonne c thinking
        pause 0.2
        y.c "Hmm...{w=1.0}{nw}"

        $ selectableClasses = classes.copy()
        if (forMain==False): 
            $ selectableClasses.remove(main_class)

        if forMain:
            $ main_class = renpy.random.choice(classes)
            y.c c closeup "Well then, your main class is going to be... a {image=[main_class].png} [main_class]!"
        else:
            $ sub_class = renpy.random.choice(classes)
            y.c c closeup "Well then, your sub class is going to be... a {image=[sub_class].png} [sub_class]!"


        return

    label .mainhired:
        show yvonne icecream
        with dissolve

        y.c "I really appreciate you coming for me."
        return