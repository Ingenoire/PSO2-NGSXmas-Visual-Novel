label trial_caveescape:
    return

init 2 python:
    ref_trials.append("trial_caveescape")

label .begin_trial:
    $ caver = getCharacter(["cave_trekker"])

    camera:
        perspective True
        ease 0.01 zpos 0.0 xpos 0.0 ypos 0.0
    
    scene bg kanai field at zbg
    with fade

    $ renpy.show(caver.img + " trekker idle", [truecenter])

    "This is the South Aelio Cave Escape."

    "After venturing into the cave with a ally, fight your way out!"

    jump chooseNextAdventure