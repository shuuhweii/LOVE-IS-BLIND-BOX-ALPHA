# HIROSHI DAY 6

label hiro_D6:
    "In front of me is a vast land, the grass pink and filled with small white flowers dancing in the breeze. The sky is a light purple, 
    and I’m surrounded by trees that are the same pink hue as the ground."
    
    "I feel myself walk to the clearing, and I lie on the soft pasture, the plants softer than I expected. It’s like lying on a cloud."

    "Above me are small, white birds flying in the distance. The clouds shine as if covered in glitter, and for once, I feel at peace."

    "Bubbles pass my vision, and I smile. Their reflections cast the soft meadow line, and the sight calms me. The bubbles grow bigger, and strangely, I see one carrying something…"

    "…is that a fish?"

    "That big bubble pops, and the sight of this wretched creature landing on my face while I relax makes me scream."

    mc "AAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH!"

    "I’m up with a start, and Hiroshi comes running to my bedroom door, his eyes red and adjusting his glasses. His voice is startlingly gruff when he speaks."

    # hiro_surprised
    hiro "Hey, hey. What’s wrong? What happened?"

    "He sees me visibly sweating and comes up to offer his handkerchief for me. I take it without really thinking and he sits next to me on my bed cautiously, still maintaining a big space between us."

    # hiro_flustered
    hiro "Are… are you okay? Talk to me."

    menu:
        "Choose"
        "I had the weirdest fucking dream!":
            call hiro_dream_romantic
        "A… a fish that landed on my face…":
            call hiro_dream_platonic
        "Rub your face in disdain and tell him nothing.":
            call hiro_dream_bad

    # continue from the dream part
    "I shake my head and groan, heading to the bathroom to wash my face and brush my teeth. Maybe that would help me feel better."

    "I hear Hiroshi follow behind me, but not too closely. He waits patiently outside while I freshen up and try to get that dream out of my system."

    # hiro_neutral
    hiro "[name]?"

    mc "Yeah?"

    # hiro_neutral
    hiro "What… what are these things outside?"

    "I groan and spit the foam out, rinsing my face one last time and scrubbing it with a towel to dry off."

    mc "What things, Hiroshi?"

    "I call out from the bathroom. He doesn’t respond."

    mc "Hiroshi?"

    "I step out and the hallway is filled with… bubbles? Hiroshi is standing to the side trying not to get near any of them. I squint my eyes, feeling another presence in my house."

    mc "Hiro."

    # hiro_frustrated
    hiro "Yes?"

    menu:
        "Can you grab the…"
        "...heavy platform boots by the shoe rack?":
            pass
            # $ weapon = "platformBoots"
        "...metal book ends on the shelf by the TV?":
            pass
            # $ weapon = "metalBook"
        "...wii remotes on the table?":
            pass
            # $ weapon = "wiiRemotes"
    
    # hiro_flustered
    hiro "You kind of have… a lot of those…"

    "My eyes dart to him, and then to the thing I asked him to grab."

    "…right."

    mc "Then grab a pair. And give me one."

    "He does what he’s told and I tell him to be quiet, trying to figure out where the other person is amidst the floating novelties. I walk quietly across the piles and notice the strange water drippings on the floor. My face scrunches in disgust."

    mc "The fuck..?"

    "I notice a strange, misshapen bubble right outside the balcony, and I signal Hiroshi to follow me quietly. He does so clumsily, knocking over a stack of trinkets by the door."

    "I turn my head slowly and give him the most mystified and horrified look I’ve ever given anyone in my entire life."

    # hiro_flustered
    hiro "Sorry."

    mc "You would have been shot right there."

    # hiro_flusered
    hiro "I know..."

    mc "A marvelous display of spy prowess."

    # hiro_flustered
    hiro "I said I was sorry!"

    "I give him a wide eyed glare and continue sneaking to the balcony. He learns his lesson and gets on his tippy toes, trying hard to be silent. I whisper the plan."

    mc "The moment I open this door, you throw your thing the same direction as me. Got it?"

    "He nods furiously."

    "I swing the sliding door open, screaming as I throw my weapon to the misshapen bubble."

    "PLAP"

    "When the bubble pops, a familiar fish in a suit falls to the floor, flopping around out of breath. I panic and grab it by their wet clothes. I quickly turn the sink on and plug the hole to keep the water in."

    mc "Oh my god are you okay???"

    "Its big fat eye somehow scrunches to show their displeasure at the situation."

    # sponsor_wtf
    sponsor "You got my suit wet."

    "..."

    "It stands and dusts the water off its suit and… wait how did it do that…"

    # sponsor_happy
    sponsor "Well! That’s about enough for greetings."

    "It flops off the sink and walks to the living room where Hiroshi is left standing bewildered. I follow it and I stand next to him, just as confused."

    mc "What are you doing here?"

    # sponsor_hyped
    sponsor "You must have known that I was going to imprison him again!"

    mc "W-what?"

    # sponsor_neutral
    sponsor "I told you, didn’t I?"

    "I shake my head in disdain."

    # sponsor_happy
    sponsor "Ah, well I told him!"

    "It points its fishy little fin accusingly to Hiroshi. He has the same, disgusted look on his face when MS wiggles it in amusement."

    # hiro_frustrated
    hiro "Gross. Don’t do that."

    "I turn to Hiroshi, feeling conflicted."

    mc "I don’t recall you telling me what was in that paper…"

    # hiro_flustered
    hiro "Paper?"

    mc "The one from the other day. When you were still gagging at the state of my house."

    "My lips curl a bit."

    mc "Now look at you. You’re standing so well-"

    # hiro_neutral
    hiro "Not the time to tease me, I think."

    "I shut my mouth, but give him an apprehensive look."

    mc "So are you going to tell me what was actually written?"

    # hiro_flustered
    hiro "I… needed to help you. I mean, I can’t tell you the consequence, but what was important was I needed to help you and that… thing would claim me back. A-as a figurine."

    "What?"

    mc "What??"

    # hiro_flustered
    hiro "Yeah."

    # sponsor_happy
    sponsor "Communication is key! Even if it’s last minute and would have totally helped the plot if told earlier!"

    mc "So… he’ll just be gone?"

    # sponsor_hyped
    sponsor "Yup! Imprisoned once more."

    "I shake my head incredulously."

    mc "...do I have a choice?"

    # sponsor_happy
    menu:
        sponsor "I believe so! Let me pull up the choices screen."

        "I want him to stay with me! I like him more than I want to admit.":
            call hiro_choice_romantic
        "Can’t he stay? I actually like him as a friend.":
            call hiro_choice_platonic
        "Stay silent.":
            call hiro_choice_bad

    mc "What do you mean next one?"

    return


label hiro_dream_romantic:
    "I tell him exactly the details of the pink meadow, the serenity in that world, and the fateful second that this slippery animal just flat out lands on my face. 
    
    He has an amused look on his face, and I can tell he’s trying not to laugh at me."

    mc "You’re making fun of me. This is serious!"

    "He shakes his head and scoots closer. He takes my hand, caressing the back of it gently."

    # hiro_happy
    hiro "I believe you. I’m sorry if I look like I’m not being serious. What else happened?"

    mc "That… I woke up after that."

    "He nods and offers a small smile."

    hiro "You sure have an active imagination. But why a fish out of everything?"

    mc "Hell if I know!"

    return

label hiro_dream_platonic:
    # hiro_neutral
    hiro "A fish?"

    "I tell him exactly the details of the pink meadow, the serenity in that world, and the fateful second that this slippery animal just flat out lands on my face. He has an amused look on his face, and I can tell he’s trying not to laugh at me."

    mc "You’re making fun of me. This is serious!"

    hiro "I didn’t say it wasn’t. But I don’t see a fish in your room anywhere."

    "I throw a pillow at him and he laughs and apologizes as he sets it back on my bed."

    mc "Hmph!"

    hiro "Sorry, sorry. Any idea why it might have been a fish that woke you up?"

    mc "Hell if I know!"

    return

label hiro_dream_bad:
    hiro "Are you sure? It doesn’t seem like it was nothing."

    mc "Ugh… just leave it."

    return

label hiro_choice_romantic:
    "I grab Hiro’s hand and stare that fish down. I can feel his grip tighten with mine, and I can already tell he’s blushing."

    "Good."

    mc "You can’t just take him away like that!"

    # sponsor_hyped
    sponsor "He’s a prisoner of mine! Of course I can!"

    "When I give it an even more challenging stare, it gulps."

    # sponsor_nervous
    sponsor "Er, well, you can say a couple of words before he gets turned into the collectible you adore so much!"

    "Hiroshi and I meet eyes, and without thinking, I pull him by the collar and kiss him."

    # hiro_flustered
    hiro "..!"

    "He makes a disgruntled noise, his hands not knowing where to rest. I take them and place them on my hips, and he pulls me closer instinctively. I can hear him whimper and groan softly as I deepen the kiss, and that’s just about the very last thing I hear before he pulls away in embarrassment."

    "We look at each other, completely flustered, and we laugh, resting our foreheads against each other. God, we’re so pathetic together."

    mc "Hiro…"

    "He chuckles and caresses my cheek."

    # hiro_happy
    "I’ll be back soon. I promise."

    "I frown, fighting back the tears that threaten to fall. I embrace him and he wraps his arms around me for the first and last time, before I hear the dreaded poof."

    "His little figurine floats to Mystery Sponsor, and I watch as it snaps its fin and Hiroshi disappears."

    # sponsor_happy
    sponsor "So! Ready for the next one?"

    "I swallow back my anger, only realizing now just how good it felt to be that close to him only for it to be taken away so quickly."

    return

label hiro_choice_platonic:
    "I step in front of Hiro and stare that fish down. Even standing in front of him, I can already tell he’s blushing."

    "Good."

    mc "You can’t just take him away like that!"

    # sponsor_hyped
    sponsor "He’s a prisoner of mine! Of course I can! It’s part of his deal."

    "I glare down at it until Hiro’s figure steps to my front. He looks down on me and smiles, patting the top of my head."

    # hiro_happy
    hiro "I appreciate what you’re trying to do. I’ll be okay, [name]."

    mc "But..!"

    # hiro_happy
    hiro "I’ll be okay. It’s okay. I hope whatever it is that this… fish has for you will help you so much more than I ever will."

    "I feel tears prick at the corner of my eyes. This jerk!"

    "Before I could protest, I hear the dreaded poof, and he’s back to his figurine self. His form floats to Mystery Sponsor, and I watch as it snaps its fin and Hiroshi disappears."

    # sponsor_hyped
    sponsor "So! Ready for the next one?"

    "I swallow back my anger, genuinely upset that the one person I finally considered a friend got taken away so quickly."

    return

label hiro_choice_bad:
    "It’s awkward. The silence is deafening as Mystery Sponsor waits for something that I want to say. Does it think I’ll defend this man?"

    "I can feel Hiroshi get more and more tense until he swallows audibly and speaks."

    # hiro_sad
    hiro "I’ll be going. I’m… really sorry for everything I’ve done. I hope… you get to move on well and have people by your side to help you fix your situation."

    "I don’t even want to look at him. I nod quietly and cross my arms."

    mc "...yeah."

    "I hear him sigh, and I hear the poof that frees me from the shackles of his company. I see the figurine float to Mystery Sponsor, and I watch as it snaps its fin and Hiroshi disappears."

    # sponsor_hyped
    sponsor "So! Ready for the next one?"

    "I look down to the ground dejected, feeling empty."

    return