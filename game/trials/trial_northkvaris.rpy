label trial_northkvaris:
    return

init 2 python:
    ref_trials.append("trial_northkvaris")

label .begin_trial:
    camera:
        perspective True
        ease 0.01 zpos 0.0 xpos 0.0 ypos 0.0
    
    scene bg kanai field at zbg
    with fade

    "This is the North Kvaris trial."

    "Legends have it that a glorious treasure hides itself in the depths of North Kvaris, but no one has returned."
    "Explore North Kvaris without falling to the bottom and find the treasure. Nobody will help. There are no threats. You are all alone."

    jump chooseNextAdventure