################################################################################
screen barra_energia_info:
    image "images/pergamino_info.png" xalign 0.5 yalign 0.5
    hbox:
        xalign 0.5
        yalign 0.5
        xsize 1200
        text "La barra se llenará cuando comas, no dejes que la barra baje del 25 porciento o las mariposas empezarán a morir por falta de energía." xalign 0.5 yalign 0.5

    imagebutton auto "gui/mis_botones/aceptar_%s.png" xpos 1351 ypos 664 focus_mask True action Jump("escena_3") hovered [Play("sound", "audio/sonido/clic.mp3")]

################################################################################
screen comer_campo_info:
    image "images/pergamino_info.png" xalign 0.5 yalign 0.5
    hbox:
        xalign 0.5
        yalign 0.5
        xsize 1200

        text "¿Sabías que?... El uso de plaguicidas, agroquímicos e insecticidas para actividades agrícolas y de control sanitario, han provocado una disminución de 58 porciento del algodoncillo. Lo que de 1999 a 2010 significó una reducción de 81 porciento en la población de Mariposas Monarca." xalign 0.5 yalign 0.5

    imagebutton auto "gui/mis_botones/aceptar_%s.png" xpos 1351 ypos 664 focus_mask True action Jump("escena_4") hovered [Play("sound", "audio/sonido/clic.mp3")]

################################################################################
screen no_comer_campo_info:
    image "images/pergamino_info.png" xalign 0.5 yalign 0.5
    hbox:
        xalign 0.5
        yalign 0.5
        xsize 1200

        text "Las mariposas Monarca sólo ponen huevos en el algodoncillo y las orugas solo comen algodoncillo, lo que hace a esta planta crucial para la supervivencia de la población monarca. Los habitantes de E.U. y Canadá pueden ayudar a la sustentabilidad de las Monarcas si siembran algodoncillo en sus patios, macetas y jardineras." xalign 0.5 yalign 0.5

    imagebutton auto "gui/mis_botones/aceptar_%s.png" xpos 1351 ypos 664 focus_mask True action Jump("no_comer_campo2") hovered [Play("sound", "audio/sonido/clic.mp3")]

################################################################################
screen hembra_info:
    image "images/mariposa_genero.png" xalign 0.5 yalign 0.5
    hbox:
        xalign 0.7
        yalign 0.5
        xsize 600

        text "Las mariposas hembras tienen las rayas negras de sus alas más anchas que las mariposas machos."
    imagebutton auto "gui/mis_botones/aceptar_%s.png" xpos 1351 ypos 664 focus_mask True action Jump("hola") hovered [Play("sound", "audio/sonido/clic.mp3")]

################################################################################
screen macho_info:
    image "images/mariposa_genero.png" xalign 0.5 yalign 0.5
    hbox:
        xalign 0.7
        yalign 0.5
        xsize 600

        text "Las mariposas machos tienen dos puntitos en las alas, a diferencia de las mariposas hembras que no los tienen."
    imagebutton auto "gui/mis_botones/aceptar_%s.png" xpos 1351 ypos 664 focus_mask True action Jump("hola") hovered [Play("sound", "audio/sonido/clic.mp3")]



################################################################################
screen energia_100_info:
    image "gui/frame.png" xalign 0.5 yalign 0.5
    hbox:
        xalign 0.5
        yalign 0.5
        xsize 1200
        text "Barra de energía 100 porciento" xalign 0.5 yalign 0.5

################################################################################
screen energia_50_info:
    image "gui/frame.png" xalign 0.5 yalign 0.5
    hbox:
        xalign 0.5
        yalign 0.5
        xsize 1200
        text "Barra de energía 50 porciento" xalign 0.5 yalign 0.5

################################################################################
screen menos_10_energia_info:
    image "gui/frame.png" xalign 0.5 yalign 0.5
    hbox:
        xalign 0.5
        yalign 0.5
        xsize 1200
        text "-10 porciento de energía" xalign 0.5 yalign 0.5

################################################################################
screen menos_5_mariposas_info:
    image "gui/frame.png" xalign 0.5 yalign 0.5
    hbox:
        xalign 0.5
        yalign 0.5
        xsize 1200
        text "Mariposas muertas: 5" xalign 0.5 yalign 0.5

################################################################################
screen aldoncillo_pistas_info:
    image "gui/frame.png" xalign 0.5 yalign 0.5
    hbox:
        xalign 0.5
        yalign 0.5
        xsize 800
        text "Pistas para encontrar algodoncillo: Búscalo en jardineras" xalign 0.5 yalign 0.5

################################################################################
screen final_malo_cap1_info:
    image "gui/frame.png" xalign 0.5 yalign 0.5
    hbox:
        xalign 0.5
        yalign 0.5
        xsize 800
        text "Intenta tomar mejores decisiones en el próximo capítulo." xalign 0.5 yalign 0.5

    imagebutton auto "gui/mis_botones/aceptar2_%s.png" xpos 1248 ypos 605 focus_mask True action Jump("fin") hovered [Play("sound", "audio/sonido/clic.mp3")]

################################################################################
screen final_bueno_cap1_info:
    image "gui/frame.png" xalign 0.5 yalign 0.5
    hbox:
        xalign 0.5
        yalign 0.5
        xsize 800
        text "Felicidades conseguiste que las mariposas encontraran comida." xalign 0.5 yalign 0.5

    imagebutton auto "gui/mis_botones/aceptar2_%s.png" xpos 1248 ypos 605 focus_mask True action Jump("fin") hovered [Play("sound", "audio/sonido/clic.mp3")]


################################################################################
screen danaus_info:
    image "images/monarca.png" xalign 0.5 yalign 0.5
