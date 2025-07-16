# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define C = Character("Callie", color = "#893727")
define N = Character("Narrator")
define Pc = Character("[Player]")
image CLive2D = Live2D("resources/CallieLive2D/MC MODEL PSP.model3.json", default_fade=0.0, loop=True)

label start:
    # getting player name
    N "Before we begin, tell me: What is your name?"
    $ Player = renpy.input("Enter your name:", length=32)
    show screen ttcard("# Date 1")
    
    call meetup
    show screen ttcard("# Part 1 Hobbies")
    # show screen no
    call end

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

    show CLive2D with moveinright:
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

label end:
    N "The waiter arrives with the check. You should pay."

    $ counter = 0
    # label repeat:
    # show screen QTE(1, 'after')
    # menu:
    #     # you're not supposed to click it so this repeats but the player doesn't realize
    #     "Pay for the meal":
    #         hide screen QTE
    #         jump repeat


# on a side note, another way to do this could be on choice hover callie says no
    show screen QTE(1.5, 'after')
    show screen butt_hover
    label repeat:
    menu:
        "Pay for the meal":
            jump repeat
            
    label after:
        hide screen QTE
        hide screen butt_hover
        # hide screen no
    pause 0.25
    hide screen no
    C "No-no-no! I got this! Just let me just take out my card! It's in my purse... Somewhere…"
    C "Just give me a bit, I totally got this!"

    N "{i}Callie{/i}. Just. Pay. {b}UP{/b}"

    C "I—but—if I do then the date"
    C "—it ends!"

    N "That's how it's supposed to be."

    $ renpy.quit()

    return

# Custom screens

# timer_length = the amount of seconds you want the QTE to last for
# missed_event = the label/event to jump to if QTE fails
screen QTE(timer_length, missed_event):
    on "show" action SetVariable('counter', timer_length)
    timer 0.1 action If(counter > 0, true = SetVariable("counter", counter - 0.1), false = Jump(missed_event)) repeat True

screen no():
    text "NO!" size 1000:
        at truecenter

screen butt_hover():
    mousearea:
        # area(800, 350, 300, 100) # xpos, ypos, xlength, ylength (based on top left corner)
        area(350, 350, 1250, 100)
        hovered Show("no", transition=vpunch)

screen ttcard(current_phase):
    text current_phase