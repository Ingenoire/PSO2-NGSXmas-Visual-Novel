# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# The game starts here.

label day1:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    "You are in a hallway."

    "You see a door and open it."

    jump room

    

label room:
    camera:
        perspective True
        xpos 0 zpos -600
        linear 2 xpos 200

    scene bg cg01
    with fade

    pause 2

    yn "Huh? Who are you?"

    camera:
        perspective True
        xpos 0
        linear 1 zpos 0

    pause 2

    yn "Oh, hello."

    jump gatearea

label gatearea:

    camera:
        perspective True
        zpos 0 xpos 0 ypos 0

    scene bg gateway at zbg
    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show yvonne idle at trueleft
    with dissolve

    # These display lines of dialogue.

    yn "No! I changed the script!"

    show yvonne unease at trueleft

    yn "Once you add a story, pictures, and music, you can release it to the world!"

    $ emote("yvonne","exclamation")

    yn idle "Hello world!"

    camera:
        perspective True
        xpos 0
        linear 0.5 xpos 50
        
    pause 0.5

    show alternoire idle at trueright
    with dissolve

    

    a "Oh, hello Yvonne!"

    a worried "For a second I thought placing the left and right was going to be impossible!"

    a unease "But hey, all's well that ends well. {image=poggers.png}"

    show yvonne shock

    pause 0.5

    a worried "So uh, what brings you here? "

    extend "You had me concerned..."

    # This ends the game.

    menu:

        "I'm going to record a video!":
            jump video

        "Nothing in particular...":
            jump nothing


label nothing:

    yn fedup "Hmmm... I'm not sure."

    a "Oh, come on! You can spill the beans..."

    jump video


label video:

    yn worried "I'm actually in the middle of filming a video."

    yn "Maybe it's best I get into outfit."

    window hide

    show yvonne:
        xcenter 0.25
        ease 1 xcenter 0.10 zpos 300
    pause 0.5
    hide yvonne with dissolve

    camera:
        perspective True
        xpos -500
        zpos -500
        ypos 200

    pause 1

    show cyvonne proud at trueleft
    with dissolve

    pause 1

    camera:
        perspective True
        ease 2 ypos -150

    pause 1

    yc smug "Well?"

    show alternoire cam

    camera:
        perspective True
        ease 0.4 xpos 200 zpos -300 ypos 100

    pause 1

    a "Huh! That's a surprisingly tame outfit, coming from you."

    camera:
        perspective True
        ease 0.4 xpos -200 zpos 0 ypos 0

    pause 1

    yc boast "Aha, thanks..."
    pause 1

    camera:
        perspective True
        ease 0.2 xpos -500 zpos -600 ypos -200

    yc sad "Hey! What does that mean? "
    extend "I'm... supposed to be wholesome for all ages!"

    a "Right..."

    camera:
        perspective True
        xpos 0 zpos 0 ypos 0

    scene bg gateway:
        ycenter 0.5 xcenter 0.7 zoom 1.5
        ease .8 zoom 2.0 ycenter 0.5
    show cyvonne proud:
        ycenter 0.5 xcenter 0.6 zoom 1.5
        ease .8 zoom 2.0 ycenter 0.5

    image arrow = "arrow.png"
    show arrow:
        ycenter 0.4 xcenter 0.3

    a "I mean, your outfit is clipping, silly!"
    
    show arrow:
        ease 0.4 ycenter 0.5 xcenter 0.25

    yc shoulderhide "Hey! What does that mean?"

    scene bg gateway
    show cyvonne shoulderhide at trueleft
    show alternoire idle at trueright

    yc glanceoff "Why don't you ask {b}SEGA{/b} why this outfit has begun clipping, huh?"

    a passive "Anyway, I've got some errands to run."

    yc ponder "E-errands? You have a life outside of PSO2?"

    camera:
        perspective True
        ease 0.4 xpos 300 zpos -200 ypos -100

    pause 0.5

    a closedeyes "Uh, yes."

    a "Work is getting quite hectic, and I have to also prepare my future gamedev project on my own."

    a present "You kept posting on twitter about doing a ngsmas, so go ahead and commit to that idea!"

    camera:
        perspective True
        ease 0.5 xpos -300 zpos -400 ypos -100

    pause 0.5

    yc fedup "Okay fine, I'll do something myself."
    
    yc unpleased "Just, one question before you leave."

    camera:
        perspective True
        ease 0.4 xpos 300 zpos -300 ypos -100

    pause 0.5

    a heart "What?"

    return