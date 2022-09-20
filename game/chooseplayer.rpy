

label playerselectmenu:
    scene bg kanai summit
    with fade
    "Choose your identity."
    call screen chooseplayer

label playerselected(n_player=g):
    $ p1 = n_player
    hide screen confirm

    "Well then!"

    $ renpy.show(p1.img + " idle")
    with dissolve

    "Hello [p1.c.name]!"

    $ renpy.call(p1.img + ".mainhired")
    jump enterbar

screen chooseplayer: 

    grid 3 1:
        
        imagebutton:
            auto "portraits/portrait_yvonne_%s.png"
            action [Show("confirm", None, "Pick Yvonne?", Call("playerselected", y), Hide("confirm"))]

            hovered Show("displayPlayerScreen", 
                player_name = "Yvonne",
                player_img = "yvonne idle")
            unhovered Hide("displayPlayerScreen")

        imagebutton:
            auto "portraits/portrait_alternoire_%s.png"
            action [Hide("displayPlayerScreen"), Jump("exitbar")]

            hovered Show("displayPlayerScreen", 
                player_name = "Alternoire",
                player_img = "alternoire idle")
            unhovered Hide("displayPlayerScreen")

        imagebutton:
            auto "portraits/portrait_goddess_%s.png"
            action [Hide("displayPlayerScreen"), Jump("exitbar")]

            hovered Show("displayPlayerScreen", 
                player_name = "Goddess",
                player_img = "goddess idle")
            unhovered Hide("displayPlayerScreen")

    