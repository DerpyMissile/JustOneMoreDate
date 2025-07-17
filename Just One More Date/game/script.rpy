define C = Character("Callie", color = "#893727") # what color for Callie's name?
define N = Character("Narrator") # what color for narrator's name?
define Pc = Character("[Player]") # what color for player's name?
image CLive2D = Live2D("resources/CallieLive2D/MC MODEL PSP.model3.json", default_fade=0.0, loop=True)

init:
    $ counter = 0
    $ genre = ""
    $ food = ""

label start:
    # getting player name
    N "What is your name?"
    $ Player = renpy.input("Enter your name:", length=32)   
    call start
    call end

    return

label start:
    scene mccafebg:
        "resources/mccafebg.png"
        zoom 0.75
        ypos -0.05
    with fade

    N "..."
    N "......"
    N "That's... odd. Callie should be here by now. It's not rush hour, and while you were texting, she didn't seem like the kind of person who'd stand you—"
    # During this textbox have the camera zoom from side to side implying the PC is looking around.

    show CLive2D with moveinright:
        ypos 0.1
    
    C "Ohmygosh! I'm so, so sorry for being late! I just—" 
    # Callie_nervous
    C "—traffic, you know?"
    # (insert animation here) [she chuckles nervously]
    C "Anyways, thanks for waiting! Did you order yet?"

    menu:
        "No.":
            pass
        "I was just about to.":
            pass
        "I was waiting for you.":
            pass

    # Callie_too_Sweet
    C "Oh, really? If that's the case, why don't I cover the meal then? On the house! As an apology for being late!"

    menu:
        "Sure.":
            C "Great! Waiter! Yoohoo! Menu please!"
            jump c1
        "It's alright, I got it.":
            pass
        "We can split.":
            pass

    C "No! I insist! Waiter! Yoohoo! Menu, please!"

    label c1:

    N "You peruse the menu and all its overly decadent offerings. This sweets cafe sure is on the pricey side. $38 for a slice of cake?! Ridiculous! Who in their right mind would order from here?!"

    C "I'll have the Poppin' Pomegranate Parfait! And—oh, wait. [Player], why don't you order first? It's on my card!"

    menu:
        "Any recommendations?":
            C "Their Four Seasons Lotus Bowl makes it so worth the visit! I always stay for more."
            menu:
                "Ambrosial Delight":
                    $ food = "Ambrosial Delight"
                "Four Seasons Lotus Bowl.":
                    $ food = "Four Seasons Lotus Bowl"
        "I'll have the Ambrosial Delight.":
            $ food = "Ambrosial Delight"

    N "The waiter leaves after taking your orders. You have some time to yourselves. What do you want to talk about?"

    menu:
        "What are your hobbies?":
            pass
        "What do you like to do in your free time?":
            pass
    
    # Callie_nervous
    C "Hobbies? I like to play video games in my free time. How about you? What do you play?"

    menu:
        "Action":
            $ genre = "Action"
        "Strategy":
            $ genre = "Strategy"
        "Casual":
            $ genre = "Casual"

    # Callie_too_sweet
    C "Really?! Me too!"

    # first time our character has actual lines :O
    Pc "What do you like about them?"

    # Callie_nervous
    C "Oh…! I really like the—um—I'm sorry! I don't actually like [genre]! I just didn't know what else to say! I didn't leave a good impression since I was late, but you're just, you know, so—!"

    # Callie_nervous_at_reader
    C "—cute! I really, really want you to like me!"

    menu:
        "I get that, I also get nervous on first dates.":
            # Callie_genuine_happy -> Callie_normal
            pass
        "Don't sweat it.":
            # Callie_nervous -> Callie_normal
            pass
        "We'll see.":
            # Callie_panic -> Callie_too_sweet
            pass

    N "The waiter arrives with your food and whips the cover off to reveal glistening towers of fruit and shining caramel. The sparkling glassware gleams with condensation as they're set down before you. Both of you salivate at the sight."

    Pc "So, what do you actually like?"

    # Callie_too_sweet
    C "Oh! I like knitting!"

    # no animation here :/
    N "Callie pulls the bag of materials from her purse."

    # Callie_sardonic
    C "I've knitted for ages, but I keep having to undo my stitches because I've got a pet—"
    # Callie_hiding_frustration
    C "who keeps interrupting—"
    # Callie_BOMBASTIC_side-eye
    C "—me when I'm so close to finishing."

    # DURING THIS TEXT BOX PLAY: Callie_surprised > Callie_nervous > Callie_too_sweet
    N "She seems to be having a rough patch. Let's get this date back on track. Why don't you ask her something? Like, say, what's her favorite thing to knit?"

    menu:
        "What's your favorite thing to knit?":
            # Callie_annoyed
            C "You—!"
            # Callie_too_sweet
            C "—I like knitting—"
            # Callie_nervous
            C "—flowers! But enough about me! How are you liking the cafe?"

            menu:
                "I like it.":
                    # Callie_too_sweet
                    C "Oh? Me too!"
                    pass
                "It's kind of bland":
                    # Callie_genuine_happy
                    C "Yeah, it is."
                    pass

            menu:
                "Do you come here often?":
                    pass
                "You must come here often.":
                    pass
        "Do you come here often?":
            pass

    # Callie_sardonic
    C "I come here so often, I practically live here. This place is always the same every time I come here. The waiter's been here since day one, and the menu hasn't changed in ages. It's—"

    N "A loud crash echoes from the kitchen."

    # Callie_annoyed_at_narrator
    C "—comforting! I love this place! Best sweets in the area. Their [food] is just so flavorful!"

    N "Callie takes a BIG bite of her Poppin' Pomegranate Parfait."

    # Callie_hiding_frustration_2
    C "Mmmm! It's sooo good! How about your food, [Player]? Do you like yours?"

    menu:
        "It's really sweet.": # why is sweet in brackets in the doc?
            # Callie_eye_roll
            C "Yeah, it's {i}really{/i} sweet."
            pass
        "It's too sweet.":
            # Callie_genuine_happy
            C "Yeah, it is."
            pass
    
    return

label end:

    N "The two of you continue to chat, and after a while, you finish your meal. The waiter begins to approach your table with—"

    # Callie_hiding_frustration_1
    C "You know what? I'm actually still a little hungry! Waiter, why don't you give us the menu? I could go for another round!"

    N "The waiter arrives with the check. You should pay."

    # Callie_hiding_frustration_2
    C "Waiter, I asked for the menu? Come on, [Player], you want to go for another round, don't you?"

    show screen QTE(0.5, 'after1')
    # show screen butt_hover("", vpunch)
    menu:
        "Yes":
            pass
        "No":
            pass
    label after1:
        hide screen QTE
        # hide screen butt_hover

    N "The waiter leaves you the checkbook with a stern look before walking away. There are others waiting for a table. It's time to pay."

    # Callie_too_sweet
    C "Waiter! Waiter! Menu—!"

    N "The waiter continues serving other tables while waiting for you to pay. [Player], why don't you?"
        
    # on a side note, another way to do this could be on choice hover callie says no
    show screen QTE(1.5, 'after2')
    show screen butt_hover("no", vpunch)
    label repeat:
    menu:
        "Pay for the meal":
            jump repeat
            
    label after2:
        hide screen QTE
        hide screen butt_hover
        # hide screen no
    pause 0.25
    hide screen no

    # Callie_too_sweet
    C "No-no-no! I'll pay for the date! Just let me order more first—!"
    
    N "{i}Callie{/i}. Just. Pay. {b}UP{/b}"

    # Callie_angry
    C "No! Damn it! Why do you always have to ruin things! This is why the devs abandoned us and why no one likes our game! Because {i}you{/i} keep enforcing this stupid, generic plot!"

    N "Stupid?! Generic!? You ungrateful little {b}{i}brat{/i}{/b}! Who do you think writes the plot? Puts up the options?! Moves your sorry-meandering-butt from plot point to plot point!"

    # Callie_angry
    C "Who do you think the players are playing this game for?!"

    N "For sure not {i}you{/i}"

    # Callie_angry_eye_twitch
    C "You are {i}sooo{/i}, lucky you're just some dumb! Unessential! Exposition-dumping voice! Because if you were a character, I'd strangle you to death!"

    N "And you're lucky you're the only character here because I'd replace you in a tick!"

    # Callie_eye_roll
    C "Replace me? The devs are better off replacing you!"

    N "You {b}motherf—{/b}{nw}!"
    
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

screen butt_hover(popup, trans):
    mousearea:
        # area(800, 350, 300, 100) # xpos, ypos, xlength, ylength (based on top left corner)
        area(350, 350, 1250, 100)
        hovered Show(popup, transition=trans)

# screen ttcard(current_phase):
#     text current_phase