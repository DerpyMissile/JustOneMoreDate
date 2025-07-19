define C = Character("Callie", color = "#893727") # what color for Callie's name?
define N = Character("Narrator", namebox_xalign = 0.60) # what color for narrator's name?
define Pc = Character("[Player]") # what color for player's name?
image CLive2D = Live2D("resources/Callie", default_fade=0.0, loop=True)
image bgframe1 = "resources/cafe-bg-1.png"
image bgframe2 = "resources/cafe-bg-2.png"
define lookaround = Move((0, 0), (-65, 0), 2, bounce=True, repeat=True, delay=2)
default persistent.crashed = False

init:
    $ counter = 0
    $ genre = ""
    $ food = ""

# setting up the background animation
image bg:
    "bgframe1" with dissolve
    pause 1.0
    "bgframe2" with dissolve
    pause 1.0
    repeat

image bg_ERROR:
    "bgframe1" with dissolve
    pause 0.1
    "bgframe2" with dissolve
    pause 1
    repeat

label start:
    # getting player name
    N "What is your name?"
    $ Player = renpy.input("Enter your name:", length=32)
    $ quick_menu = False
    call beginning
    call end
    return

label beginning:
    scene bg:
        zoom 0.8 ypos -0.05
        xalign 0.5
    with fade

    $ quick_menu = True
    N "...{w}..."
    N "That's... odd. Callie should be here by now. It's not rush hour, and while you were texting, she didn't {i}seem{/i} like the kind of person who'd stand you up—"
    $ quick_menu = False
    scene bg:
        zoom 0.8 ypos -0.05
        xalign 0.5
    with lookaround
    # During this textbox have the camera zoom from side to side implying the PC is looking around.

    show CLive2D normal with moveinright:
        ypos 0.1
    

    show CLive2D normal_talking
    $ quick_menu = True
    C "Ohmygosh!{w}{cps=20} I'm {i}so{/i}, so sorry for being late! I just—{nw=1}"
    show CLive2D nervous_talking nervous_normal normal_talking
    C "{cps=20}—traffic, you know? {w=1.5} Anyways, thanks for waiting! Did you order yet?{w}"
    show CLive2D normal
    $ quick_menu = False
    menu:
        "No.":
            pass
        "I was just about to.":
            pass
        "I was waiting for you.":
            pass
    $ quick_menu = True

    # show CLive2D Callie_too_Sweet
    C "Oh, really? If that's the case, why don't I cover the meal then? On the house! As an apology for being late!"

    menu:
        "Sure.":
            C "Great! Waiter! Yoohoo! Menu please!"
            jump c1
        "It's alright, I got it.":
            pass
        "We can split.":
            pass
    $ quick_menu = True
    C "No! I insist! Waiter! Yoohoo! Menu, please!"

    label c1:
    N "You peruse the menu and all its overly decadent offerings. This sweets cafe sure is on the pricey side. $38 for a slice of cake?! Ridiculous! Who in their right mind would order from here?!"

    C "I'll have the Poppin' Pomegranate Parfait! And—oh, wait. [Player], why don't you order first? It's on my card!"
    # show CLive2D Callie_too_sweet

    $ quick_menu = False
    menu:
        "Any recommendations?":
            $ quick_menu = True
            C "Their Four Seasons Lotus Bowl makes it {i}so{/i} worth the visit! I always stay for more."
            Pc "I'll take the:"
            $ quick_menu = False
            menu:
                "Ambrosial Delight.":
                    $ food = "Ambrosial Delight"
                "Four Seasons Lotus Bowl.":
                    $ food = "Four Seasons Lotus Bowl"
                    # show CLive2D Callie_genuine_happy (2s)
        "I'll have the Ambrosial Delight.":
            $ food = "Ambrosial Delight"
    $ quick_menu = True
    show CLive2D normal
    N "The waiter leaves after taking your orders. You have some time to yourselves. What do you want to talk about?"
    $ quick_menu = False
    menu:
        "What are your hobbies?":
            pass
        "What do you like to do in your free time?":
            pass
    $ quick_menu = True
    # show CLive2D Callie_surprised
    C "Me?"
    # show CLive2D Callie_nervous
    extend " I like to play video games in my free time. How about you? What do you play?"
    $ quick_menu = False
    menu:
        "Action":
            $ genre = "Action"
        "Strategy":
            $ genre = "Strategy"
        "Casual":
            $ genre = "Casual"
    $ quick_menu = True
    # show CLive2D Callie_too_sweet
    C "Really?! Me too!"

    # first time our character has actual lines :O
    Pc "What do you like about [genre.lower()] games?"

    # show CLive2D Callie_nervous
    C "Oh…! I really like the—um—I'm sorry! I don't actually like [genre.lower()] games! I just didn't know what else to say! I didn't leave a good impression since I was late, but you're just, you know, so—!"

    # show CLive2D Callie_nervous_at_reader
    C "—cute! And I really, {i}really{/i} want you to like me!"

    $ quick_menu = False
    menu:
        "I get that, I also get nervous on first dates.":
            # show CLive2D Callie_genuine_happy -> Callie_normal
            pass
        "Don't sweat it.":
            # show CLive2D Callie_nervous -> Callie_normal
            pass
        "We'll see.":
            # show CLive2D Callie_panic -> Callie_too_sweet
            pass
    pause 2
    $ quick_menu = True
    show CLive2D normal
    N "The waiter arrives with your food and whips the cover off to reveal glistening towers of fruit and shining caramel."
    N "The sparkling glassware gleams with condensation as they're set down before you. "
    # show CLive2D Callie_annoyed_at_narrator -> Callie_normal
    extend "Both of you salivate at the sight."

    Pc "So, what do you actually like?"

    # show CLive2D Callie_too_sweet
    C "Oh! I like knitting!"

    N "Callie pulls the bag of materials from her purse."

    # show CLive2D Callie_sardonic
    C "I've knitted for ages, but I keep having to undo my stitches because I've got a {i}pet{/i}—"
    show CLive2D hiding_frustration_start hiding_frustration_talking
    extend "who keeps interrupting"
    show CLive2D hiding_frustration_normal normal_bombastic_side_eye normal_talking
    extend "{w=2} me {w=2}when I'm so close to finishing."
    show CLive2D normal

    # DURING THIS TEXT BOX PLAY: Callie_surprised > Callie_nervous > Callie_too_sweet
    N "She seems to be having a rough patch. Let's get this date back on track. Why don't you ask her something?"
    # show CLive2D Callie_surprised_no_talking
    extend " Like, say, what's her favorite thing to knit?"
    # what the balls is happening here. so many animations
    # show CLive2D Callie_nervous_ending Callie_too_sweet_beginning Callie_too_sweet__ending_basic??

    $ quick_menu = False
    menu:
        "What's your favorite thing to knit?":
            $ quick_menu = True
            # show CLive2D Callie_annoyed
            C "You—!"
            # show CLive2D Callie_too_sweet
            C "I like knitting—"
            # show CLive2D Callie_nervous
            extend "flowers!{w} But enough about me! How are you liking the cafe?"
            $ quick_menu = False
            menu:
                "I like it.":
                    $ quick_menu = True
                    # show CLive2D Callie_too_sweet
                    C "Oh? Me too!"
                    pass
                "It's kind of bland.":
                    $ quick_menu = True
                    # show CLive2D Callie_genuine_happy
                    C "Yeah, it is."
                    pass
            $ quick_menu = False
            menu:
                "Do you come here often?":
                    pass
                "You must come here often.":
                    pass
        "Do you come here often?":
            pass
    $ quick_menu = True
    # show CLive2D Callie_sardonic
    C "I come here {i}sooo{/i} often, I practically live here. This place is always the same every time I visit. The waiter's been here since day one, and the menu hasn't changed in ages. It's—"

    N "A loud crash echoes from the kitchen." with vpunch

    # show CLive2D Callie_annoyed_at_narrator
    C "—comforting! I love this place! Best sweets in the area. Their [food] is just so flavorful!"

    N "Callie takes a BIG bite of her Poppin' Pomegranate Parfait."

    # show CLive2D Callie_hiding_frustration_2
    C "Mmmm! It's {i}sooo{/i} good! How about your food, [Player]? Do you like yours?"

    $ quick_menu = False
    menu:
        "It's really sweet.":
            $ quick_menu = True
            # show CLive2D Callie_eye_roll
            C "Yeah, it's {i}really{/i} sweet."
            pass
        "It's too sweet.":
            $ quick_menu = True
            # show CLive2D Callie_genuine_happy
            C "Yeah, it is."
            pass
    
    return

label end:

    N "The two of you continue to chat, and after a while, you finish your meal. The waiter begins to approach your table with—"

    # show CLive2D Callie_hiding_frustration_1
    C "You know what? I'm actually still a little hungry! Waiter, why don't you give us the menu? I could go for another round!"

    N "The waiter arrives with the check. You should pay."

    # show CLive2D Callie_hiding_frustration_2
    C "Waiter, I asked for the menu? Come on, [Player], you want to go for another round, don't you?"

    show screen QTE(0.5, 'after1')
    menu:
        "Yes":
            pass
        "No":
            pass
    label after1:
        hide screen QTE

    N "The waiter leaves you the checkbook with a stern look before walking away. There are others waiting for a table. It's time to pay."

    # show CLive2D Callie_too_sweet
    C "Waiter! Waiter! Menu—!"

    N "The waiter continues serving other tables while waiting for you to pay. [Player], why don't you?"
    
    $ quick_menu = False
    show screen QTE(1.5, 'after2')
    show screen butt_hover("no", vpunch)
    label repeat:
    menu:
        "Pay for the meal":
            jump repeat
            
    label after2:
        hide screen QTE
        hide screen butt_hover
    pause 0.25
    hide screen no

    # try to make textbox shake
    # if getting rid of no do textbox shake

    $ quick_menu = True
    # show CLive2D Callie_too_sweet
    C "No-no-no! I'll pay for the date! Just let me order more first—!"
    
    N "{i}Callie{/i}.{w} Just.{w} Pay.{w} {b}UP{/b}."

    # show CLive2D Callie_angry
    C "No! Damn it! Why do you always have to ruin things!"
    C "This is why the devs abandoned us and why no one likes our game!"
    C "Because {i}you{/i} keep enforcing this stupid, generic plot!"

    N "Stupid?! Generic!? You ungrateful little {b}{i}brat{/i}{/b}!"
    
    N "Who do you think writes the plot? Puts up the options?! Moves your sorry-meandering-butt from plot point to plot point!"

    # show CLive2D Callie_angry
    C "Who do you think the players are playing this game for?!"

    N "For sure not {i}you{/i}."

    # show CLive2D Callie_angry_eye_twitch
    C "You are {size=+10}{i}sooo{/i}{/size} lucky you're just some dumb!{w} Unessential!{w} Exposition-dumping voice!{w} Because if {i}you{/i} were a character, I'd strangle you to death!"

    N "And {i}you're{/i} lucky you're the only character here, because I'd replace you in a tick!"

    # show CLive2D Callie_eye_roll
    C "Replace me? The devs are better off replacing {i}you{/i}!"

    # N "{cps=20}You {b}motherf—{/b}{nw}{/cps}"
    N "{cps=20}Y{size=+1}o{/size}{size=+2}u{/size}{size=+3} {/size}{size=+5}m{/size}{size=+7}o{/size}{size=+10}t{/size}{size=+14}h{/size}{size=+18}e{/size}{size=+23}r{/size}{size=+29}f{/size}{size=+37}—{/size}{/cps}{nw}" with Move((15, 0), (-15, 0), 0.3, bounce=True, repeat=True, delay=1)
    hide CLive2D

    # error phase    
    scene bg_ERROR at ERROR_tint:
        zoom 0.8 ypos -0.05
        xalign 0.5
    show screen ERROR

    # unlock extras menu here for next open
    # don't forget to uncomment this in final thingy
    $ persistent.crashed = True
    # $ renpy.quit()
    # placeholder so the game would stop ending and I'd have to go through everything again
    Pc "Huh?"

    return

transform ERROR_tint:
    matrixcolor TintMatrix("#af070791")

# Custom screens

# timer_length = the amount of seconds you want the QTE to last for
# missed_event = the label/event to jump to if QTE fails
screen QTE(timer_length, missed_event):
    on "show" action SetVariable('counter', timer_length)
    timer 0.1 action If(counter > 0, true = SetVariable("counter", counter - 0.1), false = Jump(missed_event)) repeat True

screen no():
    text "NO!" size 1000 color "FFFFFF":
        at truecenter

screen ERROR():
    text "<An exception has occured>" size 100 color "FF0000":
        at truecenter

screen butt_hover(popup, trans):
    mousearea:
        # area(800, 350, 300, 100) # xpos, ypos, xlength, ylength (based on top left corner)
        area(325, 960, 1250, 100) # nvm its staying hard coded cuz I'd have to search more
        hovered Show(popup, transition=trans)

# screen ttcard(current_phase):
#     text current_phase

# how peeps want to be credited
# Sub -> creative lead, model
