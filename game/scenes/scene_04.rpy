label scene_04:
    "Several weeks have gone by since Azula first started asking personal questions. Her attraction to you became increasingly apparent, and it wasn't long before she demanded that you act as if you were courting her. According to her, she wants to be prepared for when she has to marry, but you can almost believe that she likes you."
    "Almost."
    "Even though she's ordered you to call her 'Azula' instead of 'Fire Lord', you still have to be careful about what you say. There's no question that she still expects to be treated as royalty. You can live with that. In fact, it may be the only way you stay alive."
    "Of course, this new challenge does have its perks…"
    "As you approach the door to the War Room, you notice a piece of paper pinned to the door."
    "It's a note that reads, 'Come to my personal quarters at once."
    pc "I guess she's skipping the briefing today. This should be interesting."
    $ cg_scene = "bedroom"
    $ cg("blank", "blank","blank", "blank", "blank", "blank", "blank", "blank", "blank")
    "When you come to Azula's room, you see that the door is ajar."
    menu:
        "Knock":
            "Not quite sure what to do, you extend your fist and rap on the door a few times."
            $ changeAzula("annoyed")
            a "Do you not understand the meaning of an open door!?"
            a "It means 'come in' and don't waste any time!"
            $ black("hide")
            "You immediately walk into the room and find Azula sitting on her bed."
            $ changeAzula("disappointed")
            a "Finally!"
        "Enter":
            $ black("hide")
            "Taking that as a sign to just go in, you walk into the room to find Azula sitting on her bed."
            $ changeAzula("neutral")
            a "It's about time you showed up!"
            a "I was becoming extremely bored."
            pc "Miss me that much, huh?"
            $ changeAzula("bemused")
            a "That would be a bit generous to say, [pc_name]."
    "With that, Azula hops up from the bed and strides across the room, stopping in front of you."
    $ cg("0", "eyebrow default", "mouth default", "Pupil at player")
    $ changeAzula("neutral")
    $ cg(effect_3="mouth talking")
    a "Do you know why I've asked you here?"
    $ cg(effect_3="mouth default")
    pc "I wouldn't hazard a guess."
    $ cg(effect_2="eyebrow surprised", effect_3="mouth smile closed")
    "The Fire Lord briefly tilts her head back and laughs." #Laugh maybe here?
    $ changeAzula("excited")
    $ cg(effect_3="mouth smile open")
    a "Normally, a guess would indeed be quite hazardous."
    $ changeAzula("happy")
    a "But I'm not interested in hurting you, so don't worry."
    $ cg(effect_3="mouth smile closed")
    pc "That's very-"
    $ changeAzula("bemused")
    $ cg(effect_3="mouth smile open", effect_5="eyeline closing")
    a "For now."
    $ cg(effect_3="mouth smile closed")
    pc "Is that a joke?"
    $ changeAzula("happy")
    $ cg(effect_3="mouth smile open")
    a "Does it sound like I'm joking?"
    $ cg(effect_3="mouth smile closed", effect_5="blank")
    "You take a moment to study her face. She's smiling, but you can't tell if that's a good sign or a bad omen. There's a certain sickly aspect to it, at least at first glance."  #need Smile better here
    pc "I would say 'yes'."
    $ changeAzula("content")
    $ cg(effect_3="mouth smile open", effect_2="brow pushed together") #Smile talking?
    a "Nothing to worry about, then."
    $ changeAzula("happy")
    a "Now, be a good boy and take a guess."
    $ cg(effect_3="mouth smile closed")
    pc "To, ah, do something on the, uh, bed?"
    $ changeAzula("stern")
    $ cg(effect_3="mouth talking", effect_2="eyebrow mad")
    a "Don't stutter, [pc_name]."
    $ changeAzula("bemused")
    $ cg(effect_2="eyebrow little up little down")
    a "If you're lucky enough to make it into my bed, I expect you to be fully mature about the prospect."
    $ changeAzula("content")
    $ cg(effect_2="eyebrow default")
    a "But to answer your question: no."
    $ cg(effect_3="mouth default")
    pc "Then what?"
    $ changeAzula("disappointed")
    $ cg(effect_2="brow pushed together", effect_3="mouth talking")
    a "Has anyone ever told you that you're unusually bad at guessing?"
    $ cg(effect_3="mouth default")
    pc "You'd be the first."
    $ changeAzula("bemused")
    $ cg(effect_2="eyebrow little up little down", effect_3="mouth talking")
    a "Is that so?"
    $ cg(effect_3="Mouth LipBite", effect_4="Pupil left")
    "Azula bites her lip for a second before continuing." #Lipbite
    $ changeAzula("content")
    $ cg(effect_3="mouth talking", effect_4="Pupil left")
    a "I think that, since you've shown me most of your body, it's only fair that I show you most of {size=+10}my{/size} body." #emphasis on 'my'
    $ cg(effect_3="mouth default")
    "Your eyebrows shoot up as far as they can. It's one thing that she wants you to act like you're courting her, but this is downright disturbing. If anyone ever found out…"
    $ changeAzula("neutral")
    $ cg(effect_3="mouth talking", effect_2="eyebrow default", effect_4="Pupil at player")
    a "I can see what you're thinking, and you needn't worry."
    $ changeAzula("happy")
    a "Nobody is going to know about what happens between you and me, since the only people here are you and I."
    $ cg(effect_2="eyebrow mad", effect_5="eyeline closing")
    $ changeAzula("bemused")
    a "Unless you're planning on telling someone…"
    $ cg(effect_3="mouth default")
    "The Fire Princess narrows her brow, suddenly glaring at you mistrustfully. Your only option is to go along with it."
    pc "Of course not, Azula. It just seems...rather sudden, that's all."
    $ changeAzula("stern")
    a "Hmm…"
    $ cg(effect_2="eyebrow default", effect_5="blank")
    "As her face returns to a more hospitable look, you breathe a quiet sigh of relief. From now on, you'll have to be committed."
    $ changeAzula("neutral")
    $ cg(effect_3="mouth talking")
    a "Well, get used to it."
    a "I don't have any time to waste, unlike you and the rest of my subjects."
    $ cg("1", effect_3="mouth default", effect_4="Pupil down")
    $ cg(effect_4="Pupil at player")
    "With that, Azula quickly reaches under the crest of her armor. You assume that she's undoing some kind of unseen clasp. It would be impossible for her to pull it up over her head. She then tucks her hands underneath the piece, but stops to look at you."
    $ cg(effect_3="mouth talking", effect_2="eyebrow little up little down")
    $ changeAzula("bemused")
    a "Well?"
    $ cg("1", effect_3="mouth default")
    pc "What?"
    $ changeAzula("neutral")
    $ cg(effect_3="mouth talking")
    a "Aren't you going to help me?"
    $ cg(effect_2="brow pushed together")
    $ changeAzula("bemused")
    a "I don't want to just drop my ceremonial armor on the floor!"
    $ cg(effect_3="mouth default")
    pc "I'm not your servant, Azula."
    $ changeAzula("mad")
    $ cg(effect_3="mouth talking", effect_2="eyebrow mad", effect_5="eyeline closing")
    a "Oh, you aren't!?"
    $ cg(effect_3="mouth mad")
    "For a moment, you think fire is going to come shooting out of her hands, but you stand your ground, coolly returning her angry look with an impassive face." # m a d
    pc "That's not what a courter is. Don't you want to learn how to behave properly in a relationship?"
    $ cg(effect_4="Pupil left")
    a "Hmm…"
    $ cg(effect_2="eyebrow default", effect_3="mouth default", effect_5="blank")
    "Azula's anger fades while she considers the merit of your proposal, eventually disappearing altogether."
    $ cg(effect_3="mouth talking")
    $ changeAzula("neutral")
    a "Yes, I suppose you're right."
    a "Very well."
    $ cg("2", effect_3="mouth default", effect_2="eyebrow surprised")
    "She promptly pushes the crest of her armor off the back of her neck. It falls to the floor with a loud 'CLANG!'"
    $ cg(effect_3="mouth talking")
    $ changeAzula("content")
    a "Besides, I can always get a new set."
    $ cg(effect_3="mouth default")
    pc "Can you afford one?"
    $ cg(effect_3="mouth mad 2", effect_2="eyebrow mad", effect_4="Pupil at player")
    "The Fire Lord immediately looks at you, anger flashing across her face. One of these days, one of your jokes just might get you killed."
    $ cg(effect_3="mouth talking")
    $ changeAzula("mad")
    a "Of course I  ca-!"
    $ cg(effect_2="eyebrow surprised")
    $ changeAzula("content")
    a "Oh, I see."
    $ cg(effect_3="mouth smile closed", effect_2="eyebrow default")
    "Panic and regret turn to relief as Azula cracks a small smile." #S M I L E
    $ cg(effect_3="mouth smile open")
    $ changeAzula("happy")
    a "Humorous, [pc_name]."
    $ cg(effect_3="mouth smile closed")
    pc "I try."
    $ changeAzula("content")
    $ cg(effect_3="mouth smile open")
    a "Your efforts do not go entirely unappreciated."
    $ changeAzula("frustrated")
    $ cg(effect_2="eyebrow little up little down", effect_3="mouth talking")
    a "However, you might want to refrain from making light of my status too often, lest you send the wrong message."
    $ cg(effect_3="mouth default")
    "You suppose that's as close to an apology as you're going to get for giving you a minor heart attack. Still, it's progress."
    pc "Right…"
    $ cg("3", effect_4="Pupil left")
    "An uncomfortable silence fills the air as Azula unhooks her pauldrons from her breastplate, tossing them on the floor next to the crest of her armor. Once she's finished, she looks at you questioningly."
    $ cg(effect_3="mouth smile open", effect_2="eyebrow default", effect_4="Pupil at player")
    $ changeAzula("happy")
    a "So, what do you think so far?"
    $ cg(effect_3="mouth smile closed")
    pc "It's certainly well-designed."
    $ changeAzula("bemused")
    $ cg(effect_3="mouth talking", effect_5="eyeline closing", effect_6="eyebrow little up little down", effect_2="blank")
    a "That's not what I meant."
    $ changeAzula("disappointed")
    $ cg(effect_3="mouth default")
    pc "You mean...what do I think of your clothed shoulders?"
    $ cg(effect_3="mouth talking", effect_4="Pupil left", effect_2="eyebrow default")
    a "Nevermind."
    $ cg(effect_3="mouth default")
    pc "Because you don't even ha-"
    $ changeAzula("mad")
    $ cg(effect_3="mouth talking", effect_2="eyebrow mad", effect_4="Pupil at player", effect_6="blank",effect_5="blank")
    a "I said nevermind!"
    $ cg(effect_3="mouth mad")
    "You notice Azula's hands twitch, as if she's about to firebend. That's never a good sign."
    pc "I meant no offense, Azula."
    $ cg("4")
    "Thankfully, instead of making any violent moves, the Fire Princess tucks her hands under her breastplate, preparing to lift it."
    $ changeAzula("neutral")
    $ cg(effect_3="mouth talking", effect_2="eyebrow default", effect_4="pupil down")
    a "Fine, fine…"
    $ cg(effect_2="eyebrow surprised")
    a "Oh, and one more thing."
    $ changeAzula("stern")
    $ cg(effect_2="eyebrow mad", effect_3="mouth default", effect_4="pupil at player")
    "Azula looks at you seriously before continuing. Whatever she's about to say must be meaningful, meaning it'll be trouble for you."
    $ cg(effect_3="mouth talking")
    a "Just because I'm removing my armor doesn't mean I'm vulnerable in the slightest, so don't even think of attacking me, or I'll burn you to a crisp and throw your charred remains into the sewer!"
    a "Am I clear?"
    $ cg(effect_3="mouth default")
    menu:
        "Yes":
            pc "Of course. Azula, I wouldn't even dare to dream of harming you."
            $ cg(effect_3="mouth talking")
            $ changeAzula("mad")
            a "I didn't say 'harm', I said 'attack'."
            a "Why would you even say 'harm'?"
            $ cg(effect_2="eyebrow little up little down", effect_5="eyeline closing")
            a "A slip of the tongue, perhaps?"
            $ cg(effect_3="mouth default")
            pc "N-no, my Lord."
            $ changeAzula("happy")
            $ cg(effect_3="mouth smile open", effect_2="eyebrow default", effect_5="blank")
            a "I was only joking,[pc_name] ."   #[Lee_name]
            $ cg(effect_4="Pupil left", effect_3="mouth smile closed")
            $ changeAzula("content")
            a "Mostly…"
            $ changeAzula("stern")
            $ cg(effect_2="eyebrow mad", effect_3="mouth talking", effect_4="pupil at player")
            a "And what have I told you about calling me 'Lord'!?"
            $ cg(effect_3="mouth default")
            pc "My apologies, Azula."
        "No":
            pc "I'm not sure what you mean. Why would I ever want to attack you?"
            $ changeAzula("bemused")
            $ cg(effect_3="mouth talking", effect_5="eyebrow surprised", effect_4="Pupil down", effect_2="blank")
            a "Why indeed..."
            $ cg(effect_4="Pupil left", effect_6="eyeline closing")
            $ changeAzula("not_amused_3")
            a "Why should anyone want to attack a head of state who would be a valuable asset to anyone who wanted to harm her nation?"
            a "After all, the Fire Nation doesn't have any enemies."
            $ cg(effect_3="mouth default")
            pc "Is that sarcasm?"
            $ cg(effect_5="blank", effect_3="mouth mad 2", effect_2="eyebrow mad", effect_4="pupil at player", effect_6="blank")
            $ changeAzula("mad")
            a "Of course it is, [pc_name]!" #[Lee_name] here
            a "Do I have to spell everything out for you!?"
            a "Honestly, sometimes I question if you're even intelligent enough to warrant my attention."
            $ cg(effect_3="mouth default")
            pc "My apologies, Azula."
    $cg(effect_4="pupil left", effect_3="mouth mad")
    $ changeAzula("not_amused_2")
    a "Hmph!"
    $ cg("5")
    "Scoffing in disgust at your servile response, Azula pulls the breastplate over her head and throws it across the room. After hitting the wall, it loudly crashes against the floor. Evidently, her emotions are running high."
    pc "A woman undressing usually isn't this violent."
    $ cg(effect_3="mouth talking", effect_4="pupil at player")
    $ changeAzula("mad")
    a "Is it any wonder!?"
    $ cg(effect_4="pupil left")
    a "I'm disrobing for a peasant who doesn't even appreciate what he's seeing!"
    $ cg(effect_3="mouth default")
    pc "Of course I appreciate it."
    $ cg(effect_3="mouth lipbite", effect_4="pupil at player", effect_2="eyebrow surprised")
    $ changeAzula("excited")
    "Azula's look rapidly transforms from one of anger to anticipation. It's disconcerting how fast her mood can change, not to mention dangerous."
    $ cg(effect_3="mouth smile open", effect_5="eyeline closing")
    a "Really?"
    $ cg(effect_3="mouth smile closed")
    pc "Yes, it's just...there's not much to comment on, yet."
    $ cg(effect_2="brow pushed together", effect_3="mouth talking", effect_5="blank")
    $ changeAzula("stern")
    a "Ah, I see."
    $ cg(effect_3="mouth smile open", effect_2="eyebrow little up little down")
    $ changeAzula("happy")
    a "Well then, let's not waste any more time!"
    $cg ("base_1", "6", "BrowNeutral P3", "EyeDownP3","mouthp3","blank","blank")
    "True to her word, the Fire Lord immediately bends down and begins rolling down her right boot."
    pc "Huh."
    $cg (effect_4="eyeatplayerp3")
    "However, she pauses at your grunt and looks up at you."
    $ cg(effect_5="mouthp3 talking", effect_3="BrowMad p3")
    $ changeAzula("stern")
    a "What?"
    $ cg(effect_5="mouthp3")
    pc "It's nothing."
    $ cg(effect_5="mouthp3 talking", effect_3="browneutral p3")
    $ changeAzula("neutral")
    a "If you have something to say, I'm interested in hearing it."
    a "That's the point of this little exercise, after all."
    $ cg(effect_5="mouthp3")
    pc "I assumed that your boots were made of metal, what with the armor and everything."
    $ cg(effect_5="mouthp3 talking", effect_3="BrowPerplexedP3")
    $ changeAzula("stern")
    a "Then you're a simpleton."
    $ cg(effect_2="7", effect_5="mouthp3", effect_3="BrowNeutral P3", effect_4="eyedownp3")
    "Satisfied with your answer, Azula finishes removing her boot, tossing it to the side where it limply recedes into itself."
    $ cg("5", "brow pushed together", "mouth smile closed","pupil at player","blank","blank")
    "Following that, she takes a moment to stand up straight, looking at you contemptuously."
    $ cg(effect_3="mouth smile open")
    $ changeAzula("happy")
    a "Metal boots may be superior protection for a simple soldier such as yourself, but it also hinders the wearer's speed."
    a "It's an advantage that a skilled bender such as {size=+10}myself{/size} can't pass up." #emphasis on 'myself'
    $ cg(effect_3="mouth smile closed")
    pc "Oh...I see."
    $cg ("base_1", "8", "BrowNeutral P3", "EyeDownP3","mouthp3","blank","blank")
    "With a sigh, Azula bends down once more to unroll her other boot."
    $ cg(effect_5="mouthp3 talking")
    $ changeAzula("neutral")
    a "No, I very much doubt that you do, [pc_name]." #[lee_name]
    a "How could you?"
    $ cg(effect_4="eyerightp3")
    a "After all, you're just a…"
    $ cg(effect_3="BrowPerplexedP3", effect_4="eyeatplayerp3")
    "The Fire Princess pauses to sigh again, only this time, her tone is one of satisfaction rather than disappointment."
    $ changeAzula("happy")
    a "...brute."
    $ cg(effect_2="9", effect_5="mouthp3")
    $ cg("5", "eyebrow default", "mouth default", "Pupil at player", "blank")
    "Finished, Azula again tosses her footwear, where it lands next to the other boot, and stands up."
    $ cg(effect_3="mouth talking")
    $ changeAzula("neutral")
    a "Now, onto the main course."
    $ cg(effect_5="eyeline closing")
    $ changeAzula("not_amused")
    a "But first...what do you think of my figure?"
    $ cg(effect_3="mouth default")
    menu:
        "I want to see more":
            pc "It leaves me wanting."
            $ cg(effect_3="mouth frown")
            "Azula frowns at your response, but doesn't appear angry."
            $ cg(effect_3="mouth talking")
            $ changeAzula("bemused")
            a "As in, it is wanting?"
            $ cg(effect_3="mouth frown")
            pc "That's not what I-"
            "She doesn't seem to hear you, rolling on as if you hadn't said anything."
            $ cg(effect_3="mouth talking", effect_2="eyebrow mad")
            $ changeAzula("mad")
            a "You'd rather I look like someone else, is that it?"
            $ cg(effect_3="mouth mad")
            pc "No, I-"
            $ cg(effect_3="mouth talking", effect_5="blank")
            $ changeAzula("annoyed")
            a "Because I can very easily find a replacement who is more appreciative of my body!"
            $ cg(effect_3="mouth mad 2")
            "Obviously, you were wrong. She {size=+10}is{/size} angry." #emphasis on 'is'
            pc "If you'll give me the chance to speak…"
            $ cg(effect_3="mouth mad")
            "An uncomfortable silence fills the air, made moreso with Azula continuing to glare at you."
            $ cg(effect_3="mouth talking")
            $ changeAzula("annoyed")
            a "Well!?"
            $ cg(effect_3="mouth mad")
            pc "I wasn't sure if you-"
            $ cg(effect_3="mouth talking")
            $ cg(effect_3="mouth mad")
            "The Fire Lord loudly clears her throat, interrupting your excuse for not talking."
            pc "Right...what I meant was, it leaves me wanting to see more. I like your body."
            $ cg(effect_2="eyebrow surprised", effect_3="mouth default", effect_4="pupil left", effect_5="blush")
            "Azula's look changes to one of slight embarrassment as she realizes how insecure she sounded."
            $ cg(effect_3="mouth talking")
            $ changeAzula("surprised")
            a "Oh."
            $ cg(effect_3="mouth smile closed", effect_4="pupil at player")
            "She gives you an uncharacteristically sincere but weak smile."
            $ cg(effect_3="mouth smile open")
            $ changeAzula("content")
            a "Well...thank you." 
        "I'd have to see more":
            pc "Like I said earlier, you're not showing enough skin to tell."
            "Azula simply looks at you for a moment before cracking a smile."
            $ cg(effect_3="mouth smile open")
            $ changeAzula("content")
            a "Really?"
            a "Tell me, exactly, how much more you need to see before forming an opinion."
            $ cg(effect_3="mouth smile closed", effect_2="eyebrow mad")
            "The Fire Lord maintains her smile, but her brow narrows. You're beginning to suspect she's being insincere."
            $ cg(effect_3="mouth smile open")
            $ changeAzula("happy_mad")
            a "Are you saying my clothes are not suited to my body?"
            $ cg(effect_3="mouth smile closed")
            pc "I-"
            $ cg(effect_3="mouth mad", effect_5="blank")
            "As she interrupts you, her smile disappears, replaced with a cold grimace. There's no doubt that dodging the question again made her angry."
            $ cg(effect_3="mouth talking")
            $ changeAzula("mad")
            a "Or perhaps that the color of my shirt makes my skin look pale and clammy?"
            $ cg(effect_3="mouth mad")
            pc "That's not-"
            $ cg(effect_3="mouth talking")
            $ changeAzula("annoyed")
            a "Is this not a flattering light?"
            $ cg(effect_3="mouth mad")
            pc "Well, it could be brighter in here."
            $ cg(effect_3="mouth mad 2")
            "Your comment only seems to infuriate Azula further. If you weren't in her personal chambers, you're sure the lighting would be a lot more blue."
            $ changeAzula("not_amused_p1")
            a "Maybe I should replace you with someone who has better vision!"
            a "Or maybe I should just set you on fire and look in the mirror to see how the light from your burning corpse catches against my reflection!"
            pc "All I meant was, I'd like to see more clothes come off!"
            $ cg(effect_3="mouth talking")
            $ changeAzula("mad")
            a "I know exactly what you meant, you insolent idiot!"
            $ cg(effect_4="pupil left")
            $ changeAzula("not_amused_p3")
            a "However...I suppose we've come this far."
            $ cg(effect_3="mouth default", effect_5="eyeline closed")
            "Thankfully, Azula appears to force herself to become calm again. You were almost afraid for you life, though you're beginning to suspect all the bluster is really for show."
            $ cg(effect_3="mouth talking", effect_5="blank")
            $ changeAzula("annoyed")
            a "It would be a shame to start all over again."
    $ changeAzula("neutral")
    a "Now then, I suppose...we'll proceed with...my belt."
    $ cg("10", "brow pushed together", "mouth default", "pupil down")
    "As she places her hands on her belt, she looks down at her waist, suddenly unsure of herself."
    pc "What's the matter?"
    $ cg(effect_3="mouth talking")
    $ changeAzula("sad")
    a "It's just that…"
    $ cg(effect_4="Pupil left")
    a "I don't know if…"
    $ cg(effect_3="mouth default", effect_4="pupil down")
    "Azula's gaze drops to her feet. You almost want to ask what's wrong, but then again, you prefer to have a body that isn't burnt to a crisp."
    $ changeAzula("stern")
    a "…………."
    $ cg(effect_5="eyeline closed",effect_3="mouth talking", effect_2="eyebrow default", effect_4="pupil at player")
    $ changeAzula("neutral")
    a "Nevermind."
    $ cg(effect_3="mouth default")
    pc "If you don't want to take it off, then-"
    $ cg(effect_5="blank", effect_2="eyebrow mad")
    "The Fire Lord looks up and gives you a cold stare, so you don't finish your sentence."
    $ cg(effect_3="mouth talking")
    $ changeAzula("mad")
    a "I'm perfectly fine, thank you!"
    $ cg(effect_3="mouth default")
    pc "Because-"
    $ cg(effect_3="mouth talking")
    $ changeAzula("annoyed")
    a "[pc_name]!"
    $ cg(effect_2="brow pushed together",effect_3="mouth default")
    "Curiously, Azula doesn't sound angry. Instead, she simply seems frustrated, though with you or herself, you're not sure."
    $ cg(effect_3="mouth talking")
    $ changeAzula("frustrated")
    a "I said, I'm fine."
    $ cg(effect_3="mouth default")
    pc "If you say so…"
    $ cg(effect_2="eyebrow mad", effect_3="mouth talking")
    $ changeAzula("mad")
    a "I do!"
    $ cg("11", effect_3="mouth default", effect_4="pupil down")
    "As if to prove herself to you, she swiftly unbuckles her belt and throws it at your feet."
    $ cg(effect_3="mouth talking", effect_4="pupil at player")
    $ changeAzula("annoyed")
    a "There!"
    a "Satisfied?"
    $ cg(effect_3="mouth default")
    pc "Not quite yet."
    $ cg(effect_3="mouth frown", effect_2="eyebrow mad")
    $ changeAzula("stern")
    "The Fire Lord scoffs, apparently forgetting her unease from earlier."
    $ cg(effect_3="mouth talking")
    a "Of course not."
    $ cg(effect_4="pupil down", effect_2="eyebrow default")
    $ changeAzula("neutral")
    a "Next thing to go is my dress…"
    $ cg("12", effect_3="mouth default")
    "With equal haste, the Fire Lord begins pulling down her dress, but stops abruptly before she's even halfway done."
    $ cg(effect_2="eyebrow down", effect_3="mouth talking")
    $ changeAzula("sad")
    a "This dress...was a gift from my father…"
    $ cg(effect_4="pupil at player")
    a "...and now I'm taking it off for some soldier boy."
    $ cg(effect_3="mouth default")
    pc "Technically, isn't everything you have a gift from your father?"
    $ cg(effect_2="eyebrow mad", effect_3="mouth frown", effect_4="pupil left")
    "Snorting derisively at your oversimplification, Azula momentarily glances away."
    $ cg(effect_3="mouth talking", effect_4="pupil at player")
    $ changeAzula("stern")
    a "This was a special gift."
    a "And don't be so insolent, [pc_name]!"
    $ cg(effect_3="mouth default")
    pc "Why? What are you gonna do, burn me?"
    $ cg(effect_5="eyeline closing", effect_3="mouth talking")
    $ changeAzula("mad")
    a "Don't think I'm not considering it."
    $ cg(effect_4="pupil down")
    a "But no, it just doesn't become you."
    $ cg("13", effect_3="mouth default", effect_2="eyebrow default", effect_5="blank")
    "As you continue your conversation, Azula finishes pulling down her dress, leaving it at her feet once it's off."
    pc "Because I was about to say, this relationship won't work if you're always-"
    $ cg(effect_2="eyebrow mad", effect_3="mouth talking", effect_4="pupil at player")
    $ changeAzula("stern")
    a "This relationship will work exactly as I wish it to!"
    a "Is that clear?"
    $ cg(effect_3="mouth default")
    pc "Yes, my Lord…"
    $ cg(effect_5="eyeline closed", effect_3="mouth talking")
    $ cg(effect_3="mouth default")
    "For a second, it looks as if she's going to yell at you for referring to her so formally. Instead, she takes a deep breath simply shakes her head."
    $ cg(effect_5="blank", effect_2="eyebrow default", effect_3="mouth talking")
    $ changeAzula("neutral")
    a "Oh, don't pout, you silly man."
    a "I'm not going to burn you."
    a "You're currently more useful to me alive than dead."
    $ cg(effect_3="mouth default")
    "Sometimes, you struggle not to roll your eyes at how seriously this girl takes everything."
    pc "That's comforting…"
    $ cg(effect_3="mouth talking", effect_5="eyeline closing")
    $ changeAzula("mad")
    a "You're not here to be comforted."
    a "You're here to service my needs."
    $ cg(effect_3="mouth default")
    pc "Look, you told me to treat you as if I was courting you. I thought you wanted to get used to being in an actual relationship."
    $ cg(effect_3="mouth talking", effect_5="blank")
    $ changeAzula("neutral")
    a "That's correct."
    $ cg(effect_3="mouth default")
    pc "I can't do that if you're always threatening me, and then you'll never be ready for the day someone starts pursuing you for real."
    $ cg(effect_4="pupil left")
    $ changeAzula("bemused")
    a "Hmm…"
    "Azula pauses for a moment to contemplate your words, stroking her chin as she does so."
    $ cg(effect_3="mouth talking")
    $ changeAzula("neutral")
    a "...point taken."
    $ cg(effect_4="pupil at player", effect_5="eyeline closed")
    a "Fine, then."
    $ cg(effect_5="eyeline closing")
    $ changeAzula("not_amused")
    a "I will no longer directly threaten you, happy?"
    $ cg(effect_3="mouth default")
    pc "As happy as I can be with such a weak reassurance."
    $ cg(effect_3="mouth talking", effect_5="blank")
    $ changeAzula("bemused")
    a "Well, it's the best you're going to get."
    $ cg(effect_4="pupil left")
    a "I do have a reputation to uphold, after all."
    $ cg(effect_3="mouth default", effect_4="pupil down")
    "You can only wonder what would happen to Azula's reputation if her subjects could see her now, clad in only pantyhose and a shirt, alone with someone like you, ready for anything..."
    $ cg("14")
    "A loud sort of ripping noise interrupts your train of thought. You blink in surprise as the Fire Lord removes the sleeves from her shirt, casting the bands to the side as they come off."
    pc "You didn't have to go that far, Azula." #velcro orclev
    $ cg(effect_3="mouth talking", effect_2="pupil at player", effect_4="brow pushed together",effect_5="eyeline closing")
    $ changeAzula("not_amused_p1")
    a "What?"
    $ cg(effect_3="mouth default", effect_5="blank", effect_2="eyebrow default", effect_4="pupil left")
    "You point to the discarded pieces of clothing, eyebrow raised. She glances at them briefly before nodding her head knowingly."
    $ cg(effect_5="eyeline closing", effect_3="mouth talking")
    $ changeAzula("not_amused_p3")
    a "Oh, that."
    a "Yes, I suppose you don't have any experience with fine clothing."
    a "They're intended to come off and go on like that."
    $ cg(effect_5="eyeline closed")
    $ changeAzula("bemused")
    a "I wouldn't expect you to understand the intricacies of modern cotton weaving."
    a "It's really a shame they don't last very long, though."
    $ cg(effect_3="mouth default")
    pc "So long as you're not just ripping off your clothes like a madwoman."
    $ cg(effect_4="pupil at player", effect_5="blank", effect_2="eyebrow mad")
    "Azula stops moving and goes silent. You could hear a pin drop."
    $ cg(effect_3="mouth talking")
    $ changeAzula("mad")
    a "Are you calling me crazy?"
    $ cg(effect_3="mouth mad")
    menu:
        "Yes":
            pc "Well…"
            $ cg(effect_3="mouth talking", effect_4="pupil at playerbigger")
            $ changeAzula("surprised")            
            a "I knew it!"
            $ changeAzula("mad")
            a "You think I'm insane, don't you?"
            $ cg(effect_3="mouth mad 2")
            pc "I-"
            $ cg(effect_3="mouth talking")
            a "Stark raving mad Azula, that's what you think of me!"
            pc "I wouldn't go that far."
            $ cg(effect_3="mouth mad 2",effect_5="firerightarm")
            a "You won't be going anywhere, not anymore!"
            $ cg("Base_2-Firescene","23", "eyebrow mad", "mouth mad 2", "pupil at playerbigger", "firerightarm","FireAtPlayer", "FireForeground")
            "Blue balls of flame appear in Azula's hands. Before you can even utter another word, she blasts you in the face. You fall to the ground, convulsing and sputtering in pain." #black screen and only chatbox
            $ black("show")
            $ changeAzula("happy_mad")
            a "Yes!"
            a "Burn, [pc_name]!"
            "Not satisfied with just setting your head on fire, Azula conjures up more fire and throws it at your shaking body. You lose consciousness almost immediately. The last thing you hear is the Fire Lord's laughter."
            "GAME OVER" #no period is intentional
            return 
        "No":
            pc "Of course not, Azula."
            $ cg(effect_3="mouth talking", effect_2="eyebrow default")
            $ changeAzula("neutral")
            a "Good."
            a "Because I'm not crazy, [pc_name]."
            $ cg(effect_3="mouth default")
            pc "Of course you aren't."
            $ cg(effect_2="eyebrow mad", effect_3="mouth talking")
            $ changeAzula("mad")
            a "I'm {size=+10}not!{/size}" #emphasis on 'not'
            $ cg(effect_3="mouth default")
            pc "That's what I said."
            $ cg("23", effect_3="mouth talking", effect_5="eyeline closing")
            $ changeAzula("bemused")
            a "And you wouldn't happen to be lying, would you?"
            $ cg(effect_3="mouth default")
            pc "Of course not, Azula."
            $ cg("14", effect_3="mouth talking", effect_5="blank", effect_2="eyebrow default")
            $ changeAzula("neutral")
            a "Good."
            a "Because I'm not crazy, [pc_name]…"
            $ cg("23", effect_3="mouth mad", effect_2="eyebrow mad")
            $ changeAzula("mad")
            a "No matter what the voices in my head tell me!"
            $ cg("14", effect_3="mouth default", effect_4="pupil left")
            $ cg(effect_4="pupil up")
            "Your concern must be more obvious than you thought, as Azula rolls her eyes at your expression."
            $ cg(effect_4="pupil at player", effect_5="eyeline closing", effect_3="mouth talking", effect_2="eyebrow little up little down")
            $ changeAzula("bemused")
            a "[pc_name], it's a joke."
            $ cg(effect_3="mouth default")
            pc "Oh...of course."
            "You laugh nervously, wishing you didn't sound so shaken up. No matter what, that's a topic you'll be staying clear of in the future."
    $ cg(effect_4="pupil left", effect_3="mouth talking")        
    $ changeAzula("neutral")
    a "Anyway…"
    $ cg(effect_4="pupil at player", effect_5="blank")
    a "Are you ready for this?"
    $ cg(effect_3="mouth default")
    pc "You know I am."
    $ cg(effect_3="mouth smile closed")
    $ cg("15", effect_3="mouth default", effect_4="pupil down")
    "Azula gives you a quick smile and begins to lift her shirt above her head, but then pauses mid-motion."
    $ changeAzula("sad")
    a "…………."
    $ cg(effect_3="mouth talking")
    a "This shirt was-"
    $ cg(effect_4="pupil at player", effect_3="mouth frown", effect_2="eyebrow mad")
    pc "Okay, look, I don't mean to be disrespectful, but I don't need a personal history lesson for each piece of clothing you have on."
    $ cg("14", effect_3="mouth talking")
    $ changeAzula("stern")
    a "Is that so?"
    $ cg(effect_3="mouth default")
    pc "We're just getting to the good part, so now's not really a great time for talking."
    $ cg(effect_2="eyebrow surprised", effect_3="mouth talking")
    $ changeAzula("surprised")
    a "You...really want to see the rest of me that badly?"
    $ cg(effect_3="mouth default")
    pc "Well, yeah. Of course. Who wouldn't?"
    $ cg(effect_3="mouth talking")
    $ changeAzula("neutral")
    a "Most men I meet aren't so straightforward."
    $ cg(effect_3="mouth default")
    pc "Neither was I, when we first met. It's because of your position."
    $ cg(effect_3="mouth talking",effect_5="eyeline closing", effect_2="eyebrow default")
    $ changeAzula("not_amused_p1")
    a "You don't need to state the obvious, [pc_name]."
    $ cg(effect_3="mouth default")
    pc "Are you going to take that shirt off, or what?"
    $ cg(effect_3="mouth talking")
    $ changeAzula("bemused")
    a "Is rudeness a quality of a romantic relationship?"
    $ cg("15", effect_3="mouth default", effect_4="pupil down", effect_5="blank")
    "As you respond, Azula resumes lifting her shirt."
    pc "I would say it's more familiari-"
    $ cg("16")
    "You stop short as the Fire Lord finishes, again leaving her clothing at her feet."
    $ cg(effect_3="mouth talking", effect_4="pupil at player")
    $ changeAzula("neutral")
    a "What were you saying?"
    $ cg(effect_3="mouth default")
    pc "Uh...I forget. Nevermind."
    $ cg(effect_3="mouth smile open", effect_2="eyebrow surprised")
    $ changeAzula("content")
    a "So, what do you think?"
    $ cg(effect_3="mouth smile closed")
    pc "Black with lace trim...nice. Very classy."
    $ cg(effect_2="eyebrow down", effect_5="eyeline closing", effect_3="mouth talking")
    $ changeAzula("not_amused_p1")
    a "What did you expect?"
    a "Something more plain?"
    a "For a person of {size=+10}my{/size} stature?" #emphasis on 'my'
    $ cg(effect_3="mouth default")
    pc "No, it's just-"
    $ changeAzula("mad")
    $ cg(effect_3="mouth talking", effect_2="eyebrow mad")
    a "Just what?"
    $ cg(effect_3="mouth default")
    pc "It's a compliment, that's all."
    $ cg(effect_2="eyebrow surprised", effect_3="mouth talking", effect_4="pupil left", effect_5="blush")
    $ changeAzula("surprised_2")
    a "Oh...I see."
    $ cg(effect_5="blank", effect_2="eyebrow little up little down", effect_4="pupil at player")
    a "You're rather carefree for a soldier, aren't you?"
    $ cg(effect_3="mouth default")
    pc "Not particularly, no."
    $ cg(effect_4="pupil left", effect_5="eyeline closing", effect_2="eyebrow default")
    $ changeAzula("bemused")
    a "Hmm…"    
    $ cg(effect_3="mouth talking")
    a "{size=-7}...must be something else, then.{/size}" #de-emphasis on all
    $cg(effect_3="mouth default")
    pc "What's that?"
    $ cg(effect_3="mouth talking", effect_4="pupil at player", effect_5="blank")
    $ changeAzula("neutral")
    a "I said, time for the rest of it."
    $ cg("base_1","17", "mouthp3", "EyeDownP3", "browneutral p3")
    "Azula quickly guides her pantyhose down her legs, stopping only to adjust her balance when she removes it from each leg."
    $ cg("18", "eyebrow default", "mouth default", "pupil at player", effect_5="blank")
    pc "That was fast."
    $ cg(effect_3="mouth talking")
    $ changeAzula("disappointed")
    a "It's not very difficult to take off."
    $ cg(effect_5="eyeline closing")
    $ changeAzula("bemused")
    a "Would you prefer I put on a little show while I balance my weight one foot at a time?"
    pc "No, it's just-"
    $ cg(effect_4="pupil left")
    $ changeAzula("bemused")
    a "Just this, just that…"
    $ cg(effect_2="eyebrow mad", effect_4="pupil at player", effect_5="blank")
    $ changeAzula("mad")
    a "Would you {size=+10}just{/size} say what you mean!?" #emphasis on 'just'
    $ cg(effect_3="mouth default")
    pc "I like watching you undress."
    $ cg(effect_2="brow pushed together", effect_3="mouth talking")
    $ changeAzula("sad")
    a "You...do?"
    $ cg(effect_2="eyebrow little up little down")
    $ changeAzula("bemused")
    a "You mean, you're not solely interested in seeing my body?"
    $ cg(effect_3="mouth default")
    pc "Right."
    $ cg(effect_2="eyebrow surprised", effect_3="mouth smile open")
    $ changeAzula("content")
    a "So, you {size=+10}do{/size} want a show!" #emphasis on 'do'
    $ cg(effect_3="mouth smile closed")
    pc "It's more complicated than that. You'd be sexier if you took off your clothes with a little more flair."
    $ cg(effect_3="mouth talking", effect_2="eyebrow default", effect_4="pupil left")
    $ changeAzula("bemused")
    a "Mmm, I see."
    $ cg(effect_3="Mouth LipBite", effect_5="eyeline closing")
    a "It's all about the...experience." #lip bite
    pc "You got it."
    $ cg(effect_3="mouth talking", effect_4="pupil at player", effect_5="blank")
    $ changeAzula("neutral")
    a "And when will you be doing this for me?"
    $ cg(effect_3="mouth default")
    pc "We can talk about that later."
    $ cg(effect_3="mouth talking", effect_5="eyeline closing")
    $ changeAzula("not_amused_p1")
    a "Yes, we will."
    $ cg(effect_3="mouth smile open", effect_4="pupil left")
    $ changeAzula("not_amused")
    a "Slow and sexy, hmm?"
    $ cg(effect_5="eyeline closed", effect_3="mouth smile closed")
    a "…………."
    $ cg(effect_3="mouth talking", effect_4="pupil at player", effect_5="blank")
    $ changeAzula("neutral")
    a "Well, maybe another time, after I've thought about it a little more."
    a "Today, I'm just interested in showing you me."
    $ cg(effect_3="mouth default")
    pc "Who's stopping you?"
    $ cg(effect_3="mouth smile open", effect_2="eyebrow surprised")
    $ changeAzula("happy")
    a "Ha!"
    $ cg(effect_2="eyebrow mad")
    $ changeAzula("happy_mad")
    a "Nobody has {size=+10}ever{/size} stopped me from doing {size=+10}anything!{/size}" #emphasis on 'ever' and 'anything'
    $ cg(effect_5="eyeline closing")
    a "Or from {size=+5}taking{/size} whatever I want…" #emphasis on 'taking'
    $ cg(effect_3="mouth smile closed")
    pc "Including me?"
    $ cg(effect_3="mouth smile open")
    $ changeAzula("content")
    a "Yes, including you."
    $ cg("19", effect_2="eyebrow default", effect_3="mouth default", effect_4="pupil down", effect_5="blank")
    "Azula's hands make their way down to the center of her bra, and she slowly begins to undo the straps that keep it around her breasts. You're unsure if her lack of speed is because she's trying out the 'slow and sexy' style of undressing that she referred to earlier or if it has more to do with the reality of what she's doing."
    pc "You could bounce up and down a little while you do that to make it sexier."
    $ cg(effect_2="eyebrow mad", effect_3="mouth talking", effect_4="pupil at player")
    $ changeAzula("mad")
    a "I told you, I'm not-!"
    $ cg(effect_3="mouth default", effect_5="eyeline closing")
    $ changeAzula("neutral")
    a "…………."
    $ cg(effect_2="eyebrow default", effect_3="mouth talking", effect_4="pupil down")
    a "Yes, I'll keep that in mind next time."
    $ cg("20", effect_4="pupil at player", effect_5="blank", effect_3="mouth default")
    "Finished with unfastening her bra, the Fire Lord wastes no time in pulling it off over her shoulders and letting it fall to the floor behind her. She then looks at you expectantly, as if she's awaiting your judgment, instead of waiting for an excuse to admonish you for being too familiar."
    $ cg(effect_3="mouth talking")
    $ changeAzula("stern")
    a "You're the first one to ever see my naked breasts, [pc_name]."
    $ cg(effect_3="mouth default")
    pc "Why does that not surprise me?"
    $ cg(effect_3="mouth talking", effect_5="eyeline closed")
    $ changeAzula("not_amused")
    a "Consider yourself honored, and leave it at that."
    $ cg(effect_3="mouth default", effect_5="blank")
    "Almost a minute of silence passes as you study her breasts. They're supple and definitely large enough to be satisfying, but not so big that you'd really sexualize her when she's fully clothed. It's befitting of a princess."
    $ cg(effect_3="mouth talking")
    $ changeAzula("bemused")
    a "Well?"
    $ cg(effect_3="mouth default")
    pc "They're great."
    $ cg(effect_3="mouth talking")
    $ changeAzula("not_amused")
    a "Is that…"
    $ cg(effect_5="eyeline closing")
    $ changeAzula("not_amused_p1")
    a "...is that all you have to say?"
    $ cg(effect_3="mouth default")
    pc "I'm no poet."
    $ cg(effect_3="mouth talking", effect_4="pupil left")
    $ changeAzula("stern")
    a "Clearly."
    $ cg(effect_3="mouth default")
    "If you didn't know any better, you'd say that Azula is a little hurt by your lack of commentary."
    pc "May I feel them?"
    $ cg(effect_3="mouth talking", effect_2="eyebrow surprised", effect_4="pupil at playerbigger", effect_5="blank")
    $ changeAzula("bemused")
    a "May you...what?"
    $ cg(effect_3="mouth default")
    pc "Feel your breasts."
    $ cg(effect_3="mouth talking")
    $ changeAzula("surprised")
    a "What!?"
    $ cg(effect_2="eyebrow mad")
    $ changeAzula("mad")
    a "I have just given you the great honor of seeing them, and already you aren't satisfied?"
    $ cg(effect_3="mouth default")
    pc "That's not what I meant, [azula_name]."
    $ cg(effect_3="mouth talking")
    a "I've half a mind to send you packing!"
    $ cg(effect_4="pupil left", effect_5="eyeline closing")
    $ changeAzula("not_amused_p3")
    a "Still...I appreciate your low-class attempt at conveying your romantic sentiments."
    a "{size=-5}...as much as one could appreciate it, anyway.{/size}" #de-emphasis on all
    $ cg(effect_3="mouth default")
    pc "Thanks?"
    $ cg(effect_3="mouth talking")
    $ changeAzula("neutral")
    a "You're welcome."
    $ cg(effect_3="mouth default")
    "It’s almost unbelievable that you've actually gotten this far. Even combat was less stressful than this. At least then, you had a weapon. Now, you're dealing with a crazy, sex-starved, royal firebending bitch, and you know very well how women can be."
    pc "Um…"
    $ cg(effect_3="mouth talking", effect_4="pupil at player", effect_5="blank", effect_2="eyebrow default")
    $ changeAzula("bemused")
    a "What is it?"
    $ cg(effect_3="mouth default")
    pc "And then there was one."
    $ cg(effect_3="mouth talking", effect_5="eyeline closing", effect_2="brow pushed together")
    $ changeAzula("frustrated")
    a "What?"
    $ cg(effect_3="mouth default", effect_4="pupil down", effect_2="eyebrow default")
    "Instead of responding, you simply point to her still-clothed crotch. Azula follows your gaze downwards; when she realizes what you're pointing at, her hands jerk towards the area as if to cover it, but she forces them back to where they were."
    $ cg(effect_3="mouth talking", effect_2="brow pushed together")
    $ changeAzula("not_amused")
    a "You're a rather lewd person under it all, aren't you?"
    $ cg(effect_3="mouth default")
    pc "Men tend to be."
    $ cg(effect_3="mouth talking", effect_5="eyeline closed")
    $ changeAzula("stern")
    a "How ridiculous."
    $ cg(effect_3="mouth default")
    "The Fire Lord takes a moment to crack her neck, like she's preparing herself to fight. You'd best be careful."
    $ cg(effect_2="eyebrow default", effect_3="mouth talking", effect_4="pupil at player", effect_5="blank")
    $ changeAzula("neutral")
    a "Very well."
    a "I suppose it can't be helped."
    $ cg("base_1", "21", "BrowNeutral P3","mouthp3","EyeDownP3")
    $ cg(effect_5="EyeatPlayerP3", effect_3="BrowMad p3")
    "Azula unceremoniously hooks her thumbs under her panties and pulls down. She's halfway done when you cough loudly, causing her to look up at you."
    $ cg(effect_4="MouthP3 Talking")
    $ changeAzula("mad")
    a "What is it {size=+10}now?{/size}" #emphasis on 'now'
    $ cg(effect_4="mouthp3")
    pc "You could try the 'slow and sexy' thing with this last bit."
    $ cg("20", "eyebrow mad", "mouth default", "pupil at player", "blank")
    "She shakes her head, but pulls her panties back up."
    $ cg(effect_3="mouth talking")
    $ changeAzula("bemused")
    a "Could I now?"
    $ cg(effect_3="mouth default")
    pc "It would be a good start."
    $ cg(effect_3="mouth talking",)
    $ changeAzula("frustrated")
    a "Are you saying that everything until now has been bad?"
    $ cg(effect_3="mouth default")
    pc "I wouldn't go that far."
    $ cg(effect_3="mouth talking",effect_4="pupil at playerbigger")
    $ changeAzula("mad")
    a "Then what {size=+10}are{/size} you saying?" #emphasis on 'are'
    $ cg(effect_3="mouth default")
    pc "Just that it could be better, that's all."
    $ cg(effect_3="mouth talking", effect_4="pupil at player", effect_5="eyeline closing")
    $ changeAzula("bemused")
    a "Slow and sexy, hmm?"
    $ cg(effect_3="mouth default")
    pc "Exactly."
    $ cg(effect_5="eyeline closed")
    $ changeAzula("neutral")
    a "Hmm…"
    $ cg(effect_3="mouth talking", effect_4="pupil left", effect_5="blank")
    $ changeAzula("frustrated")
    a "Nothing ventured, nothing gained, I suppose."
    $ cg("base_1", "21", "BrowNeutral P3","mouthp3","EyeDownP3")
    "Azula takes a deep breath, then begins again, only more slowly, sliding her panties downwards one side at a time. As she shimmies her underwear down her legs, she wiggles her hips slightly. While you're not sure if it's intentional, it's certainly sexy."
    "Her breasts sway back and forth as she continues, their movements becoming more and more free the lower to the ground Azula brings them in the course of her undressing. It's mesmerizing not because you've never seen it before, but because of who they belong to."
    $ cg("22", "eyebrow default", "mouth default", "pupil at player", "blank")
    "Finally, Azula finishes, lightly stepping out of her panties and casting them to the side with one of her now-free feet. Letting out another deep breath, the Fire Lord now looks at you impatiently. The 'show' being over, apparently the whole experience has left her a little wanting."
    $ cg(effect_3="mouth talking", effect_4="pupil left")
    $ changeAzula("neutral")
    a "Now...what do you think of my body?"
    $ cg(effect_3="mouth default")
    menu:
        "Cute":
            pc "You're very cute."
            $ cg(effect_3="mouth talking", effect_2="eyebrow mad",effect_4="pupil at player")
            $ changeAzula("frustrated")
            a "Is {size=+10}that{/size} what you think?" #emphasis on 'that'
            $ cg(effect_3="mouth default")
            pc "Uh…"
            $ cg(effect_3="mouth talking")
            $ changeAzula("not_amused")
            a "A baby turtleduck is cute."
            a "Fire Nation children are cute."
            a "I'm not cute."
            $ changeAzula("mad")
            a "I'm {size=+10}beautiful!{/size}" #emphasis on 'beautiful!'
            $ cg(effect_3="mouth mad")
            pc "I never meant to-"
            $ cg(effect_3="mouth talking")
            $ changeAzula("stern")
            a "{size=+10}Get out!{/size}" #emphasis on all
            $ cg(effect_3="mouth mad 2")
            pc "But I'm not done looking."
            $ cg(effect_3="mouth talking", effect_4="pupil at playerbigger")
            $ changeAzula("mad")
            a "{size=+12}Out!{/size}" #emphasis
            $ cg(effect_3="mouth mad 2",effect_5="firerightarm")
            "Fireballs spring to life in her hands, though she doesn't adopt a combat stance."
            $ cg(effect_3="mouth talking")
            $ changeAzula("mad")
            a "{size=+15}Now!{/size}" #emphasis
            $ black("show")
            "You can still hear her still yelling at you until you pass out of earshot."
            pc "Touchy, touchy…"
            jump sauna
        "Gorgeous":
            pc "You're absolutely gorgeous."
            $ changeAzula("happy")
            $ cg(effect_3="mouth smile open", effect_2="eyebrow surprised", effect_4="pupil at player")
            a "You really think so?"
            $ cg(effect_3="mouth smile closed")
            pc "Naturally. There's no other word for it."
            $ changeAzula("content")
            $ cg(effect_3="mouth smile open", effect_5="eyeline closed", effect_6="blush")
            a "That's very flattering."
            $ cg(effect_5="blank", effect_6="blank", effect_2="eyebrow down")
            $ changeAzula("happy")
            a "Thank you, [pc_name]."
            a "Not that I didn't already know, but it's nice to hear someone else say it."
            $ cg(effect_3="mouth smile closed")
            pc "Can you give me a little twirl?"
            $ cg(effect_5="eyeline closing")
            "Azula looks at you curiously before shaking her head."
            $ cg(effect_5="blank", effect_3="mouth smile open")
            $ changeAzula("content")
            a "That's not necessary today."
            a "I've already gotten what I wanted."
            $ changeAzula("frustrated")
            a "You can go now, [pc_name]."
            $ cg(effect_2="eyebrow default", effect_3="mouth talking")
            $ changeAzula("neutral")
            a "But I expect you back here next week for more."
            $ cg(effect_3="mouth default")
            pc "As you wish, Azula."
            jump sauna