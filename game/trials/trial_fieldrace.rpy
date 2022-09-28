label trial_fieldrace:
    return

init 2 python:
    ref_trials.append("trial_fieldrace")

label .begin_trial:
    camera:
        perspective True
        ease 0.01 zpos 0.0 xpos 0.0 ypos 0.0
    
    scene bg kanai field at zbg
    with fade

    "This is the Field Race trial."

    "On hoverboards, race to the finish!"

    jump chooseNextAdventure