label trial_foodshop:
    return

init 2 python:
    ref_trials.append("trial_foodshop")

label .begin_trial:

    $ food = getCharacter(["foodshop"])

    camera:
        perspective True
        ease 0.01 zpos 0.0 xpos 0.0 ypos 0.0
    
    scene bg kanai field at zbg
    with fade

    $ renpy.show(food.img + " food patient", [truecenter])

    food.c "This is the food shop trial"

    food.c "You help out the food shop counter... to not be bored. The activities you do are typical bored person at work kind of things!"

    jump chooseNextAdventure