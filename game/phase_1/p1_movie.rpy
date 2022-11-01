init 2 python:
    p1_trials.append("p1_movie")

label p1_movie:

    scene eradi cg getuptable_optimized at zcg
    with dissolve

    e.c "C'mon! Sit!"

    scene eradi cg reachingout_optimized at zcg
    with dissolve

    e.c "C'mon! Sit!"

    scene cg projector_optimized at zcg
    with fade
    
    e.c "C'mon! Sit!"

    scene cg laser video_optimized at zcg
    with fade

    e.c "C'mon! Sit!"

    scene black

    camera:
        zoom 2
        perspective True
        ypos 2500
        xpos 300

    scene eradi cg lookingdown_optimized at zcg
    with fade

    pause 0.5

    camera:
        perspective True
        ease 2 ypos 400

    pause 3

    e.c "Can I sit near you? A movie is no fun when lovers are apart."

    scene black

    camera:
        perspective True
        zoom 1
        zpos 0 xpos 0 ypos 0

    scene eradi cg projector crying_optimized at zcg
    with dissolve

    camera:
        perspective True
        zpos 0 xpos 0 ypos 0

    e.c "C'mon! Sit!"

    scene eradi cg projector happy_optimized at zcg
    with dissolve

    e.c "C'mon! Sit!"

    scene eradi cg projector smile_optimized at zcg
    with dissolve

    e.c "C'mon! Sit!"

    scene eradi cg projector stoic_optimized at zcg
    with dissolve

    e.c "C'mon! Sit!"

    scene cg video frame_optimized at zcg
    with dissolve

    e.c "C'mon! Sit!"

    image rng_movie = Movie(play="movies/yvonnealterfight.webm")
    show rng_movie at movie_pos

    
    e.c "C'mon! Sit!"
    e.c "C'mon! Sit!"
    e.c "C'mon! Sit!"
    e.c "C'mon! Sit!"
    e.c "C'mon! Sit!"

    jump nextEvent