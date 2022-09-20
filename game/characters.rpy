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
        def __init__(self, character, name, img, main_class, personality):
            self.c = character
            self.name = name
            self.main_class = main_class
            self.personality = personality
            self.img = img

    

define defaultCharacter = Character("Yvonne", color="#FFFFFF")
define narrator = Character(window_background="gui/textbox_red.png")


define personalities = ["brave", "showoff", "withdrawn", "leader", "clumsy", "elder", "sick", "innocent", "airhead", "intellect"]

# Player 1
define p1 = Person(Character("Megami"), "Megami", "goddess", "hunter", "airhead")
define p2 = Person(Character("Megami"), "Megami", "goddess", "hunter", "airhead")

label characterSetup:
    $ g = Person(Character(
        "Megami", 
        kind=defaultCharacter, 
        image="goddess", 
        window_background="gui/textbox_green.png", 
        namebox_background="gui/namebox_green.png", 
        callback=high_beep), 
        "Megami", 
        "goddess", 
        "hunter", 
        "airhead")
    
    $ y = Person(Character(
        "Yvonne", 
        kind=defaultCharacter, 
        image="yvonne", 
        window_background="gui/textbox_red.png", 
        namebox_background="gui/namebox.png", 
        callback=high_beep),
        "Yvonne", 
        "yvonne", 
        "hunter", 
        "airhead")
    $ a = Person(Character("Alternoire", kind=defaultCharacter, image="alternoire", window_background="gui/textbox_blue.png", namebox_background="gui/namebox_blue.png", callback=high_beep), "Alternoire", "alternoire", "hunter", "withdrawn")


    return