label trial_helpnewbie:
    return

init 2 python:
    ref_trials.append("trial_helpnewbie")

label .begin_trial:
    $ noob = getCharacter(["newbie_noob"])
    $ pro = getCharacter(["newbie_pro"])

    camera:
        perspective True
        ease 0.01 zpos 0.0 xpos 0.0 ypos 0.0
    
    scene bg kanai field at zbg
    with fade

    $ renpy.show(noob.img + " noob shy", [trueleft])
    $ renpy.show(pro.img + " pro idle", [trueright])


    "This is the Help Newbie trial."

    "A beginner requests your help in central to gather some experience."
    "However, you have been told to do a task with a friend. Doing the friends' task is easy and easily gets you the adventure point."
    "Doing the beginner's task gets you no points, is much more tedious and lengthier, and the beginner leaves without giving a thanks. The beginner never logged in again."

    jump chooseNextAdventure