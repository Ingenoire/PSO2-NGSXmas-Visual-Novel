## START
label enterbar:
    scene bg kanai summit
    with fade
    "Go ahead, pick a partner."
    call screen choosepartner

label exitbar: 
    "You are in \"label end\""
    return

label hireYvonne:
    show yvonne worried
    with dissolve

    y.c "So, you want to hire me?"

    menu:
        "Yes!":
            $ p2 = y
            call exitbar
        "No, I'll think again...":
            y.c giveup "Oh... it's okay, take your time."

            hide yvonne
            with dissolve

            call screen choosepartner
    
    return
    




#############################################################################################
## IMAGE BUTTON
screen choosepartner: 
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.35
        auto "pac/pac_goddess_%s.png"
        action [Hide("displayTextScreen"), Jump("exitbar")]

        hovered Show("displayTextScreen", 
            displayText = "Megami",
            n_x = 0.5,
            n_y = 0.35) 
        unhovered Hide("displayTextScreen")

    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.2
        ypos 0.5
        auto "pac/pac_yvonne_%s.png"
        action [Hide("displayTextScreen"), Jump("hireYvonne")]

        hovered Show("displayTextScreen", 
            displayText = "Yvonne",
            n_x = 0.2,
            n_y = 0.5) 
        unhovered Hide("displayTextScreen")



