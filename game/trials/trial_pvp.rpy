label trial_pvp:
    return

init 2 python:
    ref_trials.append("trial_pvp")

label .begin_trial:
    $ pvp_1 = getCharacter(["pvp"])

    camera:
        perspective True
        ease 0.01 zpos 0.0 xpos 0.0 ypos 0.0
    
    scene bg kanai field at zbg
    with fade

    $ renpy.show(pvp_1.img + " pvp start", [truecenter])

    "This is the PVP Trial"

    "React at the right time with the right key to defeat enemies before they can strike."

    jump chooseNextAdventure