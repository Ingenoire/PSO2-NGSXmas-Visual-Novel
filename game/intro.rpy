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

        if not p_name:
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

    y.c "Before we can begin, you're going to have to take a Main Class and a Sub Class."

    menu:
        "What is your Main Class?"

        "{image=hunter.png} HUNTER":
            $ main_class = "hunter"
            g.c "Guess you're a hunter."
        "{image=fighter.png} FIGHTER":
            $ main_class = "fighter"
            g.c "Guess you're a fighter."
        "{image=ranger.png} RANGER":
            $ main_class = "ranger"
            g.c "Guess you're a ranger."
        "{image=gunner.png} GUNNER":
            $ main_class = "gunner"
            g.c "Guess you're a gunner."
        "{image=force.png} FORCE":
            $ main_class = "force"
            g.c "Guess you're a force."
        "{image=techter.png} TECHTER":
            $ main_class = "techter"
            g.c "Guess you're a techter."
        "{image=braver.png} BRAVER":
            $ main_class = "braver"
            g.c "Guess you're a braver."
        "{image=bouncer.png} BOUNCER":
            $ main_class = "bouncer"
            g.c "Guess you're a bouncer."

    menu:
        "What is your Sub Class?"

        "{image=hunter.png} HUNTER" if (main_class != "hunter"):
            $ sub_class = "hunter"
            g.c "Guess you're a hunter."
        "{image=fighter.png} FIGHTER" if (main_class != "fighter"):
            $ sub_class = "fighter"
            g.c "Guess you're a fighter."
        "{image=ranger.png} RANGER" if (main_class != "ranger"):
            $ sub_class = "ranger"
            g.c "Guess you're a ranger."
        "{image=gunner.png} GUNNER" if (main_class != "gunner"):
            $ sub_class = "gunner"
            g.c "Guess you're a gunner."
        "{image=force.png} FORCE" if (main_class != "force"):
            $ sub_class = "force"
            g.c "Guess you're a force."
        "{image=techter.png} TECHTER" if (main_class != "techter"):
            $ sub_class = "techter"
            g.c "Guess you're a techter."
        "{image=braver.png} BRAVER" if (main_class != "braver"):
            $ sub_class = "braver"
            g.c "Guess you're a braver."
        "{image=bouncer.png} BOUNCER" if (main_class != "bouncer"):
            $ sub_class = "bouncer"
            g.c "Guess you're a bouncer."

    menu:
        "Something happens! What do you do?"

        "Do something as a generic":
            g.c "You don't have much to do huh..."
        "{image=hunter.png} Do this action because you're a Hunter!" if (main_class == "hunter" or sub_class == "hunter"):
            g.c "Guess you're a hunter."
        "{image=fighter.png} Do this action because you're a Fighter!" if (main_class == "fighter" or sub_class == "fighter"):
            g.c "Guess you're a fighter."
        "{image=ranger.png} Do this action because you're a Ranger!" if (main_class == "ranger" or sub_class == "ranger"):
            g.c "Guess you're a ranger."
        "{image=gunner.png} Do this action because you're a Gunner!" if (main_class == "gunner" or sub_class == "gunner"):
            g.c "Guess you're a gunner."
        "{image=force.png} Do this action because you're a Force!" if (main_class == "force" or sub_class == "force"):
            g.c "Guess you're a force."
        "{image=techter.png} Do this action because you're a Techter!" if (main_class == "techter" or sub_class == "techter"):
            g.c "Guess you're a techter."
        "{image=braver.png} Do this action because you're a Braver!" if (main_class == "braver" or sub_class == "braver"):
            g.c "Guess you're a braver."
        "{image=bouncer.png} Do this action because you're a Bouncer!" if (main_class == "bouncer" or sub_class == "bouncer"):
            g.c "Guess you're a bouncer."

    g.c "I hope you can make it safely to N-Oracle, and be rewarded with the content your soul has desired for nearly 2 years now..."

    $ g.c("I am a , so I can handle myself in battle you know!")

    g.c "I have heard Halpha's Collective Cry for Content."
    g.c "I was merely passing by this universe, and I thought I could do something."
    g.c "I've read the collective consciousness of ARKS. I know what all of you want."
    g.c "You want to return to the Oracle Fleet, but in HD. You want that good old classic PSO2 back, in glorious Hi-Definition Graphics."
    g.c "But, you want more than just the old stuff. You want 8 years worth of new content, to satisfy the content famine caused by NGS."
    g.c "With my powers, I have manifested a portal to N-Oracle."
    g.c "However, this paradise of ideals will only open by shedding sweat and tears."
    g.c "I have... re-adjusted, your microscopic world, to be a linear course."
    g.c "All you have to do is reach the Volcanic Mountain, Stia."
    g.c "But the quality of the N-Oracle you'll find will depend on your accomplishments on your journey there."
    g.c "Your actions will lead to either getting points or losing points."
    g.c "Finally, you must bring a partner with you."

    jump playerselectmenu

    return