label sauna:
    $ black("show")
    "When you approach the door to the War Room, you notice yet a piece of paper pinned to the door."
    pc "If this girl keeps skipping briefings, I'm going to be in serious trouble at Command."
    "The only thing written on the note is a simple haiku."
    "I await your touch."
    "Steaming water everywhere."
    "Be very careful."
    pc "Be careful? What is that supposed to mean?"
    "You grab the note and stuff it in your pocket."
    pc "Nice of her to put a location on here...I guess that's the point, though. Steaming water, huh? Must be a bathroom…"
    "You spend the next hour searching the palace, room-by-room. As you proceed, you grow increasingly uneasy at Azula's warning. You're not sure what kind of 'surprise' she has in store for you, but whatever it is, it can't be safe."
    "Finally, you open a door and are met with a blast of steam. This must be it."
    $ changeAzula("surprised")
    a "[pc_name]?"
    a "Is that you?"
    pc "Of course, it's me!"
    $ changeAzula("neutral")
    a "Then come in!"
    "While you didn't encounter any traps in your search, if there was ever a time to be wary, it would be now."
    $ cg_scene = "sauna"
    $ cg("bg_steam", "blank","blank","blank","blank","blank","blank","blank")
    $ black("hide")
    pc "Alright, I'm...coming in…"
    "As soon as you very carefully step through the threshold, you hear a sharp click. You immediately roll forward, and feel a rush of air against your neck."
    "Twisting your head around, you see a large blade swinging from the ceiling, right where you had been standing. You hear Azula laughing, clapping her hands."
    $ changeAzula("happy")
    a "Excellent!"
    $ cg("underwear","HeadBase_1", "Mouth_Default", "EyeBrow_happy", "Eyes_At_player","blank", "bra_normal", "Towel")
    "Taking the time to study your surroundings, you slowly turn your head back towards the Fire Lord. However, that trap at the entrance seems to have been the only danger, other than Azula herself. You stand up."
    pc "Are you kidding me!?"
    $ cg(effect_3="mouth_talking", effect_4="eyebrow_pushed_up")
    $ changeAzula("bemused")
    a "Is there a problem?"
    $ cg(effect_3="Mouth_Default")
    pc "Why was that door fucking booby-trapped, Azula?"
    $ cg(effect_3="mouth_talking", effect_4="EyeBrow_Normalh1", effect_6="eyeline2")
    $ changeAzula("neutral")
    a "Isn't it obvious?"
    $ cg(effect_3="mouth_default")
    pc "Ain't it obvious I'm gonna-!"
    $ cg("Towel","Headbase_1","slight_smile_h1", "eyebrow_happy","eyes_at_player", "eyeline2")
    "You stop short as you realize what you're saying. The Fire Lord smirks at you."
    $ cg(effect_3="mouth_talking")
    $ changeAzula("content")
    a "What?"
    a "What will you do, [pc_name]?"
    $ cg(effect_3="mouth_default")
    "Remembering that there's nothing you can do, you simply hang your head."
    pc "My Lord, I would very much appreciate it if you didn't leave traps lying around. I don't want to be on alert every time I come to the palace."
    $ cg(effect_4="eyebrow_angerh1", effect_3="mouth_talking")
    $ changeAzula("mad")
    a "Resorting to formality to make me feel bad, is that it?"
    $ cg(effect_3="mouth_default")
    "Instead of responding, you simply lift your head and raise an eyebrow at her."
    $ cg(effect_6="eyelinefully_closed", effect_4="eyebrow_normalh1", effect_3="mouth_talking")
    $ changeAzula("neutral")
    a "Oh, very well."
    $ cg(effect_6="blank", effect_5="eyes_right")
    a "No more traps."
    a "Besides, you've already proven yourself to be quite...adept at handling a dangerous situation."
    $ cg(effect_3="mouth_default")
    pc "I could have died, Azula."
    $ cg(effect_3="mouth_talking", effect_5="eyes_at_player")
    $ changeAzula("bemused")
    a "You received a fair warning."
    $ cg(effect_3="mouth_default")
    pc "That's not the point."
    $ cg(effect_3="mouth_talking", effect_6="eyeline2", effect_4="eyebrow_angerh1")
    $ changeAzula("mad")
    a "If you weren't able to survive that trap, then I don't think you would have been worthy of me anyway."
    $ cg(effect_3="mouth_default") 
    pc "Worthy of you? I thought you just wanted me to teach you."
    $ cg(effect_3="mouth_talking", effect_5="eyes_right", effect_6="blank")
    $ changeAzula("annoyed")
    a "True…"
    a "It doesn't really matter, though."
    $ cg(effect_5="eyes_at_player", effect_4="eyebrow_normalh1")
    $ changeAzula("neutral")
    a "I promise, no more deadly traps." #sly look
    $ cg(effect_3="mouth_default")
    pc "No more traps of any kind!"
    $ cg(effect_3="mouth_talking", effect_4="eyebrow_happy")
    $ changeAzula("content")
    a "I'm not making any more promises today, [pc_name]."
    $ cg(effect_3="mouth_default")
    pc "But-"
    $ cg(effect_3="mouth_talking", effect_4="eyebrow_normalh1")
    $ cg(effect_3="mouth_default")
    "Azula clears her throat loudly, signaling she's done with the conversation. You suppose you'll have to let sleeping polar bear dogs lie...for now."
    $ cg(effect_3="mouth_talking")
    $ changeAzula("neutral")
    a "Do you recall the first line of today's haiku?"
    $ cg(effect_3="mouth_default")
    pc "Were you waiting long?"
    $ cg(effect_5="eyedown", effect_3="Smile_h1")
    "Azula smiles at your remembrance. It's like she's actually happy to see you, or at least, your body."
    $ cg(effect_5="eyes_at_player", effect_3="mouth_talking")
    $ changeAzula("happy")
    a "You arrived soon enough."
    $ cg(effect_4="eyebrow_happy")
    a "It {size=+10}is{/size} a rather large palace to search, after all." #emphasis on 'is'
    $ cg(effect_3="smile_h1")
    pc "Tell me about it…"
    $ cg(effect_3="mouth_talking", effect_4="eyebrow_angerh1")
    $ changeAzula("mad")
    a "Are you complaining {size=+10}again?{/size}" #emphasis on 'again'
    $ cg(effect_3="mouth_default")
    "She's obviously referring to your hostility regarding the trap. You grit your teeth in anger, but there's nothing you can do."
    pc "I-"
    $ cg(effect_3="mouth_talking", effect_4="eyebrow_normalh1")
    $ changeAzula("neutral")
    a "Actually, I don't care."
    $ cg(effect_5="eyes_right")
    a "I've brought you here today to, ah, {size=-5}touch my breasts.{/size}" #slight de-emphasis on 'touch my breasts'
    $ cg(effect_3="mouth_default")
    pc "You want me to grope you?" #emphasis on 'want'
    $ cg(effect_3="mouth_talking", effect_4="eyebrow_angerh1")
    $ changeAzula("mad")
    a "[pc_name], don't be crass."
    $ cg(effect_6="eyelinefully_closed", effect_4="eyebrow_happy")
    $ changeAzula("annoyed")
    a "Although I suppose you can't really help it…"
    $ cg(effect_6="blank")
    a "But in so many words, yes."
    $ cg(effect_3="mouth_default", effect_5="eyedown")
    "Azula briefly looks down at her breasts as she speaks."
    $ cg(effect_3="mouth_talking", effect_5="eyes_at_player", effect_4="eyebrow_normalh1")
    $ changeAzula("neutral")
    a "You are to treat them as your playthings."
    $ cg(effect_3="biting_lip")
    a "Do {size=+3}whatever{/size} you want." #lip bite, look at PC, slight emphasis on 'whatever'
    pc "Through the towel, or what?"
    $ cg("underwear",effect_8="blank", effect_3="mouth_default", effect_5="eyes_right", effect_6="blush")
    "The Fire Lord scoffs, then drops the towel to the floor, revealing her scantily-clad, sweaty body."
    $ cg(effect_3="mouth_talking")
    $ changeAzula("not_amused_3")
    a "And not through my clothes, either."
    $ cg(effect_3="mouth_default")
    pc "Sounds good to me."
    $ cg(effect_6="blank")
    "You walk up close to Azula. With only a couple of inches between you and her, it's the closest you've ever been to the Fire Lord thus far. What strikes you most is just how much taller you are than her. For the first time since you met her, you feel empowered."
    pc "Take off that bra."
    $ cg(effect_3="mouth_talking", effect_4="eyebrow_angerh1", effect_5="eyes_at_player", effect_6="eyeline2")
    $ changeAzula("annoyed")
    a "{size=+3}I've{/size} already done that for you once." #slight emphasis on 'I've'
    $ cg(effect_3="mouth_default")
    pc "Fine, then."
    $ cg(effect_5="eyedown", effect_4="eyebrow_normalh1", effect_6="blank", effect_7="HandBraPull")
    "Hooking a finger underneath the middle of her bra, you draw Azula slightly closer to you. She exhales loudly, as if she's trying to calm herself."
    pc "You don't mind, do you?"
    $ cg(effect_6="blush", effect_5="eyes_right", effect_3="mouth_talking", effect_4="eyebrow_angerh1")
    $ changeAzula("bemused")
    a "Of course not…"
    $ cg(effect_5="eyedown", effect_4="eyebrow_normalh1", effect_6="blank", effect_7="blank")
    "You don't waste any time in removing the only article of clothing between you and her royal breasts. Azula helps you by moving her arms so it's easier to pull off her bra, returning them to her back once it's gone." #(sides? I forget - tf)
    $ cg(effect_3="mouth_talking", effect_5="eyes_at_player")
    $ changeAzula("content")
    a "Thanks."
    a "It was getting a bit soaked."
    $ cg(effect_3="smile_h1")
    "Suddenly, you remember that you're in a sauna, fully clothed. It's grown mildly uncomfortable since you entered."
    pc "Excuse me for a moment."
    "You turn around to walk out, but Azula grabs your hand to stop you."
    $ cg(effect_3="mouth_talking")
    $ changeAzula("surprised_2")
    a "Wait!"
    $ changeAzula("mad")
    $ cg(effect_4="eyebrow_angerh1")
    a "Where do you think you're going!?"
    $ cg(effect_3="mouth_default")
    pc "Just to take off some of these clothes. We are in a sauna, after all."
    $ cg(effect_4="eyebrow_normalh1", effect_3="mouth_talking")
    $ changeAzula("bemused")
    a "Oh, right…"
    $ changeAzula("neutral") 
    a "Well, don't take too long!"
    $ cg(effect_3="mouth_default")
    "The Fire Lord glowers at you impatiently, but lets go of your hand. You navigate your way around the used trap still hanging in front of the door and step into the hallway, where you quickly undress down to your underwear. When you return, her expression hasn't changed a bit. You decide to try a bit of sarcasm."
    pc "Sorry for the wait."
    $ cg(effect_3="mouth_talking")
    $ changeAzula("annoyed")
    a "Unamusing, [pc_name]."
    $ cg(effect_4="eyebrow_angerh1")
    $ changeAzula("mad")
    a "{size=+10}Highly{/size} unamusing." #emphasis on 'highly'
    $ cg(effect_3="mouth_default")
    pc "Azula, I was gone for less than a minute."
    $ cg(effect_3="mouth_talking")
    $ changeAzula("annoyed")
    a "Enough talk!"
    $ cg(effect_4="eyebrow_normalh1", effect_3="mouth_default")
    "To emphasize her point, the Fire Lord shakes her upper body from side to side, slightly swinging her breasts in tandem. Your cock twitches at the sight."
    pc "Very well."
    $ cg(effect_9="boob_grab_pushup", effect_6="eyelinefully_closed")
    "Without any further hesitation, you reach out and cup Azula's breasts. They're relatively firm, but cushiony enough to rest comfortably in your hands. You'd be lying if you said holding the Fire Lord like this didn't make you nervous."
    $ cg(effect_6="blank")
    "Remaining silent, you lightly juggle her chest, to better gauge the quality. They're not the best boobs you've come across, but they're definitely up there."
    $ cg(effect_2="Headbase_H2",effect_3="mouth_openh2", effect_4="EyeBrowLittle_Up_little_Down", effect_5="Eye_at_player_h2", effect_6="Eyeline2_h2")
    $ changeAzula("neutral")
    a "So, first impressions?"
    $ cg(effect_3="mouth_default_h2")
    menu:
        "Perfect":
            pc "They're perfect, just as I'd expect from royalty."
            $ cg("underwear","HeadBase_1", "Mouth_talking", "EyeBrow_happy", "Eyes_At_player", "blank")
            $ changeAzula("bemused")
            a "After just a cursory inspection?"
            $ cg(effect_4="eyebrow_angerh1")
            $ changeAzula("mad")
            a "I don't appreciate being lied to, [pc_name]."
            $ cg(effect_3="mouth_default")
            pc "Of course not. I was just being polite."
            $ cg(effect_3="mouth_talking")
            $ changeAzula("angry")
            a "What would you say if you weren't so polite?"
            $ cg(effect_3="mouth_default")
            pc "I'm not sure. I have to {size=+10}feel{/size} out the situation." #slight emphasis on 'feel'
            $ cg(effect_3="mouth_talking", effect_6="eyeline2")
            $ changeAzula("annoyed")
            a "Cute."
            $ cg(effect_3="mouth_default")
            "From her tone, you can tell she's being sarcastic. Some people just can't appreciate a well-timed pun."
        "Good":
            pc "They're very good. I don't see any problems."
            $ cg("underwear", "HeadBase_1", "Mouth_talking", "EyeBrow_Normalh1", "Eyes_At_player", "blank")
            $ changeAzula("bemused")
            a "Just 'good', hmm?"
            $ cg(effect_6="eyeline2")
            $ changeAzula("neutral")
            a "I'm sure you'll come to a more appropriate conclusion after closer study."
            $ cg(effect_3="mouth_default")
            pc "Do you want the truth, or do you want me to kiss your ass?"
            $ cg(effect_3="mouth_talking", effect_4="eyebrow_happy")
            $ changeAzula("content")
            a "Is it really too much to ask for both?"
            $ cg(effect_4="eyebrow_normalh1")
            a "So long as you present the truth in a sycophantic manner, I'll be satisfied."
            $ cg(effect_3="Slight_Smile_H1")
            pc "(What does 'sycophantic' mean?)"
            pc "Sure, whatever you say, Azula."
            "While you'd expect the Fire Lord to show some sign of discomfort or pleasure, she appears unaffected. You make up your mind to change that. If she wants to be groped, you'll give her a first session worth remembering."   
    $ cg(effect_5="eyedown", effect_9="boob_grab_push_together")
    $ cg(effect_9="boob_grab_pushup")
    $ cg(effect_2="Headbase_H2",effect_3="mouth_openh2", effect_4="EyeBrowLittle_Up_little_Down", effect_5="Eye_at_player_h2", effect_6="EyeLinefully_closed_h2", effect_9="boob_grab_push_together")
    "With that idea in mind, you slowly begin to press together her breasts, applying pressure with your fingers while nestling your thumbs up against her nipples. Azula doesn't react immediately, but as you repeat the process, you notice that she lets out a long breath of slight satisfaction." #head2
    $ cg(effect_3="mouth_default_h2")
    pc "Feeling something already, are we?"
    $ cg("underwear","HeadBase_1", "Mouth_talking", "EyeBrow_normalh1", "Eyes_At_player", "blank")
    $ changeAzula("neutral")
    a "It's only natural, I suppose."
    $ cg("underwear","HeadBase_1", "Mouth_talking", "EyeBrow_normalh1", "Eyes_At_player", "eyeline2")
    $ changeAzula("bemused")
    a "I don't expect it has anything to do with your 'skills,' such as they are."
    $ cg(effect_3="mouth_default")
    pc "We just got started."
    $ cg(effect_3="mouth_talking", effect_4="eyebrow_angerh1")
    $ changeAzula("disappointed")
    a "And already you're disappointing me."
    $ cg(effect_3="mouth_default")
    "You decide not to take the bait. This is uncharted territory, and while you're not sure what game Azula is playing, you're absolutely sure it's not one you can win with words. After all, actions speak louder."
    pc "Would you like me to be rough or soft?"
    $ cg(effect_3="mouth_talking", effect_4="EyeBrow_Pushed_Up")
    $ changeAzula("bemused")
    a "How should I know?"
    $ cg(effect_3="mouth_default")
    pc "Surely you've played with your tits before."
    $ cg(effect_3="mouth_talking", effect_4="eyebrow_angerh1", effect_6="blank")
    $ changeAzula("mad")
    a "Watch your mouth!"
    a "Remember, you're speaking to your Fire Lord."
    $ cg(effect_3="mouth_default")
    "Stopping for the moment, you cock your brow and simply look at her."
    $ cg(effect_3="mouth_talking")
    $ changeAzula("annoyed")
    a "I didn't tell you to stop!"
    $ cg(effect_6="eyeline2")
    a "And don't look at me like that, you insolent little squirrel toad!"
    $ cg(effect_3="mouth_default", effect_9="boob_grab_pull")
    "You sigh, but begrudgingly continue your work, now focusing on squeezing her adequately-sized mammaries. They're supple and soft, without any of the hardness of the Fire Lord's personality."
    $ cg(effect_2="HeadbaseH3",effect_3="mouth_basic_H3", effect_4="Brow_Cocky", effect_5="Iris_Down_RightH3", effect_6="EyeLine2_H3")
    "Azula shivers underneath your grip as you slowly press your thumbs deep into her flesh and close your hands around her chest." #head3
    pc "Do you like that?"
    $ cg(effect_4="Brow_Pushed_in", effect_5="Eye_At_PlayerH3", effect_6="blank")
    "Although the pace of her breathing has increased, the Fire Lord glares at you, as if you're doing something wrong."
    $ cg("underwear","HeadBase_1", "Mouth_talking", "EyeBrow_angerh1", "Eyes_At_player", "blank")
    $ changeAzula("mad")
    a "Of course I do!"
    a "But that's not the point."
    $ cg(effect_3="mouth_default")
    pc "I'm confused. What is the point?"
    $ cg(effect_3="mouth_talking", effect_6="eyeline2")
    $ changeAzula("annoyed")
    a "I'm perfectly capable of achieving this effect on my own, so why do I need you?"
    $ cg(effect_3="mouth_default", effect_6="blank", effect_9="blank")
    "To make herself clear, Azula pushes you off her."
    pc "Why indeed."
    $ cg(effect_3="mouth_talking")
    $ changeAzula("bemused")
    a "You're supposed to be an expert!"
    $ cg(effect_3="mouth_default")
    pc "Well, I wouldn't go that far."
    $ cg(effect_3="mouth_talking", effect_6="eyeline2")
    $ changeAzula("mad")
    a "At this rate, neither would I."
    $ cg(effect_5="eyes_right",effect_4="EyeBrow_Normalh1")
    $ changeAzula("not_amused_p3")
    a "However...I suppose there is a certain charm in having another person have his hands all over my body."
    $ cg(effect_3="mouth_talking", effect_5="eyes_at_player", effect_6="blank")
    $ changeAzula("neutral")
    a "I'll allow you to start over."
    $ cg(effect_3="mouth_default")
    pc "That's very gracious of you."
    "You decide to repeat the process, only…"
    menu: 
        "Harder":
            $ cg(effect_8="boob_grab_pushup", effect_4="EyeBrow_angerh1")
            "Without warning, you reach forward and cup Azula's breasts, slightly pushing her back. She quickly regains her footing, and while she gives you a dirty look, she doesn't say anything."
            $ cg(effect_5="eyes_right")
            "Taking that as a sign to move forward, you roughly bounce her chest up and down in your hands. You relish in the sensation of her breasts continually returning to your grip, the soft flesh jiggling against your skin."
            $ cg(effect_3="mouth_talking")
            $ cg(effect_3="mouth_default", effect_4="EyeBrow_Normalh1", effect_5="eyedown")
            "Although you've taken a wholly new approach, Azula doesn't react, save for a barely noticeable uptick in her breathing. She also isn't complaining, which is a good sign."
            $ cg(effect_8="boob_grab_push_together")
            "Still, you don't want her to start. With that in mind, you switch to forcing her breasts together, squishing one against the other at an even pace. As you do so, your thumbs pass over her nipples, over and over again."
            $ cg(effect_2="Headbase_H2",effect_3="mouth_default_h2", effect_4="EyeBrowLittle_Up_little_Down", effect_5="Eye_down_h2", effect_6="EyeLinefully_closed_h2", effect_8="boob_grab_push_together")
            "As you continue, the Fire Lord tilts her head, as if she's trying to steel herself against your assault on her bust. You even catch her smiling a few times, though she's obviously trying not to. Apparently, she likes it hard." #head2
            pc "Enjoying yourself?"
            $ cg(effect_3="mouth_openh2", effect_4="EyeBrow_Normal", effect_5="Eye_at_player_h2", effect_6="Eyeline2_h2")
            $ changeAzula("bemused")
            a "It's...adequate, I suppose. Nothing to be proud of, [pc_name]."
            $ cg(effect_6="EyeLinefully_closed_h2", effect_3="mouth_default_h2", effect_8="boob_grab_pull")
            "Instead of responding, you turn to forcefully squeezing her mammaries, digging your fingers into the soft flesh as you do so. By this point, Azula's breathing has gotten heavy and ragged, though the pace has hardly quickened."
            $ cg(effect_2="HeadbaseH3",effect_3="Slight_Grin_h3", effect_4="Brow_Cocky", effect_5="Iris_Down_RightH3", effect_6="EyeLinefully_closed_h3")
            "Still, it's obvious that your rough treatment has done the job. Azula's head has turned further down, giving you a sense of her enjoyment, and she gives you a sly grin."
            $ cg(effect_3="Talking_mouth_h3", effect_5="Iris_Down_RightH3", effect_6="EyeLine2_H3")
            $ changeAzula("content")
            a "I see you...haa...figured it out."
            $ cg(effect_5="Eye_At_PlayerH3")
            $ changeAzula("happy")
            a "Good for you, boy."
            a "But do you...haa...have any other tricks up your sleeve?"
        "Softer":
            $ cg(effect_5="eyedown", effect_8="boob_grab_pushup")
            "Deciding to take a more gentle approach, you slowly reach forward and again cup Azula's breasts. You let them rest in your hands for a few moments before lightly juggling them in your hands."
            $ cg(effect_6="eyeline2", effect_5="eyes_right")
            "The Fire Lord seems unimpressed, and her breathing has returned to a normal pace. However, you're not sure if it's because you're doing something wrong or if it's just because of the interruption."
            $ cg(effect_8="boob_grab_push_together")
            "Pushing forward with your plan for a gentler response regardless, you tenderly press Azula's breasts together, squishing one against the other at a slow pace. As you do so, your thumbs brush against her nipples."
            $ cg(effect_5="eyes_at_player", effect_6="blank")
            "As you continue, the Fire Lord sighs, though you're not sure if it's one of disappointment or satisfaction. Her expression doesn't change. It seems that she plans on hiding her reaction, if she's even having one at all."
            pc "Enjoying yourself?"
            $ cg(effect_4="EyeBrow_angerh1", effect_5="eyes_right")
            $ changeAzula("mad")
            a "Hmph."
            $ cg(effect_3="mouth_talking")
            a "Hardly."
            $ cg(effect_3="mouth_default", effect_6="blank")
            "Despite her words, you have noticed that the pace of her breathing has increased again. Perhaps she's enjoying herself more than she lets on, but she's not letting on much."
            $ cg(effect_8="boob_grab_pull")
            "Instead of responding, you turn to softly squeezing her mammaries, pressing your fingers into the soft flesh as you do so. You wish that she had more of a reaction to your efforts, but-"
            $ cg(effect_3="mouth_talking", effect_4="EyeBrow_angerh1", effect_5="eyes_at_player")
            $ changeAzula("annoyed")
            a "Is that all you're capable of?"
            $ cg(effect_3="mouth_default")
            pc "What?"
            $ cg(effect_3="mouth_talking", effect_6="eyeline2")
            $ changeAzula("disappointed")
            a "If this is your idea of breast play, then I'm sorely disappointed."
            $ cg(effect_3="mouth_default")
            pc "I thought-"
            $ cg(effect_3="mouth_talking", effect_6="blank")
            $ changeAzula("annoyed")
            a "Well, you thought wrong."
            $ cg(effect_3="mouth_talking", effect_6="eyelinefully_closed")
            $ cg(effect_3="mouth_default")
            "Azula sighs, clearly exasperated. You can tell she's turned on at least a little, but apparently it's not enough for her."
            $ cg(effect_3="mouth_talking", effect_6="blank", effect_4="EyeBrow_normalh1")
            $ changeAzula("neutral")
            a "I'll give you one last chance to make this right."
            a "You're a soldier, aren't you?"
            $ cg(effect_4="EyeBrow_angerh1")
            $ changeAzula("mad")
            a "Be {size=+10}aggressive!{/size}" #emphasis on 'aggressive'
            $ cg(effect_3="mouth_default")
            pc "I thought you'd never ask." 
    $ cg(effect_2="HeadBase_1", effect_3="slight_smile_h1", effect_4="EyeBrow_Normalh1", effect_5="eyes_at_player", effect_6="eyeline2", effect_8="boob grab")
    "Ready and willing to treat the Fire Lord like a piece of meat, you roughly grab Azula's breasts, seizing a good handful of each. She squirms slightly within your tight grip, but shows no sign of discomfort."
    pc "Is this what you want?"
    $ cg(effect_6="eyelinefully_closed")
    $ cg(effect_6="eyeline2")
    "Without any hesitation, Azula nods. You wonder how far you'd have to push for her to shake her head, but that'll have to wait for another day."
    $ cg(effect_2="Headbase_H2", effect_3="mouth_default_h2", effect_4="eyebrow_normal", effect_5="Eye_at_player_h2", effect_6="EyeLinefully_closed_h2", effect_8="boob_grab_pushup")
    "As you begin to manhandle the Fire Lord's breasts, squeezing and juggling them as if judging a piece of fruit, Azula continues to react, grinding up against you. Her breathing has become ragged and heavy now, and she lets out the occasional moan, apparently forgetting her station." #head2
    $ cg(effect_6="Eyeline2_h2")
    pc "Doing alright?"
    $ cg(effect_3="mouth_openh2")
    $ changeAzula("neutral")
    a "I'm...haa...fine…"
    $ cg(effect_2="HeadbaseH3",effect_3="Talking_mouth_h3", effect_4="Brow_Pushed_in", effect_5="Eye_At_PlayerH3", effect_6="EyeLinefully_closed_h3")
    a "Just keep...haa...going…" #head3
    $ cg(effect_3="mouth_basic_H3")
    $ cg(effect_6="blank")
    "The two of you keep on in that fashion for several minutes before the pace of Azula's breathing begins to slow again. She gazes at you expectantly, but doesn't say a word."
    pc "What's with the look? I thought you liked it rough."
    $ cg(effect_2="Headbase_H2", effect_3="mouth_openh2", effect_4="eyebrow_normal", effect_5="Eye_at_player_h2")
    $ changeAzula("bemused")
    a "Keep it...haa...interesting." #head2
    $ cg(effect_3="mouth_default_h2", effect_8="boob_grab_pushup")
    pc "You sure?"
    $ cg(effect_2="HeadBase_1", effect_3="mouth_talking", effect_4="EyeBrow_angerh1", effect_5="eyes_at_player", effect_6="eyeline2", effect_8="boob grab") #Questa espressione fa schifo, devo migliorarla
    a "Haa...{size=+10}yes!{/size}" #emphasis on 'yes' #head1
    $ cg(effect_8="boob_touch")
    "Not one to disappoint your royal overlord, you carry out an all-out assault on Azula's breasts, clenching them with the whole of your hands as you draw Azula even closer to your own body. Your cock is practically bursting out of your underapants at this point, and while Azula doesn't seem to mind, she doesn't do anything with it either."
    $ cg(effect_2="Headbase_H2", effect_3="mouth_openh2", effect_4="eyebrow_normal", effect_5="Eye_at_player_h2", effect_6="EyeLine2_H2", effect_8="boob_grab_pull")
    $ changeAzula("happy")
    a "Mmm...haa...yes…" #head 2
    $ cg(effect_2="HeadbaseH3",effect_3="Talking_mouth_h3", effect_4="Brow_Cocky", effect_5="Iris_Down_RightH3", effect_6="EyeLinefully_closed_h3", effect_8="boob_grab_push_together")
    $ changeAzula("content")
    a "Just like...haa...just like that...mmm…" #head 3
    $ cg(effect_3="mouth_basic_H3")
    $ cg(effect_9="Dick_press", effect_5="Iris_Down_RightH3", effect_6="EyeLine2_H3")
    $ cg(effect_2="Headbase_H2", effect_3="mouth_default_h2", effect_4="eyebrow_anger", effect_5="Eye_at_player_h2", effect_6="blank")
    "As you continue to roughly molest Azula's breasts, you quickly reach down and pull off your underwear before picking up where you left off. Close as you are to the Fire Lord, your cock has nowhere to go, pressing up against her nubile body. Azula's head snaps up and she gives you a sudden glare, but doesn't push you away."
    $ cg(effect_3="mouth_openh2")
    $ changeAzula("mad")
    a "What do you...haa...think you're doing!?"
    $ cg(effect_3="mouth_default_h2", effect_8="boob_grab_push_together")
    pc "It was getting uncomfortable down there."
    $ cg(effect_3="mouth_openh2", effect_8="boob grab")
    $ changeAzula("disappointed")
    a "Your...mmm...{size=+10}comfort{/size} is not...haa...my concern!" #emphasis on 'comfort'
    $ cg(effect_3="mouth_default_h2", effect_8="boob_grab_pull")
    pc "Do you want me to put it away?"
    $ cg(effect_3="mouth_openh2", effect_6="EyeLine2_H2", effect_8="boob_grab_pushup")
    $ changeAzula("neutral")
    a "No, it's...mmm...fine…" #head2
    $ cg(effect_2="HeadBase_1", effect_3="mouth_talking", effect_4="EyeBrow_angerh1", effect_5="eyes_at_player", effect_6="eyeline2", effect_8="boob grab")
    $ changeAzula("stern")
    a "But keep it in your...haa...pants next time!" #head1
    $ cg(effect_3="mouth_default")
    pc "I can't help it. You're too sexy for that."
    $ cg(effect_2="HeadbaseH3",effect_3="Slight_Grin_h3", effect_4="Brow_happy", effect_5="Iris_Down_RightH3", effect_6="EyeLine2_H3", effect_7="blush_h3", effect_8="boob_grab_pull")
    "Remaining silent, Azula looks away, but you can tell that she's flattered. You meant what you said, though it doesn't hurt that it also reinforces your position with her." #head3, happy brow, eyeline2, irisdownright, slightgrin, blush
    $ cg(effect_3="Talking_mouth_h3", effect_6="EyeLinefully_closed_h3", effect_7="blank", effect_8="boob_grab_pushup")
    "The two of you go on like that for a few more minutes, your stiff cock pressing against her torso as you play with her breasts. She continues to moan and grind against you as you do so, and you can tell she's getting close to being satisfied." #head3
    $ cg(effect_3="mouth_basic_H3", effect_5="Eye_At_PlayerH3", effect_6="EyeLine2_H3", effect_8="boob_grab_pushup")
    pc "I'm going to play with your nipples now, okay?"
    $ cg(effect_2="Headbase_H2", effect_3="mouth_openh2", effect_4="eyebrow_normal", effect_5="Eye_at_player_h2", effect_6="EyeLine2_H2", effect_8="boob_grab_pull")
    $ changeAzula("neutral")
    a "Haa...okay…" #head2
    "The uncharacteristically placid tone in her voice turns you on even more. You decide to go a bit further than you planned."
    pc "Take off your panties."
    $ cg(effect_4="EyeBrowLittle_Up_little_Down")
    $ changeAzula("bemused")
    a "Mmm...why?"
    pc "Just do it."
    $ cg(effect_2="HeadBase_1", effect_3="mouth_default", effect_4="EyeBrow_Normalh1", effect_5="eyes_at_player", effect_6="eyeline2")
    "Azula looks up at you, her eyes a bit harder than they were before. Maybe you should have posed it as a question, rather than a demand." #head1
    $ cg(effect_3="mouth_talking")
    $ changeAzula("mad")
    a "Are you...haa...trying to give me...mmm...orders?"
    $ cg(effect_3="mouth_default")
    pc "That's what the man does."
    $ cg(effect_2="Headbase_H2", effect_3="mouth_default_h2", effect_4="eyebrow_tense", effect_5="Eye_at_player_h2", effect_6="EyeLine2_H2")
    "Azula gives you a strange look, but she doesn't appear to be particularly angry."
    $ cg(effect_3="mouth_openh2", effect_4="EyeBrowLittle_Up_little_Down")
    $ changeAzula("bemused")
    a "Haa...oh, fine…" #head2
    $ changeAzula("stern")
    a "Just remember...mmm...who's really in...haa...charge here."
    $ cg(effect_1="blank", effect_2="HeadbaseH3",effect_3="mouth_basic_H3", effect_4="Brow_Cocky", effect_5="Iris_Down_RightH3", effect_6="EyeLine2_H3")
    "The Fire Lord gazes away while she follows your instructions. As she obediently lowers her panties, the back of her soft hands graze the head of your cock, almost sending you into a frenzy. It's been a while." #head3
    $ cg(effect_9="dong_in_legs")
    $ cg(effect_6="blank", effect_4="Little_Up_little_down")
    "Unable to help yourself, you reach down and slide your cock between Azula's thighs. She looks down, shocked by your audacity." #head1
    $ cg(effect_2="Headbase_H2", effect_3="mouth_openh2", effect_4="eyebrow_tense", effect_5="Eye_at_player_h2", effect_6="blank")
    $ changeAzula("mad")
    a "That's...haa...going too far, [pc_name]!"
    $ cg(effect_3="mouth_default_h2")
    pc "Relax. I'm just repositioning myself."
    $ cg(effect_5="Eye_down_h2")
    a "Hmm...mmm…"
    $ cg(effect_6="EyeLine2_H2", effect_4="EyeBrowLittle_Up_little_Down", effect_3="mouth_openh2")
    $ changeAzula("stern")
    a "Well, so long as...haa...you don't get...mmm...carried away...haa...I suppose I can allow it…"
    $ cg(effect_1="dong_in_legs", effect_3="mouth_openh2", effect_4="eyebrow_tense", effect_5="Eye_down_h2", effect_6="blank",effect_8="boob_pinch_left_noblur", effect_9="boob Pull Pinch left")
    "Like you said you would earlier, you begin to play with Azula's nipples, pinching them between your fingers. This elicits an immediate reaction, and the Fire Lord jerks her body from side to side, letting out little squeaks as you pinch her."
    $ cg(effect_6="EyeLinefully_closed_h2")
    $ changeAzula("surprised")
    a "That...eek!"
    $ cg(effect_4="EyeBrow_Normal")
    a "That feels so...haa...good...eek!"
    $ cg(effect_3="mouth_default_h2")
    pc "I know it does."
    $ changeAzula("neutral")
    $ cg(effect_3="mouth_openh2", effect_4="eyebrow_tense", effect_5="Eye_down_h2", effect_6="blank")
    a "At this rate I...eek!"
    $ cg(effect_6="EyeLine2_H2", effect_4="EyeBrow_Normal", effect_5="Eye_Right_h2")
    $ changeAzula("content")
    a "Might even...haa..."
    $ cg(effect_3="mouth_default_h2", effect_6="EyeLinefully_closed_h2")
    "Interrupting her train of thought, you rub your fingers over Azula's nipples, twisting them within your digits. She grinds against you harder, but doesn't spasm like before."
    $ cg(effect_3="mouth_openh2", effect_4="eyebrow_tense", effect_6="blank")
    $ changeAzula("coming")
    a "{size=+10}Eeeek!{/size}" #emphasis
    $ cg(effect_3="mouth_default_h2")
    pc "Might even what?"
    $ changeAzula("neutral")
    $ cg(effect_3="mouth_openh2", effect_5="Eye_at_player_h2", effect_6="EyeLine2_H2")
    a "Give you...haa...a promotion...eek!"
    $ cg(effect_3="mouth_default_h2")
    pc "Is that all?"
    $ cg(effect_3="mouth_openh2", effect_6="EyeLinefully_closed_h2")
    $ changeAzula("stern")
    a "What more do you...eek!"
    $ cg(effect_6="EyeLine2_H2")
    $ changeAzula("mad")
    a "What more do you...haa...want?"
    $ cg(effect_3="mouth_default_h2")
    pc "I want the same thing you want."
    $ cg(effect_3="mouth_openh2")
    $ changeAzula("coming")
    a "You had...haa...better, boy...eek!"
    $ cg(effect_3="mouth_default_h2")
    pc "But more than that, I want you to say it."
    $ cg(effect_3="mouth_openh2", effect_4="EyeBrowLittle_Up_little_Down", effect_6="blank")
    $ changeAzula("bemused")
    a "Haa...why?"
    $ cg(effect_3="mouth_default_h2")
    pc "Indulge me."
    $ cg(effect_3="mouth_openh2", effect_6="EyeLine2_H2")
    $ changeAzula("stern")
    a "Or...haa...what?"
    $ cg(effect_3="mouth_default_h2")
    pc "Or else I'll-"
    $ cg(effect_3="mouth_openh2", effect_4="eyebrow_tense", effect_5="Eye_Right_h2", effect_6="blank")
    "You stop short as the Fire Lord lets out a particularly high-pitched squeal. You didn't even do anything differently."
    $ changeAzula("coming")
    a "{size=+10}Eeeek!{/size}" #emphasis
    $ cg(effect_3="mouth_default_h2", effect_4="EyeBrow_Normal", effect_5="Eye_at_player_h2")
    pc "Or else I'll stop."
    $ cg("dong_in_legs","HeadBase_1", "Mouth_talking", "EyeBrow_angerh1", "Eyes_At_player", "eyeline2")
    $ changeAzula("mad")
    a "You...haa...better not!"
    $ cg(effect_3="mouth_default")
    menu:
        "Continue":
            $ cg(effect_9="boob_pinch_blur")
            "You continue to play with Azula's nipples, only now you speed up your efforts, pinching her right one and pulling it out until you're practically tugging on the Fire Lord's breast." #right blur
            $ cg(effect_1="dong_in_legs", effect_2="Headbase_H2", effect_3="mouth_openh2", effect_4="eyebrow_tense", effect_5="Eye_down_h2", effect_6="blank",effect_8="boob_pinch_left_noblur")
            $ changeAzula("coming")
            a "{size=+10}Eeek!{/size}" #emphasis
            "At the same time, you ease up on her left breast, providing her with a striking difference in sensations. It's not entirely rough, but you can tell she's enjoying it all the same."
            $ cg(effect_4="EyeBrow_Normal", effect_6="EyeLine2_H2")
            $ changeAzula("content")
            a "Mmm...I like that…"
            $ cg(effect_3="mouth_default_h2")
            pc "I bet you do."
            $ cg(effect_3="mouth_openh2", effect_5="Eye_at_player_h2")
            $ changeAzula("stern")
            a "Don't be...haa...snide, [pc_name]...eek!"
            $ changeAzula("coming")
            a "Just keep...mmm...doing what...haa...you're doing...eek!"
            $ cg(effect_3="mouth_default_h2")
            pc "I wouldn't dream otherwise, Azula."
            "Of course, that's because you're sure she'd burn you alive if you stopped this close to her inevitable orgasm. However, helping her out in this way should serve your goals very well. You might even get something out of it yourself."
            $ cg(effect_1="dong_in_legs", effect_2="Headbase_H2", effect_3="mouth_openh2", effect_4="eyebrow_tense", effect_5="Eye_down_h2", effect_6="blank",effect_8="boob_pinch_left_blur", effect_9="boob Pull Pinch left") 
            "Switching it up, you begin to tug on her left nipple while you return to simply teasing her right one. As you do, she slightly jerks to her left, but keeps her composure." #left blur
            a "{size=+10}Eeek!{/size}" #emphasis
            $ cg(effect_3="mouth_default_h2")
            pc "Anyway, you should tell me when you get close."
            $ cg(effect_5="Eye_at_player_h2", effect_3="mouth_openh2")
            $ changeAzula("neutral")
            a "Haa...and why's that?"
            $ cg(effect_4="EyeBrowLittle_Up_little_Down", effect_6="EyeLine2_H2")
            $ changeAzula("bemused")
            a "You want to...mmm...hear me squirm?"
            a "Is that it!?"
            $ cg(effect_3="mouth_default_h2")
            pc "I want to help push you over the edge."
            $ cg(effect_3="mouth_openh2", effect_4="EyeBrow_Normal")
            $ changeAzula("stern")
            a "Haa...very well...eek!"
            $ cg(effect_6="EyeLinefully_closed_h2")
            $ changeAzula("bemused")
            a "I will let you know...mmm…"
            $ cg(effect_3="mouth_default_h2", effect_5="Eye_Right_h2")
            "With any other woman, you'd say you'd have her in the palm of your hand at this point. With Azula, though, you're sure that if she doesn't cum, not only will you be stripped of your position, but you may very well be killed as well. If not today, then maybe tomorrow."
            "Intending to make this one count, you start to slowly tighten your grip on her right nipple as you rub it between your fingers. At the same time, you tug on her left breast a bit harder, pulling it out by her nipple."
            $ cg(effect_3="mouth_openh2", effect_5="Eye_Right_h2", effect_6="EyeLine2_H2")
            $ changeAzula("content")
            a "That's right...haa...I've been a bad girl…"
            $ cg(effect_2="HeadbaseH3",effect_3="Talking_mouth_h3", effect_4="Brow_Cocky", effect_5="Iris_Down_RightH3", effect_6="EyeLine2_H3")
            $ changeAzula("happy")
            a "If only my dear father...mmm...could see me now…"
            $ cg(effect_6="EyeLinefully_closed_h3")
            a "He'd punish me...eek!"
            $ cg(effect_5="Eye_At_PlayerH3", effect_6="blank")
            $ changeAzula("happy")
            a "Punish me, [pc_name]!"
            $ cg(effect_4="brow_happy", effect_5="Iris_Down_RightH3", effect_8="boob_pinch_left_blur", effect_9="boob_pinch_blur")
            "Taking that as your cue that she's at the brink of orgasm, you begin to roughly tug on both her breasts at a regular pace, continually loosening your grip on her nipples whenever you get close to her body, but then pinching them tightly as you pull them towards you." #both blur
            $ changeAzula("happy_mad")
            a "Yes!"
            $ cg(effect_5="Eye_At_PlayerH3")
            a "{size=+5}Yes!{/size}" #emphasis
            $ cg(effect_6="EyeLinefully_closed_h3")
            $ changeAzula("coming2")
            a "{size=+10}I'm...eeeek!{/size}" #emphasis on all
            $ cg(effect_3="mouth_basic_H3")
            "You can't help but also slide your cock through her thighs as you lay it on, feeling her legs shudder around you as she cums. Azula's body moves along with your pulls, and she constantly presses up against you, grinding against your body in an animalistic display of lust."
            $ cg(effect_1="dong_in_legs", effect_2="Headbase_H2", effect_3="mouth_openh2", effect_4="EyeBrow_Normal", effect_5="Eye_down_h2", effect_6="EyeLine2_H2", effect_8="boob_pinch_left_noblur", effect_9="boob Pull Pinch left") 
            $ changeAzula("happy")
            a "Haa...yes...just like...mmm…"
            $ cg(effect_6="EyeLinefully_closed_h2")
            $ changeAzula("coming")
            a "Just like that...eek!"
            $ cg(effect_3="mouth_default_h2")
            "After another minute of this, Azula's breathing steadily begins returning to normal, and she stops grinding against you. Whatever she was looking for out of all this, she appears to have found it, although from all the 'daddy' talk, you're not sure what exactly it was."
            $ cg(effect_2="HeadBase_1", effect_3="slight_smile_h1", effect_4="EyeBrow_happy", effect_5="eyes_at_player", effect_6="blank", effect_8="blank", effect_9="blank")
            "Still, so long as she's satisfied, you feel safe and secure. She'll certainly want to keep you around after all this. You remove your hands from her breasts, but Azula doesn't complain. In fact, she gives a quick sigh of relief, as if she didn't want to bring it up."
            $ changeAzula("content")
            a "That was marvelous, [pc_name]."
            $ cg(effect_3="mouth_talking")
            $ changeAzula("happy")
            a "We'll have to do that again sometime."
            $ cg(effect_3="mouth_default")
            pc "And perhaps go even farther."
            $ cg(effect_3="mouth_talking", effect_4="EyeBrow_angerh1", effect_6="blank")
            $ cg(effect_3="mouth_default", effect_4="EyeBrow_Normalh1", effect_5="eyes_right")
            "Suddenly, Azula appears angry and opens her mouth as if to yell at you, but then looks away thoughtfully."
            $ cg(effect_3="mouth_talking")
            $ changeAzula("content")
            a "Yes...and perhaps go even farther."
            $ cg(effect_5="eyes_at_player")
            $ changeAzula("happy")
            a "But as for today, I'm done with you, boy."
            a "You may leave."
            $ cg(effect_3="mouth_default")
            pc "So, about that promotion."
            $ cg(effect_3="mouth_talking", effect_6="eyeline2")
            $ changeAzula("stern")
            a "{size=+10}I said{/size}, you may leave!" #emphasis on 'said'
            $ cg(effect_3="mouth_default")
            "You want to argue with her, but decide to save that for next time, after she's had more time to digest the amount of pleasure you're able to bring to her life."
            pc "See you soon, Azula."
            $ cg(effect_3="mouth_talking", effect_6="blank")
            $ changeAzula("neutral")
            a "Goodbye, [pc_name]."
            $ black("show")
            "With that, you leave the sauna, being sure not to cut yourself on the blade still hanging in front of the doorway, and get dressed again outside. As you leave, you hear Azula begin to laugh behind you, though you're not sure at what. That girl is crazy."
            jump eventmenu
        "Stop":
            $ black("show")
            "You stop playing with Azula's nipples and put some space in between you and her. She immediately brings her hands out from behind her back. Blue flames erupt from her palms, and you don't even have a chance to scream before she incinerates you on the spot."
            $ changeAzula("stern")
            a "Insolent fool!"
            "The Fire Lord lightly kicks your corpse to see if you're still alive. You're not."
            $ changeAzula("bemused")
            a "Perhaps I was a bit...hasty."
            $ changeAzula("neutral")
            a "Oh well."
            a "Plenty of fish in the sea."
            "GAME OVER"
            jump eventmenu
