# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define C = Character("Callie", color = "#893727")
define N = Character("Narrator")
define Pc = Character("[Player]")
image CLive2D = Live2D("resources/CallieLive2D/MC MODEL PSP.model3.json", default_fade=0.0, loop=True)

label start:
    # show screen QTE
    # C "Testing"
    # N "You're about to test a quick time event."
    # show QTEv2
    # N "I have no idea if it worked."

    # getting player name
    N "Before we begin, tell me: What is your name?"
    $ Player = renpy.input("Enter your name:", length=32)

    call meetup


    return

label meetup:
    scene mccafebg:
        "resources/mccafebg.png"
        zoom 0.75
        ypos -0.05
    with fade

    N "..."
    N "......"
    N "That's... Odd. Callie should be here by now. The parking lot is empty and it\'s not rush hour. She doesn\'t seem like the kind of person who would stand you up when you were chatting over—"    

    show CLive2D with fade:
        ypos 0.1
    
    C "Ohmygosh! I'm so-so sorry for being late! I just—" 
    # (insert animation here) [her eyes dart around]
    C "—traffic, you know?"
    # (insert animation here) [she chuckles nervously]
    C "Anyways, thanks for waiting! Did you order yet?"

    menu:
        "No.":
            jump c_all1
        "I was just about to.":
            jump c_all1
        "I was waiting for you.":
            jump c_all1
    
    label c_all1:

    # (insert animation here) Callie smiles wide, maybe too wide. There’s an undertone of nervousness in her voice:
    C "Oh, really? If that's the case, why don't I cover the meal then? On the house! As an apology for being late!"

    menu:
        "Sure.":
            jump c_1
        "It's alright, I got it.":
            jump c_all2
        "We can split.":
            jump c_all2

    label c_1:
        C "Great! Waiter! Yoohoo! Menu please!"

    label c_all2:
        C "No! I insist! Waiter! Yoohoo! Menu, please!"

    N "You peruse the menu and all its overly decadent offerings. This sweets cafe sure is on the pricey side. $38 for a slice of cake?! Ridiculous! Who in their right mind would order from here?!"

    C "I'll have the...<WIP>"

    return

# QTE testing area
screen QTEv2:
    timer 2.0 action Jump("too_slow")

screen QTE:
    vbox:
        textbutton "1" action Jump("yes")
        textbutton "2" action Jump("no")
    timer 3.0 action Jump("too_slow")

label yes:
    N "Well done."
    return

label no:
    N "Aw man."
    return

label too_slow:
    N "You're too slow. Goodbye now."
    return