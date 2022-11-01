init 2 python:
    p1_trials.append("p1_hug")

label p1_hug:
    scene eradi cg attable lookingback_optimized at zcg
    with fade

    e.c "C'mon! Sit!"

    scene eradi cg attable thonk_optimized at zcg
    with dissolve

    e.c "C'mon! Sit!"

    scene eradi cg pensive idle_optimized at zcg
    with dissolve

    e.c "C'mon! Sit!"

    scene eradi cg pensive regret_optimized at zcg
    with dissolve

    e.c "C'mon! Sit!"

    scene eradi cg pensive smile_optimized at zcg
    with dissolve

    e.c "C'mon! Sit!"

    jump nextEvent