label char_eradi:
    return

init 1 python:
    e = Person(Character(
        "Eradi",
        kind=defaultCharacter,
        image="eradi",
        window_background="gui/textbox_purple.png",
        namebox_background="gui/namebox_purple.png",
        callback=high_beep),
        "Eradi",
        "eradi",
        []
    )
    actors.append(e)

    unknown = Person(Character(
        "???",
        kind=defaultCharacter,
        image="eradi",
        window_background="gui/textbox_purple.png",
        namebox_background="gui/namebox_purple.png",
        callback=high_beep),
        "???",
        "eradi",
        []
    )
    actors.append(unknown)