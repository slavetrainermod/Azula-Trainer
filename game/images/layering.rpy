screen background:
    add back_image
    #text "Money: $ "+str(money) xpos 1050 ypos 5
    #text "Time: "+timeString xpos 800 ypos 5
    zorder -5

screen g_stats:
    ##add back_image
    text "Money: $ "+str(money) xpos 550 ypos 300
    text "Corruption: "+str(corruption) xpos 550 ypos 320
    text "Obedience: "+str(obedience) xpos 550 ypos 340
    text "Morals: "+str(morals) xpos 550 ypos 360
    zorder -3

screen q_stats:
    ##add back_image
    text "Quest 1 Status:" xpos 550 ypos 300
    text "Quest 2 Status:" xpos 550 ypos 320
    text "Quest 3 Status:" xpos 550 ypos 340
    text "Quest 4 Status:" xpos 550 ypos 360
    zorder -3

screen cg_screen:
    add cg_image_base
    add cg_image_1
    add cg_image_2
    add cg_image_3
    add cg_image_4
    add cg_image_5
    add cg_image_6


    zorder -1



init python: ###Method Definition for controlling transitions and outfits
    def azula_sprite(input, input2):
        return LiveComposite(
        (0, 290),
        (0,0), azula_sprite_base,
        (0,0), azula_eye,
        (0,0), azula_eyebrow,
        (0,0), azula_mouth), .1



    def background(image=None):
        global back_image
        ###HIDE OLD SCREEN
        renpy.hide_screen("background")
        #renpy.with_statement(Dissolve(0.5))
        if image is not None:
            back_image = image
        ###DISPLAY THE UPDATED SCREEEN
        renpy.show_screen("background")
        renpy.with_statement(Dissolve(0.5))
        
        
    def cg( effect_1=None,
            effect_2=None,
            effect_3=None,
            effect_4=None,
            effect_5=None,
            effect_6=None,):
        global cg_image_base
        global cg_image_1
        global cg_image_2
        global cg_image_3
        global cg_image_4
        global cg_image_5
        global cg_image_6
        global cg_scene

        ###HIDE OLD SCREEN
        renpy.hide_screen("cg_screen")
        #renpy.with_statement(Dissolve(0.5))
        fp = "images/cg/scene_01/"+cg_scene+"/"

        cg_image_base = fp+"base.png"

        if effect_1 != None:
            cg_image_1 = fp+effect_1+".png"
        if effect_2 != None:
            cg_image_2 = fp+effect_2+".png"
        if effect_3 != None:
            cg_image_3 = fp+effect_3+".png"
        if effect_4 != None:
            cg_image_4 = fp+effect_4+".png"
        if effect_5 != None:
            cg_image_5 = fp+effect_5+".png"
        if effect_6 != None:
            cg_image_6 = fp+effect_6+".png"







        ###DISPLAY THE UPDATED SCREEEN
        renpy.show_screen("cg_screen")
        renpy.with_statement(Dissolve(0.5))

    def changeAzula(emotion):
        global azula_sprite_base
        global azula_eye
        global azula_mouth
        global azula_eyebrow

        ap = "images/cg/azula/"

        if emotion == "disappointed":
            azula_eye = ap+"default_eye_1.png"
            azula_eyebrow = ap+"tense_eyebrow.png"
            azula_mouth = ap+"default_mouth_3.png"
        elif emotion == "bemused":
            azula_eye = ap+"default_eye_1.png"
            azula_eyebrow = ap+"little_up_little_downbrow.png"
            azula_mouth = ap+"default_mouth_1.png"
        elif emotion == "content":
            azula_eye = ap+"default_eye_1.png"
            azula_eyebrow = ap+"content_eyebrow_1.png"
            azula_mouth = ap+"default_mouth_2.png"
        elif emotion == "excited":
            azula_eye = ap+"default_eye_1.png"
            azula_eyebrow = ap+"excited_eyebrow.png"
            azula_mouth = ap+"smiling_mouth.png"
        elif emotion == "stern":
            azula_eye = ap+"default_eye_1.png"
            azula_eyebrow = ap+"mad_eyebrow.png"
            azula_mouth = ap+"default_mouth_1.png"
        elif emotion == "neutral":
            azula_eye = ap+"default_eye_1.png"
            azula_eyebrow = ap+"content_eyebrow_2.png"
            azula_mouth = ap+"default_mouth_1.png"
        elif emotion == "frustrated":
            azula_eye = ap+"default_eye_1.png"
            azula_eyebrow = ap+"bored_eyebrow.png"
            azula_mouth = ap+"mad_mouth.png"
        elif emotion == "happy":
            azula_eye = ap+"default_eye_1.png"
            azula_eyebrow = ap+"content_eyebrow_1.png"
            azula_mouth = ap+"smiling_mouth.png"
        elif emotion == "surprised":
            azula_eye = ap+"eye_open_1.png"
            azula_eyebrow = ap+"excited_eyebrow.png"
            azula_mouth = ap+"talking_mouth_1.png"
        elif emotion == "annoyed":
            azula_eye = ap+"partial_eye_1.png"
            azula_eyebrow = ap+"mad_eyebrow.png"
            azula_mouth = ap+"default_mouth_1.png"
        elif emotion == "mad":
            azula_eye = ap+"partial_eye_1.png"
            azula_eyebrow = ap+"mad_eyebrow.png"
            azula_mouth = ap+"mad_mouth.png"