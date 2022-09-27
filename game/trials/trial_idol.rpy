label trial_idol:
    return

init 2 python:
    ref_trials.append("trial_idol")

label .begin_trial:
    camera:
        perspective True
        ease 0.01 zpos 0.0 xpos 0.0 ypos 0.0
    
    scene bg kanai field at zbg
    with fade

    "This is the Idol Sim trial."

    "A beginner idol is preparing to enter the fray. You must help them improve so that they can eventually take to the stage! Her performance will determine your points."

    jump chooseNextAdventure