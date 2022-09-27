label trial_shopbarter:
    return

init 2 python:
    ref_trials.append("trial_shopbarter")

label .begin_trial:
    camera:
        perspective True
        ease 0.01 zpos 0.0 xpos 0.0 ypos 0.0
    
    scene bg kanai field at zbg
    with fade

    "This is the shop barter trial"

    "A guest wants a new outfit, but the vendor is a scalper. Convince them to sell the item at a reasonable price for the guest!"

    jump chooseNextAdventure