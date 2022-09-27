label bonus_quiz:
    return

init 2 python:
    ref_bonuses.append("bonus_quiz")

label .begin_trial:
    camera:
        perspective True
        ease 0.01 zpos 0.0 xpos 0.0 ypos 0.0
    
    scene bg christmas at zbg
    with fade

    "This is a quiz segment!"
    "You can get some points and maybe even extra goodies!"

    jump chooseNextAdventure