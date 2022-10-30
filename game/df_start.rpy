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
        "{image=hunter.png} C'mon, I won't die to that!" if (main_class == "Hunter"):
            unknown.c "..."
        "{image=fighter.png} Thankfully, Overload saved me." if (main_class == "Fighter"):
            unknown.c "..."
        "{image=ranger.png} Just part of the job." if (main_class == "Ranger"):
            unknown.c "..."
        "{image=gunner.png} You messed with my ranking, jerk!" if (main_class == "Gunner"):
            unknown.c "..."
        "{image=force.png} The force protects me." if (main_class == "Force"):
            unknown.c "..."
        "{image=techter.png} You're right, I was going to die." if (main_class == "Techter"):
            unknown.c "..."
        "{image=braver.png} I'm going to strangle you." if (main_class == "Braver"):
            unknown.c "..."
        "{image=bouncer.png} Did something happen? Didn't feel it." if (main_class == "Bouncer"):
            unknown.c "..."
        "{image=waker.png} Chuck Marron" if (main_class == "Waker"):
            unknown.c "..."

    scene eradi cg intro mouth_optimized at zbg
    with dissolve
    
    unknown.c "I'm so happy to hear you're OK!"
    unknown.c "..."

    scene eradi cg intro smile_optimized at zbg
    with dissolve

    unknown.c "You're an ARKS Defender, right?"
    unknown.c "I'm the Dark Falz you're looking for, but please, call me Eradi!"
    e.c "Let me get you up."

    scene bg dfden at zbg
    with fade

    show eradi idle at truecenter
    with dissolve

    window show
    window auto

    e.c "Please, make yourself at home! You're my guest of honor."
    e.c "So then, what would you like, dear viewer?"

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

    jump newPhase

    return