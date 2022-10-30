label trial_rigrepairs:
    return

init 2 python:
    ref_trials.append("trial_rigrepairs")

label .begin_trial:
    $ orange = getCharacter(["rigs_orange"])
    $ purple = getCharacter(["rigs_purple"])
    $ green = getCharacter(["rigs_green"])

    camera:
        perspective True
        ease 0.01 zpos 0.0 xpos 0.0 ypos 0.0
    
    scene bg kanai field at zbg
    with fade

    $ renpy.show(purple.img + " rig idle", [trueleft])
    $ renpy.show(green.img + " rig idle", [truecenter])
    $ renpy.show(orange.img + " rig idle", [trueright])

    "This is the rig maintenance trial."

    "You are working alongside the Mining Rig Corps featuring 2 people to initialize the Mining Rig Orange, Purple or Green, which has some issues."
    "Very casual, no enemies. You’re told to do some tasks and that’s it!"

    jump chooseNextAdventure