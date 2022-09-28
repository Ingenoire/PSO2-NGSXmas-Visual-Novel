label trial_tokyorelax:
    return

init 2 python:
    ref_trials.append("trial_tokyorelax")

label .begin_trial:
    camera:
        perspective True
        ease 0.01 zpos 0.0 xpos 0.0 ypos 0.0
    
    scene bg kanai field at zbg
    with fade

    "This is the Tokyo Relax trial."

    "Shopping in Tokyo/Las Vegas, you end up going to a cafe with someone you meet."
    "The goal is to simply have a good conversation with them."

    jump chooseNextAdventure