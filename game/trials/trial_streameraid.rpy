label trial_streameraid:
    return

init 2 python:
    ref_trials.append("trial_streameraid")

label .begin_trial:
    $ streamer = getCharacter(["streamer"])

    camera:
        perspective True
        ease 0.01 zpos 0.0 xpos 0.0 ypos 0.0
    
    scene bg kanai field at zbg
    with fade

    $ renpy.show(streamer.img + " streamer idle", [truecenter])

    "This is the Streamer Aid trial."

    "Encountering a YT/Streamer who's trying to grow, you try lending them a hand in being part of their operations."
    "99% of the time, you will fail this trial."
    "The 1% of the time you succeed, you will be forgotten."

    jump chooseNextAdventure