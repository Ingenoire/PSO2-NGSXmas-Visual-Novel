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
            "host",         # host: Hosts the show, Yvonne/Alternoire only.
            "foodshop",      # foodshop: Attendant in the foodshop trial.
            "newbie_noob",      # newbie_noob: The newbie in the Help Newbie trial
            "newbie_pro",      # newbie_pro: The pro in the Help Newbie trial
            "idol",      # idol: The idol the player helps in the Idol Trial
            "winning_idol",      # winning_idol: The idol the player helps in the Idol Trial
            "magnus_trekker",      # magnus_trekker: A friend who helps you out in the Mt Magnus Trek trial
            "cave_trekker",      # cave_trekker: A friend who helps you out in the Cave Escape trial
            "monomate_host",      # monomate_host: The host of the violent Monomate Quiz trial
            "kvaris_bather",      # kvaris_bather: A beauty who's a part of the secret of the North Kvaris trial.
            "medic",      # medic: A doctor/nurse who's helping you assess PQs in the PQ Checker trial.
            "pq_owner",      # pq_owner: A unsuspecting owner of a Personal Quarters in the PQ Checker trial.
            "pvp",      # pvp: Shows up in the PvP trial as an enemy.
            "resol_treasure",      # resol_treasure: Someone lost in Resol Forest in the Resol Maze trial.
            "void_god",      # void_god: A god that you end up imagining in the Retem Void trial.
            "void_guide",      # void_guide: A cryptic being who helps you navigate the void of retem in the Retem Void trial
            "rigs_purple",      # rigs_purple: The person who's handling the repairs of the Purple Rig in the Rig Repair trial
            "rigs_green",      # rigs_green: The person who's handling the repairs of the Purple Rig in the Rig Repair trial
            "rigs_orange",      # rigs_orange: The person who's handling the repairs of the Purple Rig in the Rig Repair trial
            "salon_victim",      # salon_victim: Your friend who's stuck in an embarrasing way in the Salon Trap trial
            "salon_spectator",      # salon_spectator: A random dude who'll show up to laugh at the victim in the bad end of the Salon Trap trial.
            "shopkeep",      # shopkeep: The owner of a shop in the Shop Barter trial
            "streamer",      # streamer: The streamer/ytber of the Streamer Aid trial
            "tokyo_citizen",      # tokyo_citizen: A citizen in tokyo for the Tokyo relax trial
            "trucker",      # trucker: The one who drives the truck in the Truck Ride Trial
        ])
    actors.append(y)

label .visitor:
    show yvonne idle at truecenter
    y.c "Hello!"
    y.c "So you seem to want to face off against Dark Falz!"
    y.c "Good luck!"

    return

# Yvonne judges your name at the name entry screen.
label .namejudge:
    
    python:
        lewd_detected = False
        sad_human_detected = False
        # Naughty words
        lewdwords = ["boob", "ass", "butt", "tits", "shit", "fuck", "piss", "pussy", "cum", "titties", "vagina", "dick", "penis", "cunt", "bitch", "bastard"]
        for s in lewdwords:
            if s in p_name.lower(): lewd_detected = True

        if(("Xx" in p_name) and ("xX" in p_name)):
            sad_human_detected = True

        if "popona" in p_name.lower():
            renpy.call("char_yvonne.poponaname")

    if lewd_detected:
        call char_yvonne.lewdnameentry
    elif sad_human_detected:
        call char_yvonne.poornameentry

    return

# Yvonne reacts to your comments
# Cheat codes are parsed here!
label .commentjudge:
    
    y.c "I... see! That's good to hear!"

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
    $ p_name = p_name + "{image=wheeze.png}"
    return

# Its Popona pog
label .poponaname:
    show yvonne c shock at bounce
    $ emote("yvonne","confused")
    y.c "Po-po-Popona?!"
    y.c c wink "Hi! I'm a big fan!"
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