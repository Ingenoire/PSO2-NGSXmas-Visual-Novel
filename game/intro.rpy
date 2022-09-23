label intro:
    camera:
        perspective True
        zpos 0 xpos 0 ypos 0

    scene bg intro at zbg
    with fade

    "You are in a hallway."

    show goddess idle
    with dissolve

    y.c "In my presence, I welcome you."

    scene bg goddess welcome
    with fade
    camera:
        perspective False


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