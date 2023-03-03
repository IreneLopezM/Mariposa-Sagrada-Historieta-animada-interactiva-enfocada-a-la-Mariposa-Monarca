define narr = Character("Narrador")
define abe = Character("Abeja")

default num_mari = 400
default energia = 0
default genero = ""

define config.mouse = {
    "default" : [("images/cursor_puntero.png", 0, 0)],
    "say" : [("images/cursor_mariposa.png", 0, 0)]
}

################################################################################
label start:
    #Crear usuario
    scene bosque1
    $ usuario = renpy.input("Ingrese su nombre de usuario")
    $ usuario = usuario.strip()
    if usuario == "":
        jump start

    play sound "audio/sonido/notificacion.mp3"
    menu:
        "Elige el género de tu mariposa"
        "Hembra":
            $genero = True
        "Macho":
            $genero = False

    play sound "audio/sonido/papel.mp3"
    if genero:
        call screen hembra_info
    else:
        call screen macho_info

label hola:
    play sound "audio/sonido/notificacion.mp3"
    menu:
        "¡Hola [usuario]!":
            play sound "audio/sonido/clic.mp3"
            jump escena_0

################################################################################
label escena_0:
    pause 1.0
    #Imagen de fondo
    scene fondo_negro with fade
    #Musica de fondo
    play music "audio/musica/Intro.mp3" loop fadein 2.0

    #Dialogo de Introducción
    narr """Desde hace mucho tiempo han existido.

    En algunas culturas se cree que son el alma de los seres queridos que regresan.

    En otras, son guerreros que vuelven después de haber muerto en batalla.

    Lo cierto es que son un símbolo de transformación. De huevo a oruga, a crisálida y al final a mariposa.
    Cambian durante toda su vida para poder extender sus alas y volar.

    Al final el ciclo se vuelve a repetir...

    Y por junio, cuando los meses se acercan más al invierno nace la última generación de ese año.

    Y este año no será la excepción pues ya han salido de las crisálidas la nueva generación y se llaman..."""
    centered "Matusalén: Mariposa Sagrada." (what_color="#ffffff")

    #Imagen de fondo del capitulo 1
    scene cap_1
    #Parar musica con desvanecimiento de 3 s
    stop music fadeout 3.0
    #Mantener la imagen por 5 s
    pause 5

    scene fondo_circulo with fade
    show screen danaus_info
    play sound "audio/sonido/notificacion.mp3"
    "[usuario] es el personaje principal de esta historia, de tus decisiones dependerá su supervivencia."
    play sound "audio/sonido/notificacion.mp3"
    "¡Suerte en esta nueva aventura!"
    hide screen danaus_info

    scene parque with fade
    #Musica de fondo del capitulo 1
    play music "audio/musica/Cap_1.mp3" volume 0.5 loop fadein 1.0
    #Dialogo del capitulo 1
    narr """Cuando [usuario] salió de la crisálida, lo primero que vio fueron los tallos verdes y altos acompañados del
    follaje espeso que formaban las plantas de algodoncillo.

    Era el mismo escenario que vio antes de irse a dormir en su cálido capullo, pero...

    Ahora se sentía diferente.

    Y su cuerpo también era diferente.

    Apoyando sus seis patas en la hoja que le dio cobijo durante su transformación movió sus alas y las extendió
    poco a poco.

    La sangre acumulada en su cuerpo se fue desplazando por sus alas y cuando terminó estas se mostraron en todo
    su esplendor.

    Fue una tarea ardua, que duró casi dos horas. [usuario] estaba exhausta...

    Y mirando alrededor se encontró con otras iguales a ella, aún aturdidas y cansadas por el cambio.

    Al ser la primera en salir batió sus alas suavemente y se acercó a ellas mostrándoles cómo debían extender sus
    alas. Agradecidas copiaron sus movimientos."""

    play sound "audio/sonido/notificacion.mp3"
    menu:
        "[usuario] tienes bajo tu cuidado a 400 mariposas Monarca": #Numero de huevecillos que puede llegar a poner una mariposa Monarca
            play sound "audio/sonido/clic.mp3"
            jump escena_1


################################################################################
label escena_1:
    show screen num_mariposas
    narr """Para cuándo la última mariposa Monarca terminó de extender sus alas, el sol estaba en su punto más alto.

    [usuario] se debatió entre comer el néctar de las plantas que las protegieron durante su metamorfosis o extender
    sus alas y volar por los alrededores antes de que anocheciera."""
    menu:
        "Comer":
            play sound "audio/sonido/clic.mp3"
            jump comer_parque
        "Volar":
            play sound "audio/sonido/clic.mp3"
            jump volar


################################################################################
label comer_parque:
    narr "[usuario] se posó sobre una flor y bebió de su néctar, sus compañeras siguieron su ejemplo."
    play sound "audio/sonido/papel.mp3"
    $ energia = 100
    show screen barra_energia
    show screen energia_100_info
    pause 2.0
    jump escena_2


################################################################################
label volar:
    play sound "audio/sonido/papel.mp3"
    $ energia = 50
    show screen barra_energia
    show screen energia_50_info
    pause 2.0
    jump escena_2


################################################################################
label escena_2:
    hide screen energia_100_info
    hide screen energia_50_info

    play sound "audio/sonido/papel.mp3"
    call screen barra_energia_info


################################################################################
label escena_3:
    narr """Los pequeños arbustos de algodoncillo han sido su alimento desde que eran larvas.

    Las hojas verdes y lechosas que son venenosas para cualquier otro animal, para ellas son su mayor fuente de
    alimento y las que pintan sus alas de colores naranjas y negros vibrantes pues ahí se esconden las toxinas del
    algodoncillo que han comido desde bebés.

    Dando a través de esos colores un claro mensaje para sus depredadores de lo tóxicas que son.

    Al ser el único alimento que [usuario] conocía desde que nació, decidió buscar más allá de lo que sus ojos
    alcanzaban a ver.

    Y extendiendo sus alas se alzó tan alto como pudo y vio un mundo totalmente distinto.

    Plantas tan altas que llegaban hasta un manto azul que lo cubría todo y en el cual flotaban motitas blancas
    y esponjosas.

    Seres vivos muy diferentes a ella y sus hermanos se paseaban por doquier en una danza singular.

    Y grandes pilares grises se veían más allá de los árboles.

    [usuario] contempló emocionada estás rarezas y aleteando fuertemente sus alas exploró lo que había más allá
    de su pequeño hogar en el arbusto de algodoncillo."""

    stop music fadeout 4.0
    narr "Sus compañeras la siguieron en armonía."

    scene campo_cultivo1 with fade
    play music "audio/musica/suspenso_suave.mp3" loop fadein 3.0
    narr """Después de merodear por un tiempo, las mariposas llegaron a un inmenso campo un tanto peculiar, pues las
    plantas se erigían en filas paralelas en perfecta simetría.

    Sin embargo, arbustos de algodoncillo y otras malezas brotaban aquí y allá rompiendo el orden entre las plantas.
    [usuario] contempló emocionada los arbustos de algodoncillo en flor, pero..."""

    play sound "audio/sonido/avion.mp3"
    narr "Antes de que pudiera volar hacia ellos, un estruendo se hizo presente en el campo."

    scene campo_cultivo2
    narr """El sonido provenía de una enorme bestia de metal que sobrevolaba por el campo espaciando un rocío turbio
    sobre este.

    Las flores del algodoncillo parecían un poco más marchitas después de recibir la brisa de la bestia de metal. Y
    [usuario] dudó si deberían comer de ellas."""
    menu:
        "Comer":
            play sound "audio/sonido/clic.mp3"
            jump comer_campo
        "No comer":
            play sound "audio/sonido/clic.mp3"
            jump no_comer_campo


################################################################################
label comer_campo:
    play music "audio/musica/triste_violin.mp3" loop fadein 1.0
    narr """Vacilante [usuario] se posó sobre un arbusto aún dudosa de comer.

    Sin embargo, algunas de sus compañeras se apresuraron a comer gustosas, pero...

    Tan pronto como bebieron el néctar cayeron al suelo en un profundo sueño del que jamás despertarán. Asustada
    [usuario] se alejó de la planta envenenada y la siguieron las mariposas que aún no probaban bocado.

    La bestia de metal había rociado veneno sobre las plantas rebeldes que rompían la armonía de las plantas
    cultivadas en hileras.

    Dolida por sus compañeras muertas, [usuario] aleteo lejos de ese campo y su bestia de metal, con las sobrevivientes
    a sus espaldas."""

    play sound "audio/sonido/papel.mp3"
    $ energia -= 10
    show screen menos_10_energia_info
    pause 2.0
    hide screen menos_10_energia_info

    play sound "audio/sonido/papel.mp3"
    $ num_mari -= 5
    show screen menos_5_mariposas_info
    pause 2.0
    hide screen menos_5_mariposas_info

    stop music fadeout 15.0
    play sound "audio/sonido/papel.mp3"
    call screen comer_campo_info


################################################################################
label no_comer_campo:
    narr """Observando una vez más el aspecto marchito de las flores de algodoncillo [usuario] decidió retroceder.

    Probablemente el rocío de la bestia de metal las había contaminado, por lo que dando media vuelta [usuario] y las
    otras mariposas se marcharon del campo."""

    stop music fadeout 4.0
    play sound "audio/sonido/papel.mp3"
    call screen no_comer_campo_info

label no_comer_campo2:
    play sound "audio/sonido/papel.mp3"
    show screen aldoncillo_pistas_info
    pause 3.0
    hide screen aldoncillo_pistas_info
    jump escena_4


################################################################################
label escena_4:
    scene bosque1 with fade
    narr "[usuario] se posó sobre la hoja de un árbol exhausta después de volar por un largo tiempo buscando comida."
    play music "audio/musica/musica_piano.mp3" loop fadein 2.0
    narr "En una hoja más arriba de donde está, una pequeña abeja la observó con curiosidad."
    abe "{i}Mariposita luces cansada {/i}"
    menu:
        "Interactuar con la abeja":
            play sound "audio/sonido/clic.mp3"
            jump hablar_abeja
        "Alejarse de la abeja":
            play sound "audio/sonido/clic.mp3"
            jump no_hablar_abeja


################################################################################
label hablar_abeja:
    narr """[usuario] la volteo a ver con ojos agotados y un rugido de su panza sonó en medio del silencio.

    La abeja la miró pensativa juntando sus patas delanteras y de repente se iluminó su expresión."""

    abe "{i}Ya sé, los tuyos comen de las flores de algodoncillo, ¿Verdad?{/i}"

    narr"[usuario] asintió."

    abe """{i}Cerca de aquí, donde brotan las torres de piedra hay plantas a sus alrededores, algunas son arbustos
    de algodoncillo llenos de flores con dulce néctar.{/i}

    {i}Anda vete con tus amigas a buscarlos.{/i}"""

    narr "[usuario] con renovada energía asintió en agradecimiento a la abeja y voló con sus compañeras hacia las
    torres de piedra."
    jump escena_5


################################################################################
label no_hablar_abeja:
    narr """[usuario] se sobresaltó al escuchar la voz y temerosa dejó la hoja en la que estaba, volando lejos
    de la abeja que solo la miraba con la palabra en la boca.

    Sus compañeras la siguieron de cerca."""
    jump escena_5


################################################################################
label escena_5:
    scene ciudad with fade
    narr """Las mariposas surcaron los cielos y poco a poco las grandes torres grises aparecieron frente a ellas.

    Y un poco más al este se asomaba lo que parecía ser una pradera verde.

    [usuario] debatió a dónde deberían ir cuando vio por el rabillo del ojo algo familiar cerca de las torres grises."""
    menu:
        "Examinar el objeto":
            play sound "audio/sonido/clic.mp3"
            jump examinar_objeto
        "No examinar el objeto":
            play sound "audio/sonido/clic.mp3"
            stop music fadeout 3.0
            jump no_examinar_objeto


################################################################################
label examinar_objeto:
    narr """Con la chispa de la curiosidad encendida [usuario] se acercó al objeto en el suelo.

    Era un ramito de flores de algodoncillo y más allá de él había un rastro de polen que se adentraba a la zona de
    las torres de piedra. [usuario] contempló si debía seguir el rastro o volar hacia la pradera."""

    menu:
        "Seguir el rastro de polen":
            play sound "audio/sonido/clic.mp3"
            jump seguir_rastro
        "No seguir el rastro de polen":
            play sound "audio/sonido/clic.mp3"
            stop music fadeout 3.0
            jump no_seguir_rastro


################################################################################
label seguir_rastro:
    scene algodoncillo with fade
    narr """Con su estómago gruñendo decidió seguir el polen esparcido por el suelo y se adentró a la ciudad de
    piedra junto con sus compañeras.

    Aunque había pocas plantas alrededor de las torres, entre ellas estaban las distintivas plantas de algodoncillo
    presumiendo sus coloridas flores en todo su esplendor.

    Emocionada [usuario] voló rápidamente hacia ellas y probó el dulce néctar hasta saciar su estómago.

    Sus compañeras siguieron su ejemplo y comieron contentas después de muchos percances."""

    play sound "audio/sonido/papel.mp3"
    $ energia = 100
    show screen energia_100_info
    pause 2.0
    hide screen energia_100_info

    scene algodoncillo_win with fade
    play sound "audio/sonido/win.mp3"
    call screen final_bueno_cap1_info


################################################################################
label no_seguir_rastro:
    "Temerosa de entrar a la ciudad de piedra, se alejó del objeto y voló con dirección a la pradera."
    jump escena_6


################################################################################
label no_examinar_objeto:
    "Con su estómago gruñendo decidió no perder el tiempo y voló lejos del objeto con dirección a la pradera."
    jump escena_6


################################################################################
label escena_6:
    scene pradera with fade
    play music "audio/musica/campo_de_cultivo.mp3" loop fadein 1.0
    narr """Cuando [usuario] y sus compañeras llegaron fueron recibidas por un paisaje lleno de pasto verde y brilloso,
    con algunos árboles de fondo, pero...

    No se veían plantas de algodoncillo a la vista...

    El pasto, aunque deslumbrante, había sido podado y los hierbajos habían sido arrancados y tirados aún lado para
    que se marchitaran y se hicieran uno con la tierra.

    Aunque [usuario] y sus compañeras volaron por toda la pradera no encontraron ni el más pequeño retoño de
    algodoncillo brotando del suelo.

    El sol poco a poco se iba escondiendo y con ello las esperanzas de encontrar comida. Así que abatidas volaron al
    árbol más cercano y se acurrucaron para dormir sintiendo los estragos del hambre."""

    play sound "audio/sonido/papel.mp3"
    $ energia -= 10
    show screen menos_10_energia_info
    pause 2.0
    hide screen menos_10_energia_info

    scene pradera_gameover with fade
    play sound "audio/sonido/game_over.mp3"
    call screen final_malo_cap1_info


label fin:
    return
