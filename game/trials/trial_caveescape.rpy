label trial_caveescape:
    return

init 2 python:
    ref_trials.append("trial_caveescape")

label .begin_trial:
    camera:
        perspective True
        ease 0.01 zpos 0.0 xpos 0.0 ypos 0.0
    
    scene bg kanai beach at zbg
    with fade

    "This is the South Aelio Cave Escape."

    "After venturing into the cave with a ally, fight your way out!"

    jump chooseNextAdventure