label trial_pqchecker:
    return

init 2 python:
    ref_trials.append("trial_pqchecker")

label .begin_trial:
    camera:
        perspective True
        ease 0.01 zpos 0.0 xpos 0.0 ypos 0.0
    
    scene bg kanai beach at zbg
    with fade

    "This is the PQ Checker trial."

    "With the help of a medical board, assess several PQs and determine the owner's health."

    jump chooseNextAdventure