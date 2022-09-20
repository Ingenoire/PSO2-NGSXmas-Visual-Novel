label testscenario:
    camera:
        perspective True
        zpos 0 xpos 0 ypos 0

    scene bg kanai summit at zbg
    with fade

    "You see a friend on the horizon..."

    menu:
        "It's Yvonne!":
            $ p1 = y

        "It's Alternoire!":
            $ p1 = a

    "So as it turns out..."

    p1.c "Well, look who it is!"

    $ personal = p1.personality

    $ renpy.show(p1.img + " idle", [trueleft])

    p1.c "Well, look who it is!"

    if(personal == "brave"):
        p1.c "Im actually quite BRAVE"
    elif(personal == "showoff"):
        p1.c "Woo! I'm a showoff!"
    elif(personal == "withdrawn"):
        p1.c "...don't approach me, i'm withdrawn."
    elif(personal == "leader"):
        p1.c "Follow my lead! I'm a leader."
    elif(personal == "clumsy"):
        p1.c "UUUUwwwwaaaah! I'm clumsy and I mess up too often for my own good..."
    elif(personal == "elder"):
        p1.c "Stay a while and listen..."
    elif(personal == "sick"):
        p1.c "I'm emo and frail."
    elif(personal == "innocent"):
        p1.c "I will heed your worries, but I might get kidnapped."
    elif(personal == "airhead"):
        p1.c "Sorry, what are we doing again?"
    elif(personal == "intellect"):
        p1.c "There is nothing my books and my giga brain can't solve."
    else:
        p1.c "Nobody bothered..."    

