label intro_scene:
    $ background("images/environments/throne.png")
    "Four months have passed since you were assigned the post of personal military liaison to Fire Lord Azula, who has spent three of the last four years isolated in her palace, ruling from afar."
    "You can only imagine how furious she was when the Phoenix King Ozai then demanded that she at least pass orders through a living person, rather than by a messenger hawk."
    "All of your predecessors were killed or banished, but you have managed to survive, though you're not sure if it's due to your wits, her attraction to you, or just luck."
    "In the last four months, it's become obvious that she's perhaps the most sexually frustrated person in the whole Fire Nation, though she'd never admit it."
    "She has ordered you to help her to become the perfect lover, so that she can effectively manipulate the person she marries to the utmost extreme, though she has also demanded that you treat her as you would almost any other woman, within reason."
    "However, you're starting to believe that, on some level, she simply wants a man in her life, though you're certain that it has nothing to do with love or affection."
    "What you want is to find out who sent you here and take revenge on them, and while things seem to be going well with Fire Lord Azula, you know that your fortune could turn at any time."
    "If you can survive long enough to find some psychological weakness in the girl, then maybe you can even take more power than you could have ever imagined…"




label scene_01:
    $ cg_scene = "FireThrone"
    $ cg("mouth_closed", "angry", "eyes_at_player", "foreground_flames")
    $ changeAzula("neutral")
    a "Good morning, [pc_name]."
    pc "And to you, Fire Lord Azula."
    #$ changeLee("")
    "Heat washes over you as the flames between the two of you flare up."
    $ cg("mouth_way_open", "super_turbo_mad", "angry_flames", "foreground_flames") #in addition to "foreground_flames"
    $ changeAzula("mad")
    a "I told you to stop addressing  me so formally!"
    pc "Forgive me, Azula. It's difficult to change after so many years of respecting authority."
    #$ changeLee("")
    $ changeAzula("neutral")
    a "There's nothing to forgive."
    $ cg("mouth_open", "confused", "eyes_at_player")
    "As the flames return to their normal size, you breathe a quiet sigh of relief."
    $ cg("mouth_closed") #remove "angry_flames"
    $ changeAzula("stern")
    a "However, should I need to remind you again, I'm afraid I might need to banish you for ugliness in addition to stupidity."
    $ cg("angry")
    $ changeAzula("content")
    a "Burn victims aren't particularly attractive."
    $ cg("you_sure", "eyes_to_side", "mouth_open")
    "You clench your fist in anger. As a veteran, you've seen your fair share of burn victims. Most of them weren't lucky enough to only suffer a superficial wound. Even if they were your enemies, it's not a fate to make light of. She has no right to speak this way."
    pc "With all your experience on the front lines, naturally you would know."
    #$ changeLee("")
    "Azula narrows her eyes at you, unsure if you're insulting her."
    $ cg("angry", "eyes_at_player")
    $ changeAzula("annoyed")
    a "It's an obvious fact, [pc_name]."
    $ changeAzula("stern")
    a "But enough about weaklings of the past!"
    $ cg("eyes_aimed_up")
    $ changeAzula("content")
    a "I'm feeling a bit parched today."
    $ cg("confused", "eyes_at_player")
    $ changeAzula("bemused")
    a "What are you going to do about it?"
    $ cg("you_sure")
    menu:
        "Blowjob":
            pc "I'm going to let you suck my cock."
            #$ changeLee("")
            "Azula rolls her eyes."
            $ cg("eyes_to_side")
            $ changeAzula("disappointed")
            a "Could you be any more blunt?"
            pc "Your last performance was not very inspiring."
            #$ changeLee("")
            $ changeAzula("mad")
            a "Are you really blaming your lack of imagination on me!?"
            $ cg("angry", "eyes_at_player")
            pc "So many questions. Yet not one is the answer. My cock in your mouth."
            #$ changeLee("")
            $ changeAzula("bemused")
            a "Hmm..."
            $ cg("eyes_to_side")
            $ changeAzula("content")
            a "Crude, but effective."
            $ cg("you_sure")
            $ changeAzula("excited")
            a "Truly, I am quite thirsty."
            $ cg("confused", "eyes_aimed_up")
            $ changeAzula("stern")
            a "Enough of haiku."
            $ cg("angry", "eyes_at_player")
            "Azula leaps from her pillow and through the flames, quickly walking past you as she orders you to follow her." #screen cuts to black
            $ changeAzula("excited")
            a "Come, boy."

    "As you exit the war room after Azula, you grab her shoulder to stop her. She stiffens, but doesn't turn around."
    $ changeAzula("bemused")
    a "Another one of your little pep talks?"
    $ changeAzula("annoyed")
    a "I assure you, I'm quite ready this time."
    pc "No, it's a new challenge. Your hands will be bound behind your back today."
    #$ changeLee("")
    $ cg_scene = "Trainer"
    $ cg("Norope", "ArmsNormal", "Eye1")
    "Azula turns towards the wall and looks sidelong at you, intrigued."
    $ changeAzula("frustrated")
    a "Why would I ever agree to that?"
    menu:
        "Better for me":
            pc "Frankly, I'll enjoy it more, as would your husband, whoever he'll be."
            #$ changeLee("")
            "She glowers at you."
            $ changeAzula("annoyed")
            a "He should consider himself lucky just to have my lips wrapped around his rod!"
            $ changeAzula("mad")
            a "And you should consider yourself very lucky that I don't bind your hands and legs before throwing you down a well!"
            $ changeAzula("bemused")
            a "Though I do like the prospect of being...challenged in such a way."
        "Better for you":
            pc "It may seem submissive, but if you learn how to suck a cock without using your hands to steady yourself, then you'll perfect it much faster than you would otherwise."
            #$ changeLee("")
            "She smiles at you confidently."
            $ changeAzula("happy")
            a "Very well."
            $ changeAzula("frustrated")
            a "Of course, don't think that my bondage will stop me from burning you to death."
            $ changeAzula("content")
            a "Most people aren't talented enough at firebending to be able, but I'm very good at breathing fire."
    
    "Azula places her arms behind her back and nods her head at you, so you immediately begin to tie her hands."
    $ cg("RopeHold", "ArmTiedSet")
    $ changeAzula("stern")
    a "You had better be right that tying my hands will be worth it."
    $ changeAzula("disappointed")
    a "Otherwise, I'll just feel humiliated, and you know what happens then."
    pc "I imagine you'll shout at me to untie you while threatening to kill me and then pretend it never happened after you're free."
    #$ changeLee("")
    $ changeAzula("mad")
    a "Don't mock me simply because I'm in this ludicrous position!"
    "As you finish tying Azula's hands, she looks at you with contempt, although there's a trace of disappointment in her voice."
    $ changeAzula("bemused")
    a "Is that the best knot you can tie, [pc_name]?"
    pc "(Of course not...)"
    #$ changeLee("")
    $ changeAzula("annoyed")
    a "A child could escape from this!"
    "With a shrug, you grab the rope binding her hands together and pull it as hard as you can."
    "Azula practically trips backwards from the force of your motion, breathing in sharply out of surprise."
    $ changeAzula("stern")
    a "That's better...somewhat..."
    "You give the rope another hard tug, but Azula doesn't lose her balance in the slightest. She just glares at you."
    $ changeAzula("mad")
    a "Fine, it's perfectly tight."
    $ cg("Norope")
    $ changeAzula("neutral")
    a "Let's move on, so I can see whether or not this charade is worth my-"
    pc "Pride?"
    #$ changeLee("")
    $ changeAzula("frustrated")
    a "Shut up."
    pc "Honor?"
    #$ changeLee("")
    $ changeAzula("bemused")
    a "Now you sound like my stupid brother."
    pc "Dignity?"
    #$ changeLee("")
    $ changeAzula("mad")
    a "I told you to be quiet!"
    $ changeAzula("annoyed")
    a "Time is the word that I was looking for."
    pc "Speaking of time..."
    #$ changeLee("")
    "You push Azula forward. With a low growl of annoyance, she begins to walk as directed." #black screen
    
    $ cg_scene = "t8"
    $ cg("a1", "d1", "st", "eplay")
    "Once you reach her bed chamber, you undress and lie down. Azula kneels between your legs." #T8.psd, "a1", "d1", "st", "eplay"
    $ changeAzula("bemused")
    a "Well?"
    pc "Well what?"
    #$ changeLee("")
    $ changeAzula("disappointed")
    a "When are you going to get..."
    "Azula glances away before finishing her question."
    $ cg("lilup", "eoff")
    $ changeAzula("frustrated")
    a "...hard?"
    pc "That's up to you."
    #$ changeLee("")
    $ changeAzula("mad")
    a "Is that so!?"
    $ cg("mad", "eplay")
    $ changeAzula("stern")
    a "You've never had trouble before!"
    $ cg("st")
    pc "The novelty of fucking the Fire Lord has worn off somewhat."
    #$ changeLee("")
    $ changeAzula("disappointed")
    a "Feh..."
    $ cg("lil", "eoff")
    "Without further comment, Azula dips her head below your growing member and balances it on the side of her face, pressing against your balls to keep your cock steady."
    $ cg("a2_nl", "d2",  "mad", "enuts")
    pc "Is that all you're going to do?"
    #$ changeLee("")
    $ changeAzula("mad")
    a "What is it, exactly, that you expect of me, [pc_name]?"
    $ cg("eplay")
    "The venom in her voice is unmistakable, but seeing her like this emboldens you."
    pc "You could lick my balls for a start. They're already on your lips."
    #$ changeLee("")
    $ changeAzula("frustrated")
    a "Disgusting..."
    $ cg("enuts")
    "Azula's expression of anger soon disappears as she moves from hesitantly dabbing her tongue against your sack to actually passing her whole tongue over the wrinkles."
    $ cg("pp")
    $ changeAzula("annoyed")
    a "(I can't believe men enjoy this.)"
    $ changeAzula("stern")
    a "(It just seems so unnatural.)"
    $ cg("bm")
    $ changeAzula("content")
    a "(And yet...)"
    $ cg("sp", "edick")
    pc "Don't be afraid to suck on them too."
    #$ changeLee("")
    "As a response, Azula painfully whips her tongue against one of your balls."
    $ cg("mad")
    pc "Ow!"
    #$ changeLee("")
    "Azula chuckles as she begins to lick the root of your shaft."
    $ cg("a2_l", "sp")
    $ changeAzula("happy")
    a "Sorry, did I do it wrong?"
    $ changeAzula("stern")
    a "How clumsy of me!"
    $ cg("bm")
    pc "You're just making it harder for me to get hard."
    #$ changeLee("")
    $ changeAzula("bemused")
    a "Do you have difficulty using the word 'difficult' as well?"
    $ cg("mad")
    pc "What are you, a thesaurus?"
    #$ changeLee("")
    "Declining to trade words with you any longer, Azula continues to lick your cock, moving higher up as it rises off her face."
    $ cg("bm", "ed")
    "Once you're fully aroused, she dips her head back under your cock and rests it on her forehead."
    $ cg("a3", "st", "edick")
    menu:
        "Question her":
            pc "What are you doing?"
            #$ changeLee("")
            $ changeAzula("mad")
            a "I wasn't aware I had to explain myself to you!"
            $ cg("mad", "ebig")
            $ changeAzula("neutral")
            a "Anyway, I just wanted to see how large it was from this angle."
            $ cg("st", "edick")
            pc "So, what do you think?"
            #$ changeLee("")
            $ changeAzula("content")
            a "It is rather impressive..."
            $ cg("pp")
            $ changeAzula("disappointed")
            a "I don't expect I'll be able to fit much of it into my mouth, even after our last session."
            $ cg("sh")
            $ changeAzula("happy")
            a "Small wonder that it feels so invasive when you enter me..."
            $ cg("edick")
            pc "But in a good way, right?"
            #$ changeLee("")
            $ changeAzula("stern")
            a "Hmph!"
            $ cg("st", "ebig")
            $ changeAzula("mad")
            a "As if I would keep you around otherwise!"
            $ cg("mad")
            $ changeAzula("annoyed")
            a "And stop asking so many questions!"
            $ cg("edick")
        "Bounce your cock":
            "You lean back for a moment before pushing forward, gently slapping you cock against her forehead with a soft 'smack'."
            $ changeAzula("stern")
            a "What was that for?"
            $ cg("pp", "ebig")
            pc "I'm just playing around."
            #$ changeLee("")
            $ changeAzula("annoyed")
            a "It seems more as if you're impatient with me."
            $ cg("mad")
            pc "Well, I can only stay aroused for so long without some action."
            #$ changeLee("")
            $ changeAzula("frustrated")
            a "Hmph..."
            $ cg("st")
            $ changeAzula("")
            a "How's this for action?"
            $ changeAzula("happy")
            a "I wanted to see how...large your rod was resting..."
            $ cg("pp", "edick")
            $ changeAzula("excited")
            a "...resting on my pristine, royal face..."
            pc "Was that your idea of dirty talk? It'd be better without all the pauses."
            #$ changeLee("")
            $ changeAzula("mad")
            a "Nevermind then!"
            $ cg("mad", "ebig")
    
    "With that exclamation, Azula moves her head up and presses her soft lips against the head of your cock."
    $ cg("a4_k", "re", "eplay")
    "You shiver slightly at the unexpected tenderness. The girl does learn quick, you'll give her that."
    "Apparently, she noticed your reaction. Instead of commenting on it, she simply glances away."
    $ cg("eside")
    $ changeAzula("bemused")
    a "(Is that really all it takes to twist a man around like that?)"
    $ cg("cf")
    $ changeAzula("happy")
    a "(Well then!)"
    $ cg("mad")
    "With sudden determination, Azula begins kissing the head of your cock, making a loud popping noise each time she removes her suctioned lips from the sensitive skin."
    $ cg("edick")
    "Even as your cock bobs towards and away from her mouth, she seems dissatisfied with your muted reaction, slowing down while she thinks about it."
    $ cg("re")
    $ changeAzula("disappointed")
    a "(So, kisses aren't good enough, is that it?)"
    $ cg("cf")
    $ changeAzula("frustrated")
    a "(Well then...)"
    $ cg("mad")
    "With renewed vigor, Azula begins licking your cock, starting from the middle before slowly dragging her tongue along the bottom of your shaft."
    $ cg(" ") #remove "mouth_kiss"
    "When she reaches the head of your cock, she tilts her head back to flick your urethra with the tip of her tongue, sending another strong shiver throughout your body." 
    $ cg("re")
    "As Azula repeats the process, she begins to meet your eyes with each lick, obviously looking for a sign of weakness. Though you're growing impatient, there's a certain charm in watching the Fire Lord lick your cock and grow more exasperated as she fails to cause another involuntary reaction."
    $ cg("cf", "eplay")
    $ changeAzula("bemused")
    a "(Is my sense of foreplay not strong enough?)"
    $ cg("eoff")
    $ changeAzula("neutral")
    a "(Maybe I'm licking too fast...)"
    $ cg("re")
    $ changeAzula("disappointed")
    a "(...but maybe it's too late to slow down.)"
    $ changeAzula("frustrated")
    a "(He should be begging me to put it in my mouth!)"
    $ cg("mad")
    "Azula returns to her original position."
    $ cg("az1", "lil", "eplay")
    $ changeAzula("mad")
    a "What's the matter with you?"
    $ cg("st")
    $ changeAzula("stern")
    a "Are you planning to ask me to suck your dick or what!?"
    $ cg("mad")
    menu:
        "No":
            pc "Of course not. You should be able to judge for yourself when it's time to take it to the next level."
            #$ changeLee("")
            $ changeAzula("bemused")
            a "Hmm..."
            $ cg("lil", "eoff")
            $ changeAzula("content")
            a "I suppose you're right."
            $ cg("bm")
            $ changeAzula("excited")
            a "Well, I think that moment has long since passed."
            $ cg("st", "eplay")
        "Yes":
            pc "I'm sorry. Of course I was going to. It's just that I was enjoying myself so much."
            #$ changeLee("")
            $ changeAzula("annoyed")
            a "Oh, so I'm a source of amusement, is that it!?"
            $ cg("mad")
            $ changeAzula("mad")
            a "I imagine I would enjoy the sight of your burning corpse almost as much!"
            $ changeAzula("frustrated")
            a "Anyway, I'll take your response as a 'yes', so we can get on with this stupid exercise."
            $ cg("st", "eoff")
    
    "Azula unceremoniously opens her mouth and manages to fit half your cock into her mouth before you feel the back of her throat."
    $ cg("az5", "d4_nw", "sd", "eplay")
    pc "That's a good girl."
    #$ changeLee("")
    "She glares at you and lightly bites down on your cock."
    $ cg("mad")
    pc "What? I gave you a compliment!"
    #$ changeLee("")
    "That was the wrong thing to say. Azula begins scraping her teeth around your cock as she pulls her head back, tugging your member up with her."
    $ cg("edick")
    pc "I mean, good woman! That's a good woman!"
    #$ changeLee("")
    "Satisfied with your reversal, Azula relaxes her jaw, but continues to pull back as she sucks until the head of your cock is resting in her mouth."
    $ cg("sd")
    "After holding it there for a moment while passing her tongue around the top of you cock, she begins to blow as she pushes her head forward, taking your cock all the way back into her mouth until it nudges against the back of her throat."
    $ cg("pp")
    "Azula's spit runs down your shaft after she repeats the process several times, speeding up as the surface of your cock becomes slicker and easier for her lips to slide across."
    $ cg("az_w")
    pc "You're doing a good job, Azula."
    #$ changeLee("")
    $ cg("sd")
    "Exaggerating her efforts, Azula noisily slurps on your cock as she pulls back and blows spit further down the shaft as she pushes forward."
    menu:
        "Force her further down":
            pc "But I know how you can do a better job."
            #$ changeLee("")
            $ changeAzula("bemused")
            a "Hmmb daa?"
            $ cg("pp", "eplay")
            "Without warning, you reach around the back of her head, grab her hair, and push her head further down, forcing your cock down her throat. She gags a couple of times, but otherwise just seems surprised."
            $ cg("az6", "d6_w", "hairgrab", "L72", "eshock")
            $ changeAzula("surprised")
            a "Goog ga goo googing!"
            $ cg("mad", "eplay1")
            pc "It's called 'deepthroat'. You should get used to it."
            #$ changeLee("")
            "You remove your hand and lay back. If she can't take it, you don't want to be in her way."
            $ cg("L72")
        "Ask her to take it deeper":
            pc "But you could do a better job if you could get it further down."
            #$ changeLee("")
            $ changeAzula("bemused")
            a "Ha gaag goh..."
            $ cg("pp", "eplay")
            "Somewhat reluctantly, Azula presses down further, breathing in deeply as she tries to keep herself from gagging while she forces your cock down her throat."
            $ cg("az6", "d6_w", "pl", "edick")
            $ changeAzula("excited")
            a "Gaag gig?"
            $ cg("L72", "eplay")
            pc "Yeah, just like that."
            #$ changeLee("")
            "You sigh contentedly and lay back. If she can do this herself, it's only a matter of time until you can be more rough."
    
    pc "And whatever you do, don't bite down!"
    #$ changeLee("")
    $ changeAzula("annoyed")
    a "Gaah gaah, gah go..."
    $ cg("st", "elarplay")
    $ changeAzula("stern")
    a "(He could at least have the decency to look at me while I do this for him!)"
    $ cg("edick")
    $ changeAzula("content")
    a "(Not that I don't enjoy it...)"
    $ cg("re")
    $ changeAzula("bemused")
    a "(I wonder if he knows that.)"
    $ cg("L72")
    "Azula cautiously tries to take more of your cock into her throat, but shudders and stops after managing another inch before returning to her previous position."
    $ cg("pl")
    $ changeAzula("neutral")
    a "(It's too much...)"
    $ changeAzula("disappointed")
    a "(I can hardly breathe!)"
    $ cg("eshock")
    $ changeAzula("frustrated")
    a "(How am I supposed to stuff the rest of it down my throat?)"
    $ cg("L72")
    pc "Do you need some time to recover, or are you going to finish the job?"
    #$ changeLee("")
    "She pauses to glare at you."
    $ cg("mad", "eplay")
    pc "Hey, I'm just saying. You're the one who asked me to help you to become a better lover."
    #$ changeLee("")
    "Your reminder refocuses her efforts, though for a moment, you thought she'd start biting again."
    $ cg("edick")
    "Instead of trying to immediately take it deeper again, Azula slowly bobs her head up and down, practically massaging your cock with her throat."
    $ cg("re")
    pc "So good..."
    #$ changeLee("")
    "Although you were hoping that she'd fill her throat with more and more of your member as she slurps on your cock, she doesn't even go as far as she did before."
    "Despite your disappointment, you can feel your orgasm start to build up inside you."
    $ changeAzula("excited")
    a "(It's pulsing...)"
    $ cg("elarplay")
    menu:
        "Warn her":
            pc "I'm gonna cum, Azula!"
            #$ changeLee("")
            "Azula immediately pulls off your cock. Instead of moving out of the way, she keeps her mouth open as you spray her with cum."
            $ cg("az1", "dickew", "blur", "spidjr" "lil", "edick", "mouthopen")
            "As your seed splashes across her face, she closes her eyes, but opens them again when she realizes none of it hit her eyes."
            $ cg("eplay", "jizzums", "mjizzc", "jizzc", "jizzL", "jizzlips", "jizz") #remove "blur", "spidjr"
            $ changeAzula("content")
            a ".........."
            $ cg("bm", "eoff")
            "You hear a loud 'gulp' as Azula swallows your cum. Meanwhile, the cum on her chin drips off and falls to the bed."
            $ cg("mcumlipsc", "cumlips")
            $ changeAzula("happy")
            a "There, I ate it all."
            $ cg("lil", "eplay", "mouthopen", "jizzc", "jizzL", "jizzlips")
            pc "You missed some."
            #$ changeLee("")
            $ changeAzula("frustrated")
            a "Feh..."
            $ cg("st", "eoff", "mcumlipsc", "cumlips") #remove "mouthopen"
            "Before continuing, Azula licks the cum off her lips."
            $ cg("lick") #remove "mcumlipsc"
            $ changeAzula("excited")
            a "So, how was that?"
            $ cg("bm", "eplay")
            pc "A good ending to a great blowjob."
            #$ changeLee("")
            $ changeAzula("mad")
            a "Only a good ending!?"
            $ cg("mad")
            $ changeAzula("annoyed")
            a "I ate your slimy cum after I let it splash on my tongue!"
            $ cg("edick")
            pc "But not all of it."
            #$ changeLee("")
        "Hold her down":
            "You lean forward and, with the same motion, reach around the back of her head and grab her hair."
            $ cg("hairgrab")
            "Azula doesn't even have time to glare at you before you fill her throat with cum, though she blows out so at least she doesn't have to swallow it."
            $ cg("pl", "edick", "spidsb")
            "She tries to buck her head back as cum seeps out her nose, but it doesn't make a difference. You're too strong."
            $ cg("eplay", "spide", "spidtan") #remove "spidsb"
            "However, you know when to quit. As soon as you let go, she reels back and is overtaken by a fit of harsh coughing. Once she's done, she glares at you."
            $ cg("az1", "dickew", "mad", "eup", "cumnose", "cumlip", "mcumlip") #add "spidtan" duplicate layer to "dickew"
            "Before she does anything, Azula licks the cum off her lips."
            $ cg("lick") #remove "mcumlip"
            "For a moment, she glances at your cock. Suddenly, you recall her comment about breathing fire. Maybe you were too forceful."
            $ cg("edick") #remove "lick"
            "She opens her mouth to yell, but stops short as she realizes it's still full of cum."
            $ cg("mouthopen", "cumnose", "jizzc", "jizzL", "jizz") #"layer_87" is default, "jizzL" refers to "Jizz_Lines" while jizzlips refers to "Jizz_on_Lips")
            "You have to suppress a smile as she glances away while she swallows your cum, wincing as it travels down her bruised gullet."
            $ cg("bm", "eoff", "cumnose", "cumlip") #remove "mouthopen" layers
            $ changeAzula("mad")
            a "What the fuck was that!?"
            $ cg("mouthopen", "mad", "eplay", "cumnose", "jizzc") #no "jizz" layer
            pc "A great ending to a good blowjob."
            #$ changeLee("")
            $ changeAzula("mad")
            a "Only a good blowjob!?"
            $ changeAzula("annoyed")
            a "I took your dirty cock farther than it's ever been!"
            $ cg("edick")
            pc "But not all the way."
            #$ changeLee("")
    
    $ changeAzula("bemused")
    a "You're beginning to sound very selfish."
    $ cg("eplay", "cumnose", "cumlip") #remove "mouthopen"
    $ changeAzula("frustrated")
    a "I don't like selfish people."
    $ cg("st")
    $ changeAzula("stern")
    a "Do you know what happens to people that I don't like?"
    $ cg("edick")
    pc "I feel obliged to remind you that it was your command to treat you like this, despite my protests, Fire Lord Azula."
    #$ changeLee("")
    $ changeAzula("mad")
    a "You think I don't know that, you imbecile!?"
    $ cg("eplay")
    $ changeAzula("frustrated")
    a "I was just being-"
    $ cg("bm", "eoff")
    pc "A royal pain?"
    #$ changeLee("")
    $ changeAzula("neutral")
    a "Yes, [pc_name]."
    $ cg("lil", "eplay")
    "Azula stands up and turns around." #fade to black
    $ changeAzula("content")
    a "Now, untie me."
    $ changeAzula("bemused")
    a "Your 'Fire Lord' commands it."
    pc "My cock could still use a little more-"
    #$ changeLee("")
    $ changeAzula("mad")
    a "Now!"
    "You immediately stand up and undo her bondage, knowing that she isn't just being a 'royal pain' this time. It's hard to tell when she's serious, but not impossible; you're starting to develop a knack for it. Once you do, then you can begin the enormously difficult task of figuring out how to manipulate her, if such a thing is even possible."
    pause 
    "We hope you enjoyed our demo!"
    "Learn more by visiting our Patreon page at {a=https://patreon.com/mindbreakstudios2}patreon.com/mindbreakstudios2{/a}"
