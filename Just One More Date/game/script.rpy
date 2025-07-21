define C = Character("Callie", color = "#D02F3C") # what color for Callie's name?
define N = Character("Narrator", namebox_xalign = 0.60) # what color for narrator's name?
define Pc = Character("[Player]") # what color for player's name?
image CLive2D = Live2D("resources/Callie", default_fade=0.0, loop=True)
image bgframe1 = "resources/cafe-bg-1.png"
image bgframe2 = "resources/cafe-bg-2.png"
define lookaround = Move((0, 0), (-65, 0), 2, bounce=True, repeat=True, delay=2)
default persistent.crashed = False
default shake_textbox = False
default preferences.text_cps = 20

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
    call ERROR_end
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

    play music "audio/Einspanner.mp3" volume 0.025

    show CLive2D normal with moveinright:
        ypos 0.1

    show CLive2D normal_talking
    $ quick_menu = True
    play sound "C1p1.wav" noloop volume 1
    C "Ohmygosh! "
    play sound "C1p2.wav" noloop volume 1
    extend "I'm {i}so{/i}, so sorry for being late! I just—{nw=1}"
    show CLive2D nervous_talking nervous_normal
    pause 1.0
    show CLive2D normal_talking
    play sound "C1p3.wav" noloop volume 1
    C "—traffic, you know? Anyways, thanks for waiting! Did you order yet?"
    show CLive2D normal
    $ quick_menu = False
    stop sound # including all of these for people who skip text so it doesn't end up overlapping with future sounds
    menu:
        "No.":
            pass
        "I was just about to.":
            pass
        "I was waiting for you.":
            pass
    $ quick_menu = True

    show CLive2D too_sweet_start
    pause 1
    # maybe redo: this one sounds a bit crunchy, like you can hear the sheets for both versions...
    show CLive2D too_sweet_talking
    play sound "C2.wav" noloop
    # va says "for your meal" instead of "the meal"
    C "{cps=25}Oh, really? If that's the case, why don't I cover the meal then? On the house! As an apology for being late!"
    show CLive2D normal
    stop sound
    menu:
        "Sure.":
            show CLive2D normal_talking
            play sound "C3.wav" noloop volume 2
            C "Great! Waiter! Yoohoo! Menu please!"
            jump c1
        "It's alright, I got it.":
            pass
        "We can split.":
            pass
    $ quick_menu = True

    show CLive2D normal_talking
    play sound "C4.wav" noloop
    C "No! I insist! Waiter! Yoohoo! Menu, please!"

    label c1:
    stop sound
    show CLive2D normal
    N "You peruse the menu and all its overly decadent offerings. This sweets cafe sure is on the pricey side. $38 for a slice of cake?! Ridiculous! Who in their right mind would order from here?!"

    show CLive2D normal_talking
    play sound "C5p1.wav" noloop
    queue sound "C5p2.wav" noloop
    C "{cps=30}I'll have the Poppin' Pomegranate Parfait! And—oh, wait. [Player], why don't you order first? It's on my card!"
    show CLive2D too_sweet_start too_sweet_normal normal

    $ quick_menu = False
    stop sound
    menu:
        "Any recommendations?":
            $ quick_menu = True
            show CLive2D normal_talking
            play sound "C6.wav" noloop
            # va says "bowl is so" instead of "bowl makes it so"
            C "{cps=40}Their Four Seasons Lotus Bowl makes it {i}so{/i} worth the visit!{cps=35} I always stay for more."
            show CLive2D normal
            stop sound
            Pc "I'll take the:"
            $ quick_menu = False
            menu:
                "Ambrosial Delight.":
                    $ food = "Ambrosial Delight"
                    show CLive2D normal
                "Four Seasons Lotus Bowl.":
                    $ food = "Four Seasons Lotus Bowl"
                    show CLive2D genuine_happy_start normal
        "I'll have the Ambrosial Delight.":
            $ food = "Ambrosial Delight"
            show CLive2D normal
    $ quick_menu = True
    N "The waiter leaves after taking your orders. You have some time to yourselves. What do you want to talk about?"
    $ quick_menu = False
    menu:
        "What are your hobbies?":
            show CLive2D surprised normal
            play sound "C7p1.wav" noloop
            C "{cps=30}Hobbies? {nw=1}"
            pass
        "What do you like to do in your free time?":
            C "{nw}"
            pass
    $ quick_menu = True

    show CLive2D nervous_start nervous_talking_long
    play sound "C7p2.wav" noloop
    queue sound "C7p3.wav" noloop
    extend "{cps=30}I like to play video games in my free time. How about you? What do you play?"
    show CLive2D nervous_normal normal
    $ quick_menu = False
    stop sound
    menu:
        "Action":
            $ genre = "Action"
        "Strategy":
            $ genre = "Strategy"
        "Casual":
            $ genre = "Casual"
    $ quick_menu = True
    show CLive2D too_sweet_start too_sweet_talking
    play sound "C8forgot.wav" noloop
    C "Really?! Me too!"

    # first time our character says actual lines :O
    show CLive2D too_sweet_normal normal
    stop sound
    Pc "What do you like about [genre.lower()] games?"

    show CLive2D nervous_start nervous_talking_long
    # maybe redo: sounds like it has other bumpy sounds
    play sound "C8p1.wav" noloop
    queue sound "C8p2.wav" noloop
    queue sound "C8p3.wav" noloop
    # va says "those" instead of the "genre" and "you're just so, you know" instead of "you're just, you know"
    C "Oh…! I really like the—um—I'm sorry! I don't actually like [genre.lower()] games! I just didn't know what else to say! I didn't leave a good impression since I was late, but you're just, you know, so—!"

    # show CLive2D Callie_nervous_at_reader - we don't have that / not in the technical script
    play sound "C8p4.wav" noloop
    # va says "wanted" instead of "want"
    C "—cute! And I {i}really{/i}, really want you to like me!"

    show CLive2D nervous
    stop sound
    $ quick_menu = False
    menu:
        "I get that, I also get nervous on first dates.":
            show CLive2D genuine_happy_start genuine_happy_normal normal
            pass
        "Don't sweat it.":
            show CLive2D nervous_start nervous_normal normal
            pass
        "We'll see.":
            show CLive2D nervous_start nervous_normal too_sweet_start too_sweet_normal normal
            pause 2
            pass
    pause 2
    $ quick_menu = True
    show CLive2D normal
    N "The waiter arrives with your food and whips the cover off to reveal glistening towers of fruit and shining caramel."
    N "The sparkling glassware gleams with condensation as they're set down before you. "
    show CLive2D annoyed_at_narrator annoyed_normal normal 
    extend "Both of you salivate at the sight."

    Pc "So, what do you actually like?"

    show CLive2D too_sweet_start too_sweet_talking
    play sound "C9.wav" noloop
    C "Oh! I like knitting!"

    show CLive2D too_sweet_normal normal
    stop sound
    N "Callie pulls the bag of materials from her purse."


    show CLive2D sardonic_start sardonic_talking 
    play sound "C10p1.wav" noloop
    # va says "kept undoing my stitches" instead of "keep having to undo"
    C "{cps=30}I've knitted for ages, but I keep having to undo my stitches because I've got a {i}pet{/i}—"
    show CLive2D hiding_frustration_start hiding_frustration_talking
    play sound "C10p2.wav" noloop
    extend "who keeps {i}interrupting{/i}"
    show CLive2D hiding_frustration_normal normal_bombastic_side_eye normal_talking
    extend "{nw=2}"
    play sound "C10p3.wav" noloop
    extend " me{nw=1}"
    play sound "C10p4.wav" noloop
    extend " when I'm so close to finishing."
    show CLive2D normal

    stop sound
    N "She seems to be having a rough patch. Let's get this date back on track. Why don't you ask her something?"
    show CLive2D surprised nervous_start nervous
    extend " Like, say, what's her favorite thing to knit?"
    show CLive2D too_sweet_start too_sweet_normal normal
    $ quick_menu = False
    menu:
        "What's your favorite thing to knit?":
            $ quick_menu = True
            # show CLive2D Callie_annoyed
            show CLive2D annoyed_start annoyed_normal normal
            play sound "C11p1.wav" noloop
            C "You—!"
            # show CLive2D Callie_too_sweet
            show CLive2D too_sweet_start too_sweet_talking
            play sound "C11p2.wav" noloop
            C "I like knitting—"
            # show CLive2D Callie_nervous
            show CLive2D nervous_start nervous_normal too_sweet_start too_sweet_talking
            # maybe redo: not sure if the way flowers is pronounced matches
            play sound "C11p3.wav" noloop
            extend "flowers! "
            play sound "C11p4.wav" noloop
            extend "But enough about me! How are you liking the cafe?"
            show CLive2D too_sweet_normal normal
            $ quick_menu = False
            stop sound
            menu:
                "I like it.":
                    show CLive2D too_sweet_start too_sweet_talking
                    play sound "C12c1.wav" noloop
                    $ quick_menu = True
                    C "Oh? Me too!"
                    show CLive2D too_sweet_normal normal
                    pass
                "It's kind of bland.":
                    show CLive2D genuine_happy_start genuine_happy_talking
                    play sound "C12c2p1.wav" noloop
                    queue sound "C12c2p2.wav" noloop
                    $ quick_menu = True
                    C "Yeah, it is."
                    show CLive2D genuine_happy_normal normal
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
    stop sound
    show CLive2D sardonic_start sardonic_talking
    play sound "C13p1.wav" noloop
    # maybe redo: has some click sound in the bg near beginning, also it doesn't match with the sooo often.
    # va says "that I practically" instead of "I practically", "this place has" instead of "this place is", "the menu" instead of "and the menu"
    # I can't tell if the sigh is intentional so I'm keeping it in
    C "{cps=30}I come here {i}sooo{/i} often, I practically live here. This place is always the same every time I visit. "
    play sound "C13p2.wav" noloop
    C "{cps=30}{w=2}The waiter's been here since day one, and the menu hasn't changed in ages. It's—"

    show CLive2D annoyed_at_narrator
    stop sound
    N "A loud crash echoes from the kitchen." with vpunch

    # show CLive2D Callie_annoyed_at_narrator
    show CLive2D annoyed_start annoyed_normal too_sweet_start too_sweet_talking
    if food == "Ambrosial Delight":
        play sound "C14c1.wav" noloop
    elif food == "Four Seasons Lotus Bowl":
        play sound "C14c2.wav" noloop
    C "—comforting! I love this place! Best sweets in the area. Their [food] is just so flavorful!"

    show CLive2D too_sweet_normal normal
    stop sound
    N "Callie takes a BIG bite of her Poppin' Pomegranate Parfait."

    show CLive2D hiding_frustration_start hiding_frustration_talking
    play sound "C15p1.wav" noloop
    queue sound "C15p2.wav" noloop
    C "{cps=10}Mmmm! It's {i}sooo{/i} good! {nw=1}"
    queue sound "C15p3.wav" noloop
    extend "{cps=20}How about your food, [Player]? Do you like yours?"
    show CLive2D hiding_frustration_normal normal

    $ quick_menu = False
    stop sound
    menu:
        "It's really sweet.":
            $ quick_menu = True
            show CLive2D normal_eyeroll_talking
            play sound "C16c1.wav" noloop
            C "Yeah, it's {i}really{/i} sweet."
            show CLive2D normal
            pass
        "It's too sweet.":
            $ quick_menu = True
            show CLive2D genuine_happy_start genuine_happy_talking
            play sound "Yeah.wav" noloop
            C "Yeah, it is."
            show CLive2D genuine_happy_normal normal
            pass
    stop sound
    return

label end:
    N "The two of you continue to chat, and after a while, you finish your meal. The waiter begins to approach your table with—"

    show CLive2D hiding_frustration_start hiding_frustration_talking
    # play sound "C17_old.wav" noloop
    play sound "C17p1.wav" noloop
    queue sound "C17p2.wav" noloop
    queue sound "C17p3.wav" noloop
    C "You know what? I'm actually still a little hungry! Waiter, why don't you give us the menu? I could go for another round!"

    show CLive2D hiding_frustration_normal normal
    stop sound
    N "The waiter arrives with the check. You should pay."

    show CLive2D hiding_frustration_start hiding_frustration_talking
    play sound "C18p1.wav" noloop
    queue sound "C18p2.wav" noloop
    C "Waiter, {nw=0.5}"
    extend "I asked for the menu? {nw=0.5}"
    extend "Come on, [Player], you want to go for another round, don't you?"
    stop sound
    show CLive2D hiding_frustration_normal normal
    show screen QTE(0.5, 'after1')
    menu:
        "Yes":
            pass
        "No":
            pass
    label after1:
        hide screen QTE

    N "The waiter leaves you the checkbook with a stern look before walking away. There are others waiting for a table. It's time to pay."

    show CLive2D too_sweet_start too_sweet_talking
    play sound "C19.wav" noloop
    C "{cps=10}Waiter! Waiter! Menu—!"

    show CLive2D too_sweet_normal normal
    stop sound
    N "The waiter continues serving other tables while waiting for you to pay. [Player], why don't you?"
    
    $ quick_menu = False
    show screen QTE(1.5, 'after2')
    # show screen butt_hover("no", vpunch)
    label repeat:
    menu:
        "Pay for the meal":
            jump repeat
            
    label after2:
        hide screen QTE
        # hide screen butt_hover
    pause 0.25
    # hide screen no

    # try to make textbox shake
    # if getting rid of "no" do textbox shake

    $ quick_menu = True

    show CLive2D nervous_start nervous_talking
    $ shake_textbox = True
    C "NO!"
    $ shake_textbox = False
    show CLive2D nervous_normal normal too_sweet_start too_sweet_talking
    play sound "C20.wav" noloop
    C "No-no-no! I'll pay for the date! Just let me order more first—!"
    
    show CLive2D too_sweet_normal normal
    stop sound
    $ shake_textbox = True
    hide screen quick_menu
    show screen quick_menu
    N "{i}Callie{/i}."
    hide screen quick_menu
    show screen quick_menu
    N "{i}Callie{/i}.{fast} Just."
    hide screen quick_menu
    show screen quick_menu
    N "{i}Callie{/i}. Just.{fast} Pay."
    hide screen quick_menu
    show screen quick_menu
    N "{i}Callie{/i}. Just. Pay.{fast} {b}UP{/b}."
    $ shake_textbox = False

    show CLive2D angry_start anger_talking
    # play sound "C21v1.wav" noloop
    # this one has a bump sound in it but I like this one more
    play sound "C21v2p1.wav" noloop
    # va says "keep ruining things" instead of "have to ruin things"
    C "No! Damn it! Why do you always have to ruin things!"
    play sound "C21v2p2.wav" noloop
    # va says "no one plays our game" instead of "no one likes our game"
    C "This is why the devs abandoned us and why no one likes our game!"
    play sound "C21v2p3.wav" noloop
    # va says "its because" instead of "because"
    C "Because {i}you{/i} keep enforcing this stupid, generic plot!"

    show CLive2D anger_no_talking
    stop sound
    N "Stupid?! Generic!? You ungrateful little {b}{i}brat!{/i}{/b}"
    
    N "Who do you think writes the plot? Puts up the options?! Moves your sorry-meandering-butt from plot point to plot point!"

    show CLive2D angry_start anger_talking
    play sound "C22.wav" noloop
    C "Who do you think the players are playing this game for?!"

    show CLive2D anger_no_talking
    stop sound
    N "For sure not {i}you{/i}."

    show CLive2D anger_talking
    play sound "C23p1.wav" noloop
    # va says "that you're just some" instead of "you're just some", "Exposition-dumpingening voice" instead of "Exposition-dumping voice", "I will strangle you" instead of "I'd strangle you"
    C "You are {size=+10}{i}sooo{/i}{/size} lucky you're just some dumb! "
    play sound "C23p2.wav" noloop
    extend "Unessential! "
    play sound "C23p3.wav" noloop
    extend "Exposition-dumping voice! "
    play sound "C23p4.wav" noloop
    extend "Because if {i}you{/i} were a character, I'd strangle you to death!"

    show CLive2D anger_no_talking
    stop sound
    N "And {i}you're{/i} lucky you're the only character here, because I'd replace you in a tick!"

    show CLive2D anger_talking_eyeroll anger_talking
    play sound "C24.wav" noloop
    C "Replace me? The devs are better off replacing {i}you!{/i}"
    stop sound

    $ shake_textbox = True
    N "{cps=20}Y{size=+1}o{/size}{size=+2}u{/size}{size=+3} {/size}{size=+5}m{/size}{size=+7}o{/size}{size=+10}t{/size}{size=+14}h{/size}{size=+18}e{/size}{size=+23}r{/size}{size=+29}f{/size}{size=+37}—{/size}{/cps}{nw}" with Move((15, 0), (-15, 0), 0.3, bounce=True, repeat=True, delay=1)
    $ shake_textbox = False
    hide CLive2D

    return

label ERROR_end:
    scene bg_ERROR at ERROR_tint:
        zoom 0.8 ypos -0.05
        xalign 0.5
    show screen ERROR
    show screen finalcrash

    # little callie glitch scene nah
    # $ i = 0
    # while i < 100:
    #     show CLive2D anger_talking
    #     pause 0.1
    #     $ i = i + 1
        
    # unlock extras menu here for next open
    # don't forget to uncomment this in final thingy
    $ persistent.crashed = True
    $ quick_menu = False
    $ renpy.pause(2, hard=True)
    $ renpy.quit()

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
    text "<An exception has occured>" size 100 color "FF0000" outlines [ (absolute(4), "#000000", absolute(0), absolute(0)) ]:
        at truecenter

screen butt_hover(popup, trans):
    mousearea:
        # area(800, 350, 300, 100) # xpos, ypos, xlength, ylength (based on top left corner)
        area(325, 960, 1250, 100) # nvm its staying hard coded cuz I'd have to search more
        hovered Show(popup, transition=trans)

screen finalcrash:
    add "gui/textbox.png" xalign 0.5 ypos 815