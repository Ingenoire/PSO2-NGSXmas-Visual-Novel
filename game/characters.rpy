init python:
    
    class Person:
        def __init__(self, character, name, img, tags):
            self.c = character
            self.name = name
            self.img = img
            self.tags = tags
            self.appeared = False


define classes = [
        "Hunter",
        "Fighter",
        "Ranger",
        "Gunner",
        "Force",
        "Techter",
        "Braver",
        "Bouncer",
        "Waker"
    ]

define defaultCharacter = Character("Yvonne", color="#FFFFFF")
define narrator = Character(window_background="gui/textbox_red.png")