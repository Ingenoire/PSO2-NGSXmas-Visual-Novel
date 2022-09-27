label trial_truckride:
    return

init 2 python:
    ref_trials.append("trial_truckride")

label .begin_trial:
    camera:
        perspective True
        ease 0.01 zpos 0.0 xpos 0.0 ypos 0.0
    
    scene bg kanai beach at zbg
    with fade

    "This is the Truck Ride trial."

    "You're being driven to several points inside a truck by a nice fellow."
    "Sometimes you need to defend the truck, but you need to maintain the truck: either your colleague is a better fit or you are, and you need to decide."

    jump chooseNextAdventure