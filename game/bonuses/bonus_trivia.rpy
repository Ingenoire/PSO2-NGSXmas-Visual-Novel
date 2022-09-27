label bonus_trivia:
    return

init 2 python:
    ref_bonuses.append("bonus_trivia")

label .begin_trial:
    camera:
        perspective True
        ease 0.01 zpos 0.0 xpos 0.0 ypos 0.0
    
    scene bg christmas at zbg
    with fade

    "This is an trivia segment!"
    "Did you know people live and die? Silly humans!"

    jump chooseNextAdventure