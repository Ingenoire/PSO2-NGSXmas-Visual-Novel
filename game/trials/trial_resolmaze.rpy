label trial_resolmaze:
    return

init 2 python:
    ref_trials.append("trial_resolmaze")

label .begin_trial:
    $ resolt = getCharacter(["resol_treasure"])

    camera:
        perspective True
        ease 0.01 zpos 0.0 xpos 0.0 ypos 0.0
    
    scene bg kanai field at zbg
    with fade

    $ renpy.show(resolt.img + " resolt worry", [truecenter])

    "This is the resol maze trial."

    "You lose yourself in Resol Forest enhanced by illusions. Get out of Resol. Along the way, you can rescue a lost soul."

    jump chooseNextAdventure