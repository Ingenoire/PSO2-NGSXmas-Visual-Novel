label char_yvonne:
    return

init 1 python:
    y = Person(Character(
        "Yvonne",                                           # The Character's name, shown on screen.
        kind=defaultCharacter,                              # ----- Ignore -----
        image="yvonne",                                     # This character's images should all start with the word defined here, the prefix.
        window_background="gui/textbox_red.png",            # The image for this character's Chat Background
        namebox_background="gui/namebox.png",               # The image for this character's Nameplate Background
        callback=high_beep),                                # The voice tones when this character speaks: high_beep, mid_beep or low_beep
        "Yvonne",                                           # Due to coding shenanigans, you must add the Character's name, shown on screen, again.
        "yvonne",                                           # Due to coding shenanigans, you must add this character's images prefix here, again.
        [                                                   # TAGS === Each one defines how and where this character can appear in game.
            "host"                                             # host: Hosts the show, Yvonne only.
        ])
    actors.append(y)

# Yvonne judges your name at the name entry screen.
label .namejudge:
    
    python:
        lewd_detected = False
        sad_human_detected = False
        # Naughty words
        lewdwords = ["boobs", "ass", "butt", "tits", "shit", "fuck", "piss", "pussy", "cum", "titties", "vagina", "dick", "penis", "cunt", "bitch", "bastard"]
        for s in lewdwords:
            if s in p_name.lower(): lewd_detected = True

        if(("Xx" in p_name) and ("xX" in p_name)):
            sad_human_detected = True

    if lewd_detected:
        call char_yvonne.lewdnameentry
    elif sad_human_detected:
        call char_yvonne.poornameentry

    return

# Yvonne laughs at your... name.
# Some names just aren't cool lmao.
label .poornameentry:
    y.c c giveup "Oh-{w=0.5}{nw}"
    y.c c smug "AHAHAHAHAHAHAHAAHAHAHAHHAAHAHAHAHAHAHA!!!"
    y.c "I'm sorry... \"[p_name]\"... AHAHAHAHAHAHAHAHAHAHAHA"
    y.c "Are you seriously... calling yourself that? Like, for real?"
    y.c "That's so mid 2000's edgy! Ahaha-haaaa..."
    y.c "Sorry about that. I'll try to remain professional."
    return

# Yvonne asks you to think twice about using such a name.
label .lewdnameentry:
    y.c c smug "Oh dear. Are you sure you wanna play the game with a silly name like that?"

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

# Yvonne decides your main or sub class for you.
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