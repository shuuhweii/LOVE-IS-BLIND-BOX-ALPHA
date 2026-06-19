
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

    menu:
        "He's waiting for me to respond."
        "Have you eaten? Do you wanna eat with me?":
            call eating_breakfast
        "I'd rather clean...":
            call rather_clean
        "This is all really nice, but I'm not hungry.":
            call not_hungry

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
        hiro "I've smelt better..."
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
        mc "It's..."
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
        hiro "Do you think buying cheaper is better than expensive?"
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
    "His hand pins my wrists above my head and his other hand prods my chest with his finger harshly."
    
    # show hiro frustrated
    # CG maybe eyes emoji?

    hiro "I've had just about enough of you."
    hiro "You're a weak, spineless, shrivelling little brat that has NO control over anything in her life."
    hiro "NOBODY is here for you except for me."
    hiro "Maybe if you had just a sliver of self restraint and dignity, we wouldn't be here right now dealing with all this."

    "His face comes closer, and I freeze."
    "I can feel his hot breath on my cheek, his eyes filled with fury I didn't know he could have."
    "I could hear his heartbeat get faster and faster."

    hiro "I LOATHE every second I'm looking around the obscenity of this house."
    hiro "I absolutely LOATHE that of all the chances in all the world, I get chosen to be stuck with you and your filth."
    hiro "And just so you know?"
    hiro "I LOATHE every second I have to spend with you, you pathetic, whiny little shit."

    # play around with wait timers

    "..."

    "..."

    "..."

    "He's heaving on me at this point, and I could see his face flushed in anger."
    "I feel my throat constrict, and my eyes get teary."

    window hide

    menu:
        "Push him off.":
            pass
        "Push him off.":
            pass
        "Push him off.":
            pass

    window show

    "Shakily, I attempt to gather myself to pull my wrists down to escape from him."
    "When I successfully do, I shove him with all my strength, caushing his stature to step back."

    # show hiro in pain or whatever depending on what sprites y'all have

    mc "FUCK YOU!"

    # hide hiro

    "I hide my face in my hands and run to the bedroom, completely overwhelmed by what just happened."

    "I spend the rest of the afternoon sobbing harshly into my pillow until my lungs feel like collapsing."

    "..."

    "..."

    "..."

    hiro "... [name]?"

    "I can hear his incessant knocking on my door."
    "Impudent man."

    hiro "Please, can you open the door? Please?"

    "..."

    hiro "Let me apologize where I can see you... please..." # You're into this guy?

    "..."

    "..."

    "..."

    "The knocking continues for over an hour."
    "Then two hours."
    "Then three,"
    "then four."

    "I see the sun set from outside, and the knocking doesn't stop."
    "His knuckles should be raw from doing that at this point."

    hiro "I'm not going to stop, you know. Not until you let me in..." # You're into THIS guy?
    
    "..."

    hiro "Please, [name]..."

    "The raps became softer and softer, and I could feel him tire from the constant motion."
    "I let it be the last thing I hear until I fall asleep exhausted."

    return

label eating_breakfast:
    "I see him physically tense up, and the undeniable red that spreads across his face tells me he hasn’t eaten."
    "And he’s maybe a little flustered."

    # show hiro flustered

    hiro "N-no, but..."
    hiro "I made it for you."
    hiro "I... have a sense you might not have had a cooked meal in a while, so this was really n-no issue."

    "I cross my arms and actually smile at him."

    mc "We should eat together. And then I'll rate your cooking."

    "He gives me a surprised look and we walk over to the table where he had served the food."
    "I have to admit, it’s actually quite endearing how he had woken me up today."

    mc "Wow. I didn’t know that I even had this stocked up…"

    "He gives me an awkward chuckle."

    hiro "I didn’t know either."
    hiro "I was honestly expecting, uh…"
    hiro "... a horde of bugs or something."

    "I squint at him."

    mc "I’m not that gross!"

    "He bows his head low in return, mumbling an apology."
    "This guy!"

    mc "Hey! Come on, it was a joke. Lighten up a little!"

    "When he shows his face again, his cheeks are even more red than I remember."
    "He lets out a stiff laugh and tries to loosen his shoulders."

    hiro "R-right. Thank you?"

    "I snort and we take our seats together. My stomach grumbles again as I scoop up the food and swallow."

    "My eyes widen at the taste."

    menu:
        "My eyes widen at the taste."
        '"This is...!"':
            call breakfast_reaction_good
        '"Hmm..."':
            call breakfast_reaction_neutral
        "Eat, fast!":
            call breakfast_reaction_bad

    return

label breakfast_reaction_good:
    "I look at him with stars in my eyes. Never have I ever cooked something this good for myself in the morning!"
    "This wonderfully, perpetually nervous kind of a loser minimum wage worker has some tricks up his sleeve!"

    mc "Hiroshi!"

    # show hiro flustered

    hiro "Y–yeah, [name]? H-how is it?"

    mc "How on god's green earth did you ever manage to make a meal as good as this?"

    "He fidgets, but I can see the way his face brightens up when I compliment his cooking."

    hiro "O-oh! Well, I... I live alone, so I..."

    "He gives me a small look, but I can't decipher what it is. Not when I'm busy gulping down on heaven."

    # show hiro happy
    hiro "I like to learn. A-a lot of things."
    hiro "And I enjoy a lot of… finer things? Expensive."
    hiro "And I used to eat a lot of really nice food in… some really good places."
    # how hiro neutral
    hiro "Alone."
    hiro "So… I, maybe, um… thought I could cook at home."
    # show hiro happy
    hiro "And I did. A-and I do."

    mc "I can tell. I mean, alone. Alone why? Can I ask that, actually?"

    # show hiro neutral
    "He tilts his head to the side and encourages me to keep talking."

    mc "The... friend thing. You honestly have no one?"

    "He swallows, his Adam's apple bobbing up and down."
    "I see him avoid my gaze, and it feels like he’s struggling to speak about it."
    "But just when I’m about to change the topic--"

    # show hiro sad
    hiro "My... planet? My h-home is.. A little complicated."
    # "Then, even lower:"
    hiro "I don’t think I’m a very good person there, honestly."

    mc "Why do you think so?"

    "He goes silent for a little bit and gently places his utensil down. He seems like he’s pondering something again."

    # show hiro neutral
    hiro "I-If I answer the question… can you answer it in return, too?"

    "I give him a reassuring half smile."

    mc "Of course. Go ahead."

    "He pushes his plate to the side with his fingers and kind of fidgets a little with his hands."
    "I picked up now that it’s a habit he does out of stress."
    "I eat quietly while waiting for him to tell his story."

    # play around with wait times here
    "..."

    "Wow, he’s really taking his sweet time--"

    hiro "I work as a… cybersecurity agent. A-and my government convinces me that I… am doing a service well, and my status is earned."

    "Huh. Status? What does that have to do with--"

    hiro "I d-don’t feel like I’m doing an honorable service."
    hiro "Keeping tabs on a lot of people, finding out their most private information… And having to store them somewhere the government can access it so easily."
    hiro "T-They reward me very, very generously… and make sure I’m also protected."
    hiro "But the isolation in that job is… draining."

    hiro "But it isn’t only me."
    hiro "People are forbidden to have… intimate relations. Not after the previous war."
    hiro "So… I d-don’t really know how to… be… social. Or… decent..?"
    hiro "S-sorry."

    "Ah. There it is."
    
    call my_story_leadup

    return

label breakfast_reaction_neutral:
    "He looks at me nervously as I chew my food slowly. A small nod of approval leaves me, and he exhales in relief."

    # show hiro flustered
    hiro "W-well? What do you think?"

    "I have to admit, it’s decent."

    mc "It’s not bad."

    "He gives me a tight lipped smile, and allows himself to eat."
    "I observe him quietly, and I blurt a question out without really thinking."

    mc "How did you learn to cook like this?"

    # show hiro flustered
    hiro "W-well, I don’t really… I read a lot of books."

    "I chuckle at that. How cute."

    mc "Books? Didn’t you learn these from, I don’t know, your mom maybe?"

    # show hiro sad?

    "His eyes dart to the side, and my shoulders tense."

    mc "S-sorry, I forgot--"

    # show hiro flustered

    hiro "Now who’s being sexist…"

    "My eyes widened at his statement. The actual nerve!"

    mc "... damn, you got me there."

    "He seems to not take it well, so I give him a pity laugh."
    "He smiles in return and the tension eases even just for a little bit."

    # show hiro neutral
    hiro "I… I don’t remember much about my mom growing up."
    hiro "It was… a strange time to be growing up.."
    hiro "After the war. I… my form of entertainment and education was reading."

    hiro "There were surprisingly loads of books available in my house."
    hiro "My parent’s house… That’s honestly what I remember most, and I guess it bled out as I grew up."
    hiro "I wasn’t… allowed interaction. Much. Not even after I got a job, s-so…"

    "I listen quietly as he continues to try and fight himself to tell me about himself."
    "I kind of feel like an asshole for judging him so quickly. But not really."
    "We all have our own shit."

    call my_story_leadup

    return

label breakfast_reaction_bad:
    "I accidentally shove my utensil deeper than anticipated and the food goes straight down my throat."
    "I cover my mouth with my hand, shuddering and coughing."
    "Holy fuck, this is so embarrassing!"

    # show hiro sad
    hiro "Ah, I’m sorry…"
    
    "He’s giving me the goddamn puppy dog eyes again."
    "Goddamit, this man! My eagerness and greed has betrayed me!"

    mc "N-no!"
    mc "I mean, it’s fine, it’s great!"
    mc "The cooking, I mean the food is… it’s great, yummy, really!"

    "He squints his eyes and bites the side of his cheek, thinking if he should believe me or let it pass like that."

    mc "I swear! I was just really, really clumsy and shoved too far down and… choked."

    "I feel my face flush and he clicks his tongue."

    # show hiro neutral

    hiro "You don’t have to… make excuses, you know."
    hiro "I could just store the food back into the refrigerator--"

    mc "Hiro, I swear, your cooking is fine!"
    mc "It’s… it’s decent, alright? It’s good."

    "He stays silent and starts poking at his own food, looking like he lost his appetite. Man…"

    hiro "Maybe we should… just clean. I’ll let you finish what you can stomach."

    "We eat in heavy silence, and I kick myself in my head for being so goddamn awkward."
    
    return



label rather_clean:
    "He kind of frowns and shakes his head at me."

    # show hiro sad
    hiro "Y-you should really eat. How else are we going to be cleaning if you don’t have the fuel to do anything?"

    menu:
        hiro "Y-you should really eat. How else are we going to be cleaning if you don’t have the fuel to do anything?"
        '"You\’re right… Maybe you should eat with me, then!"':
            "His cheeks flush a deep red. I have to admit, it’s kind of amusing how easily I can make this man flustered."
        '"Okay, okay. I wouldn’t want your cooking to be for nothing."':
            "He nods and smiles approvingly, laying out the plate for just me."

            mc "But."
            
            "His gaze goes to me."

            # show hiro neutral
            hiro "But?"

            mc "You have to eat with me. There’s no way I’m eating alone while you sit doing nothing."

    "He gives me a bashful look and takes a seat across from me."
    "He serves both of us and waits for me to eat before taking a bite himself."

    # show hiro neutral
    hiro "I noticed… You younger people have some real stubborn tendencies…"

    "I grin."

    mc "At least my joints don’t creak while walking, like you older people."

    "He frowns, and I laugh at him."

    mc "I'm joking!"

    "He seems to loosen up and chuckles awkwardly."
    "While we’re eating our food, I speak up."

    menu:
        "While we’re eating our food, I speak up."
        '"How old are you, anyway?"':
            call how_old
        '"You don’t seem to be as uncomfortable as yesterday."':
            call not_uncomfortable
        '"Why did you cook this dish in particular?"':
            call why_dish

    mc "Would it be fine if I just… talk about it?"

    "Hiroshi nods eagerly and stops to give me a small smile."
    
    # show hiro flustered
    hiro "O-of course. I asked, so I should listen."

    "I give him a half grin."
    
    menu:
        "I give him a half grin."
        "Tell him my story.":
            call my_story
        "Be dodgy.":
            call be_dodgy

    return

label how_old:
    "Hiroshi swallows his food before answering."

    # show hiro flustered
    hiro "Can you promise not to make fun of me when I tell you?"

    "I smile mischievously."

    mc "Maybe."

    "He sighs in defeat."

    # show hiro neutral
    hiro "I'm 30 years old."

    menu:
        hiro "I'm 30 years old."
        '"Damn!"':
            call how_old_damn
        '"That\'s not so bad."':
            call how_old_not_bad
        '"Explains a lot."':
            call how_old_explains_a_lot

    mc "Sure. Go ahead."
    
    # show hiro neutral
    hiro "H-how did you… get yourself in this mess?"

    "I sigh softly."
    return

label how_old_damn:
    "Like clockwork, his face flushes red at my comment. I laugh at him for a good minute before waving my hand in the air."

    mc "Sorry! I mean, I kind of expected it, you know? You seem around that age with the way you move."

    "He pouts and gives me a look, chewing his food slowly."

    # show hiro flustered
    hiro "...d-do I really seem that old?"
    hiro "Is 30 old to you?"

    menu:
        hiro "Is 30 old to you?"
        "Yup.":
            "He looks away and pouts even more. I giggle a little."

            mc "But the way you act feels so much more… juvenile."

            # show hiro embarrassed
            hiro "I-is… that a bad thing?"

            "I ponder his question."

            mc "I think it depends on context?"
            mc "Like, it’s fine if you pout when you don’t agree with what I say, or give me an attitude when things don’t go your way. Just as long as you don’t overreact."
            mc "It’s quite endearing to see someone a little older feel a bit more… human."

            "His gaze goes down on his plate and he adjusts his collar nervously."
        "Nope.":
            "His eyes glimmer a bit when I tell him that."
            "I swear this guy’s face..."
            
            # show hiro flustered
            hiro "Well… I mean why?"

            mc "I don’t really necessarily think it’s old."
            mc "You get to do a lot of things physically, and have the money to do it, I guess."
            mc "It’s like a sweet spot for life. You think?"

            "He purses his lips and actually thinks for a moment before responding."

            # show hiro happy
            hiro "Yeah, I guess so."

            "Without missing a beat--"
            
            hiro "I m-mean… do you think I look younger than I actually am?"

            "Honestly? He looks a little youthful, save for the eyebags and the slightly growing stubble on his chin."
            "His skin is surprisingly clear for someone who looks like they never get a wink of sleep."
            "And his eyes when he looks at me with a curious gaze… they kind of sparkle nicely--"

            "Wait. What the hell am I saying?"

            mc "You look just fine, Hiro. Quite good for your age."

            "He gives me a sheepish smile."

            # show hiro embarrassed
            hiro "T-thanks."

    "He shakes his head and continues to eat. "
    
    hiro "I think that’s enough about me. I… can I ask about you?"

    return

label how_old_not_bad:
    "He gives me a hesitant look."

    # show hiro flustered
    hiro "Oh. T-then…  Yeah. I’m 30. Can I ask how old you are?"

    "I shrug and smile."

    mc "I would assume I’m around your age if that was my reaction, no?"

    "He gives me a tight lipped look and I wave my hand to dismiss it."

    mc "I don’t think you need to worry about looking old. What matters more is how you feel."
    mc "Like, do your joints really creak while walking? Because mine don’t."

    "I flash him a grin. He gives me a scoff, smiling a little wider."

    hiro "Well… maybe you just have some really lucky genes if they don’t do that."

    mc "Oh? So you are admitting that yours creak?"

    hiro "I never said..!"

    "I laugh heartily. It’s been a long while since I did that."

    mc "I never said it was bad, either! It’s a normal part of getting old! Like needing to wear glasses to see better."

    hiro "I d-don’t think there’s a correlation with bad sight and age!"

    mc "Oh yeah? Where’s your scientific study?"

    hiro "I-I mean, there is! But bad sight could just be caused by--"

    mc "Genes, right?"

    "He looks just about as flustered as he is frustrated. It’s pretty funny."

    hiro "You’re not giving me a fair shot here. And I made you food!"

    "We gave each other a look and burst out laughing. For a kind of loser, he’s kind of nice to just talk to."

    "He shakes his head and continues to eat. "

    hiro "I think that’s enough about me. I… can I ask about you?"

    return

label how_old_explains_a_lot:
    # show hiro flustered
    hiro "What… what is that supposed to mean?"

    mc "It means, it explains a lot why you do what you do, no?"

    "He frowns in confusion."

    hiro "I don’t understand…"

    mc "You know."
    mc "The way you kind of carry yourself,"
    mc "the reactions you have to the mess that is in my home,"
    mc "and how you kind of speak makes me think that you’re a little more seasoned than I give you credit for."

    hiro "I-is that a compliment?"

    "I smile playfully."

    mc "You’re older. Wouldn’t you know that better?"

    "He shakes his head and continues to eat."

    hiro "I disagree, but I think that’s enough about me. I… can I ask about you?"

    return

label not_uncomfortable:
    "He gives me a shrug with a contemplative look."

    hiro "Maybe I’m just… much more acclimated to the mess. It starts to feel a little numbing after a long while of being… overwhelmed, honestly."
    hiro "I don’t want to be… I d-didn’t want to react like that, just so you know."

    "I raise an eyebrow."

    mc "Like what, exactly?"

    hiro "L-like, being uncomfortable. Or the… gagging. Or anything else offensive."
    hiro "I… was just really surprised, and I… I am sorry again for reacting like that."
    hiro "It didn’t occur to me that it was off putting for you, o-or… embarrassing?"

    "I huff quietly. So he does have a heart somewhere."

    mc "I still don’t forgive you entirely."
    mc "But… thanks. And… sorry. I know it can feel really jarring to be in here."

    "He gives me a look, like he wants to ask something. I nod."

    hiro "Can… you tell me how you got yourself in this mess in the first place?"

    "I sigh gently."

    return

label why_dish:
    "He thinks for a moment, taking another bite before answering."

    # show hiro neutral
    hiro "I just… I made do of what was in your pantry."
    hiro "I-I… I thought how I acted yesterday wasn’t very… um… appropriate, especially since I’m the one i-in your house."
    hiro "A-and… I figured you would have been hungry after getting upset. Because {i}I{/i} would have…"

    "Huh. So he does have some composure."

    mc "Thanks. What you cooked is quite nice."

    "He gives me a timid smile."

    # show hiro flustered
    hiro "I’m glad you t-think so."
    hiro "It was… interesting, challenging, yes."
    hiro "To um… go through your pantry and look for something. And… something I would know to cook, a-actually."

    "I tilt my head to the side, eyeing him playfully."

    mc "So you went through my stuff without asking permission?"

    "He immediately turns pink and I have to hold in my laughter like a sin."

    hiro "I-I thought-- maybe if I-- oh I’m... shit--"

    "I burst out laughing, feeling actually really bad for him as he sits there stunned to silence."

    mc "Chill out, Hiro! It’s okay."
    mc "If I’m honest… I’m grateful you cooked. And… maybe slightly got over that gagging problem."
    mc "I’m grateful you’re here to help me."

    "I give him an encouraging smile, and he turns pinker."

    mc "You know what? Maybe… I won’t forgive you."

    hiro "W-what? Why?"

    mc "You need to cook for me. All the time now."

    "He’s silent for a bit and then we both burst into laughter."

    hiro "S-see, that wouldn’t be a problem for me if..."

    mc "If?"

    "He shoots me a curious gaze."

    hiro "Can... I ask s-something a little more... serious?"

    "I nod coolly."

    hiro "How.. h-how did you um… get into this mess?"

    "I sigh quietly."

    return


label not_hungry:
    "His face drops instantly. He shakes his head and gives me an attempt to smile, albeit strained."

    # show hiro frustrated
    hiro "Y-you’re joking, right?"

    "Setting the dishes down, he dusts his hands off on the kitchen towel cloth and gives me a stern look."

    hiro "Why not?"

    menu:
        hiro "Why not?"
        '"I\'m just not hungry."':
            $not_hungry_reason = "not hungry"
        "Scoff and roll your eyes.":
            $not_hungry_reason = "scoff"
        '"We could just put it in the fridge and eat later?"':
            $not_hungry_reason = "eat later"

    if not_hungry_reason == "not hungry":
        "He takes a moment to process my words with furrowed brows."

        hiro "How could you not be hungry when you literally slept through yesterday without eating?"
        mc "That’s none of your business? I’m simply not hungry?"

        "He frowns and shakes his head."
        "He grabs the plates and opens the refrigerator door, shoving the meals inside harshly."
        "He turns to me but doesn’t meet my gaze."

        hiro "You don’t know the shit I dug through in your nasty fridge just to make you breakfast. You brat."

        mc "Excuse me?"

        "He scoffs and I inhale sharply, utterly flabbergasted."

    elif not_hungry_reason == "scoff":
        "I see him grit his teeth, his hand balling up into a fist."

        hiro "Answer me and don’t give me that attitude."
        hiro "You have no idea what shit I had to shovel out just to prepare you that food."

        mc "You’re unbelievable. I just said I’m not hungry and you’re suddenly so worked up about it?"

        hiro "And I’m asking why like a grown fucking adult."
        hiro "You couldn’t give me a proper response? Or at least be grateful I cooked for you, you brat?"

        mc "I didn’t ask you to cook."

        "With a frustrated grunt, he slams his hands down on the table and takes the plates away, shoving them into the fridge."
        "His back is turned when he speaks in a lower voice."

    elif not_hungry_reason == "eat later":
        hiro "But this food is better eaten when it’s fresh. You don’t want to try it, at least?"

        mc "I just said I’m not hungry!"

        "Out of nowhere, he slams his hands down and stares at me with a piercing glare."

        hiro "I’ve spent a good amount of my own time digging through what you call your fridge and {i}this{/i} is the thanks I get?"
        hiro "You fucking brat."

        "Before I can even retaliate, he grabs the plate and shoves them back inside my refrigerator."
        "He slams the door and speaks eerily calmly."
    

    hiro "...we should just start cleaning. Forget I said anything."

    return




label my_story_leadup:
    # show hiro flustered
    hiro "I don’t think I like talking about it right now..."

    "He gives me a solemn look. I wave my hands and smile awkwardly."

    mc "Don’t worry about it! I mean… I kind of get it?"
    mc "I mean, look at my mess, right?"

    "He gives me a stiff smile and I nod."

    # show hiro neutral
    hiro "Can… can I ask about you, now? What about you?"

    "I place my utensil down and purse my lip for a moment."

    menu:
        "I place my utensil down and purse my lip for a moment."
        "Tell him my story.":
            call my_story
        "Be dodgy.":
            call be_dodgy
    return

label my_story:
    mc "I… used to be successful. So, so successful. I worked hard for the things I wanted."

    "I grip the hem of my shirt, a strange feeling bubbling over my chest as I open up to him."

    mc "But then, shit kept hitting the fan. I didn’t know what to do, so I did the one thing I knew that would comfort me."
    mc "I spent so much money."

    "I kind of look up and see Hiroshi debating with himself if he should say something or not. I keep talking."

    mc "I know you must think I’m... irresponsible."
    mc "And I am. I know. I… know what I need to fix, the risks I faced when indulging myself in the adrenaline of material gratification."
    mc "It’s..."
    mc "...something I need to work on."

    "Of course, I see him basically sweating, on the verge of asking so many more questions. I give him a small chuckle."

    mc "... we should try focusing on the task now, I think."
    mc "And, thank you for breakfast."

    "He swallows and nods, giving me a thumbs up."

    return

label be_dodgy:
    "I feel his gaze on me, and I feel anything but comfortable opening up to this guy."

    mc "I... had some trouble keeping myself controlled. With spending money. I mean, you see my place, it must be a huge problem, right?"

    "I laugh to ease the air but he looks at me intensely."

    # show hiro frustrated

    hiro "That’s it?"
    
    mc "...pretty much?"

    "He crosses his arms and leans back on his chair."

    hiro "That simply can’t be."
    hiro "Don’t you... where are your parents? A-aren’t you... surrounded by company?"

    "I shake my head firmly. He scoffs."
    "Wow."

    hiro "That’s just great. Well. Unbelievable."
    hiro "And here I thought we were… y-you were…"

    mc "What?"

    "He shakes his head and gives me a bitter look. I shoot the same look back and cross my arms."

    mc "...look. Let’s just get back to cleaning. I don’t want to make this a bigger deal than you’re making it seem."

    return
