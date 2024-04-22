# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define kaia = Character("Kaia")
define athan = Character("Athan")

image kaia happy = "images/kaia.png"
image athan pissed = "images/athan.png"

image library = "images/library.png"
image bedroom = "images/bedroom.png"
image cafeteria = "images/cafeteria.png"
image hallway = "images/hallway.png"


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene library

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show kaia happy
    # These display lines of dialogue.

    kaia "Wow, welcome to our vampire visual novel."

    kaia "This is fucking awesome!!"

    scene bedroom with dissolve

    show kaia happy

    kaia "Now I'm over here! The future is now."


    # This ends the game.

    return
