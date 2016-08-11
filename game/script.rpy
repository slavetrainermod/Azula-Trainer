label start:
    call start_variables
    jump scene_01
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

    $ pc_name = "Lee"
    return





###Define Characters 
init:
    $ pc = Character("Lee", color="#cc0000", show_two_window=True) #Lee
    $ a = Character("Azula", color="#ffcc00", show_two_window=True) #Azula