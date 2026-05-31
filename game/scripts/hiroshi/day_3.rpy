
    # HIROSHI'S DAY 3


label hiro_D3_A:

    "My soul nearly leaves my body when I hear the loud rapping against my door."
    "It takes me a second to process my surroundings and I get up when the noise doesn't stop."

    mc "Goddamit, I'm up..."
    mc "*yawn*"

    "Opening the door reluctantly, I'm greeted by a less than enthusiastic Hiroshi."
    "His clothes seem a bit wrinkled, his stance looking like he's been doing some work on his own."
    "And... a certain smell wafts in the air between us."

    # stomach rumbling sfx

    "My stomach rumbles. It's... {w=0.5}{nw}" # testing out a feel if we want the choice to come up automatically

    # gets if this was an intentional choice to have the menu text as "Choose", but we can also have "My stomach rumbles(...)"
    menu:    
        "My stomach rumbles. It's..."
        "Eggs?":
            $ breakfast = "tamagoyaki"
        "Soup?":
            $ breakfast = "miso soup"
        "Noodles?":
            $ breakfast = "zaru soba"

    mc "Did you cook something, Hiro?"

    # show hiroshi flustered

    "He nods, managing a small, awkward smile."

    if breakfast == "tamagoyaki":
        hiro "I-I kind of went through some of your kitchen supplies."
        hiro "I cleaned up a pan and some plates, and I made tamagoyaki."

    elif breakfast == "miso soup with tofu and seaweed":
        hiro "I figured you'd be hungry this morning, so I cleaned up your kitchen a little."
        hiro "I found some stock and made miso soup with tofu and seaweed."

    else:
        hiro "I usually start my mornings with something to eat."
        hiro "I kind of went through your pantry and found some noodles..."
        hiro "So I made zaru soba."

    "I look over his shoulder, and I see that a very miniscule part of my kitchen has been cleaned."
    "I also see some trashbags in the corner of the room, assuming it’s some of the foodbags I left lying around."

    hiro "W-well?"

    "Gosh, this is actually so embarrassing..."
    "He's waiting for me to respond."

    # alladat choice shit

    # ending that choice shit

    "After everything, Hiroshi speaks up."

    # show hiroshi neutral

    hiro "There's a couple of... trashbags I was able to fish out of one of the cabinets."
    hiro "Though I couldn't find any cleaning gloves, we could work through the mess without it."

    mc "Got it. Uh..."

    # hide hiroshi

    "I look around, overwhelmed."

    mc "... Where should we start?"

    # show hiroshi tweaking

    "I look at him and he looks around as well, his jaw clenched."
    "I think he's trying not to gag."

    # show hiroshi neutral

    hiro "We could start here."
    hiro "The... kitchen and diining room, since we're already here."

    # hide hiroshi

    "I nod, and grab a trashbag before I make my way over to the other end of the room."
    "There are a couple of paper bags of rotten food in the corner, and I begin to pick them up one by one."
    "Good God..."

    # show hiroshi neutral

    hiro "There's a candle over there..."

    mc "Really? What kind is it?"

    hiro "Um, it says..."
    hiro "Supercalifragilisticexpialidociously lavender scented?"

    "My eyes widen and I immediately walk over to him, snatching the candle from his hands."
    "He steps back, surprised when I open the lid and turn it to him, smiling."

    mc "This super rare item's scent is my favorite."
    mc "You should try it."

    # show hiroshi flustered

    hiro "Er... try what?"

    "I roll my eyes."

    mc "Sniffing it, silly."

    # show hiroshi confused or whatever

    "He gives me a confused look, and chuckles awkwardly before inhaling."

    # show hiroshi something

    "He gives me another look that seems like he wants to say something, but is testing me."

    # show hiroshi grinning?

    "Though he {i}is{/i} grinning..."

    mc "What? Say it."

    # show hiroshi neutral

    hiro "I've smelt better..."

    menu:
        '"Wow. So am I not up to standard?"':
            $ candle_reaction = "not up to standard"
        '"Maybe it\'s not your type."':
            $ candle_reaction = "not your type"

    if candle_reaction == "not up to standard":
        mc "Wow. So am I not up to standard?"
        
        "He gives me a sheepish smile."

        mc "Well?"

    else:
        mc "Maybe it's not your type."

        "He gives me a sheepish smile."

        # show hiroshi flustered

        hiro "I'm just saying."

    "He put his hands in his pockets."

    # show hiroshi neutral

    hiro "Why is this one your favorite?"

    mc "It's..."

    menu:
        "... calming.":
            $ candle_reason = "calming"
        "... for my collection.":
            $ candle_reason = "collection"
        "... sentimental.":
            $ candle_reason = "sentimental"

    # show hiroshi confused

    "He tilts his head at my answer."

    # show hiroshi neutral

    if candle_reason == "calming":
        hiro "So... this is the scent that calms you the most?"

        mc "Yeah. That's why it's my favorite."

    elif candle_reason == "collection":
        hiro "It's your favorite because it's for a... a collection?"
        hiro "You ahve a collection of the same candle?"

        mc "I mean... if I like it so much, I must have bought it multiple times."
        mc "And I have a tendency to purchase without really thinking... so I most likely do."

    else:
        hiro "Sentimental? For what reason?"

        "I nod."

        mc "It reminds me of a time that I felt like I had some semblance of control over my life, I guess."
        mc "And a time where I probably had enough to not really think about my spending when buying it."

    hiro "Do you have others?"

    mc "What?"

    hiro "I m-mean, do you have other... candles like this?"
    hiro "You must have, right?"

    mc "I mean, we could look around and check if you're that curious."

    # showing different hiroshi reactions to shit

    "He nods, and we completely forget what we were supposed to be doing."
    "We dig around my piles, searching for any and all semblances of scented candles."
    "I notice him genuinely listening when I explain where I bought some of them and why I did."
    "And when he smells them, he also gives his comments about what he thinks of the quality, like some sort of candle specialist."
    "I laugh."

    "He's not so bad."

    "When we reach the bedroom pile, he fishes out another purple cnadle in a jar, and he shows it to me."

    # show hiroshi happy

    hiro "This one has your favorite scent on it, too."
    hiro "It says... Indubitably Luxuriously Eloquently Lavender scented."

    "Before I could even take a whiff myself, he turned it around to inspect the label."
    "He then carried the jar in his hand, as if to weigh it."

    # show hiroshi neutral

    hiro "Huh. This one is more expensive."
    hiro "This must be so much better than the one you had in the kitchen."

    "I shake my head."

    mc "Expensive? Yes."
    mc "Better? I can't say it is."

    hiro "Why not?"

    mc "Honestly? The kitchen works just as well."
    mc "I think this one just has a better marketing strategy and label, that's why they were able to price it so high."

    "He leaves the candle on the bedside table and we fish through the other piles."

    hiro "Do you think buying cheaper is better than expensive?"

    menu:
        "Do you think buying cheaper is better than expensive?"
        '"Yes, but it depends."':
            $ cheaper_vs_expensive = "yes"
        '"No, but..."':
            $ cheaper_vs_expensive = "no"

    if cheaper_vs_expensive == "yes":
        mc "Like if it was something that lasted longer, is of equal quality than the expensive one, then I'll buy it cheap."
        mc "But if it didn't give me any value for its cost, then I'll most likely go for a brand I trust more."

    else:
        mc "... I don't think I want to spend more on something that's of equal quality but more expensive because it has a brand name."
        mc "If it works, it works, right?"

    # show hiro happy

    hiro "That's kind of funny."

    mc "Why?"

    # show hiroshi flustered

    hiro "Well, look around."
    hiro "I didn't think you would have any sense of financial responsibility and capability, considering all the things you bought and have no place to go."

    "I turn to face him and eye him quietly."

    mc "{i}Riiight...{/i}"

    "I'm starting to get just a tiny bit apprehensive being in the same room as him with the way he's talking right now."

    # show hiro neutral

    hiro "You know, I'd rather honestly buy the more expensive one than the cheap one, if I were you."

    mc "Really now. Why?"

    hiro "Well..."
    hiro "If I had the means to even choose between them, it's so much easier to just buy the one you know has got quality, which is expensive."
    hiro "What other reason could they have to cost more?"

    "This guy."

    mc "Expensive doesn't always equate to quality, you know."

    # show hiro happy

    hiro "Well, maybe if you had enough money, no?"
    hiro "If you did, your house would probably be in an entirely different state,"
    hiro "rather than be swamped with a bunch of useless junk without any appeal or purpose."

    "Wow."

    hiro "I wouldn't be caught dead with such a mess, really."

    "{i}Wooow.{/i}"

    hiro "Then you'd also probably understand that those items work so much better than the cheap ones."

    mc "You don't think I know the difference of quality in the things I buy?"

    # show hiro neutral

    hiro "I can assume you don't."

    "With a staggered sigh, I pray to Mystery Sponsor and ask it for the strength to not sock this man's jaw this very moment."

    menu:
        "With a staggered sigh, I pray to Mystery Sponsor and ask it for the strength to not sock this man's jaw this very moment."
        '"You must have been wealthy in your own world, huh?"':
            $ hiro_quality = "wealthy"
        '"For a guy who presents himself as such, your way of thinking feels so superficial."':
            $ hiro_quality = "superficial"
        '"You think you know better than I do?"':
            $ hiro_quality = "know better"

    if hiro_quality == "wealthy":
        "He shoots me a somewhat prideful grin. That's new."
        "... It doesn't suit him."

        # show hiro happy

        hiro "I work hard. And I know I have what I deserve and more."
        hiro "That's why I refuse to buy anything less than."

        mc "Uh-huh. You think I'm stupid?"

        # show hiro flustered

        hiro "... I never said that."

    elif hiro_quality == "superficial":
        "He gives me a stern look."

        hiro "It's not."
        hiro "At least... I don't think it is. It's just an observation."
        hiro "Why would I hold back on anything nicer if I could afford it? It's like you're the one who doesn't know."

    else:
        hiro "So what if I think that?"
        hiro "I'm the one helping you clean up the mess from the very purchases you failed to subdue yourself in."
        hiro "Your piles in this room tell me so much more about your habits than what you say about yourself, and you think {i}I'm{/i} wrong for thinking I know better?"

    "I let out a sarcastic laugh."

    mc "I know how to discern items of quality, Hiroshi. Alright?"

    # show hiro neutral

    hiro "Do you, now?"
    hiro "With all the useless junk lying around, it feels like you really don't."

    "I swallow harshly, turning to face him."

    mc "And why do you suppose now I know that the expensive candle in my room wasn't worth the price?"

    "He stays quiet, and his eyes flash in recognition."

    hiro "... Oh."

    "I turn my back again."

    mc "Let's just... finish cleaning up my shit."

    "I trudge away from the bedroom, away from him and back to the dining room and kitchen where it's slightly more tolerable."
    "To my displeasure, he follows behind."

    "I don't speak for several minutes while we're cleaning, my mood sour at the interaction."

    hiro "... You're very quiet."

    mc "..."

    # show hiro frustrated

    hiro "Was it because of what I said earlier?"

    "I turn my back on him, tying up the trashbag and settling it near the door."

    # hide hiro
    # it makes sense to hide him here

    hiro "[name]?"

    "I pick up another trashbag and continue to pick up items that were either trash or I knew was filled with rotted food."

    hiro "I'm older than you, you should--"

    mc "I don't give a shit."

    "I hear him take a lengthy inhale."

    hiro "Are you upset because of the argument we had about that stupid candle?"

    mc "No, Hiroshi. I'm absolutely fine over here. You must be losing your mind."

    hiro "See, if you want me to help you out, maybe you should at least try and be decent or nice."

    mc "..."
    mc "I don't need you. I never did--"

    "Without warning, I hear his footsteps coming towards me."
    "I get whirled around and get shoved to the nearest wall." # You're into this guy?
    

    return