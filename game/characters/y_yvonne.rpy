


## This is a character file!
#### Read this carefully so that your character can work properly!



label char_yvonne:
    
    label .charsetup:
        # Please read carefully!
        # /----------- Variable Name for your Character, change it to something simple but NOT IN USE BY OTHERS
        # |            Check the file list in characters. The word before the _ is the variable for easier reading of used vars.
        # V
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
    
    label .mainhired:
        show yvonne icecream
        with dissolve

        y.c "I really appreciate you coming for me."