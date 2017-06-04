label scene_03:
    $ cg_scene = "firethronezoom"
    $ cg("base", "headdefault","d_mclosed", "d_bcocked", "d_eaimedup", "d_armlegl", "d_armlegr", "foreground_flames1", "blank")
    $ black("hide")
    "The young Fire Lord seems fairly agitated today. She rushes you through your report, repeatedly displaying the kind of impatience you've recognized in less experienced military officers. Once you finish, you give her a short bow, hoping that she doesn't insult you for taking too long."
    $ cg("base_02", "p_armleg","p_mclosed", "p_bnormal", "p_eplayer", "blank", "blank", "foreground_flames2", "blank")
    "Azula quickly stands up and walks over to the edge of the platform, parting the flames with just a flick of her finger. You mentally brace yourself for some kind of attack, but instead she simply sits down and informally hangs her legs over the raised stone." #azula pose 2
    $ changeAzula("neutral")
    $ cg(effect_3="p_mtalking")
    a "What do you think of me, boy?"
    $ cg(effect_3="p_mclosed")
    pc "My Lord?"
    $ changeAzula("stern")
    $ cg(effect_3="p_mtalking", effect_4="p_blonging")
    a "Your thoughts about Fire Lord Azula."
    pc "I don't know how you mean, my Lord."
    $ cg(effect_3="p_mclosed", effect_4="p_bangry")
    "She scoffs condescendingly, looking at you as if you were a child."
    $ changeAzula("annoyed")
    $ cg(effect_3="p_mtalking")
    a "The first thing that comes to mind!"
    $ cg(effect_3="p_mclosed")
    pc "Powerful."
    $ changeAzula("mad")
    $ cg(effect_3="p_mtalking", effect_4="p_bpissed", effect_5="p_eside")
    a "Ugh…"
    $ cg(effect_3="p_mclosed")
    "Perhaps regretting her decision to speak further with you today, Azula glances off, further down the chamber."
    $ changeAzula("bemused")
    $ cg(effect_3="p_mtalking", effect_5="p_eplayer")
    a "More than just a word, [pc_name]."
    $ changeAzula("stern")
    $ cg(effect_4="p_bangry")
    a "Try a sentence for a change."
    $ changeAzula("neutral")
    $ cg(effect_4="p_bnormal")
    a "It might do you some good to think a little more about your answers from this point on."
    $ cg(effect_4="p_bhappy")
    $ changeAzula("happy")
    a "You're not a soldier anymore, so don't act like one."
    $ cg(effect_3="p_mclosed")
    pc "As you wish, my Lord. I think-"
    $ changeAzula("annoyed")
    $ cg(effect_3="p_mtalking", effect_4="p_bpissed")
    a "And be honest with me!"
    $ cg("base_02", "p_armleg","p_mclosed", "p_bnormal", "p_eplayer")
    menu: 
        "Cold and lonely":
            pc "With respect, you're a very cold and cruel person. There's nobody else I'd rather serve under, but you're terrifyingly powerful and you don't seem to care how you affect others."
            "You hesitate, waiting to see her reaction before you continue. She appears emotionless, as if you hadn't spoken at all."
            $ changeAzula("neutral")
            $ cg(effect_3="p_mtalking")
            a "Go on."
            $ cg(effect_3="p_mclosed")
            pc "And yet, I fully believe you understand that. As someone who has been feared by even my own comrades, I know how lonely that can be. I see the same in you, though I can only imagine the magnitude of your loneliness."
            $ changeAzula("stren")
            $ cg(effect_3="p_mtalking", effect_4="p_bstern")
            a "You're right."
            $ cg(effect_3="p_mclosed",effect_4="p_bpissed",effect_5="p_eside")
            "Again, the Fire Lord glances away, but this time she appears wistful."
            $ changeAzula("disappointed")
            $ cg(effect_3="p_mtalking")
            a "I have been feeling very lonely as of late..."
            $ cg(effect_3="p_mbiting",effect_4="p_bstern", effect_6="p_eplayer", effect_5="p_erelax")
            "Azula gives you the same look as she did at the end of your last conversation. This kind of attention isn't what you expected when your superior pushed you into this position."
            #azula2 sex-hungry
            $ changeAzula("happy")
            $ cg(effect_3="p_mtalking", effect_4="p_bhappy", effect_5="p_eplayer", effect_6="blank")
            a "...though now, at least, I have someone interesting to talk to."
            $ cg(effect_3="p_mclosed")
            pc "I'm always yours to command, my Lord."
            $ changeAzula("neutral")
            $ cg(effect_3="p_mtalking", effect_4="p_bnormal")
            a "Yes, I know."
            $ changeAzula("happy")
            $ cg(effect_3="p_mtalking", effect_4="p_bhappy")
            a "That will be all for today, [pc_name]."
            $ cg(effect_3="p_mclosed")
            $ black("show")
            "You turn around and slowly walk out of the war room, not wanting to show any disrespect in your haste to leave. Whatever's going on in her mind, you don't want to ruin it just to get back home a few minutes sooner."
        "Fiery but sad":
            $ cg(effect_3="p_mclosed")
            pc "I have the utmost respect for your passion and anger. It would have been an honor to fight for you on the battlefield, under your personal command. The only question would be how crushing a victory we would have."
            "You hesitate, waiting to see her reaction before you continue. She appears emotionless, as if you hadn't spoken at all."
            $ changeAzula("neutral")
            $ cg(effect_3="p_mtalking")
            a "Go on…"
            $ cg(effect_3="p_mclosed")
            pc "But still, it seems like you're a sad person."
            $ cg(effect_4="p_bangry", effect_8="angryflames2")
            "Azula glares at you angrily. If she wasn't literally sitting in the line of fire, you think the flames would have burned the ceiling."
            $ changeAzula("annoyed")
            $ cg(effect_3="p_mtalking")
            a "Sad?"
            $ changeAzula("mad")
            $ cg(effect_3="p_mclosed")
            a "You think I'm sad!?"
            $ changeAzula("stern")
            $ cg(effect_3="p_mtalking", effect_4="p_bstern")
            a "Are you calling me pathetic!?"
            $ cg(effect_3="p_mclosed")
            pc "Of course not, my Lord!"
            $ cg(effect_2="p_armpoint")
            "She points straight down the hall as she takes a deep breath to yell at you. It's time that you left."
            $ cg(effect_3="p_myell", effect_4="p_bangry")
            #azula2 pointing + yell
            $ changeAzula("mad")
            a "Get out!"
            $ changeAzula("annoyed")
            a "You're lucky I don't burn you alive where you stand!"
            $ black("show")
            "Although you think about running, you instead briskly walk out of the war room, not wanting to show any weakness. Besides, that's one display of respect you want to save for when she really looks threatening. Judging by the stories you've heard, what you just saw was nothing."
    
    $ cg("base", "headdefault","d_mclosed", "d_bcocked", "d_eaimedup", "d_armlegl", "d_armlegr", "foreground_flames1")
    $ black("hide")
    "The next time you see Azula, she's perfectly calm, allowing you to deliver your report in a dignified manner. It's hard to reconcile her professionalism with the last couple times you've seen her."
    $ cg("base", "headdefault3","d3_mnormal", "d3_bnormal", "d3_eaway")
    "However, you do notice subtle signs of restlessness. She briefly chews on her lips a few times and occasionally stares away into space at nothing in particular, like she's quietly mulling something over as you report on the state of her nation."
    "Once you reach the end of your report, you give a deep, respectful bow."
    $ cg("base", "headdefault","d_msopen", "d_bcocked", "d_eplayer")
    a "Dismissed, [pc_name]."
    $ cg("base", "headdefault3","d3_mnormal", "d3_bnormal", "d3_eaway")
    "You promptly turn around, thankful to return to a more normal day of military service. Unfortunately, you don't get far before Azula speaks again."
    $ changeAzula("neutral")
    $ cg("base", "headdefault","d_mwopen", "d_bsurprised", "d_eplayer")
    a "Wait, don't go yet."
    $ cg(effect_3="d_mclosed")
    "Taking a moment to roll your eyes before turning around, you wonder how close you'll come to the edge of death today."
    pc "I hope my report satisfied your Lordship."
    $ changeAzula("neutral")
    $ cg(effect_3="d_mclosed", effect_4="d_bcocked")
    a "Yes, it was perfect, like always."
    pc "Thank you, my-"
    $ changeAzula("bemused")
    $ cg(effect_3="d_mwopen")
    a "Last time we spoke, I asked you what you thought of me."
    $ changeAzula("stern")
    $ cg(effect_3="d_msopen", effect_4="d_bangry")
    a "I would like to continue that conversation."
    $ cg(effect_3="d_mclosed")
    "Despite her words, Azula remains exactly where she is, displaying none of the familiarity she showed you last time."
    pc "I'm...not sure what to say, my Lord. I hope you weren't too offended by my rashness."
    $ changeAzula("bemused")
    $ cg(effect_3="d_msopen", effect_4="d_bcocked")
    a "At least you were honest."
    $ changeAzula("neutral")
    $ cg(effect_3="d_msmile", effect_4="d_bconfused")
    a "I expect more of that today."
    pc "(Of course, fuck me…)"
    pc "Of course, my Lord."
    $ cg("base", "headdefault3","d3_mnormal", "d3_bnormal", "d3_eaway")
    "The Fire Lord takes a long pause, as if she's still making up her mind on what to ask you."
    $ changeAzula("stern")
    $ cg(effect_5="d3_eplayer")
    a "Do you think that I'm attractive?"
    pc "Uh…is that a trick question?"
    $ cg("base", "headdefault","d_mclosed", "d_bcocked", "d_eplayer")
    "Without betraying the slightest hint of any motive, she simply cocks her head at you."
    $ changeAzula("happy")
    $ cg(effect_3="d_msmile")
    a "Not much of a trick if I tell you whether it is one or not, [pc_name]."
    pc "Umm…"
    menu:
        "Yes":
            pc "Yes, my Lord."
            $ cg(effect_3="d_mclosed", effect_4="d_bangry",  effect_9="d_eclosing")
            "Azula glares at you. Of course, it was a trick question. In your experience, the nobility never truly want to know what the lower classes think of them."
            $ changeAzula("annoyed")
            $ cg(effect_3="d_msopen")
            a "You hesitated."
            $ cg(effect_3="d_mclosed")
            pc "My Lord, you're a member of the royal family. It's not really my place to-"
            $ changeAzula("stern")
            $ cg(effect_3="d_msopen")
            a "Your place is whatever I decide it to be, so I will ask you again."
            $ changeAzula("mad")
            $ cg(effect_3="d_mwopen", effect_9="blank")
            a "Do you think that I'm attractive?"
            $ cg(effect_3="d_mclosed")
            "There's no point in changing your answer at this point. You decide to actually tell the truth."
            pc "Absolutely, my Lord. You're the most beautiful woman I've ever laid eyes on."
            $ cg("base", "headdefault2","d2_mlaugh", "d2_bhappy", "d2_eclosed")  
            "She lets out a short, hollow laugh, as if your answer didn't even matter."
            $ changeAzula("content")
            $ cg("base", "headdefault","d_mwopen", "d_bcocked", "d_eplayer")
            a "Well, that doesn't surprise me."
            $ changeAzula("happy")
            $ cg(effect_3="d_msmile")
            a "Though I have to assume you're not usually in the company of anyone attractive."
            pc "Oh, I've seen by fair share of good pu...-ah, people. Good-looking people, I mean. People who look good."
            $ cg(effect_3="d_mclosed", effect_5="d_erolling")
            "The Fire Lord makes a show of rolling her eyes. Normally, you're more smooth, but this is a conversation like none other you've had in the face of death."
            #more noticable eyeroll in default
            pc "People like you, only worse. I mean, they're worse! Much worse, in comparison to you, my Lord. Because you're-"
            $ changeAzula("bemused")
            $ cg(effect_3="d_mwopen", effect_4="d_bconfused", effect_5="d_eplayer")
            a "Oh, stop blathering already."
            $ changeAzula("stern")
            $ cg(effect_3="d_msopen", effect_4="d_bangry")
            a "It's starting to sound like you're only telling me what I want to hear."
            $ cg(effect_3="d_mclosed")
            pc "(Well, that's not untrue…)"
            pc "Flattery is not my strongest suite, but you are indeed beautiful, Fire Lord Azula."
            $ changeAzula("bemused")
            $ cg(effect_4="d_bcocked")
            a "Hmm…"
            $ cg(effect_5="d_eleftside",effect_6="d_armrub")
            "While Azula rubs her chin, considering your remark, you still honestly can't tell if she actually cared about your opinion. At least it doesn't seem like she's going to kill you for any perceived insolence."
            $ changeAzula("neutral")
            $ cg(effect_3="d_msopen", effect_4="d_bcocked", effect_5="d_eplayer", effect_6="d_armlegl")
            a "That will be all for today, [pc_name]."
            pc "And I-"
            $ changeAzula("annoyed")
            $ cg(effect_3="d_mwopen", effect_4="d_bangry")
            a "I said, that will be all!"
            $ cg(effect_3="d_mclosed")
            $ black("show")
            "You quickly turn back towards the exit and stride out of the war room. All in all, it wasn't that bad of a day. It's almost endearing, in a frightening sort of way, to see Fire Lord Azula so preoccupied about something other than the nation. Then again, you wish it was someone else walking along the razor's edge, even if it is somewhat fascination to watch."
        "No":
            pc "No, my Lord."
            $ cg(effect_3="d_msopen", effect_4="d_bangry",  effect_9="d_eclosing")
            $ changeAzula("mad")
            a "Why not!?"
            $ cg(effect_3="d_mclosed")
            "Though she looks absolutely livid, you sense that Azula is actually restraining herself from sending up a wall of flames, waiting for your explanation."
            pc "My Lord, you're a member of the royal family. I don't even think of-"
            $ cg(effect_3="d_mclosed", effect_4="d_bangry",  effect_8="angryflames1", effect_9="blank")
            "You recoil slightly as the flames erupt upwards. Apparently, your classic strategy of avoidance when it comes to answering nobility does not work so well with royalty."
            $ changeAzula("annoyed")
            $ cg(effect_3="d_msopen")
            a "Are you saying that I have a crude mind!?"
            $ changeAzula("mad")
            $ cg(effect_3="d_mwopen",  effect_9="d_eclosing")
            a "That I don't deserve to be Fire Lord, if I harbor such notions!?"
            $ cg("base_03", "blank","s_mclosed", "s_bmad", "s_eplayer", "blank", "blank")
            "Azula leaps to her feet, assuming a combat stance. It's quickly becoming clear that to say this was not going well was an understatement." #standing
            pc "Of course not, my Lord! But I cannot, in good conscience, answer your-"
            $ cg(effect_2="s_firehands")
            "Even as the words leave your lips, blue death springs to life in the young Fire Lord's hands." #fire
            $ cg(effect_3="s_mtalking",effect_4="s_bpissed")
            $ changeAzula("annoyed")
            a "Get out!"
            $ cg(effect_3="s_mfrown")
            "You're suddenly forced to roll to the side as Azula throws a giant ball of fire at you, though it only lands in front of where you were standing, setting the carpet ablaze." #throwing fire
            $ changeAzula("mad")
            $ cg(effect_3="s_mtalking", effect_6="s_erelax")
            a "You little worm, how dare you speak down to me like that!"
            $ cg(effect_3="s_mfrown")
            "As you run out of the war room, she continues to throw fireballs in your direction, each one landing to either side of your path."
            $ changeAzula("annoyed")
            $ cg(effect_3="s_mtalking", effect_6="blank")
            a "Nothing more than a burly peasant who knows how to use a stick!"
            $ cg(effect_3="s_mtalking")
            "Immediately following your departure, a loud explosion hits the entrance to the war room, blasting the door off its hinges with a loud 'CRACK'. The shockwave knocks you off your feet, but you quickly recover and continue to run away."
            $ changeAzula("mad")
            $ cg(effect_3="s_mtalking")
            a"And don't even think of deserting your post, coward!"
            $ black("show")
            "The infuriated firebender continues to yell after you, but you can't make out what she's shouting as you flee. You don't stop running until you're well beyond the palace walls." #black screen
            pc "Spirits protect me, what am I going to do now!?"
    
    $ cg("base", "headdefault","d_mclosed", "d_bcocked", "d_eplayer", "d_armlegl", "d_armlegr","foreground_flames1", "blank")
    $ black("hide")
    "Just like the beginning of your last encounter, Azula doesn't appear to even remember the last conversation you two had as you report to her, nor does she appear distracted in the slightest. Maybe things have finally returned to normal. "
    $ cg("base", "headdefault3","d3_mnormal", "d3_bnormal", "d3_eaway")
    "You don't really want to wait around to find out. When you're done, you immediately bow and prepare to leave. It's not exactly the proper way of doing things, but you'll take your chances, at least this one time."
    pc "Good day, my Lord."
    "You're halfway through turning around when the young Fire Lord loudly clears her throat, stopping you mid-movement."
    $ changeAzula("neutral")
    $ cg(effect_3="d3_mtalk",effect_5="d3_eplayer")
    a "I didn't dismiss you, [pc_name]."
    $ cg(effect_3="d3_mnormal")
    "Acting as formal as you know how, you turn back towards the Fire Lord and kneel again."
    $ changeAzula("annoyed")
    $ cg("base", "headdefault", "d_msopen", "d_bcocked", "d_eplayer")                 
    a "Oh, you can stand up."
    $ changeAzula("bemused")
    $ cg(effect_3="d_msopen", effect_5="d_erolling")
    a "I'm not going to hurt you."
    $ cg(effect_3="d_mclosed")
    "You hesitantly stand up again, but keep you head bowed. If you can't see her, maybe she won't be able to see you either."
    $ changeAzula("stern")
    $ cg(effect_4="d_bangry", effect_5="d_eplayer")
    a "Hmph…"
    $ changeAzula("annoyed")
    $ cg(effect_3="d_mwopen")
    a "You would do well to look at me, too."
    "Taking a deep breath, you tilt your head up to meet Azula's eyes for the first time today. She manages a weak smile, attempting to assuage your fears."
    $ cg(effect_3="d_msmile2", effect_4="d_bsurprised")
    #weak smile
    $ changeAzula("content")
    a "Naturally, as you know, I'm very intimidating."
    pc "Quite so, my Lord."
    $ changeAzula("happy")
    $ cg(effect_3="d_msmile")
    a "What do you think is my most intimidating quality?"
    menu:
        "Firebending":
            pc "I would have to say your firebending."
            $ cg("base", "headdefault","d_msopen", "d_bangry")
            $ changeAzula("mad")
            a "How lowborn of you."
            $ cg(effect_3="d_mclosed")
            pc "My lord?"
            $ changeAzula("annoyed")
            $ cg(effect_3="d_mwopen")
            a "How many firebenders have you fought alongside, [pc_name]?"
            $ cg(effect_3="d_mclosed")
            pc "Um...I would say-"
            $ changeAzula("stern")
            $ cg(effect_3="d_msopen",effect_5="d_erolling")
            a "It was a rhetorical question, idiot."
            $ changeAzula("mad")
            $ cg(effect_3="d_mwopen", effect_5="d_eplayer")
            a "There are thousands of firebenders in the world, and you think this talent, supremely common in comparison to mine, is my most intimidating quality?"
            $ cg(effect_3="d_mclosed")
            pc "Well, when you put it like that, I guess-"
            $ changeAzula("stern")
            $ cg(effect_3="d_msopen")
            a "No, there's no guessing about it."
            $ cg(effect_3="d_mwopen")
            a "You're simply wrong, admit it."
            $ cg(effect_3="d_mclosed")
            pc "I'm...wrong. Firebending isn't your most intimidating quality."
            $ changeAzula("bemused")
            $ cg(effect_4="d_bcocked")
            a "A little louder."
            $ cg(effect_3="d_mclosed")
            pc "I'm wrong."
            $ changeAzula("stern")
            $ cg(effect_4="d_bconfused")
            a "Still couldn't hear you."
            $ cg(effect_3="d_mclosed")
            pc "I'm-"
            $ changeAzula("happy")
            $ cg(effect_3="d_msmile", effect_4="d_bconfused")
            a "Perhaps a demonstration will help you find an appropriate volume."
            $ cg("base_04", "blank","s_mclosed", "s_brelax", "s_eplayer", "blank", "blank")
            "Azula slowly stands up. You bite your lip, deciding whether you should try to run or not." #standing
            pc "If you...think that's necessary, then…"
            $ cg(effect_2="s_fire2")
            "You feel yourself begin to sweat as blue fireballs appear in her hands. Even if you did run away, she could easily kill you, if she wanted to." #fire
            $ changeAzula("neutral")
            $ cg(effect_3="s_mtalking")
            a "The fire that I bend is blue, because it's hotter than that of others."
            $ changeAzula("content")
            $ cg(effect_4="s_bsurprised")
            a "Do you think I find it hard to control this much power?"
            $ cg(effect_3="s_mclosed")
            pc "You appear to be in complete control, my Lord."
            $ changeAzula("bemused")
            $ cg(effect_3="s_mtalking", effect_5="s_eside")
            a "Oh, I don't know."
            $ cg(effect_3="s_mclosed")
            $ changeAzula("annoyed")
            $ cg(effect_3="s_mtalking", effect_6="s_erelax")
            a "Just the slip of a hand or an awkward stumble and…"
            $ cg(effect_3="s_mclosed", effect_5="s_eplayer", effect_6="blank")
            "Keeping the fireballs aloft, the young Fire Lord silently glares at you. Every instinct you have is screaming to run, but you stand your ground."
            $ changeAzula("stern")
            $ cg(effect_3="s_mtalking", effect_4="s_bmad")
            a "...but I don't slip, nor do I stumble."
            $ cg("base", "headdefault","d_mclosed", "d_bcocked", "d_eplayer", "d_armlegl", "d_armlegr", "foreground_flames1", "blank")
            "You let out a breath you didn't even realize you were holding as Azula extinguishes the flames and returns to a resting position." #default
            $ changeAzula("neutral")
            $ cg(effect_3="d_mwopen")
            a "So, let me hear you say it, loud enough to convince me that you fully understand."
            $ cg(effect_3="d_mclosed")
            pc "{size=+5}I was wrong!{/size}" #emphasis on all
            $ changeAzula("stern")
            $ cg(effect_3="d_mbiting",effect_4="d_bangry", effect_8="d_eclosing", effect_5="d_eplayer", effect_9="foreground_flames1")
            a "Good boy…" #hungry
        "Cunning":
            pc "Your sharp mind. I imagine you're always at least two steps ahead of anyone."
            $ changeAzula("bemused")
            $ cg(effect_3="d_msopen", effect_4="d_bcocked")
            a "Do you mean that you're stupid?"
            $ cg(effect_3="d_mclosed")
            pc "No, my Lord. It's just that you're a genius."
            $ changeAzula("happy")
            $ cg(effect_3="d_msmile")
            a "I am, aren't I?" 
            pc "Indeed, my Lord. With respect, three generations of royals before you failed to take Ba Sing Se, including your own uncle - twice! Yet you took the city without a single casualty."
            $ changeAzula("content")
            $ cg(effect_5="d_erolling")
            a "Mmm-hmm…"
            $ cg("base", "headdefault3","d3_mnormal", "d3_bnormal", "d3_eaway")
            "As she recalls the past, Azula thoughtfully stares into space. Honestly, you would have loved to watch the Dai Li tear down their own walls."
            $ changeAzula("happy")
            $ cg("base", "headdefault3", "d3_mtalk", "d3_bnormal", "d3_eplayer")
            a "We're connected by that, in a way."
            $ cg(effect_3="d3_mnormal")
            pc "My Lord?"
            $ changeAzula("neutral")
            $ cg(effect_3="d3_mtalk")
            a "I took the city and you helped to protect and defend my victory."
            $ cg(effect_3="d3_mnormal")
            pc "Had I known I would one day have the honor of meeting you, I would have enjoyed the fighting much more."
            $ cg(effect_2="headdefault",effect_3="d_mclosed", effect_4="d_bcocked", effect_5="d_eplayer")
            "The young Fire Lord snaps her head back towards you, the magic of the moment broken by her predatory nature."
            $ changeAzula("stern")
            $ cg(effect_3="d_msopen")
            a "But not fight harder?"
            $ cg(effect_3="d_mclosed")
            pc "I always fight as hard as I can, my Lord. That would not have changed."
            $ changeAzula("happy")
            $ cg(effect_3="d_msmile", effect_4="d_bconfused")
            a "Good answer."
            $ cg("base", "headdefault2","d2_myawn", "d2_byawn", "d2_eclosed", "d_armyawn")
            "Nostalgia doesn't seem to interest her. Azula briefly tilts her head back and yawns." #yawn
            $ changeAzula("bemused")
            $ cg("base", "headdefault","d_msopen", "d_bcocked", "d_erolling", "d_armlegl")
            a "It seems such a long time ago, now."
            $ changeAzula("bemused")
            $ cg(effect_3="d_mclosed")
            pc "Of course, your rule over the Fire Nation has been exemplary. I've never seen the people so content and well-provided for."
            pc "(Though most of that is due to the spoils of war…)"
            $ changeAzula("neutral")
            $ cg(effect_3="d_msopen", effect_5="d_eplayer")
            a "That's true, even if tribute and taxes from the Earth Kingdom fund most of my programs."
            $ cg(effect_3="d_mclosed")
            pc "As you say, my Lord."
            $ changeAzula("happy")
            $ cg(effect_3="d_msmile", effect_4="d_bconfused")
            a "You sneaky little boy, you were thinking the same thing, weren't you?"
            pc "Like I said, you're always at least two steps ahead."
            $ cg("base", "headdefault2","d2_mlaugh", "d2_bhappy", "d2_eclosed")
            "Azula lets out an honest chuckle."
            $ changeAzula("content")
            $ cg("base", "headdefault","d_msopen", "d_bconfused", "d_erolling")
            a "Well, it's not hard."
            $ cg("base", "headdefault3","d3_mnormal", "d3_bnormal", "d3_eaway")
            "Sighing heavily, the young Fire Lord again turns her head away from you."
            $ changeAzula("disappointed")
            $ cg(effect_3="d3_mtalk", effect_5="d3_eplayer")
            a "I'm quite bored most of the time, actually."
            $ changeAzula("neutral")
            $ cg(effect_3="d3_mtalk", effect_4="d3_bbored",effect_5="d3_eaway")
            a "My friends are in jail…"
            $ changeAzula("disappointed")
            $ cg(effect_3="d3_mtalk", effect_4="d3_bbored_2")
            a "...the Avatar is dead…"
            $ changeAzula("bemused")
            $ cg(effect_3="d3_mnormal", effect_4="d3_bnormal", effect_5="d3_eplayer")
            a "...and I've long since tired of tormenting his imprisoned companions."
            $ changeAzula("disappointed")
            $ cg("base", "headdefault","d_msopen", "d_bangry", "d_erolling")
            a "I'm stuck here while Father is out having all the fun!"
            $ cg(effect_3="d_mclosed", effect_4="d_bcocked", effect_5="d_eplayer", effect_6="d_armnails")
            "Acting as if you weren't even present, Azula rudely pretends to inspect her fingernails."
            $ changeAzula("neutral")
            $ cg(effect_3="d_mbiting", effect_9="d_eclosing", effect_5="d_eplayer")
            a "I need something new to keep me entertained…" #hungry
        "Ambition":
            pc "It seems that your thirst for power is unquenchable, like you'd do anything to succeed."
            $ changeAzula("annoyed")
            $ cg(effect_3="d_msopen", effect_4="d_bcocked")
            a "And I've been the Fire Lord for four years."
            $ cg(effect_3="d_mclosed")
            "You can already tell from her tone that was absolutely the wrong thing to say."
            $ changeAzula("mad")
            $ cg(effect_3="d_mwopen", effect_4="d_bangry")
            a "Are you saying that I've reached the peak of my power?"
            pc "No, my Lord."
            $ changeAzula("stern")
            $ cg(effect_3="d_msopen")
            a "Then what are you saying?"
            $ changeAzula("mad")
            $ cg(effect_3="d_mwopen")
            a "Are you suggesting that I overthrow my father, throwing the entire nation into civil war even as he conquers the rest of the world!?"
            $ changeAzula("annoyed")
            $ cg(effect_3="d_msopen", effect_5="d_esurprised3")
            a "Do you think I'm a traitor!?"
            $ cg(effect_3="d_mclosed")
            pc "Of course not, my Lord. I was merely trying to compliment you."
            $ changeAzula("mad")
            $ cg(effect_3="d_mwopen", effect_5="d_eplayer")
            a "Compliment me!?"
            $ cg(effect_3="d_mclosed", effect_8="angryflames1")
            "That wasn't much better. The wall of fire separating the two of immediately erupts upwards, making it hard to even see her."
            $ changeAzula("annoyed")
            $ cg(effect_3="d_mwopen")
            a "I asked you what my most intimidating quality was, not for you to insult my honor!"
            $ cg(effect_3="d_mclosed")
            pc "My Lord, I didn't mean it like that."
            $ changeAzula("mad")
            $ cg(effect_3="d_mwopen")
            a "Are you questioning my judgment of your statement?"
            $ cg("base_03", "blank","s_mclosed", "s_bmad", "s_eplayer", "blank", "blank")
            "Azula slowly stands up. You bite your lip, deciding whether you should try to run or not." #standing
            pc "N-no, my Lord."
            $ cg(effect_2="s_firehands")
            "You feel yourself begin to sweat as blue fireballs appear in Azula's hands. Even if you did run away, she could easily kill you, if she wanted to." #fire
            $ changeAzula("stern")
            $ cg(effect_3="s_mtalking")
            a "So you admit that you think my ambition makes me inept, traitorous, and dishonorable?"
            $ cg(effect_3="s_mclosed")
            pc "I would have to say that I...spoke without thinking. Now that you've explained why my answer was so foolish, I think that your ambition, while healthy and measured, is not your most intimidating quality."
            "Keeping the fireballs aloft, the young Fire Lord silently glares at you. Every instinct you have is screaming to run, but you stand your ground."
            $ changeAzula("annoyed")
            $ cg(effect_3="s_mtalking")
            a "Fine."
            $ cg("base", "headdefault","d_mclosed", "d_bcocked", "d_eplayer", "d_armlegl", "d_armlegr", "foreground_flames1", "blank")
            "You let out a breath you didn't even realize you were holding as Azula extinguishes the flames and returns to a resting position." #default
            $ changeAzula("stern")
            $ cg(effect_3="d_msopen")
            a "I suppose your inferior blood can excuse your obvious lack of intelligence, though I expect you to think more about your answers in future conversations."
            $ cg(effect_3="d_mclosed")
            pc "Thank you, my Lord. I'm most grateful."
            $ changeAzula("annoyed")
            $ cg(effect_4="d_bangry")
            a "Hmph…"
            $ cg(effect_3="d_mbiting",effect_4="d_bangry", effect_8="d_eclosing", effect_5="d_eplayer", effect_9="foreground_flames1")
            $ changeAzula("mad")
            a "You're lucky that you...interest me." #hungry
        "Voice":
            pc "Your voice alone sends chills down my back, at times. It keeps me on edge, but in a good way."
            $ changeAzula("bemused")
            $ cg(effect_3="d_msopen", effect_4="d_bcocked")
            a "How's that?"
            $ cg(effect_3="d_mclosed")
            pc "Speaking with you is always...exciting, to say the least."
            $ changeAzula("stern")
            $ cg(effect_3="d_msopen", effect_4="d_bangry")
            a "That sounds somewhat patronizing."
            $ cg(effect_3="d_mclosed")
            pc "I only meant that-"
            $ cg(effect_3="d_msopen", effect_4="d_bcocked")
            $ changeAzula("annoyed")
            a "Alright, alright."
            $ cg("base", "headdefault3","d3_mnormal", "d3_bnormal", "d3_eaway")
            "With a dismissive scoff, Azula glances away from you."
            $ changeAzula("neutral")
            $ cg(effect_3="d3_mtalk")
            a "Don't worry about nothing."
            $ cg(effect_3="d3_mnormal")
            pc "But that's just it. Your voice is so intimidating that I assume everything means something."
            $ changeAzula("stern")
            $ cg(effect_5="d3_eplayer")
            a "Hmm…"
            "As she turns back towards you, she actually smiles. It seems sincere."
            $ changeAzula("happy")
            $ cg("base", "headdefault","d_msmile", "d_bconfused", "d_eplayer")
            a "I quite like how you put that."
            pc "What can I say? You're inspiring."
            $ cg("base", "headdefault","d_mclosed", "d_bangry")
            "And just like that, the smile disappears, giving way to a familiar, predatory scowl."
            $ changeAzula("mad")
            $ cg(effect_3="d_mwopen")
            a "Don't you mean, intimidating?"
            $ cg(effect_3="d_mclosed")
            pc "You're both. I doubt you haven't heard that before."
            $ changeAzula("neutral")
            $ cg(effect_3="d_msopen", effect_4="d_bcocked")
            a "I have, actually."
            $ changeAzula("bemused")
            $ cg(effect_4="d_bconfused")
            a "Quite an astute observation for a mere soldier, even one with your talent."
            $ cg(effect_3="d_mclosed")
            pc "Thank you, my Lord."
            $ changeAzula("neutral")
            $ cg(effect_3="d_msopen", effect_4="d_bcocked")
            a "You may continue, [pc_name]."
            $ cg(effect_3="d_mclosed")
            pc "Oh, um…"
            $ cg(effect_5="d_erolling")
            "Azula rolls her eyes at your slowness, already forgetting your brief moment of clarity."
            $ changeAzula("annoyed")
            $ cg(effect_3="d_msopen")
            a "Try not to hurt yourself."
            $ cg(effect_3="d_mclosed")
            pc "Well, I like the pitch...and how you say words...and-"
            $ cg(effect_4="d_bangry", effect_5="d_eplayer")
            $ changeAzula("mad")
            a "Ugh…"
            $ changeAzula("bemused")
            $ cg(effect_3="d_msopen", effect_4="d_bcocked")
            a "Nevermind, you're ruining it."
            pc "As you wish, my Lord."
            $ cg(effect_3="d_mclosed")
            $ changeAzula("neutral")
            $ cg(effect_3="d_msopen", effect_4="d_bcocked")
            a "Perhaps expand on your first thoughts."
            $ changeAzula("stern")
            $ cg(effect_4="d_bangry")
            a "Tell me about these 'chills' you get."
            $ cg(effect_3="d_mclosed")
            pc "It used to happen all the time, when I first started reporting to you. As soon as you began speaking, the hairs on the back of my neck stood up. With each question, it felt like a bug was creeping down my back, into my spine."
            $ changeAzula("happy")
            $ cg(effect_3="d_msmile",effect_4="d_bconfused")
            a "My, that's descriptive."
            "This is exactly what she wants to hear, how she physically affects people with her presence. You've noticed that people get a little quieter when you enter a room, but you've never wanted to ask why."
            pc "As the weeks passed, they disappeared...but came back when you started asking me to stay for a little, after my reports."
            $ changeAzula("content")
            $ cg(effect_3="d_msopen",effect_4="d_bcocked")
            a "Understandable."
            pc "Only now, I welcomed their return. Somehow, it feels different...thrilling, in a sex-...ah, sensory sort of way."
            $ changeAzula("happy")
            $ cg(effect_3="d_mbiting",effect_4="d_bangry", effect_9="d_eclosing")
            a "Intriguing phenomenon...could be worth studying…" #hungry
    $ changeAzula("neutral")
    $ cg("base", "headdefault","d_msopen", "d_bcocked", "d_eplayer", "d_armlegl","d_armlegr", "foreground_flames1", "blank")
    a "Alright, [pc_name], you can leave now."
    $ cg("base", "headdefault3","d3_mnormal", "d3_bnormal", "d3_eaway")
    pc "(Make it or break it time…)"
    pc "I was actually hoping we could talk some more, my Lord."
    $ changeAzula("annoyed")
    $ cg(effect_3="d3_mtalk", effect_5="d3_eplayer")
    a "Oh really?"
    $ changeAzula("mad")
    $ cg("base", "headdefault","d_msopen", "d_bangry", "d_eplayer")
    a "You don't think I have anything better to do than bother speaking with you further?"
    $ cg(effect_3="d_mclosed")
    pc "Uh…"
    $ changeAzula("bemused")
    $ cg(effect_3="d_mwopen", effect_4="d_bcocked")
    a "Be grateful for the conversation I grant you, [pc_name]."
    $ cg(effect_3="d_mclosed")
    "Azula snaps her fingers and points towards the door."
    #default pointing
    $ changeAzula("stern")
    $ cg(effect_3="d_mwopen", effect_4="d_bangry",effect_6="d_armpoint")
    a "Out."
    $ cg(effect_3="d_mclosed", effect_6="d_armlegl")
    "You immediately turn around and saunter out of the war room. At least you didn't have to flee. That's always a good thing, although if that's the bar for success, maybe you should reconsider your approach. Then again, you're not dead yet."
    $ changeAzula("mad")
    $ cg(effect_5="d_erolling")
    a "(Hmph...talk some more, he says…)"
    $ changeAzula("annoyed")
    $ cg("base", "headdefault3","d3_mnormal", "d3_bnormal", "d3_eaway")
    a "(As if I don't have an entire nation to rule!)"
    $ black("show")
    jump scene_04
    


