# GACHA SCRIPT HELP AAAAAAAAA
# Currently, I was hoping to reuse this script file again after each bachelor's endings so i don't have to copy and paste it again and again
# Ang suggestion is call_function (sabi ni mondi)
# Basta what happens is that when a bachelor is already chosen, they can no longer be chosen on for one playthrough

init python:
    import random
    import gacha
# default bachelor_choice = ["hiroshi","leo", "keiran", "soren", "mako"]

label gacha:

#    if not bachelor_choice:
#        jump return
    $ listLength = gacha.returnBachelorLength()
    if listLength != 0:
        $ pick = gacha.randomizeBachelor()
    else:
        $ print("All bachelors chosen.")
        # jump prologue_C

    # $ pick = randomizeBachelor()

    # if bachelor_choice == 0:
    #     $ print("All bachelors chosen.")
        # jump prologue_C

#    if bachelor choice == 1:
#        jump Day2Start


label prologue_C:

    mc "Shut the hell up... Just give it to me whatever, uhm— Mystery Sponsor."

    sponsor "Isn't it too late to be angsty? Let Bygonessssss-"

    sponsor "Beeeeeeeeeeee-"

    "The screen of my monitor glitches with the fish mascot gone in it, tabs that were once open are now closed."

    mc "Woah!"

    scene monitor glitch

    # BG: Screen of monitor glitching

    "My background wallpaper glitches intensely. Then I see a glimpse of the box manifesting itself in reality."

    mc "“Oh great, of course you're ruining my desktop for this gimmick.”"

    sponsor "Now, check it for yourself."

    mc "?!"

    mc "!!!"

    mc "AH!"

    "The fish in the corporate wear is right behind me who is now manifested tangibly in reality."

    sponsor "Stop being jumpy! I am what I look, did you expect anything else?"

    sponsor "Inspect while you're at it! Tell me how it looks."

    "It's a fish. Just like what it looks like in real life. Except for that loose corporate clothing."

    show kissaboo box

    #   OS: KISS-A-BOO BOX  

    mc "Don't do anything surprising while I'm at it."

    "I'm inspecting the box. It has cute elements plastered around it. Something I'm really fond of."

    "Like it was made for me. Even tapping the box, the sound it makes is music to my ears too." 

    mc "This feels too good to be true..."

    "I noticed the name of the collection. It says here \"Kiss-a-boo\"."

    mc "Kiss-a-boo? Really? What kind of a lame ass branding is that?"

    sponsor "Come on, it's free! I gave you one for free!"

    mc "Suppose, you're right."

    hide kissaboo box

    "Though you disrupted my {i}Catty MariMari{/i} transaction..."

    "Which I'll never forgive unless you give me your entire collection then I'd consider forgiving you."

    "Can I see the rest maybe?"

    "The manner this entity gasps made me look like I committed a cardinal sin."

    "Which is not true because I just asked a question."

    "A very simple question! Mind you!"

    sponsor "Greediness! The sickness of humanity! Oh! Spare me!"

    sponsor "One is enough but all? Oh, how much abundance does humanity ask for!"

    mc "Come on,it's a simple request.I want them all!"

    sponsor "Greedinessssssssssssssssssssssssssssss. That's twice already, shame on you!"

    sponsor "You have too much,already! Use your eyes and look around! HMMP!"

    mc "Okay! Forget I said anything..."

    "Now for the actual product, the figurine that Mystery Sponsor has promised me."
    
    jump expression pick

    label mako:
        jump mako_D0_A

    label hiroshi:
        jump hiro_D0_A

    label soren:
        jump soren_D0_A

    label leo:
        jump leo_D0_A
    
    label keiran:
        jump keiran_D0_A



# $ bachelor_choice = renpy.random.choice(['sixto', 'hiroshi', 'leo', 'keiran', 'mako', 'soren', 'lucas'])
# $
#if bachelor_choice == 'sixto':
#elif bachelor_choice == 'hiroshi':
#elif bachelor_choice == 'leo':
#elif bachelor_choice == 'keiran':
#elif bachelor_choice == 'mako':
#elif bachelor_choice == 'soren':
#elif bachelor_choice == 'lucas':

#  THIS IS FOR THE PROLOGUE FIRST BITCHELOR
#  $ bachelor_chosen =  jump = back to prologue
