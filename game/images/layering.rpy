﻿screen background:
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


    zorder -1




init python: ###Method Definition for controlling transitions and outfits
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
        
        
    def cg(emotion, effect_1=None,
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

        ###HIDE OLD SCREEN
        renpy.hide_screen("cg_screen")
        #renpy.with_statement(Dissolve(0.5))







        ###DISPLAY THE UPDATED SCREEEN
        renpy.show_screen("cg_screen")
        renpy.with_statement(Dissolve(0.5))

    def changeAzula(emotion):
        global cg_image_base
        global cg_image_1
        global cg_image_2
        global cg_image_3
        global cg_image_4
        global cg_image_5
        global cg_image_6

        ###HIDE OLD SCREEN
        renpy.hide_screen("cg_screen")
        #renpy.with_statement(Dissolve(0.5))








        ###DISPLAY THE UPDATED SCREEEN
        renpy.show_screen("cg_screen")
        renpy.with_statement(Dissolve(0.5))
        
        

    #disappointed: "tense_eyebrow", "defaultmouth_#3"
    #bemused: "little_up_little_downbrow", "default_mouth_#1"
    #content: "defaultmouth_#2", "contentbrow_#1"
    #excited: "smilingmouth", "excitedbrow"
    #stern: "defaultmouth", "mad_copy"
    #neutral: "content_copy_2", "default_mouth"
    #frustrated: "mad_mouth", "bored_copy"
    #happy: "smiling_copy", "content_copy"
    
    #surprised: "eye_open" (pupil 1), "excitedbrow", "talkingmouth"
    #annoyed: "eye_partially_closed" (pupil 1), "mad_brow", "defaultmouth_#1"
    #mad: "eye_partially_closed" (pupil 1), "mad_mouth", "madbrow_copy"
        
        
        
        
        
        
        
        
        
        
        
        