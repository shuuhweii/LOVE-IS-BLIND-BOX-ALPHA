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

    return