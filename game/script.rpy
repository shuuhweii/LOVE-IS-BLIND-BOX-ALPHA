
# MYSTERY SPONSOR SPRITES




# On screen imgs

image cattymarimarievent = "cattymarimarievent.png"
image cockroach = "cockroach.png"
image flying cockroach = "flyingcockroach.png"
image fan = "fan.png"

# CHARACTERS

define player = Character("Player")
define mc = Character("[name]")
define sponsor = Character("Mystery Sponsor")
define sixto = Character("Sixto")
define mako = Character("Mako")
define hiro = Character("Hiroshi")
define keiran = Character("Keiran")

label start:

    scene bg mcbedroom

    "{i}Click. Click. Click. Click.{/i}"

    "{i}Endless clicks.{/i}"

    scene bg desktopmonitor

    # Close shot of her desktop area. The website is shown on the monitor screen.

    "Nothing appears on the screen, I mean on the site, rather. It should be live now since a minute has passed already."

    "I can't afford to lose my spot, not when I already missed out on the 1st release of {i}Catty MariMari Series BlindBox Collection from the My Beloved Universe{/i} franchise." 

    "I refresh the site again."

    "Something is happening, but it's taking a while to load. Many in the queue are doing the same as me. Refreshing."

    "Fighting for a chance to spend their hard-earned money for novelty toys like this one. "

    scene bg 

    show cattymarimarievent

    # Catty MariMari Event image appears

    "The once usual menu of the site has now changed to their 2nd Chance Catty MariMari event. "

    "The website goes live."

    player "It's here..."

    "I breathe deeply, crack every bone of my body, warm muscles and center my focus."

    player "The bank is going to hate me for doing this but this is my dopamine boost they're stopping."

    player "Don't mess this up, self."

    "I'm holding the card, the last card I'm ever allowed to keep. My whole remaining savings are secured in this little rectangle..."

    "...and I'm about to spend it all on one blind box."

    player "Only ONE blindbox."

    player "Let's go-"

    "{i}Click.{/i}"

    "{i}Click.{/i}"

    "{i}Click?{/i}"

    "{i}Click? Click? Click?{/i}"

    "Nothing happened. I check my devices if they're working properly"

    "Oh, turns out."

    "My Mimiro wireless mouse just died. How convenient is that timing..."

    player "Fuck-I forgot to charge the battery!"

    player "Why does everything have to be fucking wireless when things are already working in the first place!!"

    hide cattymarimarievent

    "I was about to shove everything on top of my desk to look for wires, but the screen reminded me of the remaining hours of the sale."

    player "HhhhRRgg!"

    player "I don't have time to clean."

    "My hands hastily search. It's just mess after mess."

    player "Shit! Shit, shit!"

    player "The wire for this is usually here, ahhh the mess, the fucking mess! Show yourself already!"

    "As the search goes, I feel a crawling sensation."

    show cockroach

    # Cockroach appears

    "A cockroach appears next to my mouse."

    hide cockroach

    menu:
        "Choose"
        "Swat!":
            jump cockroach_swat
        "Look to your left.":
            jump cockroach_lookleft

label cockroach_swat:

    player "...Uhhhhhhhh! Stop ruining things for me! Shoo! Not when I'm already this close to acquiring it!"

    "With my might I swat the cockroach with my own hand."

    show flying cockroach

    # Cockroach flying

    "The roach jumps at me and clings on to my face."

    player "AHHHHHHHHHHHHHHHHHHHHHH!"

    player "GO AWAY! GO AWAY ! GO AWAY!"

    hide flying cockroach

    "I swat the cockroach off my face.  The  body falls to the ground. It's no longer moving but I'm still horrified."

    jump prologue_A

label cockroach_lookleft:

    player "I'm already dirty enough. No way I'm going to touch that cockroach."

    "I look to my left."

    show fan

    # Fan

    "There's my limited edition {i}Garbletz{/i} fan adorned with an {i}Alixer{/i} motif."

    player "Who am I kidding, this roach is cleaner than me. A simple soap can fix this."

    "I start fanning aggressively. The cockroach resists the wind and puts up a fight."

    "It uses its last strength to fly towards me, luckily I dodge its flight path."

    hide fan

    jump prologue_A

label prologue_A:

    player "Done. Stay gone for good! Now for the real challenge."

    "The wire is underneath the pile, I connect it to my mouse so I can proceed with buying."

    show site billinfo

    # Website, billing information

    # pafix nalang ung sa insert name section na kapag walang name na linagay si player, di sila pwede mag proceed. 
    # di ko sure if dapat lalagyan yan ng label or smth, pero im open to suggestions!
    # Also, this part is supposed to have interactive image in the form of imagebuttons, don't worry about this for now kasi we don't have placeholders yet

    label inputName:
        $ name = renpy.input("Your name please?", multiline=False)

        if not name:
            # If the player doesn't enter a name, show an error message and ask again if u like
            jump inputName

    "Welcome, [name]!"

    mc "Entering details, here and there. Transactions will go through I'm sure of it."

    mc "Hit enter."

    "Not sure if it went through since the site is slowly loading, I'm starting to worry."

    mc "No more fucking joking PLEASE! This is my 2nd time already!"

    # image: Website,transaction failed 

    show transaction fail

    show transaction fail2

    mc "..."

    "Meltdown. Body crashing on the floor."

    "I know I should be angry and flip my entire desk but I'm too drained for any physical outcry."

    mc "Just accept it, you're never going to get your Catty MariMari anymore. The bank would've wanted this to happen."

    mc "..."

    "{i}Sniffle{/i}"

    "But It's Catty MariMari! {i}Sniffles{/i}... Catty MariMari..."

    "I sob quietly."

    show site mainmenu

    # image: Site goes back to the main menu, it’s still 2 AM

    mc "Time to play {i}My Beloved Universe{/i} instead."

    "As I reach for my desktop, I hear a notification sound, a popup notification on my screen appears."

    "It looks too unusual for the site to do notifications this big."

    "It doesn't even look like it came from the site as well."

    mc "Compromised blind box website?"

    show notification1
    
    # Notification: “That sucks. Sorry that happened,....etc...

    show notification2

    # Small Window with an icon of a fish in business suit

    "A small window appeared next to it. Revealing an icon of a fish in a business suit. The icon suddenly laughs?"

    mc "My money's been taken by a fraud all along?! That's why it didn't push through!"

    "The fish on the screen stops laughing. It reverts back to its normal icon. "

    show msscreen1

    # “No, I didn’t take your money.I’m appall....

    "Closing tabs didn't work. The icons are present but nothing budges with my clicks."

    mc "Okay,bye. No choice but to unplug you."

    "???" "... Wait! I have a proposal for you!"

    "I hear my speakers produce an out of this world voice."

    "It doesn't sound feminine, nor masculine, it's like two voices that simultaneously played together."

    "???" "I know you're into cute collectibles!"

    menu:
        "Choose"
        "\"Hey!\"":
            jump choice_hey
        "\"Not falling for that scheme!\"":
            jump choice_scheme

label choice_hey:

    mc "How the fuck did you know that? Through cookies? I thought this browser was supposed to help me with encrypting my personal business!"

    jump prologue_B

label choice_scheme:

    mc "No! I'm not falling for that scheme. I'm not fucking stupid!"

    mc "You've already compromised the site, and later my desktop if I don't turn this off, good bye!"

    jump prologue_B

label prologue_B:

    "???" "Please! Please! Please! Try my collection! It's free! Trust me!"

    mc "Hello???"

    "???" "Mayhaps if I show the product to you instead..."

    show blindboxcollection

    # Screen plays a slideshow of their own blind box collection but it’s too fast for her
    # Most likely a video file

    mc "Slow it down! You're not convincing me of anything!"

    "???" "Then try it already!"

    mc "I don't like this but I'm intrigued."

    mc "It's not that you get free offers often by some entity of a mystery sponsor who supposedly hijacked your computer"

    "???" "Mystery Sponsor? Is that what you called me?"

    mc "Who are you, I mean what even are you THEN"

    "???" "A fish in a business suit, no more, no less! Interesting! The others call me Mystery Sponsor too! You hit the ballpark on that one!"

    "There's no point asking this unusual fella."

    mc "Fine, Mystery Sponsor but why me? This feels like a set-up…"

    "I don't know what to expect after saying yes to the deal."

    "I feel uncertain, but I'll be lying if I said this kind of prospect doesn't excite me."

    "Because my life has been very stagnant this long."

    scene personal_achievements

    mc "No. What am I saying?"

    "The presence of this otherworldly being feels foreboding, it does feel familiar but on an unimaginable level, if I'm making any sense?"

    mc "No, dummy! I mean…"

    "Fuck?"

    "Am I making another mistake again?"
    
    sponsor "Hmmmmm. You're thinking a lot for a toy."

    mc "What do you want me to do with this?"

    mc "You're giving me this away. What for?"

    sponsor "Let's say some of the collectibles need — "

    sponsor "Love..."

    sponsor "Adoration..."

    sponsor "Attention..."

    sponsor "Absolution, maybe."

    mc "Absolution?"

    sponsor "All of them do. You're right. They deserve mercy. Only if they act."

    sponsor "Clean your mess."

    sponsor "Bwahahaha~"

    "All this talking, and talking added more questions than answers. I am facing a weird metaphysical interaction."

    "Why did they mean by cleaning my mess?"

    "My mess? Their mess?"

    "What the fuck did I get myself into..."

    mc "And if I did? What happens next?"

    mc "Then you're alive again."

    mc "-with a full collection!!! Win Win!"

    show deal

    # This part is supposed to have interactive image in the form of imagebuttons, don't worry about this for now kasi we don't have placeholders yet

    menu:
        "Choose"
        "HEART":
            jump choice_heart
        "THUMBS DOWN":
            jump choice_down
        "X BUTTON":
            jump choice_xbutton

    

label choice_heart:

    # Choice is HEART option

    "I click the heart button. I'm assuming that's the yes option in this case."

    "{i}Click.{/i}"

    jump gacha

label choice_down:

    # Choice is THUMBS DOWN option

    show areyousure

    mc "Uh… I have no choice do I?"

    "I press the only button on the screen."

    "So this is the illusion of free choice... Huh..."

    jump gacha

label choice_xbutton:

    # TRIGGERS GAME OVER

    "I chose to not participate. Why would I risk my time for something I don't understand?"

    "My stagnant yet familiar life continued."

    "I used my little savings left for a new {i}My Beloved Universe collection{/i}. It was cool as heck at first! But I feel dissatisfied right after."

    "I can't eat anymore, I have no money left in the bank. They repossessed my belongings, objects that make me feel at home. I don't know anymore."

    "I wonder if I just said yes to that silly fishy sponsor. Maybe just maybe things would've turned interesting..."

    "I'm regretting not giving in, the thought kills me every night. It drives me crazy. Like parasites in my brain."

    "Well... I can't turn back time."

    "At least I'm surrounded by my buddies, right?"

    scene collectionpile

        

    return


    


return