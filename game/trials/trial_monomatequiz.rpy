label trial_monomatequiz:
    return

init 2 python:
    ref_trials.append("trial_monomatequiz")

label .begin_trial:
    camera:
        perspective True
        ease 0.01 zpos 0.0 xpos 0.0 ypos 0.0
    
    scene bg kanai field at zbg
    with fade

    "This is the Monomate Quiz trial."

    "A dangerous quiz focusing on the Motomate drink brands thoughout the milleniums. Can you survive?"

    jump chooseNextAdventure