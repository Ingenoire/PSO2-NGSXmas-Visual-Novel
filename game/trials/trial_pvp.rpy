label trial_pvp:
    return

init 2 python:
    ref_trials.append("trial_pvp")

label .begin_trial:
    camera:
        perspective True
        ease 0.01 zpos 0.0 xpos 0.0 ypos 0.0
    
    scene bg kanai field at zbg
    with fade

    "This is the PVP Trial"

    "Collect a randomly chosen weapon, and defeat enemies within the limited amount of actions!"

    jump chooseNextAdventure