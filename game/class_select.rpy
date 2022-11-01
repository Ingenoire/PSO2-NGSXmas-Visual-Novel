label class_select:
    
    camera:
        perspective True
        zpos 0 xpos 0 ypos 0

    scene bg classcounter at zbg
    with fade

    "Welcome to the Class Counter: please select a {b}Main Class{/b} and a {b}Sub Class{/b} for this run."
    "These will determine your options against Dark Falz, but the Main Class will open slightly more options."

    $ proceed = False
    while proceed == False:
        call classmenu

        "You are a {image=[main_class].png}{image=[sub_class].png} [main_class]/[sub_class]. Is this correct?"

        menu:
            "Yes":
                $ proceed = True
            "No":
                "Let's try that again."
    

    "Well then, it's time to head out."

    jump darkfalz_start

label classmenu:
    menu:
        "{b}Main Class?{/b}"

        "{image=hunter.png} HUNTER":
            $ main_class = "Hunter"
            
        "{image=fighter.png} FIGHTER":
            $ main_class = "Fighter"
            
        "{image=ranger.png} RANGER":
            $ main_class = "Ranger"
            
        "{image=gunner.png} GUNNER":
            $ main_class = "Gunner"
            
        "{image=force.png} FORCE":
            $ main_class = "Force"
            
        "{image=techter.png} TECHTER":
            $ main_class = "Techter"
            
        "{image=braver.png} BRAVER":
            $ main_class = "Braver"
            
        "{image=bouncer.png} BOUNCER":
            $ main_class = "Bouncer"
            
        "{image=waker.png} WAKER":
            $ main_class = "Waker"

    "Your main class is {image=[main_class].png} [main_class]."

    menu:
        "{b}Sub Class?{/b}"

        "{image=hunter.png} HUNTER" if (main_class != "Hunter"):
            $ sub_class = "Hunter"
            
        "{image=fighter.png} FIGHTER" if (main_class != "Fighter"):
            $ sub_class = "Fighter"
            
        "{image=ranger.png} RANGER" if (main_class != "Ranger"):
            $ sub_class = "Ranger"
            
        "{image=gunner.png} GUNNER" if (main_class != "Gunner"):
            $ sub_class = "Gunner"
            
        "{image=force.png} FORCE" if (main_class != "Force"):
            $ sub_class = "Force"
            
        "{image=techter.png} TECHTER" if (main_class != "Techter"):
            $ sub_class = "Techter"
            
        "{image=braver.png} BRAVER" if (main_class != "Braver"):
            $ sub_class = "Braver"
            
        "{image=bouncer.png} BOUNCER" if (main_class != "Bouncer"):
            $ sub_class = "Bouncer"
            
        "{image=waker.png} WAKER" if (main_class != "Waker"):
            $ sub_class = "Waker"

    return
    