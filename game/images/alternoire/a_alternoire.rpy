

## This is a character file!
#### Read this carefully so that your character can work properly!

label char_alternoire:
    
    label .charsetup:
        $ a = Person(Character(
            "Alternoire",                                           # The Character's name, shown on screen.
            kind=defaultCharacter,                              # ----- Ignore -----
            image="alternoire",                                     # This character's images should all start with the word defined here, the prefix.
            window_background="gui/textbox_blue.png",            # The image for this character's Chat Background
            namebox_background="gui/namebox_blue.png",               # The image for this character's Nameplate Background
            callback=high_beep),                                # The voice tones when this character speaks: high_beep, mid_beep or low_beep
            "Alternoire",                                           # Due to coding shenanigans, you must add the Character's name, shown on screen, again.
            "alternoire")                                           # Due to coding shenanigans, you must add this character's images prefix here, again.
        
        return
    
    label .mainhired:
        show alternoire icecream
        with dissolve

        a.c "Oh? Uhh, thank you!"