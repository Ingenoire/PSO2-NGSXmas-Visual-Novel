label char_goddess:
    return

init 1 python:
    g = Person(Character(
        "Megami",                                           # The Character's name, shown on screen.
        kind=defaultCharacter,                              # ----- Ignore -----
        image="goddess",                                     # This character's images should all start with the word defined here, the prefix.
        window_background="gui/textbox_green.png",            # The image for this character's Chat Background
        namebox_background="gui/namebox_green.png",               # The image for this character's Nameplate Background
        callback=mid_beep),                                # The voice tones when this character speaks: high_beep, mid_beep or low_beep
        "Megami",                                           # Due to coding shenanigans, you must add the Character's name, shown on screen, again.
        "goddess",                                           # Due to coding shenanigans, you must add this character's images prefix here, again.
        [                                                   # TAGS === Each one defines how and where this character can appear in game.
            "tutorial_guest"                                    # tutorial_guest: Shows up during the tutorial as a guest.
        ])                                           # Due to coding shenanigans, you must add this character's images prefix here, again.
    actors.append(g)

# Alternoire shows up as a tutorial guest.
label .tutorial_guest:

    camera:
        perspective True
        xpos 0.25
        zpos -500
        ypos 200

    pause 1
    show goddess idle at trueright_f:
        zpos 0
        ease 1 zpos 100
    with dissolve
    pause 1

    camera:
        perspective True
        ease 2 ypos -150

    pause 1

    g.c "Bow to me and kneel."
    camera:
        perspective True
        ease 0.175 xpos 0 ypos 0 zpos 0

    y.c c smug "Look who it i- wait, are you supposed to be a goddess?"

    g.c "Yes, now leave, worm."
    
    show yvonne c sidepoint
    $ emote("yvonne","sweat")
    pause 0.3

    y.c "Ah-haha ha haaa..."
    g.c "You do not amuse me, goodbye."

    show goddess at exit_right_f
    pause 1

    show yvonne at to_center
    pause 0.5

    return