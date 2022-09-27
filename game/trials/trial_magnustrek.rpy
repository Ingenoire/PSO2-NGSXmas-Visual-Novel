label trial_magnustrek:
    return

init 2 python:
    ref_trials.append("trial_magnustrek")

label .begin_trial:
    camera:
        perspective True
        ease 0.01 zpos 0.0 xpos 0.0 ypos 0.0
    
    scene bg kanai field at zbg
    with fade

    "This is the Magnus Trek trial."

    "A simple trek along Mt Magnus: get to the top."
    "It could be a simple climb, or you might be ambushed by Dark Falz Thirst, and you'll need to escape in that case."

    jump chooseNextAdventure