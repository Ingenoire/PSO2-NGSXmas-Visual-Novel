init 2 python:
    p1_trials.append("p1_concert")

label p1_concert:

    scene eradi cg preconcert idle_optimized at zcg
    with fade
    
    e.c "C'mon! Sit!"

    scene eradi cg preconcert lookatyou_optimized at zcg
    with dissolve

    e.c "C'mon! Sit!"

    scene eradi cg preconcert talk_optimized at zcg
    with dissolve

    e.c "C'mon! Sit!"

    scene eradi cg concert active_optimized at zcg
    with dissolve

    e.c "C'mon! Sit!"

    jump nextEvent