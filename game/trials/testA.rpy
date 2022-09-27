label trial_testA:
    return

init 2 python:
    ref_trials.append("trial_testA")

label .begin_trial:
    camera:
        perspective True
        ease 0.01 zpos 0.0 xpos 0.0 ypos 0.0
    
    scene bg kanai field at zbg
    with fade

    "This is test trial A."

    "Nice!"

    jump chooseNextAdventure