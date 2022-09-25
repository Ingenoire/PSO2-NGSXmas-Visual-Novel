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
    show alternoire unease at trueright_f
    with dissolve

    a.c "Oh? Uhh, hello!"
    return