##############################################################################
screen num_mariposas():
    frame:
        margin(10,10,10,10)
        padding(20,20,20,20) #izquierda, arriba, derecha, abajo

        has hbox
        spacing 10

        vbox:
            text "Mariposas:"
        vbox:
            xsize 70
            text "[num_mari]" xalign 1.0



###################################################################################
screen barra_energia():
    frame:
        margin(10,10,10,10)
        padding(20,30,20,20)
        xalign 1.0

        has hbox
        spacing 10

        vbox:
            text "Energía"

        vbox:
            xalign 0.5
            yalign 0.5
            timer 30 repeat True action If(energia < 25, true=SetVariable('num_mari', num_mari - 1))
            bar:
                value energia
                range 100
                left_bar "images/left.png"
                right_bar "images/right1.png"
                thumb "images/bar_thumb.png"
                xysize(400,50)
                xalign 0.5
                yalign 0.5


###################################################################################
screen contador:
    timer 0.5 repeat True action If(time > 0, true=SetVariable('time', time - 0.5), false=[Hide('contador'), Jump(etiqueta)])
    bar value time range rango_tiempo xalign 0.5 yalign 0.9 xmaximum 600
