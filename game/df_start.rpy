label darkfalz_start:
    scene bg dfprerp at zbg
    with fade

    "It's quiet."

    scene bg dfentry at zbg
    with fade

    "It's Dark Falz! But, it looks normal!"

    scene bg dfsuckin at zbg
    with fade
    "You're being sucked in!"

    scene bg dfden
    with fade

    "You can't see..."
    window hide

    unknown.c "Oh! Are you okay?"

    show screen eradi_hp_break

    scene eradi cg intro crying_optimized at zbg
    with fade

    unknown.c "Please, wake up! I didn't mean to use the tentacles!"

    scene eradi cg intro closed_optimized at zbg
    with dissolve

    unknown.c "Wait, I can hear a heartbeat."
    unknown.c "..."

    menu:
        "{image=hunter.png} Ha! I can't die easily!" if (main_class == "Hunter"):
            scene eradi cg intro mouth_optimized at zbg with dissolve
            unknown.c "Yes, of course!"
            scene eradi cg intro smile_optimized at zbg with dissolve
            unknown.c "You're my sturdy and beautiful Hunter!"

            $ tallied_break += 5

        "{image=fighter.png} Thankfully, Overload saved me." if (main_class == "Fighter"):
            scene eradi cg intro crying_optimized at zbg with dissolve
            unknown.c "Y-You've used Overload?"
            unknown.c "I-I'm truly sorry, I should have been more careful!"
            unknown.c "I-I could have killed you by accident!"

            $ tallied_dmg += 10
            $ tallied_break += 2

        "{image=ranger.png} Just part of the job." if (main_class == "Ranger"):
            scene eradi cg intro smile_optimized at zbg with dissolve
            unknown.c "Oh right, you're an ARKS Defender, right?"
            unknown.c "You're used to being a subservient doggie for Crawford, right?"
            scene eradi cg intro angry_optimized at zbg with dissolve
            unknown.c "Such a disregard for such a precious life!"
            scene eradi cg intro mouth_optimized at zbg with dissolve
            unknown.c "Then it's a great thing you've come to me!"

            $ tallied_break += 10

        "{image=gunner.png} No... my ranking..." if (main_class == "Gunner"):
            unknown.c "Ranking?"
            scene eradi cg intro smile_optimized at zbg with dissolve
            unknown.c "I'm not sure what you're talking about, but I hope it wasn't anything too bad."
            unknown.c "Sorry about that."
            scene eradi cg intro mouth_optimized at zbg with dissolve
            unknown.c "But in terms of my rankings, you're my number 1!"

            $ tallied_dmg += 5
            $ tallied_break += 5

        "{image=force.png} The force protects me." if (main_class == "Force"):
            scene eradi cg intro smile_optimized at zbg with dissolve
            unknown.c "It sure is, fellow Force."
            unknown.c "Now, I'll protect you."

            $ tallied_break += 3

        "{image=techter.png} Cries..." if (main_class == "Techter"):
            scene eradi cg intro crying_optimized at zbg with dissolve
            unknown.c "I-I- am sorry!"
            unknown.c "E-e-everything i-is gonna be o-okay!"
            scene eradi cg intro smile_optimized at zbg with dissolve
            "..."
            unknown.c "There! There!"
            scene eradi cg intro mouth_optimized at zbg with dissolve
            unknown.c "Feeling better?"

            $ tallied_dmg += 8
            $ tallied_break += 20

        "{image=braver.png} Ninja Recover!" if (main_class == "Braver"):
            unknown.c "..."
            scene eradi cg intro smile_optimized at zbg with dissolve
            unknown.c "Glad to hear that!"

            $ tallied_dmg += 1
            $ tallied_break += 1

        "{image=bouncer.png} I didn't feel it." if (main_class == "Bouncer"):
            scene eradi cg intro smile_optimized at zbg with dissolve
            unknown.c "Of course!"

            $ tallied_dmg += 2
            $ tallied_break += 2

        "{image=waker.png} It's okay, I was hugging Marmelo!" if (main_class == "Waker"):
            scene eradi cg intro crying_optimized at zbg with dissolve
            unknown.c "Oh right, Marmelo."
            unknown.c "It looked quite hurt, so I left it at the veterinarian, but it caused quite a bit of hurt..."
            scene eradi cg intro angry_optimized at zbg with dissolve
            unknown.c "It still stings..."
            scene eradi cg intro mouth_optimized at zbg with dissolve
            unknown.c "We can pick her up when they're done, so please, relax!"
            
            $ tallied_dmg += 20
            $ tallied_break += 10

    scene eradi cg intro mouth_optimized at zbg
    with dissolve
    
    unknown.c "Anyway, I'm just glad to hear you're OK!"

    scene eradi cg intro smile_optimized at zbg
    with dissolve

    unknown.c "I'm the Dark Falz you're looking for, but please, call me Eradi!"
    e.c "Here, I'll help you get up."

    scene bg dfden at zbg
    with fade

    show eradi idle at truecenter
    with dissolve

    window show
    window auto

    e.c "Please, make yourself at home! You're my guest of honor."
    e.c "You've must have had a hard time coming here."
    e.c "I would like to treat you well..."

    menu:
        "{image=hunter.png} HUNTER" if (main_class == "Hunter" or sub_class == "Hunter"):
            unknown.c "..."
        "{image=fighter.png} FIGHTER" if (main_class == "Fighter" or sub_class == "Fighter"):
            unknown.c "..."
        "{image=ranger.png} RANGER" if (main_class == "Ranger" or sub_class == "Ranger"):
            unknown.c "..."
        "{image=gunner.png} GUNNER" if (main_class == "Gunner" or sub_class == "Gunner"):
            unknown.c "..."
        "{image=force.png} FORCE" if (main_class == "Force" or sub_class == "Force"):
            unknown.c "..."
        "{image=techter.png} TECHTER" if (main_class == "Techter" or sub_class == "Techter"):
            unknown.c "..."
        "{image=braver.png} BRAVER" if (main_class == "Braver" or sub_class == "Braver"):
            unknown.c "..."
        "{image=bouncer.png} BOUNCER" if (main_class == "Bouncer" or sub_class == "Bouncer"):
            unknown.c "..."
        "{image=waker.png} WAKER" if (main_class == "Waker" or sub_class == "Waker"):
            unknown.c "..."

    scene eradi cg table intro_optimized at zbg
    with fade

    e.c "I've got a table for two, so please, sit down."
    e.c "We could talk all day about your great adventures, and about my passions!"

    e.c "C'mon! Sit!"

    # PHASE 1: At the table of Dark Falz.

    jump newPhase

    return