# The script of the game goes in this file.

define low_beeps = ['audio/low_beep.ogg']
define mid_beeps = ['audio/mid_beep.ogg']
define hi_beeps = ['audio/high_beepA.ogg', 'audio/high_beepB.ogg', 'audio/high_beepC.ogg']


# Detected character labels will be written here
define ref_actor_files = []
# The Character Objects are then written here
define actors = []

# Adventure Points
# Obtained or lost as a result of each trial.
define points = 0

# Player name, can be changed at the start of a new playthrough.
define p_name = "Viewer"

# Main and Sub Class of the player
# This defines the possible options you can take in certain trials
define main_class = "hunter"
define sub_class = "force"


# Detected Trials will be written here
define ref_trials = []
# Detected Bonus Segments will be written here
define ref_bonuses = []
# The gameplay route, determined when you start a new run, listing the required labels in the order desired.
define route = []
# The index for the current event on the route, it increments after every trial/bonus section.
define r_step = -1


# Declare characters used by this game. The color argument colorizes the
# name of the character.

init python:
    
    def high_beep(event, **kwargs):
        if event == "show":
            renpy.sound.play(hi_beeps[1])
            renpy.sound.play(hi_beeps[2])
            renpy.sound.queue(renpy.random.choice(hi_beeps))
            renpy.sound.queue(renpy.random.choice(hi_beeps))
            renpy.sound.queue(renpy.random.choice(hi_beeps))
            renpy.sound.queue(renpy.random.choice(hi_beeps))
            renpy.sound.queue(renpy.random.choice(hi_beeps))
            renpy.sound.queue(renpy.random.choice(hi_beeps))
            renpy.sound.queue(renpy.random.choice(hi_beeps))
            renpy.sound.queue(renpy.random.choice(hi_beeps))
            renpy.sound.queue(renpy.random.choice(hi_beeps))
            renpy.sound.queue(renpy.random.choice(hi_beeps))
            renpy.sound.queue(renpy.random.choice(hi_beeps))
            renpy.sound.queue(renpy.random.choice(hi_beeps))
            renpy.sound.queue(renpy.random.choice(hi_beeps))
            renpy.sound.queue(renpy.random.choice(hi_beeps))
            renpy.sound.queue(renpy.random.choice(hi_beeps))
            renpy.sound.queue(renpy.random.choice(hi_beeps))
            renpy.sound.queue(renpy.random.choice(hi_beeps))
            renpy.sound.queue(renpy.random.choice(hi_beeps))
            renpy.sound.queue(renpy.random.choice(hi_beeps))
            renpy.sound.queue(renpy.random.choice(hi_beeps))
            renpy.sound.queue(renpy.random.choice(hi_beeps))
            renpy.sound.queue(renpy.random.choice(hi_beeps))
            renpy.sound.queue(renpy.random.choice(hi_beeps))
            renpy.sound.queue(renpy.random.choice(hi_beeps))
            renpy.sound.queue(renpy.random.choice(hi_beeps))
            renpy.sound.queue(renpy.random.choice(hi_beeps))
            renpy.sound.queue(renpy.random.choice(hi_beeps))

        elif event == "slow_done" or event == "end":
            renpy.sound.stop()

    def mid_beep(event, **kwargs):
        if event == "show":
            renpy.sound.play("audio/mid_beep.ogg")
        elif event == "slow_done" or event == "end":
            renpy.sound.stop()
    
    def low_beep(event, **kwargs):
        if event == "show":
            renpy.sound.play("audio/low_beep.ogg")
        elif event == "slow_done" or event == "end":
            renpy.sound.stop()

    # Create an emote on the character, such as ? and !?
    def emote(name, emotion): # Name is the character sprite, emotion is the emote sprite.
        x = int(renpy.get_image_bounds(name)[0] + renpy.get_image_bounds(name)[2] / 2) + 150
        y = 150
        # Displays the emote sprite.
        trnf = None
        if emotion == "exclamation": 
            trnf = exclamation
        elif emotion == "confused": 
            renpy.sound.play("audio/confused.ogg")
            trnf = confused
        elif emotion == "question": 
            trnf = question
            renpy.sound.play("audio/question.ogg")
        elif emotion == "notice": 
            x -= 100
            trnf = notice
            renpy.sound.play("audio/notice.ogg")
        elif emotion == "sweat":
            x -= 100
            trnf = sweat
            renpy.sound.play("audio/confused.ogg")
        
        renpy.show(emotion, at_list=[Transform(pos=(x, y)), trnf])
        return

    # Get a random character that has the following tags (in an array)
    ## tags: Array of tag strings to check
    ## removeFromLater: If true, this will prevent the rest of the run from ever spawning this character.
    ## If no characters are usable due to this, will try again but this time toggle a used character back on.
    def getCharacter(tags, removeFromLater = False):
        found_person = None
        
        copyactors = actors.copy()
        renpy.random.shuffle(copyactors)

        found_person = searchCharacters(tags, copyactors)
        # If it fails, we force to find someone with the tags.
        if(found_person == None): 
            found_person = searchCharacters(tags, copyactors, True)

        if removeFromLater:
            found_person.appeared = False
        return found_person

    def searchCharacters(vtags, arr, resetAppear=False):
        found_person = None
        for person in arr:
            for tag in vtags:
                if tag in person.tags:
                    if resetAppear:
                        person.appeared = False
                        return person
                    elif person.appeared == False:
                        return person

        return

    # Generate the chain of events for this run.
    ## This includes Trials, Trivia, Interviews, ending, etc...
    def generateStoryPath():

        # Clearing stuff for subsequent plays
        possibleTrials = []
        possibleTrials.clear()
        possibleTrials.extend(ref_trials)
        renpy.random.shuffle(possibleTrials)
        
        possibleBonuses = []
        possibleBonuses.clear()
        possibleBonuses.extend(ref_bonuses)
        renpy.random.shuffle(possibleBonuses)

        route.clear()

        # First event will always be a trial
        # Pop to remove it from possible future trials, index doesn't really matter since the arra- uh, list, gets shuffled.
        route.append(possibleTrials.pop())
        # Second event will always be a bonus
        route.append(possibleBonuses.pop())

        game_length = 6
        # 33% chance of increasing the amount of events.
        if(renpy.random.randint(0, 2) == 2):
            game_length += renpy.random.randint(0, 2)

        # how many trials/bonuses?
        cpt_trials = 1
        cpt_bonuses = 1

        # Now we do a loop to populate the route.
        while (len(route) < game_length - 1):
            if(cpt_bonuses + 1 < cpt_trials):
                route.append(possibleBonuses.pop())
                cpt_bonuses += 1
            else:
                route.append(possibleTrials.pop())
                cpt_trials += 1

        # Game must always end with a trial
        route.append(possibleTrials.pop())

        return

    for i in renpy.get_all_labels():
        if i.startswith("char_"): 
            if (('.' in i) == False):
                ref_actor_files.append(i)

## The borders of the box containing the character's name, in left, top, right,
## bottom order.

define gui.name_text_outlines = [ (3, "#00000080", 0, 0) ]

transform exclamation:
    alignaround (.5, .5)
    alpha 0
    ease 0.1 alpha 1 yoffset -30 zoom 1.5
    easeout .175 yoffset 0 zoom 1
    ease 0.15 zoom 1.25
    easeout .15 yoffset 0 zoom 1
    pause 0.3
    ease 0.1 alpha 0

transform confused:
    alignaround (.5, .5)
    alpha 0
    ease 0.15 alpha 1 zoom 1.25
    easeout .15 yoffset 0 zoom 1
    pause 0.3
    ease 0.1 alpha 0

transform question:
    alignaround (.5, .5)
    alpha 0
    yoffset 20
    ease .175 alpha 1 yoffset -20
    easeout .05 yoffset 0
    pause 1
    ease 0.1 alpha 0

transform notice:
    alignaround (.5, .5)
    alpha 0
    ease .05 alpha 1
    easeout .05 alpha 0.2
    ease .05 alpha 1
    pause 1
    ease 0.1 alpha 0

transform sweat:
    alignaround (.5, .5)
    alpha 0
    ease .05 alpha 1
    easeout .05 alpha 0.2
    ease .05 alpha 1
    pause 1
    ease 0.1 alpha 0


### Positions
transform trueleft:
    xcenter 0.25
    ypos 20
    zpos 100
    yoffset 30

transform trueright:
    xcenter 0.75
    ypos 20
    zpos 100
    yoffset 30

transform truecenter:
    xcenter 0.5
    ypos 20
    zpos 100
    yoffset 30

# Flips (because I suck at programming and can't figure out a clean way to have a transform house a flip and non-flip through renpy (and time constraints))
transform trueleft_f:
    xcenter 0.25
    ypos 20
    zpos 100
    yoffset 30
    xzoom -1.0

transform trueright_f:
    xcenter 0.75
    ypos 20
    zpos 100
    yoffset 30
    xzoom -1.0

transform truecenter_f:
    xcenter 0.5
    ypos 20
    zpos 100
    yoffset 30
    xzoom -1.0

## Moves

transform to_right:
    ease 0.4 xcenter 0.75
transform to_left:
    ease 0.4 xcenter 0.25
transform exit_left:
    ease 1 xcenter 0.0 alpha 0 zpos 300
transform exit_right:
    ease 1 xcenter 1.0 alpha 0 zpos 300
transform to_center:
    ease 0.4 xcenter 0.5
transform exit_left_f:
    xzoom -1.0
    ease 0.4 xcenter 0.0 alpha 0
transform exit_right_f:
    xzoom -1.0
    ease 0.4 xcenter 1.0 alpha 0

## Item Positions

transform itemright:
    xcenter 0.88
    ycenter 0.4
    zpos 100

transform itemleft:
    xcenter 0.15
    ycenter 0.4
    zpos 100



transform zoomin:
    ycenter 0.5 xcenter 0.5
    ease .8 zoom 2.0 ycenter 0.5

transform zbg:
    zpos -1000 zzoom True
    ypos -200

transform bounce:
    yoffset 30
    easein .175 yoffset 0
    easeout .175 yoffset 30
    easein .175 yoffset 10
    easeout .175 yoffset 30
    yoffset 30


label start:
    $ renpy.random.Random(seed=None)
    $ generateStoryPath()

    "[route]"

    call intro
    return
    
label chooseNextAdventure:

    $ r_step += 1
    $ check = r_step + 1 > len(route)

    if (check):
        jump ending
    else:
        $ renpy.jump(route[r_step] + ".begin_trial")
    
    return