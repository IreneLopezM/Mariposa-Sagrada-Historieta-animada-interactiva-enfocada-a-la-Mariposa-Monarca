default desicion = 0

style boton:
    color "#3C1D07"
    hover_color "#705740"

screen boton_estadisticas():
    frame:
        margin(10,10,10,10)
        padding(20,20,20,20) #izquierda, arriba, derecha, abajo
        xalign 0.5

        button align(0.5, 0.1):
            action Show("pantalla_estadisticas") hovered [Play("sound", "audio/sonido/clic.mp3")]
            text "Estadísticas" style "boton"


screen pantalla_estadisticas():
    image "gui/frame.png" xalign 0.5 yalign 0.5 xysize(1500,1000)

    vbox:
        xalign 0.5
        yalign 0.25
        xsize 1500
        text "Malas decisiones que han tomado los jugadores " xalign 0.5 yalign 0.5

        viewport:
            xalign 0.5
            yalign 0.5
            xysize (1400,790)
            mousewheel True
            arrowkeys True
            scrollbars "vertical"
            vbox:
                xalign 0.5
                yalign 0.5
                xsize 1400

                grid 2 31:
                    yalign 0.5
                    text "Capítulo 1: El algodoncillo" xalign 0.2 yalign 0.5
                    text ""

                    text "Decisión" yalign 0.5
                    text "Número de jugadores"  xalign 0.2 yalign 0.5

                    text "Decisión 1: No comer en el parque. " yalign 0.5
                    $ desicion = len(persistent.d1_volar)
                    text "[desicion]" xalign 0.2 yalign 0.5

                    text "Decisión 2: Comer en el campo de cultivo. " yalign 0.5
                    $ desicion = len(persistent.d2_comer_campo)
                    text "[desicion]" xalign 0.2 yalign 0.5

                    text "Decisión 3: No examinar el objeto. "  yalign 0.5
                    $ desicion = len(persistent.d3_no_examinar_objeto)
                    text "[desicion]" xalign 0.2 yalign 0.5

                    text "Decisión 4: No seguir el rastro de polen. " yalign 0.5
                    $ desicion = len(persistent.d4_no_seguir_rastro)
                    text "[desicion]" xalign 0.2 yalign 0.5



                    text ""
                    text ""

                    text "Capítulo 2: Condiciones críticas" xalign 0.2 yalign 0.5
                    text ""

                    text "Decisión" yalign 0.5
                    text "Número de jugadores"  xalign 0.2 yalign 0.5

                    text "Decisión 1: Quedarse en la granja. " yalign 0.5
                    $ desicion = len(persistent.d1_quedarse)
                    text "[desicion]" xalign 0.2 yalign 0.5

                    text "Decisión 2: Elegir el árbol sin hojas. " yalign 0.5
                    $ desicion = len(persistent.d2_ArbolSinHojas)
                    text "[desicion]" xalign 0.2 yalign 0.5

                    text "Decisión 3: Elegir el árbol con pocas hojas. " yalign 0.5
                    $ desicion = len(persistent.d3_ArbolConPocasHojas)
                    text "[desicion]" xalign 0.2 yalign 0.5



                    text ""
                    text ""

                    text "Capítulo 3: Zona de riesgo" xalign 0.2 yalign 0.5
                    text ""

                    text "Decisión" yalign 0.5
                    text "Número de jugadores"  xalign 0.2 yalign 0.5

                    text "Decisión 1: No esquivar correctamente el auto 1. " yalign 0.5
                    $ desicion = len(persistent.d1_auto1)
                    text "[desicion]" xalign 0.2 yalign 0.5

                    text "Decisión 2: No esquivar correctamente el auto 2. " yalign 0.5
                    $ desicion = len(persistent.d2_auto2)
                    text "[desicion]" xalign 0.2 yalign 0.5

                    text "Decisión 3: No esquivar correctamente el auto 3. " yalign 0.5
                    $ desicion = len(persistent.d3_auto3)
                    text "[desicion]" xalign 0.2 yalign 0.5

                    text "Decisión 4: No esquivar correctamente el auto 4. " yalign 0.5
                    $ desicion = len(persistent.d4_auto4)
                    text "[desicion]" xalign 0.2 yalign 0.5

                    text "Decisión 5: No esquivar correctamente los autos 5 y 6. " yalign 0.5
                    $ desicion = len(persistent.d5_auto5y6)
                    text "[desicion]" xalign 0.2 yalign 0.5

                    text "Decisión 6: No esquivar correctamente el auto 7. " yalign 0.5
                    $ desicion = len(persistent.d6_auto7)
                    text "[desicion]" xalign 0.2 yalign 0.5



                    text ""
                    text ""

                    text "Capítulo 4: Devastación" xalign 0.2 yalign 0.5
                    text ""

                    text "Decisión" yalign 0.5
                    text "Número de jugadores"  xalign 0.2 yalign 0.5

                    text "Decisión 1: Quedarse en la zona agrícola y ganadera. " yalign 0.5
                    $ desicion = len(persistent.d1_zona_ganadera)
                    text "[desicion]" xalign 0.2 yalign 0.5

                    text "Decisión 2: Quedarse en el campo de cultivo de aguacates. " yalign 0.5
                    $ desicion = len(persistent.d2_aguacates)
                    text "[desicion]" xalign 0.2 yalign 0.5



                    text ""
                    text ""

                    text "Capítulo 5: Vecinos molestos" xalign 0.2 yalign 0.5
                    text ""

                    text "Decisión" yalign 0.5
                    text "Número de jugadores"  xalign 0.2 yalign 0.5

                    text "Decisión 1: Quedarse a las afueras del bosque. " yalign 0.5
                    $ desicion = len(persistent.d1_quedarse_afuera_bosque)
                    text "[desicion]" xalign 0.2 yalign 0.5

                    text "Decisión 2: Quedarse a las orillas del camino. " yalign 0.5
                    $ desicion = len(persistent.d2_quedarse_orilla_camino)
                    text "[desicion]" xalign 0.2 yalign 0.5

    imagebutton auto "gui/mis_botones/aceptar2_%s.png" xpos 1500 ypos 900 focus_mask True action Hide("pantalla_estadisticas") hovered [Play("sound", "audio/sonido/clic.mp3")]
