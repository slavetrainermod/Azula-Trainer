label intro_scene:
    $ black("show")
    "Avatar Aang is dead. His friends have been imprisoned. While the Phoenix King Ozai keeps busy bringing stability to the former Earth Kingdom, campaigning against the Northern Water Tribe, and searching for the new Avatar, Fire Lord Azula rules the Fire Nation."
    "For three years, she remained isolated within her palace, issuing royal decrees by messenger hawk. Despite the effectiveness of her rule, when her father returned to discover she had no personal contact with her generals, he demanded that she at least pass her orders through a military liaison."
    "At first, her generals welcomed the opportunity to be assured that her orders did not come from some imposter they were powerless to unveil. They were allowed to choose between themselves the most honorable man to serve as the go-between for the Fire Lord and the military."
    "However, it soon became apparent that the job was a death sentence for one's career, sometimes quite literally. After numerous banishments and the occasional execution, the word 'treason' lost all meaning to her generals, though the liaisons that she dismissed were never secretly forgiven by them."
    "Now, the role has become a means of political assassination, and you are the most recent victim, a casualty of your own ambition. Despite that, you're resolved to turn the situation to your absolute advantage through any means necessary. Where others see certain doom, you see a clear opportunity."
    "You will have your revenge."

label scene_02:
    "A few days later…"
    $ cg_scene = "firethronezoom"
    $ cg("base", "headdefault","d_mclosed", "d_bcocked", "d_eaimedup", "d_armlegl", "d_armlegr","blank", "foreground_flames1")
    $ black("hide")
    "As you deliver your report, Azula seems a bit distracted. She still demands that you be more specific at several points, but she acts as if they're inconveniences, rather than details she really wants to know."
    "When you reach the end, you give your customary bow and wait to be dismissed. However, the young Fire Lord remains silent. After a few seconds, you tilt your head up to look at her. You know better than to question her, though."
    $ cg(effect_3="d_msopen", effect_5="d_erolling")
    "Once she notices your look, she rolls her eyes and lets out a short sigh, apparently fed up herself by her indecision."
    $ changeAzula("stern")
    $ cg(effect_5="d_eplayer", effect_3="d_mwopen")
    a "Tell me about yourself, peasant."
    pc "What would you like to know, my Lord?"
    $ changeAzula("mad")
    $ cg(effect_3="d_mclosed", effect_4="d_bangry")
    a "Don't answer my order with a question!"
    pc "I beg your pardon, my Lord. It's just that I don't want to bore you."
    $ changeAzula("annoyed")
    $ cg(effect_3="d_mwopen")
    a "Hmph...I suppose you can't help but be directionless…"
    $ changeAzula("neutral")
    $ cg(effect_3="d_msopen", effect_4="d_bangry")
    a "Before being assigned to the command structure, [pc_name], did you see any combat?"
    pc "I served three tours between the ages of sixteen and eighteen, my Lord."
    $ changeAzula("excited")
    $ cg("base_01", "headfoward", "f_mtalking", "f_bsurprised", "f_eplayer", "f_armleg", "blank")
    a "And did you kill anyone?" #lean forward
    "You take a deep, silent breath. Having heard rumors about Azula's combat experience, you knew this question was coming eventually. The gleam in her eyes is rather disturbing, but you know you can't show any weakness."
    pc "Three hundred and nine fighting men. I don't keep count on civilians." #Rome reference
    $ changeAzula("bemused")
    $ cg(effect_3="f_mclosed", effect_4="f_bconfused")
    a "One hundred and three men per tour, hmm?"
    pc "More or less."
    $ changeAzula("excited")
    $ cg(effect_4="f_bconfused")
    a "That must have been exciting."
    $ changeAzula("bemused")
    $ cg(effect_3="f_mtalking", effect_4="f_bangry")
    a "Why don't you count civilians?"
    $ changeAzula("neutral")
    $ cg(effect_3="f_mclosed", effect_4="f_bnormal")
    a "They're as much our enemy as the soldiers, you know."
    pc "The military doesn't require one to count them in squad reports, my Lord."
    $ changeAzula("annoyed")
    $ cg("base", "headdefault","d_mclosed", "d_bcocked", "d_eaimedup", "d_armthink", "d_armlegr")
    a "Hmm...another thing I'll have to change when I become the Phoenix Queen…" #no lean forward
    $ changeAzula("mad")
    $ cg(effect_5="d_eleftside")
    a "{size=-5}...not that Father will leave me any civilians to count.{/size}" #de-emphasis on all
    pc "I couldn't hear you, my Lord."
    $ changeAzula("annoyed")
    $ cg(effect_4="d_mclosed",effect_5="d_eplayer", effect_6="d_armlegl")
    a "Nothing."
    $ cg("base_01", "headfoward", "f_mtalking", "f_bangry", "f_eplayer", "f_armchin", "blank")
    "Azula leans forward eagerly, resting her chin on her hand as she prepares to pay attention."
    #head leaning forward + "armonchin"
    $ changeAzula("stern")
    a "So, tell me about combat."
    pc "My first tour was spent destabilizing internal Earth Kingdom lines in the area of Ba Sing Se."
    $ changeAzula("bemused")
    $ cg(effect_3="f_mclosed", effect_4="f_bconfused")
    a "Quite a dangerous assignment for someone so young."
    pc "I volunteered for it, my Lord."
    $ changeAzula("stern")
    $ cg("base", "headdefault","d_mclosed", "d_bangry", "d_eplayer", "d_armlegl", "d_armlegr")
    a "Oh, did you?" #no lean forward
    $ changeAzula("happy")
    $ cg(effect_3="d_msmile", effect_4="d_bcocked")
    a "You wouldn't lie to me just to impress, would you?"
    $ changeAzula("annoyed")
    $ cg(effect_3="d_mclosed", effect_4="d_bangry")
    a "I'd give you this one for free, if you tell me the truth and promise to never lie again."
    "Somehow, you doubt that."
    pc "I'm not lying, my Lord. My father…"
    "Hesitant to burden her with personal details, you trail off."
    $ cg(effect_3="d_msopen", effect_5="d_erolling")
    $ changeAzula("stern")
    a "Ah, I see."
    $ cg(effect_3="d_msmile", effect_4="d_bcocked", effect_5="d_eplayer")
    $ changeAzula("happy")
    a "The young son, trying to avenge his poor, fallen father by killing other people's sons and fathers." #eye roll
    $ changeAzula("stern")
    $ cg(effect_3="d_mclosed", effect_4="d_bangry", effect_5="d_eleftside")
    a "How trite…"
    "You tightly clench your hands into fists at her casual dismissal of your father's death. Even if she truly knew how lucky she was to still have one, you don't think she'd care."
    pc "As you say, my Lord."
    pc "(Unbelievable...)"
    $ changeAzula("excited")
    $ cg("base_01", "headfoward", "f_mtalking", "f_bsurprised", "f_eplayer", "f_armleg", "blank")
    a "Well, go on." #lean forward
    "Unclenching your fists, you force yourself to calm down before she sees your anger. Besides, she's already set the bar so low, there's no way she could say something worse."
    pc "Our mission followed a 'scorched earth' policy. We poisoned wells, burned crops, forced villagers to salt their own fields before executing the men, took all the metal we could carry, and fought any soldiers we encountered, taking no prisoners."
    $ changeAzula("neutral")
    $ cg(effect_3="f_mclosed", effect_4="f_bnormal")
    a "It doesn't sound like you have any regrets."
    pc "Only that some managed to escape."
    $ cg("base", "headdefault","d_mclosed", "d_bangry", "d_eplayer", "d_armlegl", "d_armlegr")
    "The Fire Lord returns to an upright position at the mention of failure, adopting a more threatening tone." #no lean forward
    $ changeAzula("mad")
    a "You let enemies of the Fire Nation get away?"
    pc "Sometimes. I was capable for my age, but inexperienced."
    $ changeAzula("annoyed")
    $ cg(effect_3="d_msopen")
    a "That's to be expected, I suppose."
    pc "I appreciate you understanding, my Lord."
    $ changeAzula("happy")
    $ cg(effect_3="d_msmile", effect_4="d_bsure")
    a "Did you ever rape anyone?"
    $ cg("base_01", "headfoward", "f_mtalking", "f_bangry", "f_eplayer", "f_armchin", "blank")
    "You look at her incredulously, but she just sinks her head back down to rest it on her hand again while maintaining eye contact." #lean forward + "armonchin"
    menu:
        "No":
            pc "No."
            $ changeAzula("annoyed")
            $ cg("base", "headdefault","d_msopen", "d_bangry", "d_eplayer", "d_armlegl", "d_armlegr")
            a "That's a suspiciously short answer." #no lean forward
            pc "With respect, it was an insulting question."
            $ changeAzula("mad")
            $ cg(effect_3="d_mwopen")
            a "Are you calling me crass, [pc_name]?"
            pc "No, my Lord."
            $ changeAzula("stern")
            $ cg(effect_3="d_mclosed",effect_4="d_bangry", effect_5="d_erolling")
            a "Well, it is a rather personal question…"
            $ changeAzula("happy")
            $ cg(effect_3="d_mlaugh", effect_4="d_bconfused", effect_5="d_eplayer")
            a "Not that I'd mind if you had, by the way."
        "Absolutely not":
            pc "I would never do such an awful thing."
            $ cg("base", "headdefault","d_msopen", "d_bcocked", "d_eplayer", "d_armlegl", "d_armlegr")
            $ changeAzula("stern")
            a "Even if ordered?" #no lean forward
            pc "That's right."
            $ changeAzula("happy")
            $ cg(effect_3="d_msmile")
            a "What if {size=+5}I{/size} ordered you to rape someone?" #emphasis on 'I'
            $ cg(effect_3="d_mlaugh")
            a "Would you do it?"
            pc "Uh…"
            $ changeAzula("stern")
            $ cg(effect_3="d_mclosed", effect_4="d_bangry")
            a "You don't have to answer that."
            $ cg(effect_3="d_mwopen")
            a "Though I would fully expect you to carry out my order."
    pc "If it pleases your Lordship, I would continue."
    $ cg(effect_3="d_mclosed", effect_4="d_bcocked")
    "Azula nods her head at you, permitting you to change the subject."
    pc "My second tour took me north, preparing for and participating in the Siege of the North."
    $ cg(effect_4="d_bsurprised")
    "Her eyebrows raise up in surprise. Your very mention of it seems to catch the royal's interest."
    #surprised default brow
    $ changeAzula("bemused")
    $ cg(effect_3="d_msopen")
    a "Really?"
    $ changeAzula("happy")
    $ cg(effect_3="d_msmile", effect_4="d_bcocked")
    a "That's a battle I would have enjoyed."
    $ changeAzula("excited")
    $ cg("base_01", "headfoward", "f_mtalking", "f_bsurprised", "f_eplayer", "f_armleg", "blank")
    a "What was it like, to fight powerless waterbenders?"
    pc "Easy."
    $ cg(effect_3="f_mclosed",effect_4="f_bconfused")
    $ changeAzula("happy")
    $ cg(effect_3="f_mtalking")
    a "I don't suppose they had any real weapons."
    pc "No."
    $ changeAzula("excited")
    $ cg(effect_3="f_mtalking",effect_4="f_bsurprised")
    a "Is it true that the Avatar transformed into a monster?"
    $ cg(effect_3="f_mclosed")
    pc "Yes."
    $ cg("base", "headdefault","d_mclosed", "d_bcocked", "d_eplayer", "d_armlegl", "d_armlegr","blank", "foreground_flames1")
    "Your reluctance to talk about it obviously starts to annoy Azula. She sits up straight, reminding you that this is more than just a casual account of your life."
    $ changeAzula("frustrated")
    $ cg(effect_3="d_msopen")
    a "Maybe you don't want to remember it, [pc_name], but I want to hear about it."
    $ changeAzula("mad")
    $ cg(effect_3="d_mwopen", effect_5="d_eplayer")
    a "So get over your petty trauma and tell me!"
    $ cg(effect_3="d_mclosed")
    "Her disrespect for soldiery is so transparent, you wonder for just a moment if she really understands how horrible it can be. You grit your teeth, but take a deep breath and remember you have to play her game."
    pc "I've...never seen anything like it. As if he was made of water, but bright as lightning."
    $ changeAzula("excited")
    $ cg(effect_3="d_msmile", effect_4="d_bsurprised")
    a "A force of nature."
    pc "Yes...it was like fighting a tidal wave. There was nothing we could do. Everyone in my squad was wiped out."
    $ cg(effect_3="d_msopen", effect_4="d_bsure")
    $ changeAzula("neutral")
    a "Then how did you survive?"
    pc "Once I saw it throw a tank like a toy, I...hid."
    $ changeAzula("annoyed")
    $ cg(effect_3="d_mclosed", effect_4="d_bangry")
    a "That's cowardly."
    pc "Easy for you to-!"
    $ cg(effect_8="angryflames1")
    "You stop short, even before the flames rip through the air in front of you."
    $ cg(effect_3="d_mwopen")
    $ changeAzula("mad")
    a "What was that!?"
    menu:
        "Easy for you to say!":
            pc "Forgive me, but if you had seen what I saw, you might have hid yourself, my Lord!"
            $ changeAzula("annoyed")
            $ cg(effect_3="d_msopen")
            a "How dare you, peasant!"
            pc "I'm sorry. I meant no disrespect. It's just that-"
            $ changeAzula("mad")
            $ cg(effect_3="d_mwopen")
            a "Clearly, you have no understanding of the power of my firebending, so I will forgive you, this one time."
            $ cg(effect_3="d_mclosed", effect_8="foreground_flames1")
            "With a quick, short breath to calm herself, Azula forces the flames back down to the floor."
            $ changeAzula("stern")
            $ cg(effect_3="d_msopen", effect_5="d_erolling")
            a "Since you are so obviously still traumatized by what you saw, I won't hold you fully accountable."
            $ changeAzula("mad")
            $ cg(effect_3="d_mwopen", effect_5="d_eplayer")
            a "But if you ever again compare me to any soldier you've known, I'll show you exactly what I can do!"
        "Easy for you to get away.":
            pc "Forgive me, my Lord. I meant no disrespect. What I was going to say is that, you most certainly could have gotten away, but I only had a spear."
            $ changeAzula("stern")
            $ cg(effect_3="d_mclosed", effect_5="d_eleftside")
            a "Hmm…"
            $ cg(effect_8="foreground_flames1")
            "The flames recede, along with her anger."
            pc "There was no way for me to escape other than hiding. It was only for a short time."
            $ changeAzula("annoyed")
            $ cg(effect_3="d_msopen", effect_5="d_eplayer")
            a "Well, you did live to fight another day."
            $ changeAzula("neutral")
            $ cg (effect_3="d_mclosed",effect_4="d_bcocked", effect_5="d_erolling")
            a "That deserves some commendation, I suppose."
    pc "Thank you, my Lord…"
    $ cg("base_01", "headfoward", "f_mtalking", "f_bsurprised", "f_eplayer", "f_armleg", "blank")
    $ changeAzula("happy")
    a "Now, I'm curious as to how you escaped."
    #leans forward
    pc "I waited for an hour before coming out. Then I quietly made my way to the docks, stole a ship, and sailed away until I found the Fire Navy."
    $ changeAzula("excited")
    $ cg(effect_3="f_mclosed", effect_5="f_ecloseplayer")
    a "And killed anyone who got in your way?"
    pc "Two men and a woman, yes."
    $ changeAzula("neutral")
    $ cg(effect_3="f_mtalking", effect_4="f_bconfused", effect_5="f_eplayer")
    a "Did you personally rescue anyone?"
    pc "They would have slowed me down."
    $ changeAzula("stern")
    $ cg(effect_3="f_mclosed", effect_4="f_bangry")
    a "What makes you so sure?"
    pc "Better one of us survive than us all being caught. I couldn't risk one man wanting to rescue others. We'd have been captured for sure."
    $ changeAzula("happy")
    $ cg(effect_3="f_mtalking", effect_4="f_bnormal")
    a "Agreed."
    "While she contemplates your decision, Azula clicks her tongue a few times before asking the obvious question."
    $ changeAzula("bemused")
    $ cg(effect_3="f_mclosed", effect_4="f_bconfused")
    a "But how did you know how to sail a Water Tribe ship?"
    a "Their designs are so primitive."
    pc "In preparation for the battle, we would sometimes capture their craft, to gather information and probe their defenses. Then we used them to surprise other vessels."
    $ changeAzula("annoyed")
    $ cg(effect_3="f_mtalking", effect_4="f_bangry", effect_5="f_eside")
    a "Another dangerous assignment."
    pc "Not as much as your Lordship might think. We were just far enough away to make it seem like regular raids, as to not raise any alarms."
    $ changeAzula("neutral")
    $ cg(effect_5="f_eplayer", effect_4="f_bnormal")
    a "I assume you volunteered?"
    pc "Yes."
    $ cg(effect_3="f_mclosed")
    "The Fire Lord looks at you cooly, waiting for an explanation."
    pc "My brother was killed on one such mission."
    "As soon as you said the word 'killed', Azula began to laugh cruelly."
    $ cg("base", "headdefault2","d2_mlaugh", "d2_bhappy", "d2_eclosed", "d_armlegl", "d_armlegr")
    #default + head back laughing
    $ changeAzula("content")
    a "My, what a tragic family!"
    $ cg("base", "headdefault","d_mlaugh", "d_bcocked", "d_erolling", "d_armlegl", "d_armlegr")
    $ changeAzula("happy")
    a "First your father and then your brother!"
    $ changeAzula("content")
    $ cg(effect_3="d_msmile", effect_4="d_bsurprised", effect_5="d_eleftside")
    a "Did mommy dearest pass away as well?"
    $ changeAzula("happy")
    $ cg(effect_3="d_mlaugh", effect_4="d_bcocked", effect_5="d_eplayer")
    a "I bet she did, or perhaps committed suicide!"
    "Stunned by the sheer callousness of her attitude, you pause briefly before continuing."
    pc "She died from a disease when I was young."
    $ changeAzula("neutral")
    $ cg(effect_3="d_mclosed", effect_4="d_bsure", effect_5="d_eplayer")
    a "Oh."
    $ cg("base", "headdefault3","d3_mfrown", "d3_bbored", "d3_eaway")
    "Azula looks away for a moment, disinterest clearly written across her face."
    #head turned away
    $ changeAzula("disappointed")
    a "Well, that’s boring."
    pc "Sorry to disappoint…"
    $ changeAzula("neutral")
    $ cg(effect_3="d3_mtalk", effect_4="d3_bnormal", effect_5="d3_eplayer")
    a "Oh, don't pout."
    "With a shrug, the Fire Lord turns her head back towards you."
    $ changeAzula("happy")
    $ cg(effect_2="headdefault",effect_3="d_msmile", effect_4="d_bcocked", effect_5="d_erolling")
    a "As a whole, you life is quite interesting."
    $ cg(effect_3="d_mclosed", effect_4="d_bangry")
    "Despite the admission, her expression hardens. You tense up at the sight, drawing in a sharp breath through your nose."
    $ changeAzula("bemused")
    $ cg(effect_3="d_msopen", effect_5="d_eplayer")
    a "It's almost as if you're making it all up..."
    pc "There's a reason why I was eventually assigned to command, my Lord. I'm an exceptional soldier."
    pc "(Even if it was a stunt to encourage morale…)"
    $ cg(effect_3="d_mclosed", effect_5="d_erolling")
    $ changeAzula("stern")
    a "Mmm-hmm…"
    $ changeAzula("neutral")
    $ cg(effect_3="d_msopen", effect_5="d_eplayer")
    a "Fair enough."
    $ cg(effect_3="d_mclosed", effect_4="d_bcocked")
    "As Azula's face returns to a more receptive look, you relax slightly."
    $ cg(effect_3="d_msopen")
    $ changeAzula("content")
    a "What of your third tour?"
    pc "I actually saw your Lordship once, while on it."
    $ changeAzula("happy")
    $ cg(effect_3="d_msmile", effect_4="d_bsurprised")
    a "Oh really?"
    pc "I was assigned to the force that took Oma-...I mean, New Ozai."
    $ changeAzula("annoyed")
    $ cg(effect_3="d_mclosed", effect_4="d_bangry", effect_5="d_erolling")
    a "Ah, yes."
    $ cg(effect_3="d_msopen")
    a "Such a troublesome city."
    $ changeAzula("neutral")
    $ cg(effect_3="d_mwopen", effect_4="d_bcocked", effect_5="d_eplayer")
    a "Did you hide again, during the eclipse?"
    pc "After the plague scare and the exodus of dissidents, I was transferred back to my old duties, destabilizing the territory surrounding Ba Sing Se."
    $ changeAzula("annoyed")
    $ cg(effect_3="d_mclosed", effect_5="d_erolling")
    a "Oh, this again…"
    pc "That didn't last long either, since your Lordship captured the city."
    $ changeAzula("neutral")
    $ cg(effect_3="d_mwopen", effect_5="d_eplayer")
    a "And then you spent your tour putting down urban resistance, I suppose."
    $ cg("base", "headdefault2","d2_myawn", "d2_byawn", "d2_eclosed", "d_armyawn")
    "Weary of hearing your life story, Azula stifles a yawn. It's a shame she didn't tire sooner. You don't like to relive the past."
    #head leaned back + yawn
    $ changeAzula("content")
    $ cg(effect_2="headdefault",effect_3="d_msopen", effect_4="d_bcocked", effect_5="d_eplayer", effect_6="d_armlegl")
    a "Did you at least get to fight when those White Lotus fools recaptured the city during Sozin's Comet?"
    pc "As hard as I could for as long as it took, my Lord."
    $ changeAzula("neutral")
    $ cg(effect_3="d_mwopen", effect_5="d_eleftside")
    a "Fine, fine."
    $ changeAzula("disappointed")
    $ cg(effect_3="d_mclosed", effect_5="d_erolling")
    a "I'm sure you were very heroic."
    "Defending the city was, by far, the toughest, most brutal combat you've ever experienced. Whoever the White Lotus were, when they made their move, they wiped out dozens of units. If that dismissal came from anyone else, you'd be furious. But coming from the Fire Lord, it's just disturbing."
    pc "Fifty-three percent of my unit was wounded or killed before reinforcements finally arrived. We were pushed all the way back into the Inner Ring."
    $ changeAzula("neutral")
    $ cg(effect_3="d_msopen",effect_4="d_bangry", effect_5="d_eplayer")
    a "And now you're here."
    pc "Yes, after I returned, the-"
    $ cg(effect_3="d_mclosed")
    a "Nevermind that."
    $ changeAzula("excited")
    $ cg(effect_3="d_msmile",effect_4="d_bsurprised")
    a "I want to hear about the good stuff now."
    pc "The...good stuff, my Lord?"
    $ cg("base_01", "headfoward", "f_mtalking", "f_bsurprised", "f_eplayer", "f_armleg", "blank")
    "Azula again leans forward, her eyes full of an almost primal kind of curiosity." #lean forward
    $ changeAzula("happy")
    $ cg(effect_3="f_mclosed", effect_4="f_bconfused")
    a "Combat, of course."
    pc "Right…"
    "This is the part you had been dreading since the conversation began. While you're proud of how you served your nation, it's not a part of your past you really enjoy remembering."
    $ changeAzula("excited")
    $ cg(effect_3="f_mtalking", effect_4="f_bsurprised")
    a "Which weapons are you proficient with, and what is your favorite weapon?"
    pc " My favorite is-"
    $ changeAzula("happy")
    $ cg(effect_3="f_mclosed", effect_4="f_bconfused")
    a "Ooh, and tell me about the last time you used each one and why."
    $ cg(effect_3="f_mtalking", effect_4="f_bnormal")
    a "I do love a good war story!"
    pc "The last time I-"
    $ changeAzula("excited")
    $ cg(effect_3="f_mtalking", effect_4="f_bsurprised")
    a "Also, the first time you used each to kill someone."
    "You take a deep breath and sigh. She might be a master firebender, but when it comes to arms, she sounds like a rookie. Maybe she's simply excited to talk to someone about it, though."
    pc "With respect, my Lord, I could tell you more quickly if you let me answer questions already asked."
    $ cg("base", "headdefault","d_mclosed", "d_bangry", "d_erolling", "d_armlegl", "d_armlegr")
    $ changeAzula("mad")
    a "Tch…" #default
    $ changeAzula("annoyed")
    $ cg(effect_3="d_msopen", effect_5="d_eplayer")
    a "You know, just because you respectfully say something rude, that doesn't mean you can say it without penalty."
    $ changeAzula("mad")
    $ cg(effect_3="d_mclosed")
    a "Something to keep in mind, [pc_name]."
    "With a simple bow, you acknowledge her warning."
    $ changeAzula("neutral")
    $ cg("base_01", "headfoward", "f_mtalking", "f_bsurprised", "f_eplayer", "f_armchin", "blank")
    a "But very well, go on." #lean forward + "armonchin"
    $ cg(effect_3="f_mclosed", effect_4="f_bnormal")
    pc "Thank you, my Lord. Like all soldiers, I am proficient with the spear…"
    "You spend the next couple of hours answering Azula's questions. She politely listens, apparently enraptured by the account of an above-average soldier. There seems to be no end to her curiosity."
    $ cg(effect_4="f_bsurprised")
    "When you begin to talk about your actual combat experience, she smiles and laughs, taking some sort of sick pleasure in the horrors of war. All recruits start eager to fight, of course, even you. However, you get the sense that Azula is more the kind of person who's eager to kill."
    pc "...and my first time with a halberd was surprising, because it cut right through the man's armor and took off his arm in one swoop."
    $ cg("base", "headdefault4","d4_mfrown", "d4_bcocked", "d4_eplayer", "d_armlegl", "d_armlegr")
    "Slightly confused by your account, Azula cocks her head to the side." #default
    $ changeAzula("bemused")
    $ cg(effect_3="d4_mtalk")
    a "But surely, you had to expect that, having trained with it."
    $ cg(effect_3="d4_mfrown")
    pc "The armor we put on the dummies in training was actually more protective than what he had on."
    $ changeAzula("stern")
    $ cg(effect_3="d4_mtalk", effect_4="d4_bmad")
    a "Even though it was a replication of Earth Kingdom armor?"
    $ cg(effect_3="d4_mfrown")
    pc "Their equipment varies in quality. I suppose I should have expected that, but-"
    $ cg("base", "headdefault","d_mwopen", "d_bcocked", "d_eplayer")
    $ changeAzula("bemused")
    a "And then what did you do?"
    $ changeAzula("happy")
    $ cg(effect_3="d_msmile", effect_4="d_bsurprised")
    a "That seems like it would have left you unguarded."
    pc "I would have been cut down right then and there, except I immediately turned my weapon to the side and used the back blade to cut into his comrade's leg."
    $ cg(effect_6="d_armclap", effect_7="blank")
    "Azula claps her hands, delighted. You've told that story more than once as a curiosity, but nobody has ever clapped at the turn of events. The pit in your stomach that you've felt for the last two hours grows deeper."
    #clapping
    $ changeAzula("excited")
    $ cg(effect_3="d_msopen")
    a "Excellent!"
    $ cg(effect_3="d_mclosed")
    pc "Then I stabbed him in the throat with the tip as I stood up, kicked him back, and swung at the next man."
    $ cg(effect_6="d_armlegl", effect_7="d_armlegr")
    $ changeAzula("happy")
    $ cg(effect_3="d_mwopen")
    a "Absolutely marvelous."
    $ cg(effect_3="d_msopen")
    a "I have to say, I wasn't fully aware of how wide this whole world of weaponry one could play with was."
    $ changeAzula("disappointed")
    $ cg("base", "headdefault3","d3_mfrown", "d3_bbored", "d3_eaway")
    a "Not that I'd ever be able to swing and hack with enough force to keep up…"
    "Unsurprisingly, Azula sounds disappointed, even a little jealous."
    menu:
        "Agree":
            pc "I think you could give any man more than he'd bargain for."
            $ cg("base", "headdefault","d_msopen", "d_bcocked", "d_eplayer")
            $ changeAzula("happy")
            a "That's very polite of you to say, but I understand well the physical limits of the female body."
            $ changeAzula("neutral")
            $ cg("base", "headdefault","d_mwopen", "d_bangry", "d_erolling")
            a "Besides, it still sounds very messy in comparison to firebending, despite the-"
            pc "Despite the smell."
            $ cg(effect_3="d_msopen", effect_4="d_bsurprised", effect_5="d_eplayer")
            "Azula quickly looks up at you. Even though you interrupted her, she looks pleasantly surprised."
            $ changeAzula("excited")
            a "Exactly."
            $ changeAzula("frustrated")
            $ cg(effect_3="d_mwopen", effect_5="d_erolling")
            a "I can appreciate the smell of an enemy's burning flesh as much as any other, but the stink…"
            $ cg(effect_3="d_mclosed",effect_4="d_bcocked", effect_5="d_eplayer")
            "She trails off, leaving the imagery hang in the air. As if she's testing you, Azula looks at you expectantly, waiting for you to finish her sentence."
            #default expectant
            pc "It sticks to your clothes. I assure you, the smell of cooked meat after a dip in the river is amazing when all you've been smelling for days is your unwashed combat armor, stained with soot from seared flesh."
        "Disagree":
            pc "You've got that right."
            $ cg("base", "headdefault","d_mclosed", "d_bangry", "d_eplayer", effect_8="Angryflames1")
            "Flames immediately spring to life in front of you.  Apparently, someone doesn't like being reminded that she has small muscles."
            $ changeAzula("mad")
            $ cg(effect_3="d_mwopen")
            a "Excuse me, peasant!?"
            pc "Um…"
            $ changeAzula("annoyed")
            $ cg(effect_3="d_msopen")
            a "I know well enough what I can and can't do without you pointing it out to me!"
            $ changeAzula("mad")
            $ cg(effect_3="d_mwopen")
            a "You'd do better to remember that I have a certain ability which you'll never have!"
            pc "Beg your pardon, my Lord. I don't know what I was thinking."
            $ changeAzula("stern")
            $ cg(effect_3="d_mclosed", effect_5="d_erolling")
            a "Hmph…"
            $ cg(effect_8="foreground_flames1")
            "Thankfully, the flames go back down. Royals are so touchy about the truth sometimes."
            $ changeAzula("bemused")
            $ cg(effect_3="d_msopen", effect_4="d_bcocked", effect_5="d_eplayer")
            a "I suppose you are an expert at non-bending combat, though."
            $ changeAzula("content")
            $ cg(effect_3="d_msmile")
            a "Small wonder you were so quick to deny my abilities in that particular field."
            $ changeAzula("disappointed")
            $ cg("base", "headdefault3","d3_mnormal", "d3_bbored", "d3_eaway")
            a "(I don't imagine I would survive for very long if someone like Ty Lee surprised me…)"
            pc "(Without firebending, she wouldn't last two seconds in a melee…)"
    $ cg("base", "headdefault","d_msmile", "d_bsurprised", "d_eplayer")
    $ changeAzula("happy")
    a "You're quite the soldier, [pc_name]."
    $ changeAzula("annoyed")
    $ cg(effect_3="d_msopen", effect_5="d_erolling")
    a "It's a refreshing change of pace, especially in comparison to those stupid, old, weak men they've sent me in the past year."
    pc "The only thing I have in common with them is that I'm a man, my Lord."
    $ changeAzula("stern")
    $ cg(effect_3="d_mbiting",effect_4="d_bangry", effect_8="d_eclosing", effect_5="d_eplayer", effect_9="foreground_flames1")
    a "Indeed you are…"
    "Azula gives you a strange, hungry look."
    #default sex-hungry
    pc "(What's up with that…?)"
    $ changeAzula("neutral")
    $ cg(effect_3="d_msopen",effect_4="d_bcocked", effect_5="d_eplayer", effect_8="foreground_flames1", effect_9="blank")
    a "That's enough for today."
    $ changeAzula("happy")
    $ cg(effect_3="d_msmile", effect_4="d_bsurprised")
    a "I look forward to hearing more war stories the next time we see each other, [pc_name]."
    pc "(Oh good, let me just continually relive the horrors of war for your entertainment, you cunt.)"
    $ black("show")
    jump scene_03



