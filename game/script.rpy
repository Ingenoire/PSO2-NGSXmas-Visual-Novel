# The script of the game goes in this file.

define low_beeps = ['audio/low_beep.ogg']
define mid_beeps = ['audio/mid_beep.ogg']
define hi_beeps = ['audio/high_beepA.ogg', 'audio/high_beepB.ogg', 'audio/high_beepC.ogg']


# Declare characters used by this game. The color argument colorizes the
# name of the character.

init python:
    def high_beep(event, **kwargs):
        if event == "show":
            renpy.sound.play(hi_beeps[1])
            renpy.sound.play(hi_beeps[2])
            renpy.sound.queue(renpy.random.choice(hi_beeps))
            renpy.sound.queue(renpy.random.choice(hi_beeps))
            renpy.sound.queue(renpy.random.choice(hi_beeps))
            renpy.sound.queue(renpy.random.choice(hi_beeps))
            renpy.sound.queue(renpy.random.choice(hi_beeps))
            renpy.sound.queue(renpy.random.choice(hi_beeps))
            renpy.sound.queue(renpy.random.choice(hi_beeps))
            renpy.sound.queue(renpy.random.choice(hi_beeps))
            renpy.sound.queue(renpy.random.choice(hi_beeps))
            renpy.sound.queue(renpy.random.choice(hi_beeps))
            renpy.sound.queue(renpy.random.choice(hi_beeps))
            renpy.sound.queue(renpy.random.choice(hi_beeps))
            renpy.sound.queue(renpy.random.choice(hi_beeps))
            renpy.sound.queue(renpy.random.choice(hi_beeps))
            renpy.sound.queue(renpy.random.choice(hi_beeps))
            renpy.sound.queue(renpy.random.choice(hi_beeps))
            renpy.sound.queue(renpy.random.choice(hi_beeps))
            renpy.sound.queue(renpy.random.choice(hi_beeps))
            renpy.sound.queue(renpy.random.choice(hi_beeps))
            renpy.sound.queue(renpy.random.choice(hi_beeps))
            renpy.sound.queue(renpy.random.choice(hi_beeps))
            renpy.sound.queue(renpy.random.choice(hi_beeps))
            renpy.sound.queue(renpy.random.choice(hi_beeps))
            renpy.sound.queue(renpy.random.choice(hi_beeps))
            renpy.sound.queue(renpy.random.choice(hi_beeps))
            renpy.sound.queue(renpy.random.choice(hi_beeps))
            renpy.sound.queue(renpy.random.choice(hi_beeps))

        elif event == "slow_done" or event == "end":
            renpy.sound.stop()

    def mid_beep(event, **kwargs):
        if event == "show":
            renpy.sound.play("audio/mid_beep.ogg")
        elif event == "slow_done" or event == "end":
            renpy.sound.stop()
    
    def low_beep(event, **kwargs):
        if event == "show":
            renpy.sound.play("audio/low_beep.ogg")
        elif event == "slow_done" or event == "end":
            renpy.sound.stop()

    def emote(name, emotion): # Name is the character sprite, emotion is the emote sprite.
        x = int(renpy.get_image_bounds(name)[0] + renpy.get_image_bounds(name)[2] / 2) + 150
        y = 150
        # Displays the emote sprite.
        trnf = None
        if emotion == "exclamation": 
            trnf = exclamation
        elif emotion == "confused": 
            renpy.sound.play("audio/confused.ogg")
            trnf = confused
        elif emotion == "question": 
            trnf = question
            renpy.sound.play("audio/question.ogg")
        elif emotion == "notice": 
            trnf = notice
            renpy.sound.play("audio/notice.ogg")
        
        renpy.show(emotion, at_list=[Transform(pos=(x, y)), trnf])



## The borders of the box containing the character's name, in left, top, right,
## bottom order.

define gui.name_text_outlines = [ (3, "#00000080", 0, 0) ]

transform exclamation:
    alignaround (.5, .5)
    alpha 0
    ease 0.1 alpha 1 yoffset -30 zoom 1.5
    easeout .175 yoffset 0 zoom 1
    ease 0.15 zoom 1.25
    easeout .15 yoffset 0 zoom 1
    pause 0.3
    ease 0.1 alpha 0

transform confused:
    alignaround (.5, .5)
    alpha 0
    ease 0.15 alpha 1 zoom 1.25
    easeout .15 yoffset 0 zoom 1
    pause 0.3
    ease 0.1 alpha 0

transform question:
    alignaround (.5, .5)
    alpha 0
    yoffset 20
    ease .175 alpha 1 yoffset -20
    easeout .05 yoffset 0
    pause 1
    ease 0.1 alpha 0

transform notice:
    alignaround (.5, .5)
    alpha 0
    ease .05 alpha 1
    easeout .05 alpha 0.2
    ease .05 alpha 1
    pause 1
    ease 0.1 alpha 0

transform trueleft:
    xcenter 0.25
    ypos 20
    zpos 100
    yoffset 30

transform trueright:
    xcenter 0.75
    ypos 20
    zpos 100
    yoffset 30

transform truecenter:
    xcenter 0.5
    ypos 20
    zpos 100
    yoffset 30

transform zoomin:
    ycenter 0.5 xcenter 0.5
    ease .8 zoom 2.0 ycenter 0.5

transform zbg:
    zpos -1000 zzoom True
    ypos -200

transform bounce:
    yoffset 30
    easein .175 yoffset 0
    easeout .175 yoffset 30
    easein .175 yoffset 10
    easeout .175 yoffset 30
    yoffset 30

# Adventure Points
# Obtained or lost as a result of each trial.
define points = 0

# Player name, can be changed at the start of a new playthrough.
define p_name = "Viewer"

# Main and Sub Class of the player
# This defines the possible options you can take in certain trials
define main_class = "hunter"
define sub_class = "force"

label start:
    call characterSetup from _call_characterSetup
    call intro from _call_intro
    return
    