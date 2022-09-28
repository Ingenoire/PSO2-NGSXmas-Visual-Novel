label trial_retemvoid:
    return

init 2 python:
    ref_trials.append("trial_retemvoid")

label .begin_trial:
    camera:
        perspective True
        ease 0.01 zpos 0.0 xpos 0.0 ypos 0.0
    
    scene bg kanai field at zbg
    with fade

    "This is the Retem Void trial."

    "Lost in a dream, escape to the surface. If you aren't a Hunter, you might be unable to go far."

    jump chooseNextAdventure