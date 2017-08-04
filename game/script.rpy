label start:
    call start_variables from _call_start_variables
    jump intro_scene
    return





label start_variables: ###Define Starting variables
    $ back_image = "images/environments/throne.png"
    $ cg_image_base = "images/blank.png"
    $ cg_image_1 = "images/blank.png"
    $ cg_image_2 = "images/blank.png"
    $ cg_image_3 = "images/blank.png"
    $ cg_image_4 = "images/blank.png"
    $ cg_image_5 = "images/blank.png"
    $ cg_image_6 = "images/blank.png"
    $ cg_image_7 = "images/blank.png"
    $ cg_image_8 = "images/blank.png"
    $ cg_image_9 = "images/blank.png"
    $ cg_scene = "FireThrone"


    $ azula_sprite_base = "images/cg/azula/base_2.png"
    $ azula_eye = "images/default_eye_1.png"
    $ azula_mouth = "images/default_mouth_1.png"
    $ azula_eyebrow = "images/content_eyebrow_1.png"

    $ pc_name = "Lee"
    $ azula_name = "Azula"

    return





###Define Characters 
init:
    image azula_side_image = DynamicDisplayable(azula_sprite)
    define pc = Character("Lee", color="#cc0000", show_two_window=True) #Lee
    define a = Character(color="#ffcc00", show_two_window=True, image="sidegirl", window_left_padding=300) #Azula
    image sidegirl = "images/blank.png"
    image side sidegirl = "azula_side_image"