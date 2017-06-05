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
$ cg(effect_2="eyebrow surprised")
"The Fire Lord briefly tilts her head back and laughs." #Laugh maybe here?
$ changeAzula("excited")
$ cg(effect_3="mouth talking", effect_2="eyebrow little up little down")
a "Normally, a guess would indeed be quite hazardous."
$ changeAzula("happy")
a "But I'm not interested in hurting you, so don't worry."
$ cg(effect_3="mouth default")
pc "That's very-"
$ changeAzula("bemused")
$ cg(effect_3="mouth talking", effect_5="eyeline closing")
a "For now."
$ cg(effect_3="mouth default")
pc "Is that a joke?"
$ changeAzula("happy")
$ cg(effect_3="mouth talking")
a "Does it sound like I'm joking?"
$ cg(effect_3="mouth default", effect_5="blank")
"You take a moment to study her face. She's smiling, but you can't tell if that's a good sign or a bad omen. There's a certain sickly aspect to it, at least at first glance."  #need Smile better here
pc "I would say 'yes'."
$ changeAzula("content")
$ cg(effect_3="mouth talking", effect_2="brow pushed together") #Smile talking?
a "Nothing to worry about, then."
$ changeAzula("happy")
a "Now, be a good boy and take a guess."
$ cg(effect_3="mouth default")
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
$ cg(effect_3="mouth default")
"Azula bites her lip for a second before continuing." #Lipbite
$ changeAzula("content")
$ cg(effect_3="mouth talking", effect_4="Pupil left")
a "I think that, since you've shown me most of your body, it's only fair that I show you most of {size=+5}my{/size} body." #emphasis on 'my'
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
$ cg(effect_3="mouth default")
"For a moment, you think fire is going to come shooting out of her hands, but you stand your ground, coolly returning her angry look with an impassive face." # m a d
pc "That's not what a courter is. Don't you want to learn how to behave properly in a relationship?"
$ cg(effect_4="Pupil left")
a "Hmm…"
$ cg(effect_2="eyebrow default", effect_5="blank")
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
$ cg(effect_3="mouth default", effect_2="eyebrow mad", effect_4="Pupil at player")
"The Fire Lord immediately looks at you, anger flashing across her face. One of these days, one of your jokes just might get you killed."
$ cg(effect_3="mouth talking")
$ changeAzula("mad")
a "Of course I  ca-!"
$ cg(effect_2="eyebrow surprised")
$ changeAzula("content")
a "Oh, I see."
$ cg(effect_3="mouth default", effect_2="brow pushed together")
"Panic and regret turn to relief as Azula cracks a small smile." #S M I L E
$ cg(effect_3="mouth talking")
$ changeAzula("happy")
a "Humorous, [pc_name]."
$ cg(effect_3="mouth default")
pc "I try."
$ changeAzula("content")
$ cg(effect_3="mouth talking")
a "Your efforts do not go entirely unappreciated."
$ changeAzula("frustrated")
$ cg(effect_2="eyebrow default")
a "However, you might want to refrain from making light of my status too often, lest you send the wrong message."
$ cg(effect_3="mouth default")
"You suppose that's as close to an apology as you're going to get for giving you a minor heart attack. Still, it's progress."
pc "Right…"
$ cg("3", effect_4="Pupil left")
"An uncomfortable silence fills the air as Azula unhooks her pauldrons from her breastplate, tossing them on the floor next to the crest of her armor. Once she's finished, she looks at you questioningly."
$ cg(effect_3="mouth talking", effect_2="eyebrow little up little down", effect_4="Pupil at player")
a "So, what do you think so far?"
$ cg(effect_3="mouth default")
pc "It's certainly well-designed."
$ cg(effect_3="mouth talking")
a "That's not what I meant."
pc "You mean...what do I think of your clothed shoulders?"
$ cg(effect_3="mouth talking", effect_4="Pupil left", effect_2="eyebrow default")
a "Nevermind."
$ cg(effect_3="mouth default")
pc "Because you don't even ha-"
$ cg(effect_3="mouth talking", effect_2="eyebrow mad", effect_4="Pupil at player")
a "I said nevermind!"
$ cg(effect_3="mouth default")
"You notice Azula's hands twitch, as if she's about to firebend. That's never a good sign."
pc "I meant no offense, Azula."
$ cg("4")
"Thankfully, instead of making any violent moves, the Fire Princess tucks her hands under her breastplate, preparing to lift it."
$ cg(effect_3="mouth talking", effect_2="eyebrow default", effect_4="pupil down")
a "Fine, fine…"
$ cg(effect_2="eyebrow surprised")
a "Oh, and one more thing."
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
        a "I didn't say 'harm', I said 'attack'."
        a "Why would you even say 'harm'?"
        $ cg(effect_2="eyebrow little up little down", effect_5="eyeline closing")
        a "A slip of the tongue, perhaps?"
        pc "N-no, my Lord."
        $ cg(effect_3="mouth talking", effect_2="eyebrow default", effect_5="blank")
        a "I was only joking, Lee."   #[Lee_name]
        $ cg(effect_4="Pupil left")
        a "Mostly…"
        $ cg(effect_2="eyebrow mad", effect_4="pupil at player")
        a "And what have I told you about calling me 'Lord'!?"
        $ cg(effect_3="mouth default")
        pc "My apologies, Azula."
    "No":
        pc "I'm not sure what you mean. Why would I ever want to attack you?"
        $ cg(effect_3="mouth talking", effect_2="eyebrow surprised", effect_4="Pupil down")
        a "Why indeed..."
        $ cg(effect_4="Pupil left", effect_5="eyeline closing")
        a "Why should anyone want to attack a head of state who would be a valuable asset to anyone who wanted to harm her nation?"
        a "After all, the Fire Nation doesn't have any enemies."
        $ cg(effect_3="mouth default")
        pc "Is that sarcasm?"
        $ cg(effect_5="blank", effect_3="mouth talking", effect_2="eyebrow mad", effect_4="pupil at player")
        a "Of course it is, Lee!" #[Lee_name] here
        a "Do I have to spell everything out for you!?"
        a "Honestly, sometimes I question if you're even intelligent enough to warrant my attention."
        $ cg(effect_3="mouth default")
        pc "My apologies, Azula."
$cg(effect_4="pupil left")
a "Hmph!"
$ cg("5")
"Scoffing in disgust at your servile response, Azula pulls the breastplate over her head and throws it across the room. After hitting the wall, it loudly crashes against the floor. Evidently, her emotions are running high."