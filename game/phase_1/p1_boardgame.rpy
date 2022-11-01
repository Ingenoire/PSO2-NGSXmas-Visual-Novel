init 2 python:
    p1_trials.append("p1_boardgame")

label p1_boardgame:

    scene eradi cg boredtable_optimized at zcg
    with fade

    e.c "C'mon! Sit!"

    scene cg hand boardgame_optimized at zcg
    with fade
    
    e.c "Oh, a board game!"

    scene eradi cg tablesetup idle_optimized at zcg
    with dissolve

    e.c "Oh, a board game!"

    scene eradi cg tablesetup happy_optimized at zcg
    with dissolve
    
    e.c "Oh, a board game!"

    scene eradi cg tablesetup smug_optimized at zcg
    with dissolve
    
    e.c "Oh, a board game!"
    
    scene cg eradi tablegame_optimized at zcg
    with fade

    e.c "Oh, a board game!"
    
    scene cg tablegame encounter_optimized at zcg
    with fade

    e.c "Oh, a board game!"
    
    scene eradi cg boardresult pending_optimized at zcg
    with dissolve

    e.c "Hmmm..."

    scene eradi cg boardresult dissapointed_optimized at zcg
    with dissolve

    e.c "Oh, a board game!"

    scene eradi cg boardresult angry_optimized at zcg
    with dissolve

    e.c "Oh, a board game!"

    scene eradi cg boardresult happy_optimized at zcg
    with dissolve

    e.c "Oh, a board game!"

    scene eradi cg boardresult sob_optimized at zcg
    with dissolve

    e.c "Oh, a board game!"

    jump nextEvent