label intro:
    camera:
        perspective True
        zpos 0 xpos 0 ypos 0
    
    scene bg christmas at zbg
    with fade

    show yvonne c mic at truecenter
    with dissolve

    y.c "Welcome everyone!"
    y.c "This time around, I decided to make pso2mas a gameshow!"

    show yvonne c shock at bounce
    
    $ emote("yvonne","notice")

    pause 1

    show yvonne c closeup

    camera:
        perspective True
        ease 0.175 zpos -200

    y.c c closeup "And who might you be, viewer?"

    python:
        p_name = renpy.input("What is your name?", length=13)
        p_name = p_name.strip()

        if p_name == "":
            p_name = "Viewer"

    call char_yvonne.namejudge

    camera:
        perspective True
        ease 0.175 zpos 0

    y.c c engage "Oh, [p_name]! That's a nice name."

    y.c c engage "So then, are you up for a round of the NGSXmas Game?"

    camera:
        perspective True
        ease 0.175 xpos 0.2

    show item classes at itemright

    y.c "Before we can begin, you're going to have to take a Main Class and a Sub Class."

    y.c c serious "You won't be able to change your classes during a run, however."

    hide item classes

    menu:
        y.c c sidepoint "What is your Main Class?"

        "{image=hunter.png} HUNTER":
            $ main_class = "hunter"
            y.c c smug "Oh! Nice, a Hunter! I'm a Hunter too!"
            $ ex_hunter = renpy.random.random()
            if(ex_hunter <= 0.1):
                y.c c thinking "Heh, you know, that reminds me..."
                y.c "The only reason I started as a Hunter was because of that Labrys weapon camo."
                y.c "There wasn't really an Axe weapon in PSO2, since that was what I was initially trying to go for."
                y.c c serious "Thankfully, Partisan in Classic PSO2 had very quick basic attacks."
                y.c "If I were to try using say, Sword, or worse... Katana...{w=0.5} I don't think I might have kept playing PSO2..."
                y.c c thinking "...{w=0.5}{nw}"

                show yvonne c shock at bounce
                $ emote("yvonne","exclamation")

                y.c "Oh, sorry!{w=0.1} Got a bit, nostalgic."
                y.c c closeup "Heh, uhh, let's continue!"
        "{image=fighter.png} FIGHTER":
            $ main_class = "fighter"
            y.c "A Fighter, huh? That's cool."
        "{image=ranger.png} RANGER":
            $ main_class = "ranger"
            y.c "Guess you're a ranger."
        "{image=gunner.png} GUNNER":
            $ main_class = "gunner"
            y.c "Pew pew! A Gunner, daring!"
        "{image=force.png} FORCE":
            $ main_class = "force"
            y.c "Guess you're a force."
        "{image=techter.png} TECHTER":
            $ main_class = "techter"
            y.c "Guess you're a techter."
        "{image=braver.png} BRAVER":
            $ main_class = "braver"
            y.c "Guess you're a braver."
        "{image=bouncer.png} BOUNCER":
            $ main_class = "bouncer"
            y.c "Guess you're a bouncer."
        "{image=waker.png} WAKER":
            $ main_class = "waker"
            y.c "Guess you're a waker."
        "Decide for me!":
            call char_yvonne.decideclass(True)

    show yvonne c sidepoint with dissolve

    menu:
        y.c "What is your Sub Class?"

        "{image=hunter.png} HUNTER" if (main_class != "hunter"):
            $ sub_class = "hunter"
            y.c "Guess you're a hunter."
        "{image=fighter.png} FIGHTER" if (main_class != "fighter"):
            $ sub_class = "fighter"
            y.c "Guess you're a fighter."
        "{image=ranger.png} RANGER" if (main_class != "ranger"):
            $ sub_class = "ranger"
            y.c "Guess you're a ranger."
        "{image=gunner.png} GUNNER" if (main_class != "gunner"):
            $ sub_class = "gunner"
            y.c "Guess you're a gunner."
        "{image=force.png} FORCE" if (main_class != "force"):
            $ sub_class = "force"
            y.c "Ooh! I'm a Force sub-class too!"
        "{image=techter.png} TECHTER" if (main_class != "techter"):
            $ sub_class = "techter"
            y.c "Guess you're a techter."
        "{image=braver.png} BRAVER" if (main_class != "braver"):
            $ sub_class = "braver"
            y.c "Guess you're a braver."
        "{image=bouncer.png} BOUNCER" if (main_class != "bouncer"):
            $ sub_class = "bouncer"
            y.c "Guess you're a bouncer."
        "{image=waker.png} WAKER" if (main_class != "waker"):
            $ sub_class = "waker"
            y.c "Guess you're a waker."
        "Decide for me!":
            call char_yvonne.decideclass(False)
    
    y.c "Your main class ({image=[main_class].png}) and your sub class ({image=[sub_class].png}) will determine the additional options you can perform during certain trials."

    menu:
        "Such as..."

        "So this is a class check?":
            y.c "Not exactly, but kind of."
            y.c "It is a gameshow where the trials are randomized every run."
            y.c "You're not expected to succeed all trials. Leave that meta mindset outside for just a bit, please..."
            $ ex_fe = renpy.random.random()
            if(ex_fe <= 0.2):
                y.c c thinking "..."
                y.c "Don't you dare make a meta guide for this fangame."
        "I don't understand.":
            y.c c talk "Well, I guess you'll figure things out as you play."
            y.c "It's honestly the best way to experience this."
        "{image=hunter.png} I understand." if (main_class == "hunter" or sub_class == "hunter"):
            y.c "Glad you understand! I can always rely on a Hunter like you!"
        "{image=fighter.png} Alright, gotcha, let's slay." if (main_class == "fighter" or sub_class == "fighter"):
            y.c "Yeah!! Show me some of that fire!"
        "{image=ranger.png} Glad to have you at my side." if (main_class == "ranger" or sub_class == "ranger"):
            y.c "Keep the forest safe-{w=0.3}{nw}"
            y.c "Uh, I mean, good work, Ranger!"
        "{image=gunner.png} Let's rock!" if (main_class == "gunner" or sub_class == "gunner"):
            y.c "I pray you can keep your style rank at SSS!"
        "{image=force.png} I pray for your safety." if (main_class == "force" or sub_class == "force"):
            y.c "Thank you very much, [p_name]! I hope you too stay safe!"
        "{image=techter.png} Sniff." if (main_class == "techter" or sub_class == "techter"):
            camera:
                perspective True
                ease 0.8 zpos -300 xpos 0.01
            y.c "So you're a Techt-{w=0.7}{nw}"
            $ emote("yvonne","exclamation")
            show yvonne c shock at bounce
            camera:
                perspective True
                ease 0.175 zpos -0 xpos 0.2
            y.c "Hey! No sniffing!"
            y.c "What are you trying to do by sniffin-{w=0.6}{nw}"
            y.c c thinking "Oh, that was meant to roleplay a weakling."
        "{image=braver.png} Nani?" if (main_class == "braver" or sub_class == "braver"):
            y.c "...another braver, great...{w=0.3}{nw}"
            y.c "Hey, that's no problem!"
        "{image=bouncer.png} Miss, this way." if (main_class == "bouncer" or sub_class == "bouncer"):
            y.c "H-hey, you're not a bouncer at a bar!"
        "{image=waker.png} Keep talking..." if (main_class == "waker" or sub_class == "waker"):
            y.c "Guess you're a waker."

    y.c c thinking "Anyway..."
    camera:
        perspective True
        ease 0.175 zpos 0.0 xpos 0.0 ypos 0.0
    show yvonne c wink at bounce

    y.c "The game has a score system."
    y.c "Clearing trials will net you points, while failing them will deduct points."
    y.c "As a gameshow, we'll reward you with nice prizes based on how well you perform!"
    
    y.c "Since it's also a gameshow, trials aren't the only thing that are going to happen."
    y.c "You'll get to see some interviews, trivia, and even some other strange events, based on our ratings."
    y.c "Creating this gameshow was only possible thanks to many PSO2 players from all around the world, and they'll be taking on acting roles during certain trials!"

    show yvonne c mic at to_left

    y.c "For example..."

    # Tutorial Guest Call
    $ tut_guest = None
    $ tut_guest = getCharacter(["tutorial_guest"])

    $ renpy.call("char_" + tut_guest.img + ".tutorial_guest")

    y.c "And that was our guest!"

    y.c "Well then, I think we should begin the game show!"
    show yvonne at exit_right
    camera:
        perspective True
        ease 0.5 xpos 0.0 ypos 0.0 zpos 0.0
    pause 0.3

    jump intro_cg

    return

label intro_cg:
    scene cg yvonne 02 with fade

    y.c "Beyond this doorway is your own personal journey!"
    y.c "I can't wait to see what you'll encounter, and I'll be seeing you at the other side!"

    scene cg yvonne 03 with dissolve

    "You venture into the tunnel..."
    camera:
        perspective True
        ease 3 zpos -1000 xpos 0.1 ypos 0.2

    pause 3
    "..."

    return