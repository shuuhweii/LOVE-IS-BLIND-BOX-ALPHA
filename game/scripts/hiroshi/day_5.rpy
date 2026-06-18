    # HIROSHI'S DAY 5

define mc = Character("MC", color="#FFFFFF")

label hiro_D5:
    "I find myself seated in the dining area again, this time actually seeing the kitchen and dining room in full view."
    "My floors are clean, the countertops and my stove free from the mess of food paperbag deliveries,
    and there isn’t an unpleasant odor wafting in the air."
    "It’s… actually liveable."

    "I’m still in a daze as I watch the sunrays light up my dining room, the atmosphere becoming warm and friendly."
    "There’s a tiny bit of melancholy resting in my head as I remember the times when I would stay here until morning just working."

    "A soft, gruff voice cuts through my daydreaming."

    # show hiro neutral
    hiro "[name]?"

    mc "Huh? Did you say something?"

    hiro "Good morning. I was asking how you like your coffee?"

    "I hear the hum of the espresso machine beeping, signaling that the coffee was ready."
    "I  shake my head to focus."

    # if hiro_affinity_positive:
        # call hiro_D5_good

    # elif hiro_affinity_negative:
        # call hiro_d5_bad
    call hiro_d5_bad

    return

label hiro_D5_good:
    # menu:
    #     "Sorry. Um, with sugar.":
    #     "Just black.":
    return

label hiro_D5_bad:
    menu:
        "I don't want coffee.":
            pass
    
    "I see him nod."

    hiro "Is there another drink you prefer? Something warm?"

    mc "I think I just want hot water."

    "I see him tilt his head."

    hiro "Alright. Give me a moment."

    hide hiro

    "He sets up the kettle on the side and tends to my request.
    I wait patiently and watch him serve me the hot water, handing me the mug with care."

    "As I wrap my fingers around the warm mug, I let the heat seep onto my palms and I sigh in comfort."
    "He looks at me with gentle eyes before speaking."

    # show hiro neutral

    hiro "Is there anything you would like me to make for breakfast today?"

    "I shake my head slowly, sipping my hot drink."

    mc "No, actually. I'd like you to sit down. I wanna talk about something with you."

    # hide hiro

    "He gulps nervously, but he pulls a chair out anyway, placing his own mug down on the table."
    "He sits and folds his hands over one another and nods."

    # show hiro neutral

    hiro "Talk about what?"

    mc "Well... first things first. Where did you put my piles from yesterday?"

    "Hiroshi points to two boxes situated on the floor near the cabinet, filled with the items I sorted yesterday."
    
    hiro "I didn't throw anything away. They're stacked inside those boxes and I trust that you know what to do with them without me."

    "I nod quietly, eyeing the containers. Then my gaze falls back to him."
    "He starts shifting in his seat nervously."
    
    hiro "Um... was that what you wanted to talk about? Or..."

    menu:
        "I'm really grateful for your help for the past few days. But...":
            pass
    
    "He looks at me like he knows what I'm about to say."

    mc "I just..."
    mc "I don't feel like I'll really be able to ever be comfortable with you."
    mc "You're just..."
    mc "... the things you did just..."

    # show hiro sad
    hiro "... take your time. I'm listening."

    "I rest my elbow on the table, rubbing my temple in frustration."

    mc "Everything you did and said for the past few days... I cannot and will not be able to forgive you, or move on from it."
    mc "It feels overwhelming to me, and I do not appreciate the fact that when I was considering the choice of trusting you,"
    mc "you go ahead and do something I never thought another person could do to others."
    mc "Your behavior... is too much to me."

    "His gaze drops to his hands, completely avoiding my stare."

    mc "I... I think you can be a good person in your own way."
    mc "But I don't think I want to be the one to see you through that."
    mc "I... don't want to be the one to stay and understand you through all the mistakes you're bound to make."

    "When I finish telling him what I wanted to say, I feel a weight lift off my shoulders."
    "But... I don't really feel good about it."

    # show hiro sad
    hiro "I... alright. I'm sorry. For everything."

    # hide hiro
    "Nothing is said after that. We continue to sip our own drinks under the heavy weight of my confession, and I despise the feeling."
    "It's not like I loathe him, but it doesn't feel right either if we continue to be with each other for longer."
    "I hope by the end of the week, I can talk to Mystery Sponsor to ask to take Hiroshi back."
    
    mc "... do you have any idea how to summon Mystery Sponsor?"

    "He shakes his head without uttering a single word."

    mc "...do you think he’ll... take you back?"
    mc "After the whole deal, since we kind of fulfilled our end."

    "He doesn’t even meet my eyes. He simply shrugs, refusing to communicate properly or speak."
    "I feel the tension at an all time high. It’s so quiet you could hear a pin drop."

    mc "...are you hungry?"

    "..."

    # show hiro sad
    "No, no."

    "He doesn’t really offer anything after that, either. No mention of wanting to cook for me... or any conversation either."

    "I hate this."
    "I hate this I hate this I hate this."

    mc "I'm... going back to my room."

    "He turns his back on me and sighs, standing up to go to the kitchen counter."

    hiro "Yeah, just... just leave your mug. I’ll clean up."

    "I nod quietly and push the mug away from me, standing up and feeling the coldness in the air despite the morning sun shining through the dining room windows."
    "When I get back to my room, I make sure to shut the door and lock it. I lie down and contemplate what I had just said."

    "It’s not my fault. I just… I don’t entirely hate him."
    "But I don’t think I could stand the feeling of him being around me, and I don’t think I can have any kind of amicable relationship with him knowing what he had done in his past, to me, and the kind of person he is when he gets on edge or upset."
    "It’s like I can never be in any kind of wrong, and I can’t ever be safe around him."

    "I cover my face in my pillow. I know the day just started, but I just want it to be over already."
    "I can hear his footsteps dragging across the floor from outside. I wonder if he’s still cleaning, or… what is he doing?"

    "I shake my head. I shouldn’t even be thinking about it anymore. The deal has been fulfilled, and I just have to wait for what tomorrow will bring."
    "In a tired state, I roll to my side on the bed, shutting my eyes, and waiting for sleep to claim me once more."

    return