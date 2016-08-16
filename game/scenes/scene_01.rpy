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
    $ cg("mouth_way_open", "super_turbo_mad", "eyes_at_player", "angry_flames", "foreground_flames") #in addition to "foreground_flames"
    "Heat washes over you as the flames between the two of you flare up."
    $ changeAzula("mad")
    a "I told you to stop addressing  me so formally!"
    pc "Forgive me, Azula. It's difficult to change after so many years of respecting authority."
    #$ changeLee("")
    $ changeAzula("neutral")
    $ cg("mouth_open", "confused", "eyes_at_player", "angry_flames")
    a "There's nothing to forgive."
    $ cg("mouth_closed") #remove "angry_flames"
    "As the flames return to their normal size, you breathe a quiet sigh of relief."
    $ changeAzula("stern")
    $ cg("mouth_open", "confused", "eyes_at_player", "blank")
    a "However, should I need to remind you again, I'm afraid I might need to banish you for ugliness in addition to stupidity."
    $ changeAzula("content")
    $ cg("you_sure", "eyes_to_side", "mouth_open")
    a "Burn victims aren't particularly attractive."
    "You clench your fist in anger. As a veteran, you've seen your fair share of burn victims. Most of them weren't lucky enough to only suffer a superficial wound. Even if they were your enemies, it's not a fate to make light of. She has no right to speak this way."
    pc "With all your experience on the front lines, naturally you would know."
    #$ changeLee("")
    $ cg("mouth_open", "angry", "eyes_at_player")
    "Azula narrows her eyes at you, unsure if you're insulting her."
    $ changeAzula("annoyed")
    a "It's an obvious fact, [pc_name]."
    $ changeAzula("stern")
    $ cg("mouth_open", "angry", "eyes_aimed_up")
    a "But enough about weaklings of the past!"
    $ changeAzula("content")
    $ cg("mouth_open", "confused", "eyes_at_player")
    a "I'm feeling a bit parched today."
    $ changeAzula("bemused")
    $ cg("mouth_open", "you_sure")
    a "What are you going to do about it?"
    menu:
        "Blowjob":
            pc "I'm going to let you suck my cock."
            #$ changeLee("")
            $ cg("mouth_open", "you_sure", "eyes_to_side")
            "Azula rolls her eyes."
            $ changeAzula("disappointed")
            a "Could you be any more blunt?"
            pc "Your last performance was not very inspiring."
            #$ changeLee("")
            $ changeAzula("mad")
            $ cg("mouth_open", "angry", "eyes_at_player")
            a "Are you really blaming your lack of imagination on me!?"
            pc "So many questions. Yet not one is the answer. My cock in your mouth."
            #$ changeLee("")
            $ changeAzula("bemused")
            $ cg("mouth_open", "angry", "eyes_to_side")
            a "Hmm..."
            $ changeAzula("content")
            $ cg("mouth_open", "you_sure")
            a "Crude, but effective."
            $ changeAzula("excited")
            $ cg("mouth_open", "confused", "eyes_aimed_up")
            a "Truly, I am quite thirsty."
            $ changeAzula("stern")
            $ cg("mouth_open", "angry", "eyes_at_player")
            a "Enough of haiku."
            "Azula leaps from her pillow and through the flames, quickly walking past you as she orders you to follow her." #screen cuts to black
            $ black("show")
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
    $ cg("Norope", "Norope", "Eye1", "blank", "blank", "blank")
    $ black("hide")
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
    
    $ cg("arm_tied", "arm_tied", "eye1", "dude")
    "Azula places her arms behind her back and nods her head at you, so you immediately begin to tie her hands."
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
    $ cg("arm_tied", "arm_tied")
    a "Fine, it's perfectly tight."
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
    $ black("show")
    "You push Azula forward. With a low growl of annoyance, she begins to walk as directed." #black screen
    
    $ cg_scene = "t8"
    $ cg("a1", "blank", "blank", "blank")
    $ black("hide")
    "Once you reach her bed chamber, you undress and lie down. Azula kneels between your legs." #T8.psd, "a1", "d1", "st", "eplay"
    $ changeAzula("bemused")
    a "Well?"
    pc "Well what?"
    #$ changeLee("")
    $ changeAzula("disappointed")
    a "When are you going to get..."
    $ cg("a2")
    "Azula glances away before finishing her question."
    $ changeAzula("frustrated")
    a "...hard?"
    pc "That's up to you."
    #$ changeLee("")
    $ changeAzula("mad")
    $ cg("a3")
    a "Is that so!?"
    $ changeAzula("stern")
    $ cg("a4")
    a "You've never had trouble before!"
    pc "The novelty of fucking the Fire Lord has worn off somewhat."
    #$ changeLee("")
    $ changeAzula("disappointed")
    $ cg("a5")
    a "Feh..."
    $ cg("a6")
    "Without further comment, Azula dips her head below your growing member and balances it on the side of her face, pressing against your balls to keep your cock steady."
    pc "Is that all you're going to do?"
    #$ changeLee("")
    $ changeAzula("mad")
    $ cg("a7")
    a "What is it, exactly, that you expect of me, [pc_name]?"
    "The venom in her voice is unmistakable, but seeing her like this emboldens you."
    pc "You could lick my balls for a start. They're already on your lips."
    #$ changeLee("")
    $ changeAzula("frustrated")
    $ cg("a8")
    a "Disgusting..."
    $ cg("a9")
    "Azula's expression of anger soon disappears as she moves from hesitantly dabbing her tongue against your sack to actually passing her whole tongue over the wrinkles."
    $ changeAzula("annoyed")
    a "(I can't believe men enjoy this.)"
    $ changeAzula("stern")
    $ cg("a10")
    a "(It just seems so unnatural.)"
    $ changeAzula("content")
    $ cg("a11")
    a "(And yet...)"
    pc "Don't be afraid to suck on them too."
    #$ changeLee("")
    $ cg("a12")
    "As a response, Azula painfully whips her tongue against one of your balls."
    pc "Ow!"
    #$ changeLee("")
    $ cg("a13")
    "Azula chuckles as she begins to lick the root of your shaft."
    $ changeAzula("happy")
    a "Sorry, did I do it wrong?"
    $ changeAzula("stern")
    $ cg("a14")
    a "How clumsy of me!"
    pc "You're just making it harder for me to get hard."
    #$ changeLee("")
    $ changeAzula("bemused")
    $ cg("a15")
    a "Do you have difficulty using the word 'difficult' as well?"
    pc "What are you, a thesaurus?"
    #$ changeLee("")
    $ cg("a16")
    "Declining to trade words with you any longer, Azula continues to lick your cock, moving higher up as it rises off her face."
    $ cg("a17")
    "Once you're fully aroused, she dips her head back under your cock and rests it on her forehead."
    menu:
        "Question her":
            pc "What are you doing?"
            #$ changeLee("")
            $ changeAzula("mad")
            $ cg("a18")
            a "I wasn't aware I had to explain myself to you!"
            $ changeAzula("neutral")
            $ cg("a19")
            a "Anyway, I just wanted to see how large it was from this angle."
            pc "So, what do you think?"
            #$ changeLee("")
            $ changeAzula("content")
            $ cg("a20")
            a "It is rather impressive..."
            $ changeAzula("disappointed")
            $ cg("a21")
            a "I don't expect I'll be able to fit much of it into my mouth, even after our last session."
            $ changeAzula("happy")
            $ cg("a22")
            a "Small wonder that it feels so invasive when you enter me..."
            pc "But in a good way, right?"
            #$ changeLee("")
            $ changeAzula("stern")
            $ cg("a23")
            a "Hmph!"
            $ changeAzula("mad")
            $ cg("a24")
            a "As if I would keep you around otherwise!"
            $ changeAzula("annoyed")
            $ cg("a25")
            a "And stop asking so many questions!"
        "Bounce your cock":
            "You lean back for a moment before pushing forward, gently slapping you cock against her forehead with a soft 'smack'."
            $ changeAzula("stern")
            $ cg("a26")
            a "What was that for?"
            pc "I'm just playing around."
            #$ changeLee("")
            $ changeAzula("annoyed")
            $ cg("a27")
            a "It seems more as if you're impatient with me."
            pc "Well, I can only stay aroused for so long without some action."
            #$ changeLee("")
            $ changeAzula("frustrated")
            $ cg("a28")
            a "Hmph..."
            $ changeAzula("")
            a "How's this for action?"
            $ changeAzula("happy")
            $ cg("a29")
            a "I wanted to see how...large your rod was resting..."
            $ changeAzula("excited")
            a "...resting on my pristine, royal face..."
            pc "Was that your idea of dirty talk? It'd be better without all the pauses."
            #$ changeLee("")
            $ changeAzula("mad")
            $ cg("a30")
            a "Nevermind then!"
    
    $ cg("a31")
    "With that exclamation, Azula moves her head up and presses her soft lips against the head of your cock."
    "You shiver slightly at the unexpected tenderness. The girl does learn quick, you'll give her that."
    $ cg("a32")
    "Apparently, she noticed your reaction. Instead of commenting on it, she simply glances away."
    $ changeAzula("bemused")
    $ cg("a33")
    a "(Is that really all it takes to twist a man around like that?)"
    $ changeAzula("happy")
    $ cg("a34")
    a "(Well then!)"
    $ cg("a35")
    "With sudden determination, Azula begins kissing the head of your cock, making a loud popping noise each time she removes her suctioned lips from the sensitive skin."
    $ cg("a36")
    "Even as your cock bobs towards and away from her mouth, she seems dissatisfied with your muted reaction, slowing down while she thinks about it."
    $ changeAzula("disappointed")
    $ cg("a37")
    a "(So, kisses aren't good enough, is that it?)"
    $ changeAzula("frustrated")
    $ cg("a38")
    a "(Well then...)"
    $ cg("a39") #remove "mouth_kiss"
    "With renewed vigor, Azula begins licking your cock, starting from the middle before slowly dragging her tongue along the bottom of your shaft."
    $ cg("a40")
    "When she reaches the head of your cock, she tilts her head back to flick your urethra with the tip of her tongue, sending another strong shiver throughout your body." 
    $ cg("a41")
    "As Azula repeats the process, she begins to meet your eyes with each lick, obviously looking for a sign of weakness. Though you're growing impatient, there's a certain charm in watching the Fire Lord lick your cock and grow more exasperated as she fails to cause another involuntary reaction."
    $ changeAzula("bemused")
    $ cg("a42")
    a "(Is my sense of foreplay not strong enough?)"
    $ changeAzula("neutral")
    $ cg("a43")
    a "(Maybe I'm licking too fast...)"
    $ changeAzula("disappointed")
    a "(...but maybe it's too late to slow down.)"
    $ changeAzula("frustrated")
    $ cg("a44")
    a "(He should be begging me to put it in my mouth!)"
    $ cg("a45")
    "Azula returns to her original position."
    $ changeAzula("mad")
    $ cg("a46")
    a "What's the matter with you?"
    $ changeAzula("stern")
    $ cg("a47")
    a "Are you planning to ask me to suck your dick or what!?"
    menu:
        "No":
            pc "Of course not. You should be able to judge for yourself when it's time to take it to the next level."
            #$ changeLee("")
            $ changeAzula("bemused")
            $ cg("a48")
            a "Hmm..."
            $ changeAzula("content")
            $ cg("a49")
            a "I suppose you're right."
            $ changeAzula("excited")
            $ cg("a50")
            a "Well, I think that moment has long since passed."
        "Yes":
            pc "I'm sorry. Of course I was going to. It's just that I was enjoying myself so much."
            #$ changeLee("")
            $ changeAzula("annoyed")
            $ cg("a51")
            a "Oh, so I'm a source of amusement, is that it!?"
            $ changeAzula("mad")
            a "I imagine I would enjoy the sight of your burning corpse almost as much!"
            $ changeAzula("frustrated")
            $ cg("a52")
            a "Anyway, I'll take your response as a 'yes', so we can get on with this stupid exercise."
    
    $ cg("a53")
    "Azula unceremoniously opens her mouth and manages to fit half your cock into her mouth before you feel the back of her throat."
    pc "That's a good girl."
    #$ changeLee("")
    $ cg("a54")
    "She glares at you and lightly bites down on your cock."
    pc "What? I gave you a compliment!"
    #$ changeLee("")
    $ cg("a55")
    "That was the wrong thing to say. Azula begins scraping her teeth around your cock as she pulls her head back, tugging your member up with her."
    pc "I mean, good woman! That's a good woman!"
    #$ changeLee("")
    $ cg("a56")
    "Satisfied with your reversal, Azula relaxes her jaw, but continues to pull back as she sucks until the head of your cock is resting in her mouth."
    $ cg("a57")
    "After holding it there for a moment while passing her tongue around the top of you cock, she begins to blow as she pushes her head forward, taking your cock all the way back into her mouth until it nudges against the back of her throat."
    $ cg("a58")
    "Azula's spit runs down your shaft after she repeats the process several times, speeding up as the surface of your cock becomes slicker and easier for her lips to slide across."
    pc "You're doing a good job, Azula."
    $ cg("a59")
    #$ changeLee("")
    "Exaggerating her efforts, Azula noisily slurps on your cock as she pulls back and blows spit further down the shaft as she pushes forward."
    menu:
        "Force her further down":
            pc "But I know how you can do a better job."
            #$ changeLee("")
            $ changeAzula("bemused")
            $ cg("a60")
            a "Hmmb daa?"
            $ cg("a61")
            "Without warning, you reach around the back of her head, grab her hair, and push her head further down, forcing your cock down her throat. She gags a couple of times, but otherwise just seems surprised."
            $ changeAzula("surprised")
            $ cg("a62")
            a "Goog ga goo googing!"
            pc "It's called 'deepthroat'. You should get used to it."
            #$ changeLee("")
            $ cg("a63")
            "You remove your hand and lay back. If she can't take it, you don't want to be in her way."
        "Ask her to take it deeper":
            pc "But you could do a better job if you could get it further down."
            #$ changeLee("")
            $ changeAzula("bemused")
            $ cg("a60")
            a "Ha gaag goh..."
            $ cg("a64")
            "Somewhat reluctantly, Azula presses down further, breathing in deeply as she tries to keep herself from gagging while she forces your cock down her throat."
            $ changeAzula("excited")
            $ cg("a65")
            a "Gaag gig?"
            pc "Yeah, just like that."
            #$ changeLee("")
            "You sigh contentedly and lay back. If she can do this herself, it's only a matter of time until you can be more rough."
    
    pc "And whatever you do, don't bite down!"
    #$ changeLee("")
    $ changeAzula("annoyed")
    $ cg("a66")
    a "Gaah gaah, gah go..."
    $ changeAzula("stern")
    $ cg("a67")
    a "(He could at least have the decency to look at me while I do this for him!)"
    $ changeAzula("content")
    $ cg("a68")
    a "(Not that I don't enjoy it...)"
    $ changeAzula("bemused")
    $ cg("a69")
    a "(I wonder if he knows that.)"
    $ cg("a70")
    "Azula cautiously tries to take more of your cock into her throat, but shudders and stops after managing another inch before returning to her previous position."
    $ changeAzula("neutral")
    a "(It's too much...)"
    $ changeAzula("disappointed")
    $ cg("a71")
    a "(I can hardly breathe!)"
    $ changeAzula("frustrated")
    $ cg("a72")
    a "(How am I supposed to stuff the rest of it down my throat?)"
    pc "Do you need some time to recover, or are you going to finish the job?"
    #$ changeLee("")
    $ cg("a73")
    "She pauses to glare at you."
    pc "Hey, I'm just saying. You're the one who asked me to help you to become a better lover."
    #$ changeLee("")
    $ cg("a74")
    "Your reminder refocuses her efforts, though for a moment, you thought she'd start biting again."
    $ cg("a75")
    "Instead of trying to immediately take it deeper again, Azula slowly bobs her head up and down, practically massaging your cock with her throat."
    pc "So good..."
    #$ changeLee("")
    "Although you were hoping that she'd fill her throat with more and more of your member as she slurps on your cock, she doesn't even go as far as she did before."
    "Despite your disappointment, you can feel your orgasm start to build up inside you."
    $ changeAzula("excited")
    $ cg("a76")
    a "(It's pulsing...)"
    menu:
        "Warn her":
            pc "I'm gonna cum, Azula!"
            #$ changeLee("")
            $ cg("a86")
            "Azula immediately pulls off your cock. Instead of moving out of the way, she keeps her mouth open as you spray her with cum."
            $ cg("a87", "jizz") #remove "blur", "spidjr"
            "As your seed splashes across her face, she closes her eyes, but opens them again when she realizes none of it hit her eyes."
            $ changeAzula("content")
            $ cg("a88")
            a ".........."
            $ cg("a89")
            "You hear a loud 'gulp' as Azula swallows your cum. Meanwhile, the cum on her chin drips off and falls to the bed."
            $ changeAzula("happy")
            $ cg("a90")
            a "There, I ate it all."
            pc "You missed some."
            #$ changeLee("")
            $ changeAzula("frustrated")
            $ cg("a91") #remove "mouthopen"
            a "Feh..."
            $ cg("a92") #remove "mcumlipsc"
            "Before continuing, Azula licks the cum off her lips."
            $ changeAzula("excited")
            $ cg("a93")
            a "So, how was that?"
            pc "A good ending to a great blowjob."
            #$ changeLee("")
            $ changeAzula("mad")
            $ cg("a94")
            a "Only a good ending!?"
            $ changeAzula("annoyed")
            $ cg("a95")
            a "I ate your slimy cum after I let it splash on my tongue!"
            pc "But not all of it."
            #$ changeLee("")
        "Hold her down":
            $ cg("a77", "hairgrab")
            "You lean forward and, with the same motion, reach around the back of her head and grab her hair."
            $ cg("a77")
            "Azula doesn't even have time to glare at you before you fill her throat with cum, though she blows out so at least she doesn't have to swallow it."
            $ cg("a78") #remove "spidsb"
            "She tries to buck her head back as cum seeps out her nose, but it doesn't make a difference. You're too strong."
            $ cg("a79", "blank") #add "spidtan" duplicate layer to "dickew"
            "However, you know when to quit. As soon as you let go, she reels back and is overtaken by a fit of harsh coughing. Once she's done, she glares at you."
            $ cg("a80") #remove "mcumlip"
            "Before she does anything, Azula licks the cum off her lips."
            $ cg("a81") #remove "lick"
            "For a moment, she glances at your cock. Suddenly, you recall her comment about breathing fire. Maybe you were too forceful."
            $ cg("a82") #"layer_87" is default, "jizzL" refers to "Jizz_Lines" while jizzlips refers to "Jizz_on_Lips")
            "She opens her mouth to yell, but stops short as she realizes it's still full of cum."
            $ cg("a83") #remove "mouthopen" layers
            "You have to suppress a smile as she glances away while she swallows your cum, wincing as it travels down her bruised gullet."
            $ changeAzula("mad")
            $ cg("a84") #no "jizz" layer
            a "What the fuck was that!?"
            pc "A great ending to a good blowjob."
            #$ changeLee("")
            $ changeAzula("mad")
            a "Only a good blowjob!?"
            $ changeAzula("annoyed")
            $ cg("a85")
            a "I took your dirty cock farther than it's ever been!"
            pc "But not all the way."
            #$ changeLee("")
    
    $ changeAzula("bemused")
    $ cg("a96") #remove "mouthopen"
    a "You're beginning to sound very selfish."
    $ changeAzula("frustrated")
    $ cg("a97")
    a "I don't like selfish people."
    $ changeAzula("stern")
    $ cg("a98")
    a "Do you know what happens to people that I don't like?"
    pc "I feel obliged to remind you that it was your command to treat you like this, despite my protests, Fire Lord Azula."
    #$ changeLee("")
    $ changeAzula("mad")
    $ cg("a99")
    a "You think I don't know that, you imbecile!?"
    $ changeAzula("frustrated")
    $ cg("a100")
    a "I was just being-"
    pc "A royal pain?"
    #$ changeLee("")
    $ changeAzula("neutral")
    $ cg("a101")
    a "Yes, [pc_name]."
    "Azula stands up and turns around." #fade to black
    $ black("show")
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
