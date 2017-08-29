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
    $ changeAzula("content")
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
    $ cg("Towel","Headbase_1","mouth_default", "eyebrow_happy","eyes_at_player", "eyeline2")
    "You stop short as you realize what you're saying. The Fire Lord smirks at you."
    $ cg(effect_3="mouth_talking")
    $ changeAzula("content")
    a "What?"
    a "What will you do, [pc_name]?"
    $ cg(effect_3="mouth_default")
    "Remembering that there's noting you can do, you simply hang your head."
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
    $ cg(effect_5="eyedown")
    "Azula smiles at your remembrance. It's like she's actually happy to see you, or at least, your body."
    $ cg(effect_5="eyes_at_player", effect_3="mouth_talking")
    $ changeAzula("happy")
    a "You arrived soon enough."
    $ cg(effect_4="eyebrow_happy")
    a "It {size=+10}is{/size} a rather large palace to search, after all." #emphasis on 'is'
    $ cg(effect_3="mouth_default")
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
    a "I've already done that for you once." #slight emphasis on 'I've'
    pc "Fine, then."
    "Hooking a finger underneath the middle of her bra, you draw Azula slightly closer to you. She exhales loudly, as if she's trying to calm herself."
    pc "You don't mind, do you?"
    a "Of course not…"
    "You don't waste any time in removing the only article of clothing between you and her royal breasts. Azula helps you by moving her arms so it's easier to pull off her bra, returning them to her (sides? I forget - tf) once it's gone."
    a "Thanks."
    a "It was getting a bit soaked."
    "Suddenly, you remember that you're in a sauna, fully clothed. It's grown mildly uncomfortable since you entered."
    pc "Excuse me for a moment."
    "You turn around to walk out, but Azula grabs your hand to stop you."
    a "Wait!"
    a "Where do you think you're going!?"
    pc "Just to take off some of these clothes. We are in a sauna, after all."
    a "Oh, right…"
    a "Well, don't take too long!"
    "The Fire Lord glowers at you impatiently, but lets go of your hand. You navigate your way around the used trap still hanging in front of the door and step into the hallway, where you quickly undress down to your underwear. When you return, her expression hasn't changed a bit. You decide to try a bit of sarcasm."
    pc "Sorry for the wait."
    a "Unamusing, [pc_name]."
    a "Highly unamusing." #emphasis on 'highly'
    pc "Azula, I was gone for less than a minute."
    a "Enough talk!"
    "To emphasize her point, the Fire Lord shakes her upper body from side to side, slightly swinging her breasts in tandem. Your cock twitches at the sight."