label char_crawford:
    return

init 1 python:
    c = Person(Character(
        "Crawford",
        kind=defaultCharacter,
        image="crawford",
        window_background="gui/textbox_blue.png",
        namebox_background="gui/namebox_blue.png",
        callback=low_beep),
        "Crawford",
        "crawford",
        []
    )
    actors.append(c)