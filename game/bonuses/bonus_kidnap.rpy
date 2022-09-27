label bonus_kidnap:
    return

init 2 python:
    ref_bonuses.append("bonus_kidnap")

label .begin_trial:
    camera:
        perspective True
        ease 0.01 zpos 0.0 xpos 0.0 ypos 0.0
    
    scene bg christmas at zbg
    with fade

    "This is a rare event which can occur, where Yvonne goes missing!"
    "It can only be added if it's the second bonus round."
    "This will override the next trial to always be Mt Magnus Hike, and the Dark Falz Thirst event will be guaranteed, with an extra segment to it should you succeed."
    "Succeeding that will lead to a unique ending."

    jump chooseNextAdventure