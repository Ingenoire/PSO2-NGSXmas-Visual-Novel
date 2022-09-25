label char_alternoire:
    return

init 1 python:
    a = Person(Character(
        "Alternoire",                                           # The Character's name, shown on screen.
        kind=defaultCharacter,                              # ----- Ignore -----
        image="alternoire",                                     # This character's images should all start with the word defined here, the prefix.
        window_background="gui/textbox_blue.png",            # The image for this character's Chat Background
        namebox_background="gui/namebox_blue.png",               # The image for this character's Nameplate Background
        callback=high_beep),                                # The voice tones when this character speaks: high_beep, mid_beep or low_beep
        "Alternoire",                                           # Due to coding shenanigans, you must add the Character's name, shown on screen, again.
        "alternoire",                                           # Due to coding shenanigans, you must add this character's images prefix here, again.
        [                                                   # TAGS === Each one defines how and where this character can appear in game.
            "tutorial_guest"                                    # tutorial_guest: Shows up during the tutorial as a guest.
        ])                                           # Due to coding shenanigans, you must add this character's images prefix here, again.
    actors.append(a)

# Alternoire shows up as a tutorial guest.
label .tutorial_guest:

    camera:
        perspective True
        xpos 0.25
        zpos -500
        ypos 200

    pause 1
    show alternoire unease at trueright_f:
        zpos 0
        ease 1 zpos 100
    with dissolve
    pause 1

    camera:
        perspective True
        ease 2 ypos -150

    pause 1

    a.c "Oh? Uhh, hello!"
    camera:
        perspective True
        ease 0.175 xpos 0 ypos 0 zpos 0

    y.c c smug "Look who it is! Alternoire!"

    a.c idle "Oh... uhh..."
    a.c "Aren't there better tutorial guests than me?"
    
    show yvonne c shock
    $ emote("yvonne","sweat")
    pause 0.3

    y.c "O-of course not! You'll always be my favorite guest!"
    a.c unhappy "I'm not really sure what I can say..."
    y.c c talk "Then it's a good thing that this is merely the tutorial segment, so it isn't really an interview!"
    y.c "You may go now."
    a.c "Right, take care Yvonne."

    show alternoire unease at exit_right_f
    pause 1

    show yvonne at to_center
    pause 0.5

    return