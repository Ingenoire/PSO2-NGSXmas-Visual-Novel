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
        x = int(renpy.get_image_bounds(name)[0] + renpy.get_image_bounds(name)[2] / 2)
        y = int(renpy.get_image_bounds(name)[1] + 100)
        z = 100
        # Displays the emote sprite.
        renpy.show(emotion, at_list=[Transform(pos=(x, y)), exclamation])



## The borders of the box containing the character's name, in left, top, right,
## bottom order.

define gui.name_text_outlines = [ (3, "#00000080", 0, 0) ]

transform exclamation:
    alpha 0
    "exclamation.png"
    ease 0.5 alpha 1 ycenter -20

transform trueleft:
    xcenter 0.25
    ypos 20
    zpos 100

transform trueright:
    xcenter 0.75
    ypos 20
    zpos 100

transform zoomin:
    ycenter 0.5 xcenter 0.5
    ease .8 zoom 2.0 ycenter 0.5

transform zbg:
    zpos -1000 zzoom True
    ypos -200

transform bounce:
    ease 0.2 ypos 0.8
    pause 0.2
    ease 0.2 ypos 1
    pause 0.2

# The game starts here.

# Adventure Points
# Obtained or lost as a result of each trial.
define points = 0

label start:
    call characterSetup
    call intro
    return
    