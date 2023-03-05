screen danaus_info:
    image "images/monarca.png" xalign 0.5 yalign 0.5

################################################################################
screen genero_info:
    image "images/mariposa_genero.png" xalign 0.5 yalign 0.5
    hbox:
        xalign 0.7
        yalign 0.5
        xsize 600

        text "[texto]"
    imagebutton auto "gui/mis_botones/aceptar_%s.png" xpos 1351 ypos 664 focus_mask True action Jump(etiqueta) hovered [Play("sound", "audio/sonido/clic.mp3")]

################################################################################
screen energia_info:
    image "gui/frame.png" xalign 0.5 yalign 0.5
    hbox:
        xalign 0.5
        yalign 0.5
        xsize 1200
        text "Barra de energía [energia]\% " xalign 0.5 yalign 0.5

################################################################################
screen menos_energia_info:
    image "gui/frame.png" xalign 0.5 yalign 0.5
    hbox:
        xalign 0.5
        yalign 0.5
        xsize 1200
        text "-[menos_ener]\% de energía" xalign 0.5 yalign 0.5

################################################################################
screen menos_mariposas_info:
    image "gui/frame.png" xalign 0.5 yalign 0.5
    hbox:
        xalign 0.5
        yalign 0.5
        xsize 1200
        text "Mariposas muertas: [menos_mari]" xalign 0.5 yalign 0.5

################################################################################
screen info:
    image "images/pergamino_info.png" xalign 0.5 yalign 0.5
    hbox:
        xalign 0.5
        yalign 0.5
        xsize 1200

        text "[texto]" xalign 0.5 yalign 0.5

    imagebutton auto "gui/mis_botones/aceptar_%s.png" xpos 1351 ypos 664 focus_mask True action Jump(etiqueta) hovered [Play("sound", "audio/sonido/clic.mp3")]

################################################################################
screen pistas_info:
    image "gui/frame.png" xalign 0.5 yalign 0.5
    hbox:
        xalign 0.5
        yalign 0.5
        xsize 800
        text "[texto]" xalign 0.5 yalign 0.5

################################################################################
screen final_cap_info:
    image "gui/frame.png" xalign 0.5 yalign 0.5
    hbox:
        xalign 0.5
        yalign 0.5
        xsize 800
        text "[texto]" xalign 0.5 yalign 0.5

    imagebutton auto "gui/mis_botones/aceptar2_%s.png" xpos 1248 ypos 605 focus_mask True action Jump(etiqueta) hovered [Play("sound", "audio/sonido/clic.mp3")]
