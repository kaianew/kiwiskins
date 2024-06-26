﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define kaia = Character("Kaia")
define athan = Character("Athan")

image kaia happy = "images/kaia.png"
image athan sad = "images/athan.png"
image kaia sad = "images/sad_kaia.png"
image athan happy = "images/happy_athan.png"
image npc = "images/datboi.png"

image chat 1 = "images/chat_reveal.png"
image chat 1_1 = "images/chat_finish.png"

image chat 2 = "images/nightchat_begin.png"
image chat 2_1 = "images/chat2_1.png"
image chat 2_2 = "images/chat2_2.png"
image chat 2_3 = "images/chat2_3.png"


define nrg_string = "images/energy_bar/2.png"
define nrg = 2

init python:
    def energy_change(nrg, up):
        temp_string = ""
        if up:
            if nrg == 3:
                return nrg_string
            nrg += 1
            temp_string = "images/energy_bar/" + str(nrg) + ".png"
            return temp_string
        else:
            if nrg == 0:
                # FIXME: in the future, consider adding behavior that automatically sends you home here
                return nrg_string
            nrg -= 1
            temp_string = "images/energy_bar/" + str(nrg) + ".png"
            return temp_string

image library morning = "images/bgs_resized/library_morning.jpg"
image library twilight = "images/bgs_resized/library_twilight.jpg"
image library night = "images/bgs_resized/library_night.jpg"
image library midnight = "images/bgs_resized/library_midnight.jpg"
image bedroom = "images/bgs_resized/bedroom.jpg"
image cafeteria night = "images/bgs_resized/cafeteria_night.jpg"
image cafeteria special = "images/bgs_resized/cafeteria_special.jpg"
image hallway day = "images/bgs_resized/hallway_day.jpg"
image hallway night = "images/bgs_resized/hallway_night.jpg"

transform upper_left:
    xalign 0.05
    yalign 0.05


# The game starts here.

label start:

    centered "You’ve just moved to an academy in the middle of the foggy, mossy woods of Spoons, Washington. In the last year, your parents got divorced and 
    neither of them are willing to help you with your college bills anymore. You’re financially all on your own for the last year of your poetry degree in 18th century arcane poetry. 
    With a bit of elbow grease, and a lot of luck, you managed to persuade the dean to let all of your credits transfer and lock in a great merit scholarship. The scholarly resources 
    available here are…low caliber, to say the least." with dissolve

    scene bedroom with dissolve
    show image [nrg_string] at upper_left
    "Your best friend, who you met on rumblr.com, messages you just as you’re pulling on your rain jacket to attend your first day of your last year at 
    St. Evangeline of Death University."

    scene chat 1 with dissolve

    "!? poliwag98 lives in Spoons? You knew they lived in the PNW, but you never thought you’d be moving to the same city as them."

    scene bedroom
    show image [nrg_string] at upper_left
    
    "You hesitate to tell them, since they used to be strict on never sharing parts of your identities a year ago, when you didn’t know each other well yet. 
    They’ve had a few experiences that made them more wary about online contacts."
    
    "Over the months, they’ve opened up and told you about their hobbies, such as sewing and impressionist art, but you don’t want to endanger such an 
    important friendship by breaking the secrecy just yet."

    scene chat 1_1

    "You'll try to keep it a secret for now. With a sigh, you close your laptop and head out into the fray."

    scene hallway day with dissolve
    show image [nrg_string] at upper_left

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
    $ nrg_string = energy_change(nrg, 0)
    show image [nrg_string] at upper_left
    "Edward beams, gesturing in the direction of the cafeteria."
    "Edward" "Great! I'll show you to our regular table."

    scene cafeteria special with dissolve
    show image [nrg_string] at upper_left
    show npc

    "You enjoy a nice bowl of noodles with your new pals. The friendly chatter of Edward and all his friends lightens your mood slightly."
    jump after_school

label no_lunch:
    "Edward looks a little sad, scratching the back of his head."
    "Edward" "Well, seeya, I guess. Let us know if you want to hang out later!"
    "Edward cracks a sideways, only slightly dampened smile. He waves, scuffling off to the cafeteria."
    jump after_school

label after_school:
    scene library twilight with dissolve
    show image [nrg_string] at upper_left

    "You're in the school's library, mulling over the day. Your classes were enriching. You were right to come here; your class on Emily Dickinson is enthralling."
    "But, despite all this, you've had a thought in the back of your head that's been getting louder and louder: you really do want to know who poliwag98 is. They're your best friend!"
    "You'll never get a better chance to find out who they are, you reason. You can use this scholastic year to gather information on who poliwag98 is, and gently reveal your identity
    to them when the time is right."

    "You have some time to talk to others in the library. What do you do?"
    show kaia happy
    show athan sad 

    menu:
        "Talk to the black-haired man with the tattoo.":
            jump athan_talk
        "Talk to the blond-haired man with the sweater.":
            jump kaia_talk
        "Go home. It's been a long day, and you can probably gather more information about poliwag98 by talking to them over AIM.":
            jump home_chat

label athan_talk:
    hide kaia happy
    "The tattooed man is gaming at his laptop, giant black headphones covering his ears. He has dark circles underneath his eyes and scowls as a \"Game Over\" message flickers across his screen."
    "You tap his shoulder, feeling brave."
    "You" "Sorry for your loss. What are you up to?"

    "The man still looks grumpy, but you don't {i}think{/i} it's because of you bothering him..."
    athan "Hey, you're the new student, right? I'm Athan. I do engineering, and stuff. I'm gaming -- just {i}super{/i} tired from staying up all day working."
    "He groans long-sufferingly, ruffling a hand through his fluffy hair."
    athan "I mean, come on. With a population of over 26\% vampires at St. Evangeline, you think they would make some accommodations for us vampires so we don't have to work during the day.
    Seriously, I'm dying out here. With every ray of sunshine, I feel my soul shriveling up like a raisin."

    hide athan sad
    show athan happy

    "He flashes a smile at you, a fanged incisor poking out."
    athan "But that means I'm just getting hyped up now! I mean, I'm still worn down, but...agh. Sorry, you didn't ask about any of this. Do you want to play some {i}Call of The Wild 4{/i} with me?
    I haven't gotten the chance to try the couch co-op yet."

    menu:
        "You're so down. This looks like fun!":
            # -NRG
            $ nrg_string = energy_change(nrg, 0)
            show image [nrg_string] at upper_left
            jump athan_game
        "Eh, this isn't really your style. Politely decline.":
            jump end_athan
        "You'd like to, but you really want to go home and chat with poliwag98.":
            jump end_athan

label athan_game:
    "Athan looks super excited. He starts digging around in his backpack for another mouse."
    athan "Hang on, I have another mouse with really good haptics and stability in here. You're gonna love this!"
    scene library night
    # jump energy up because it's nighttime
    $ nrg_string = energy_change(nrg, 1)
    show image [nrg_string] at upper_left
    show athan happy
    "There are a few more mechanics than you can get used to in such a short time, but Athan looks happy to teach you how to play. You're excited to see him again!"
    jump home_after

label end_athan:
    "Athan doesn't seem phased by your rejection."
    athan "I get it, you got stuff to do at home. But hey, I'm always down to play a game with you, so just let me know!"
    jump home_chat

label kaia_talk:
    hide athan sad
    "The man is reading a book with half-moon glasses on. He looks deeply invested in the material."
    "Upon glancing up at you, he appears startled, sticking a thumb between the pages he was just reading."

    "Man With Cashmere Sweater" "Oh, I didn't notice you were here. What can I do for you?"

    "You look at the title of the book he’s reading: “Darts and Bobbins for Novices.” Luckily, you vaguely understand that these words are related to 
    sewing because of poliwag98's interest."

    "You" "I was just wondering what you were up to, since I need to take a break. Are you into sewing?"

    hide kaia happy
    show kaia sad

    "He appears a bit shy, being slow to respond."
    "Man With Cashmere Sweater" "I’m a bit of a newcomer to the hobby, to be frank. This is...my second time reading this book, and I still don’t understand some things."
    "He shakes his head, as if breaking out of a reverie."

    hide kaia sad
    show kaia happy

    kaia "Where are my manners? I should introduce myself. My name is Kaia. I'm a law student here at St. Evangeline."

    "You smile at the new information, giving your name in turn."

    menu:
        "It's natural that you're not an expert at sewing yet. Rome wasn't built in a day.":
            jump rome
        "I have some hobbies I'm bad at, but still, they make me happy.":
            jump happy_hobbies

label rome:
    "This reminds you of a poem by Percy Bysshe Shelley, \"To a Skylark.\""
    "\"{i}Hail to thee, blithe Spirit! /
Bird thou never wert, /
That from Heaven, or near it, /
Pourest thy full heart /
In profuse strains of unpremeditated art...{/i}\""
    jump finish_kaia_talk

label happy_hobbies:
    "This reminds you of a poem by Margaret Deland, \"The Old-Fashioned Garden.\""
    "\"{i}When day is done, and no more labor calls, /
With tranquil heart I pass my garden-wall: /
It is so old, so full of faults and flaws, /
It is so small,-- /
And yet it seems to me, as I amble by, /
A fairer garden ne'er lay 'neath the sky.{/i}\""
    jump finish_kaia_talk    

label finish_kaia_talk:
    "Kaia quirks a smile, seeming to enjoy your comment."

    hide kaia happy
    show kaia sad
    "Then, almost as a surprise to him, a yawn overtakes him."

    "You" "Oh, are you tired?"

    kaia "Yes, I regret, but it seems I need to retire...I mean, go home to sleep."
    "Kaia nods, indeed regretful, and starts packing up his things."

    "You" "Okay. I'll see you later?"
    "You're hopeful this isn't the last time you'll see Kaia."

    hide kaia sad
    show kaia happy
    kaia "Yes, of course!"
    "He smiles, genuine."
    kaia "I wouldn't want to leave you stranded here when you're new. It can get a little...paranormal."

    scene hallway night
    # + NRG for nighttime
    $ nrg_string = energy_change(nrg, 1)
    show image [nrg_string] at upper_left
    show kaia happy

    "Satisfied that you'll see him again, you pack up and walk with him to the bike rack, chatting about mundane things."
    jump home_after

label home_chat:
    # +NRG because nighttime
    $ nrg_string = energy_change(nrg, 1)
    scene bedroom with dissolve
    show image [nrg_string] at upper_left
    "You have some time before bed."
    menu:
        "Just go to bed. You want to get to tomorrow!":
            return
        "Take a warm bath.":
            jump take_bath
        "Talk to poliwag98 on the computer.":
            jump finish_home_chat

label take_bath:
    # +NRG
    $ nrg_string = energy_change(nrg, 1)
    show image [nrg_string] at upper_left
    "The warm water feels great after straining yourself studying today and the lavender-scented bubbles are soothing."
    return

label finish_home_chat:
    "You open up your computer to start a conversation."
    show chat 2 with dissolve

    "Honestly, you're not feeling great. You feel sniffly and tired. You must have eaten something with garlic in it recently."

    show chat 2_1

    "It being dark outside {i}is{/i} helping your headache, though."

    show chat 2_2

    "You’re a bit skeptical, because you don’t have daily weariness or feel stronger at night, and your parents never showed signs of vampirism.
    Maybe poliwag98 is just paranoid about it because of their own experiences? Still, you want to say something to stop them from worrying."

    show chat 2_3

    "Your reassurance seems to stop them from worrying for now, and they drop the topic."

    scene bedroom with dissolve 
    "Your conversation turns to other matters: a new visual novel which 
    seems to include elements of both poetry and artistic styles poliwag98 likes, joining both of your interests..."
    return

label home_after:
    scene bedroom with dissolve
    show image [nrg_string] at upper_left
    "TBD...."
    return