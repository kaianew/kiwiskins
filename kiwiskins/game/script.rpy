# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define kaia = Character("Kaia")
define athan = Character("Athan")

image kaia happy = "images/kaia.png"
image athan sad = "images/athan.png"
image kaia sad = "images/sad_kaia.png"
image athan happy = "images/happy_athan.png"
image npc = "images/datboi.png"

image library = "images/library_better.png"
image bedroom = "images/bedroom.png"
image cafeteria = "images/cafeteria_bright.png"
image hallway = "images/hallway_better.png"


# The game starts here.

label start:

    centered "You’ve just moved to an academy in the middle of the foggy, mossy woods of Spoons, Washington. In the last year, your parents got divorced and 
    neither of them are willing to help you with your college bills anymore. You’re financially all on your own for the last year of your poetry degree in 18th century arcane poetry. 
    With a bit of elbow grease, and a lot of luck, you managed to persuade the dean to let all of your credits transfer and lock in a great merit scholarship. The scholarly resources 
    available here are…low caliber, to say the least." with dissolve

    centered "Your best friend, who you met on rumblr.com, messages you just as you’re pulling on your rain jacket to attend your first day of your last year at 
    St. Evangeline of Death University." with dissolve

    scene bedroom

    "FIXME: add chatroom dialogue"

    "!? poliwag98 lives in Spoons? You knew they lived in the PNW, but you never thought you’d be moving to the same city as them."
    
    "You hesitate to tell them, since they used to be strict on never sharing parts of your identities a year ago, when you didn’t know each other well yet. 
    They’ve had a few experiences that made them more wary about online contacts."
    
    "Over the months, they’ve opened up and told you about their hobbies, such as sewing and impressionist art, but you don’t want to endanger such an 
    important friendship by breaking the secrecy just yet."

    "FIXME: finish chatroom dialogue"

    scene hallway with dissolve

    "You've arrived at St. Evangeline midway through the day, and it already seems like someone wants to talk to you."

    show npc
    "Edward" "Hey, welcome to St. Evangeline! I haven't seen you around -- do you want to get lunch? I'm the student body president, so it's my job to make sure everyone feels at home
    here."

    "He puffs out his chest, seeming to take pride in the role."
    
    menu:
        "Get lunch with Edward and his friends.":
            jump ed_lunch
        "Skip lunch. You need some time to relax and find your classrooms!":
            jump no_lunch

label ed_lunch:
    # -NRG
    "Edward beams, gesturing in the direction of the cafeteria."
    "Edward" "Great! I'll show you to our regular table."

    scene cafeteria_bright with dissolve
    show npc

    "You enjoy a nice bowl of noodles with your new pals. The friendly chatter of Edward and all his friends lightens your mood slightly."
    jump after_school

label no_lunch:
    "Edward looks a little sad, scratching the back of his head."
    "Edward" "Well, seeya, I guess. Let us know if you want to hang out later!"
    "Edward cracks a sideways, only slightly dampened smile. He waves, scuffling off to the cafeteria."
    jump after_school

label after_school:
    scene library with dissolve
    return