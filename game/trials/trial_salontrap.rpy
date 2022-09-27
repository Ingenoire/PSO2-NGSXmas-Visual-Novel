label trial_salontrap:
    return

init 2 python:
    ref_trials.append("trial_salontrap")

label .begin_trial:
    camera:
        perspective True
        ease 0.01 zpos 0.0 xpos 0.0 ypos 0.0
    
    scene bg kanai field at zbg
    with fade

    "This is the Salon Trap trial."

    "A friend of yours gets… stuck in the Salon Machine. They're barely dressed. People from a Urgent Quest are about to return, you need to quickly find a way to free them!"
    "Their popularity determines how many people can see them in this state before a scandal breaks (difficulty)."

    jump chooseNextAdventure