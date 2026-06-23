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

    menu:
        "Positive Hiroshi Affinity Branch":
            call hiro_D5_good
        "Negative Hiroshi Affinity Branch":
            call hiro_D5_bad

    return

label hiro_D5_good:
    menu:
        hiro "How do you like your coffee?"
        '"Sorry. Um, with sugar."':
            call hiro_D5_good_A1
        '"Just black."':
            call hiro_D5_good_A2

    "As I wrap my fingers around the warm mug, I let the heat seep onto my palms and I sigh in comfort."
    "He looks at me with gentle eyes before speaking."

    # show hiro neutral
    hiro "Is there anything you would like me to make for breakfast today?"

    "I shake my head slowly, sipping my hot drink."

    mc "No, actually. I'd like you to sit down. I wanna talk about something with you."

    "He gulps nervously, but he pulls a chair out anyway, placing his own mug down on the table."
    "He sits and folds his hands over one another and nods."

    hiro "Talk about what?"

    mc "Well... first things first. Where did you put my piles from yesterday?"

    "Hiroshi points to two boxes situated on the floor near the cabinet, filled with the items I sorted yesterday."
    
    hiro "I didn't throw anything away. They're stacked inside those boxes and I trust that you know what to do with them without me."

    "I nod quietly, eyeing the containers. Then my gaze falls back to him."
    "He starts shifting in his seat nervously."
    
    hiro "Um... was that what you wanted to talk about? Or..."

    menu:
        hiro "Um... was that what you wanted to talk about? Or..."
        '"I realized we have a lot of things in common."':
            call hiro_D5_good_romance
        '"We\'re messed up."':
            call hiro_D5_good_platonic

    return

label hiro_D5_good_A1:
    # show hiro happy

    "He nods and starts to prepare the drink just the way I like it."

    hiro "I like it sweet, too. I might have a bias for sweeter things, actually."

    mc "Hm. Really?"

    hiro "Yeah. I love eating dessert."
    hiro "How many spoons of sugar?"

    menu:
        "How many spoons of sugar?"
        "Tell him your preferred amount.":
            # show hiro neutral

            hiro "Got it. Here."
        "Ask how many he puts in his.":
            # show hiro flustered

            hiro "Um, why do you wanna know?"

            mc "Why don't you wanna tell me? Is it an embarrassing amount?"

            "He gives me a bashful look and frowns."

            hiro "There's no such thing as an embarrassing amount of sugar... is there?"

            "I grin softly."

            mc "Maybe. I want as much sugar as you do."

            "He shakes his head and chuckles."

            # show hiro happy

            hiro "Alright, alright. I got it. Here."

    "He hands me the steaming cup of coffee with a gentle smile."

    return

label hiro_D5_good_A2:
    # show hiro neutral

    hiro "Got it. Can't say you look like a black coffee enjoyer."

    # hide hiro

    "I hear him pouring my drink."

    menu:
        "I'm not.":
            # show hiro neutral
            hiro "Oh?"

            "He hands me the mug full of freshly brewed coffee, and I take a small inhale before answering."

            mc "Yeah. I just need to be awake right now."
        "Am I supposed to look a certain way to enjoy black coffee?":
            "He looks back at me with an embarrassed expression and shakes his head."

            # show hiro flustered
            hiro "I-I don't think-- no, of course not."

            "I roll my eyes and grin. He huffs softly."

            hiro "You're teasing me again."

            mc "When aren't I?"

            hiro "You're unbelievably mean."

            mc "And you're easy to tease."

            "He has a tight lipped smile on his face when he arrives with my mug, trying not to laugh."

            hiro "Here you go."
    return

label hiro_D5_good_romance:
    # show hiro flustered
    "A blush forms on his cheeks. I don't think I'll ever get tired of seeing that."

    hiro "What... makes you say that?"

    "My grip tightens around the warm mug, and I feel my own face heating up. Tapping the side of the ceramic, I inhale deeply before talking."

    mc "I believe we both lost ourselves in our selfish desire. The desire to fill the void within ourselves, because indulgence felt much better than changing ourselves for the better..."

    # show hiro neutral
    "He looks at me intently, his hands clasped a bit more tightly now."

    mc "I'm... selfish. I want..."

    hiro "Yeah?"

    menu:
        hiro "Yeah?"
        '"I want you."':
            $ hiro_D5_good_romance_A = "want you"
        '"I want us."':
            $ hiro_D5_good_romance_A = "want us"

    # show hiro flustered
    hiro "W-what?"

    "I give him a nervous smile. I can hear my own heart race faster."

    if hiro_D5_good_romance_A == "want you":
        mc "I... want to be selfish. I want you to stay and we can figure out how we can be better people, because I know we could be so much better."
        mc "I know we’ve had our ups and downs the past few days, but nothing would make me happier than discovering what life could be like with you around."
        mc "You... make me want to be better."
        
        "Is this what it feels like to be embarrassed around him? His awkward little smile is a full blown grin now as he processes my words."
        
        hiro "[name]..."

        "He swallows, his Adam's apple bobbing up and down."

        hiro "Are... you sure? It's... I hope that's not coming from me pressuring you or anything..."

        "I shake my head vehemently."
    elif hiro_D5_good_romance_A == "want us":
        mc "I know we have our differences. Not to mention that you’re probably not even in the same world or timeline as me."
        mc "But... I think we’re good motivators for one another. To be better people. To try and move on from our mistakes in the past."
        mc "I... don’t feel scared thinking about what would happen next when you’re with me. I... feel like I’m safe when I’m with you."
        
        "Is this what it feels like to be embarrassed around him?"
        "He looks at me with gentle eyes and swallows, his Adam's apple bobbing up and down."

        hiro "Don’t… don’t just say things like that. Not after what I’ve done."
        hiro "What if I hurt you again?"

        "I shake my head vehemently."

        mc "Hiro. I want us to stay together. Won’t you do that for me?"

        "He shifts in his seat nervously, playing with his thumbs."

        hiro "I... don’t want it to come from a place of pressure or anything."

        mc "I want us, Hiro."
    
    mc "Please?"

    "To my surprise, he quickly stands up and turns around, covering his face with his hands."
    "He whines and groans in what I assume is excitement he could no longer contain."

    hiro "Goddammit, [name]..."

    mc "D-did I say something wrong?"

    "He turns to me abruptly with a helpless look with longing in his eyes."

    hiro "No, no. God, I could never say no to you. I don't ever want to dny you anything you want."
    
    "He puts his hand over mine, and I swear I could feel the heat of his touch increase tenfold when our skin makes contact."

    hiro "I... am so glad you feel the same way."
    hiro "I can’t promise that I won’t ever make mistakes, but I can promise that I’ll do everything that will help us be better people."
    hiro "For ourselves. Together."

    "He nervously brings my hand up to his lips, and kisses the back of my hand."

    # show hiro happy
    hiro "I promise."

    "I grin and cup his cheek gently, seeing the smile spread across his face."

    mc "You’re such a cheeseball."

    "He chuckles lowly and places his palm over my hand."

    # show hiro flustered
    hiro "You could say whatever you want, but I’m not the one who confessed their emotions first."

    menu:
        hiro "You could say whatever you want, but I’m not the one who confessed their emotions first."
        "Wow. Do you want me to take it back?":
            call hiro_D5_good_romance_B1
        '"What else was I supposed to do?"':
            call hiro_D5_good_romance_B2

    # TODO: SHOULD still be showing hiro happy here, but check if not
    # idk like a console log or smth
    "He gives me a cheesy grin and sighs softly."

    hiro "You know... we have the rest of the day for ourselves. Is there something you wanna do together?"

    mc "...I think I kind of want to rest for today. Maybe we could have breakfast on the balcony for today."

    hiro "I’d really love that. Is there anything in particular you want to eat?"

    menu:
        hiro "I’d really love that. Is there anything in particular you want to eat?"
        '"Something light. Can you cook something for me?"':
            "He doesn’t even hesitate. He pulls me up from my chair and leads me to the pantry, smiling contently."

            hiro "I’ll do my best and try to cook whatever request you have."

            # hide hiro

            "I point out the ingredients he needs to cook the dish I wanted, and he gets to work right away."
            "I smile as I observe him keenly, the way his hands are actually so careful with managing everything."
            "It’s a perfect mix of soft and rugged..."

            "I just noticed how veiny his hands are."
            "What the hell."
            "I can see them trail delicately down to his wrist where his gold watch shimmers..."

            # show hiro happy
            hiro "Are you enjoying the show?"

            "He’s looking at me with a sly smile. I looked away, embarrassed, not knowing I was staring."

            mc "Sorry."

            hiro "Don’t be. I’m glad you are."

            "How the hell is he suddenly saying these things so boldly? Or maybe he doesn’t know the implications?"
            "Why am I rationalizing this?!"

            # hide hiro

            "I purse my lips and look away, waiting for my face to mellow down from being so flushed as he cooks breakfast."
        '"Something heavy. I think we can order food for today."':
            "He tilts his head, looking a bit worried when I say that."

            show hiro neutral
            hiro "Order? I thought you didn’t have money?"

            "I roll my eyes."

            mc "Do you or do you not want breakfast?"

            # show hiro happy

            "He chuckles and raises his hands in surrender."

            hiro "Of course I do. But I’m also trying to think responsibly here."

            mc "It’s fine. I can pay for it... but just for today..." 

            "..." # Are they fucking

            mc "... and you get the food downstairs."

            # hide hiro

            "We settle in the dining area and I pull up my phone, browsing through different cuisines until we finally settle on one we both think would be delicious for today."
            "I press the order button and we wait."
            "Of course, I made him go fetch the food right outside the door."

    "As we carry the plates and our food, I realize that I’ve been blinded by the cleanliness of my kitchen to the holy mess that is in the other parts of my house."
    "I frown when I see the mess and clutter gathered on my balcony, but I feel a warm pair of hands rest on my shoulders to stop me from getting upset."

    # show hiro neutral

    hiro "Hey. We’ll do something about this, okay?"
    hiro "Would you like that, or would you like to just eat breakfast?"

    mc "... balcony."

    # show hiro happy
    "He smiles warmly."

    hiro "Okay, okay."

    # hide hiro

    "To my disdain, he starts another plan to efficiently get rid of the mess that stays in my balcony, but I complain and tell him I am not about to do the pile system he suggested yesterday."
    "We take turns explaining our sides, but eventually settle with my decision in the end."

    "I pick up and collect all the trinkets I could find and dump them all on my living room floor."
    "He goes to the balcony with a broom and dustpan and sweeps all the trash up, putting them in the garbage bag he took from the pantry."
    "It doesn’t take us long until the place is actually decent. He takes it a step further and wipes down the chairs and table we plan on using."

    mc "You could have just wiped the table down. I don’t mind sitting on a mildly dirty chair."

    # show hiro happy
    hiro "I do. And I think it would be good for you too if we sat on something actually clean."

    mc "What’s that supposed to mean?"

    "He chuckles at me and just smiles."

    hiro "Come on. Let’s have breakfast."

    # hide hiro

    "We grab our food from the dining room table and set it properly on the balcony table."
    "The view outside feels so, so much more refreshing compared to the constant clutter I’m used to inside my own home."

    "We sit down and eat in silence, watching the people downstairs go about their morning as they normally would."
    "There’s a sense of normalcy and peace as we observe them from a distance, and I must have been frowning a little too hard when Hiroshi speaks up."

    # show hiro neutral
    hiro "[name]. What's on your mind?"

    menu:
        hiro "[name]. What's on your mind?"
        "Those people downstairs...":
            pass
        '"I feel melancholic."':
            pass
        '"A lot of things."':
            pass

    mc "I kind of feel like I’m lagging behind."
    mc "Up until this point, it felt like my life didn’t have any chance for a hopeful change."
    mc "I got so used to the clutter and mess that I didn’t think about what it would be like if I had someone I cared about who saw my turmoil."

    "I see him from the corner of my eye put down his utensil and lean closer."
    # hide hiro
    "I continue to look over the people below, my lips curving to a smile."

    mc "I feel like a cornball for contemplating out loud. But..."
    mc "I feel comfortable enough with you."

    "I turn my head to gaze at him, my eyes soft."
    # show hiro happy

    mc "I hope that’s okay with you."

    hiro "It is. I care about you too, [name]."

    # hide hiro
    "The silence that follows is comfortable and warm. I steal a glance and his expression is..."
    # show hiro neutral
    "... not entirely calm, but not super anxious either."

    hiro "After all this... I don’t know."
    hiro "I’m just... feeling nervous about starting over."

    # show hiro happy

    hiro "... but I’m glad it’s with you."
    
    return

label hiro_D5_good_romance_B1:
    "He gives me a playful grin."

    # show hiro happy
    hiro "What, now you can't stand by your words? You're usually so prideful."

    mc "Ah, since when did {i}you{/i} learn to talk back?"

    hiro "Hmm."
    hiro "There's this brat I've been stuck with for a couple of days now, and her attitude is really starting to rub off on me."

    "I pull my hand away and cross my arms, smirking."

    mc "Really now?"

    "Hiroshi chuckles and takes my hand again, caressing the back of it with his thumb slowly."

    hiro "Yes. She's very lucky that I learned how to be patient."

    mc "Did she teach you that, too?"

    hiro "Maybe. But you know what else I learned?"

    mc "What is it?"

    hiro "I learned that I really like her. Through everything."

    "I rolled my eyes and laughed, the mood in the kitchen shifted to something warm and welcoming."

    return

label hiro_D5_good_romance_B2:
    "Hiroshi shrugs and gives me a genuine smile."

    # show hiro happy
    hiro "Maybe... not tell me?"

    mc "So you would rather not know I wanted you?"

    hiro "I didn’t say anything like that."
    hiro "I said maybe."

    mc "You’re a dick."

    "He laughs at me and leans his face into my palm."

    hiro "So quick to be vulgar. You think we can work on that when we’re together?"

    menu:
        hiro "So quick to be vulgar. You think we can work on that when we’re together?"
        '"No, you dick."':
            $ hiro_D5_good_romance_B2a = "not lewd"
        '"Fuck fuck fuckity fuck fuck."':
            $ hiro_D5_good_romance_B2a = "not lewd"
        '"Work on what? My mouth?"':
            $ hiro_D5_good_romance_B2a = "lewd"

    if hiro_D5_good_romance_B2a == "not lewd":
        "Hiroshi shakes his head and smiles cheekily."

        hiro "That’s my bad. I forgot you do what you want when you want to."
    elif hiro_D5_good_romance_B2a == "lewd":
        "He tilts his head even more to my palm and grins."

        hiro "Say that again?"

        menu:
            hiro "Say that again?"
            '"You heard me."':
                "He chuckles and smiles dreamily."
                # "I can feel his warm breath on my hand right where he's nuzzling into it."

                "He sits up straight and rests his chin on the back of his hand."

                hiro "I know."
                hiro "But I’m not allowed to say anything beyond this due to my contract, so I’ll let you imagine the response you want me to do."
                hiro "Keep it a secret from the devs working on this, yeah?"

                # hiro "But I’m not allowed to {b}say{/b} anything beyond this due to my contract, {i}but{/i}..."

                # "His fingers tighten around mine as he draws nearer."
                # "He keeps my hand pressed to his cheek, hooking one leg against the side of my chair."
                # "Then he dips toward me, and--"

                # hide hiro
                # fade to black here, add a wait time

                # "Hiroshi pulls away from me, straightening his clothes."
                # "He takes his thumb, and wipes a thin trail of wetness from the corner of his mouth."

                # show hiro happy

                # hiro "... I’ll let you fill in the blanks yourself."
                
                hiro "Keep it a secret from the devs working on this, yeah?"
            "Repeat what you said.":
                "He shakes his head, smiling and checking his surroundings before leaning it to whisper."

                hiro "I apologize, but due to my contract I can’t entertain that kind of retaliation."
                hiro "I’ll let you imagine the response you want me to do, just..."
                hiro "Make sure to keep this a secret from the devs, yeah?"

    return

label hiro_D5_good_platonic:
    "He blinks."

    # show hiro flustered
    hiro "What?"

    mc "...we’re messed up, Hiro."
    mc "We both lost ourselves in our selfish desire. The desire to fill the void within ourselves, because indulgence felt much better than changing ourselves for the better."
    
    # show hiro neutral
    "He swallows nervously, not knowing what to say."
    
    mc "..."

    hiro "..."

    mc "... but do you know what else I learned?"

    hiro "... what?"

    "My lips quirk up to a smile."

    mc "... you helped me get out of my rut. Even if it was... unwilling."

    # show hiro happy

    "I hear him laugh. Genuinely. The sound of it brightens up the mood."

    mc "I got so lost in my own misery that I forgot what it’s like to have someone else see me like this."
    mc "Having someone occasionally invade your headspace... is actually quite nice."

    # show hiro neutral

    "He sips his drink, listening closely. I look at him seriously, tapping the side of my mug."

    mc "I know we... had our differences."
    mc "And as much as I wanted to stay upset at you, I know it won't get us anywhere. And you seem to understand not to push it when I'm upset."

    # show hiro happy

    "I grin, and he chuckles softly."

    mc "Imagine if we had other people. Friends that help us get out of our minds every once in a while."
    mc "Wouldn't you like that?"

    # show hiro neutral

    "There's a moment where he quietly debates with himself on what his response is going to be."

    hiro "... I'm not used to... people."

    mc "You got used to me, didn't you?"

    hiro "In a sense, yes... But I'm not sure just how good it would be if there were more."
    hiro "You miss your... companions, right?"

    mc "... I do. All the time."

    "Things get quiet between us as we look down on our drinks, sipping and simply contemplating."

    menu:
        "Things get quiet between us as we look down on our drinks, sipping and simply contemplating."
        "Tell a story about your friends.":
            mc "I used to go out all the time."
            mc "I really liked to just... explore new cafes and stuff with my friends. They were also the ones that taught me about the latest hype with everything."
            mc "Latest bands, trending things... stuff like that."
            mc "There are days where we don’t really meet each other because of our schedules, but they were always down to call with me if I had asked."
            mc "They also reached out to me to keep me updated on their lives and I... felt the most loved when they did."
            mc "I cared about them a lot."
        "Tell a story about your workmates.":
            mc "I used to work in an office full of... a lot of interesting people."
            mc "Despite our differences, we were all amicable towards one another. I liked my job too, but... the people there were usually the ones that made me want to go to work everyday."
            mc "The cubicle conversations, the after meeting talks, the team building activities... I think management knew what they were doing, because I enjoyed them all. Even during late night overtime work and tiring shifts... They kept morale up."
            mc "They honestly kept me going and made me forget how hard work could be."
        "Tell a story about your family.":
            mc "I used to live with my family."
            mc "They were always so supportive of what I do, no matter how ridiculously ambitious my dreams were. I believe they’re the reason why I was successful."
            mc "If it wasn’t for their encouragement, I wouldn’t be brave enough to even move out and live on my own."
            mc "I didn’t want them to think that I always relied on them... so I stopped asking for help."

    mc "They shaped the person I am."
    mc "But... I got lost with myself during the pandemic, and did no work maintaining my relationships because I felt too ashamed."

    mc "They were always there for me, and I feel bad that we basically had no contact for the past years."
    mc "I want to try and reach out now... because of you."
    mc "You made me remember what it's like to have people to care about, and have people care about you."

    # show hiro flustered
    "His face flushes, and I chuckle."

    mc "I'd love to introduce you to them."

    # show hiro neutral
    hiro "... You would? What if they don't like me? And, it might be too much of a hassle to you..."
    hiro "Don't you think I've taken up enough of your time and space?"

    mc "Inconvenience is the price for community, Hiro. I don't mind, if ith elps you and I grow out of our shells."

    "He puts his lips in a thin line before looking down again, stirring his sweetened coffee."
    # show hiro happy
    "Then, he smiles."

    hiro "... I'd like that. As long as you promise not to leave me alone."

    mc "Let me think about it..."

    "He gives me a shy look. We take in the quiet morning, the way the dining room feels so much nicer after everything has been cleared and cleaned."
    "I take a sip of my drink."

    window hide

    menu:
        '"What do you think will happen tomorrow?"':
            window show
            
            # show hiro neutral
            "He sighs heavily."

            hiro "I have no idea."
            hiro "I mean, after helping you I assumed I'll just disappear, or turn back into a figurine. I feel quite silly thinking about it."
            hiro "But then again... I do feel apprehensive thinking that I could just... be gone again."
            hiro "Just like how I was gone from my world."
        '"What do you think of me?"':
            window show

            # show hiro flustered
            "He sighs softly."

            hiro "I think you have a lot of potential to get back up again."
            hiro "I know for the past few days, I probably saw nothing but your lowest points... but with what you've told me, you're so much more capable than I ever feel like I will be."
            hiro "You have a lot of life to look forward to."
        '"What are you thinking right now?"':
            window show

            # show hiro neutral
            "He sighs quietly."

            hiro "Just... a lot of things that have happened so far."
            hiro "Being poofed, meeting you, helping you clean up... and figuring out who you are as a person."
            hiro "I feel overwhelmed from everything happening in such a small amount of time..."

    # show hiro neutral
    hiro "... But all that aside, is it okay to assume that we're... friends?"

    menu:
        hiro "... But all that aside, is it okay to assume that we're... friends?"
        '"Yes, of course."':
            pass
        '"Maybe."':
            pass
    
    # show hiro happy

    "He looks to the side smiling and fidgets with his hands."

    hiro "I'm glad. Thank you."
    hiro "... For being a friend."

    "I chuckle at the cheesiness of the situation. Though I really do appreciate how far he had come in just a span of a week."

    mc "We have the entire day for ourselves. Is there anything you wanna do?"

    # show hiro flustered
    hiro "If you wouldn't mind... I could continue helping you set up the keep pile for the trinkets you chose."

    "I'm already giddy just thinking about decorating the place."

    mc "Really?"

    # show hiro happy
    hiro "Of course."

    mc "Okay, okay. Only if you let me yap about why I got those things."

    # show hiro flustered
    hiro "Y-yap?"

    mc "Talk. I'm going to infodump you on those purchases."

    hiro "Info... dump?"

    # show hiro happy
    "As I'm about to explain again for the third time, he has a sly grin on his face."
    "He's making fun of me!"

    mc "You knew what I meant and still made me talk!"

    "I shove him playfully and he laughs, rubbing his arm."

    hiro "Sorry. I thought I could try and tease you back."

    "I grin. I like this playful side of him."

    # hide hiro
    "We finish our drinks and he cleans up our mugs. I gather the box with my chosen stuff to keep to the table and place them down gently."
    "I pull the chair back to sit down again and rest my cheek on my palm, contemplating where I should put them. I hear the water stop running and Hiro coming over to sit next to me."

    # show hiro happy
    hiro "Go ahead. Where do you want to start?"

    "Smiling, I pull out all the items in the box and describe in detail the absurdity of how and why I got them."

    mc "I got this limited edition Gisney’s Royal and the Animal Luminous candle holder from my parents when I first moved to this apartment."
    mc "I told them it was my favorite movie from when I was like, 8, and they never let me live it down."

    "I place the golden holder down and take another item. I can see him smiling in the corner of my eye."

    mc "This is a rare misprinted vinyl record of my favorite band, GABBA."
    mc "I knew I had to get it because I was given a record player as a reward for rising up the ranks in my job."
    
    hiro "In your bedroom? We could try setting it up here in the dining area away from your cooking area to at least give the place some ambience."
    
    mc "And this one is my 2003 release, glass forged Thomathy and Jeremiah flower vase I bought when I was in Comic Bunch Studios with my friends to see their favorite artists’ work."
    
    # hide hiro
    "For the rest of the day, I tell him the origin stories of all the collectibles I’ve gathered over the years I felt that I truly wanted to keep. He helps me put it all up around the kitchen and dining area where it won’t be too cluttered and obstructive."
    "There’s a pensive silence when we look around and see them all placed with purpose. I cross my arms quietly, and I feel his hand pat my shoulder."

    # show hiro happy
    hiro "You chose well."

    mc "Thanks. And... thank you for helping me."

    hiro "Anything for a friend."

    "I snort and playfully punch his arm, both hating and loving his response."

    "My god, he's so painfully cheesy."
    return

label hiro_D5_bad:
    menu:
        '"I don\'t want coffee."':
            pass
    
    "I see him nod."

    hiro "Is there another drink you prefer? Something warm?"

    mc "I think I just want hot water."

    "I see him tilt his head."

    hiro "Alright. Give me a moment."

    # hide hiro

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
        '"I\'m really grateful for your help for the past few days. But..."':
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