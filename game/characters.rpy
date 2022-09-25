init python:
    
    mainclasses = {
        "hunter": "Hunter",
        "fighter": "Fighter",
        "ranger": "Ranger",
        "gunner": "Gunner",
        "force": "Force",
        "techter": "Techter",
        "braver": "Braver",
        "bouncer": "Bouncer",
        "waker": "Waker"
    }

    class Person:
        def __init__(self, character, name, img):
            self.c = character
            self.name = name
            self.img = img

    

define defaultCharacter = Character("Yvonne", color="#FFFFFF")
define narrator = Character(window_background="gui/textbox_red.png")


# Player 1
define p1 = Person(Character("Megami"), "Megami", "goddess")
define p2 = Person(Character("Megami"), "Megami", "goddess")
define actors = []

label characterSetup:
    $ g = Person(Character(
        "Megami", 
        kind=defaultCharacter, 
        image="goddess", 
        window_background="gui/textbox_green.png", 
        namebox_background="gui/namebox_green.png", 
        callback=high_beep), 
        "Megami", 
        "goddess")
    
    python:
        for i in renpy.get_all_labels():
            if i.startswith("char_"):
                actors.append(i)

        for a in actors:
            renpy.call(a + ".charsetup")
            
    return