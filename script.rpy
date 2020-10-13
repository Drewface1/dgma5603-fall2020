# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define r = Character("Shion")
define g = Character("Sue", color = "#908bf6")
define y = Character("You")

transform bottomleft:
    xalign 0.0
    yalign 0.2

transform bottomcenter:
    xalign 0.5
    yalign 0.4

transform bottomright:
    xalign 0.5
    yalign 0.7

transform lower:
    xalign 0.5
    yalign 0.1
transform lowerright:
    xalign 0.9
    yalign -0.9

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room morning

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    "You are fast asleep in your warm bed."

    "The light from the morning sun shines through the windows of the room."

    "As you adjust yourself to get more confortable, you start hearing a voice calling to you."

    r "Hey."

    "You think nothing of it and continue to sleep."

    r "Heeyyy."

    "You hear it again, but pay it no mind."

    r "HHHEEEEEYYYYY, WAKE UP!!"

    "You wake up startled to find your friend Reena staring at you."

    show shion neutral01 at bottomcenter with Dissolve(0.50)

    r "Good morning."

    show shion neutral01 at bottomcenter with dissolve

    r "..."

    show shion angry02 at bottomcenter with Dissolve(0.25)

    r "Hey Wake Up!"

    show shion angry01

    r "Geez, finally your awake."

    r "I have been trying to call you all morning!"

    show shion angry01 at bottomcenter

    r "Did you forget that we have a job we need to do today?"

    y "We do?"

    show shion angry02 at bottomcenter

    r "Yes, We got a job get rid of a moster that has been seen in some ruins."

    show shion neutral01 at bottomcenter

    menu:
     "Remember about the job?":
         y "Oh yeah, sorry about that."
         y "Hold on let me get changed an ill meet you outside."

         jump Job


     "Go back to sleep?":
         "You go back to bed"

         jump Bed


label Job:
    scene bg forest

    "You and Reena make your way into a forest"

    show shion smile01 at bottomcenter

    r "Finally we made it, now the ruins should be just beyond these woods."

    "You are rubbing your eyes, looking like you want to go back to take a nap"

    r "..."

    show shion suspicious01 at bottomcenter
    show shion angry01 with Dissolve(0.25)

    r "Hey! Do not go falling asleep on me."

    r "We are already behind schedule because of you!"

    y "I said I was sorry."

    show shion neutral02 with Dissolve(0.25)

    y "Besides, it is not like the monster is going any where."

    show shion suspicious01

    r "I know, but I have other things to do today."

    r "So lets get going!"

    scene bg forest ruins

    "You and Shion arrive at the ruins. At first you do not see anything odd."

    show shion suspicious01 at bottomcenter with Dissolve(0.50)

    r "Start looking for this monster, it has to be somewhere."

    scene bg forest ruins

    "You look around and you come across a small child crying behind a fallen pillar."

    "When you get closer you notice that there is something off about her."

    y "Are You Ok?"

    "Her head pops up and turns to look at you, then you get a good look."

    show sue frown at lower with Dissolve(0.75)

    g "Who..."

    g "Who...are you?"

    y "I am *****."

    y "And who are you?"

    g "Im....S..Sue."

    y "I was hired to take care of the monster that has been seen in these ruins."

    show sue talk at lower with Dissolve(0.75)

    g "Really?"

    g "But, I have not seen any monsters around here lately."

    "Hmm"

    r "Hey *****! Find anything?"

    show sue sad frown at lowerright with Dissolve(0.25)

    g "Who is that?"

    show shion suspicious02 at bottomleft with Dissolve(0.50)

    r "Who are you talking to?"

    r "Who is that?"

    y "This is Sue, she is a ghost."

    r "Ahhh, ***** That is the monster we are looking for."

    y "What? But she is just a little girl."

    show shion angry02 at bottomleft with Dissolve(0.30)

    r "She is still a monster, and we were hired to take care of her."

    g "But I have not harmed anyone in my after life!"

    r "We cannot let her go, we need to eliminate her right now!"

    y "But she does not look like she would harm a fly."

    r "Still we were hired to take care of the monster problem here. Either you take care of her or I will."

    y "Okay."

    menu:
        "Take care of her?":
            y "I am sorry, Shion."

            jump destroy

        "Take CARE of her?":
            y "Wait Shion!"

            jump care

    scene bg room morning

    return

label Bed:

    show shion angry02

    r "Seriuosly!?!?! You know what?"

    scene bg fire

    r "FIREBALL!"

    "Shion launches a fire ball at you as you lay in bed, setting your whole room up on fire!"

    "Shion leaves your house in a huff!"

    # These display lines of dialogue.

    # This ends the game.

    return

label destroy:

    scene bg forest ruins

    show sue sad frown at lowerright
    show shion suspicious02 at bottomleft

    show shion angry01 at bottomcenter with Dissolve(0.25)
    show shion angry02 at bottomcenter with Dissolve(0.50)

    r "Sorry little one."

    r "FIREBALL!"

    return

label care:

    scene bg forest ruins

    show sue sad frown at lowerright
    show shion angry01 at bottomleft

    y "You said that we were hired to take care of the monster problem, right?"

    r "Right?"

    y "Sue, would you like to come stay with me?"

    r "What! *****."

    y "What is the matter? If we take her away from this place the job will be completed."

    y "And no one will get hurt."

    r "..."

    show shion sad01 at bottomleft with Dissolve(0.10)

    r "Fine, but she will be your responsablitly! Not mine."

    y "Fair enough, Sue what do you say?"

    show sue talk at lowerright

    g "Really?"

    y "Yep."

    show sue smile

    g "Yes please! Thank You so much!"

    show shion smirk01 at bottomleft

    g "I will do my best to repay you for this."

    y "I look forward to it."

    return
