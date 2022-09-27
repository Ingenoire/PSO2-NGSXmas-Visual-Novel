init python:
    
    class Person:
        def __init__(self, character, name, img, tags):
            self.c = character
            self.name = name
            self.img = img
            self.tags = tags
            self.appeared = False


define classes = [
        "hunter",
        "fighter",
        "ranger",
        "gunner",
        "force",
        "techter",
        "braver",
        "bouncer",
        "waker"
    ]

define defaultCharacter = Character("Yvonne", color="#FFFFFF")
define narrator = Character(window_background="gui/textbox_red.png")