define narr = Character("Narrador")
define abe = Character("Abeja")
define gall = Character("Gallina")

default num_mari = 400
default menos_mari = 0
default energia = 100
default menos_ener = 0
default genero = ""
default texto = ""
default etiqueta = ""

#Decisiones con tiempo
default timeout = 5.0
default rango_tiempo = 0
default time = 0

#Estilos - Mouse
define config.mouse = {
    "default" : [("images/cursor_puntero.png", 0, 0)],
    "say" : [("images/cursor_mariposa.png", 0, 0)]
}

################################################################################
label start:
    hide screen boton_estadisticas
    #Crear usuario
    scene fondo_bosque
    play sound "audio/sonido/notificacion.mp3"
    menu:
        "Elige el género de tu mariposa (Haz clic sobre una de las dos opciones.)"
        "Hembra":
            play sound "audio/sonido/clic.mp3"
            $ genero = True
            $ texto = "Las mariposas hembras tienen las rayas negras de sus alas más anchas que las mariposas machos."
        "Macho":
            play sound "audio/sonido/clic.mp3"
            $ genero = False
            $ texto = "Las mariposas machos tienen dos puntitos negros en las alas, uno en cada una, a diferencia de las mariposas hembras que no los tienen."

    $ etiqueta = "nombre_usuario"
    play sound "audio/sonido/papel.mp3"
    call screen genero_info

label nombre_usuario:
    $ usuario = renpy.input("Ingresa el nombre que le darás a tu mariposa y presiona ENTER")
    $ usuario = usuario.strip()
    if usuario == "":
        jump nombre_usuario

label hola:
    play sound "audio/sonido/notificacion.mp3"
    $ texto = "¡Hola " + usuario + "!"
    $ etiqueta = "escena_0"
    call screen final_cap_info

################################################################################
label escena_0:
    scene fondo_circulo with fade
    show screen danaus_info
    play sound "audio/sonido/notificacion.mp3"
    "[usuario] es el personaje principal de esta historia, de tus decisiones dependerá su supervivencia.
    (Presiona la tecla 'espacio' para avanzar o haz clic 'izquierdo' sobre la pantalla.)"
    "¡Suerte en esta nueva aventura!"
    hide screen danaus_info

    pause 1.0
    #Imagen de fondo
    scene intro with fade
    #Musica de fondo
    play music "audio/musica/Intro.mp3" loop fadein 2.0

    #Dialogo de Introducción
    narr """Desde hace mucho tiempo han existido.

    En algunas culturas se cree que son el alma de los seres queridos que regresan.

    En otras, son guerreros que vuelven después de haber muerto en batalla.

    Lo cierto, es que son un símbolo de transformación, pasan de huevo a oruga y de oruga a crisálida para
    convertirse finalmente en mariposa.

    Cambian durante toda su vida para poder extender sus alas y volar.

    Al final, el ciclo se vuelve a repetir...

    Y por junio, cuando los meses se acercan más al invierno nace la última generación de ese año.

    Y este año no será la excepción pues ya han salido de las crisálidas la nueva generación y se llaman..."""

    scene fondo_negro with fade
    centered "Matusalén: Mariposa Sagrada." (what_color="#ffffff")

    #Imagen de fondo del capitulo 1
    scene cap1
    #Parar musica con desvanecimiento de 3 s
    stop music fadeout 3.0
    #Mantener la imagen por 5 s
    pause 5

    scene hojas_algodoncillo with fade
    play music "audio/musica/Cap_1.mp3" volume 0.5 loop fadein 1.0
    narr """Cuando [usuario] salió de la crisálida, lo primero que vio fueron los tallos verdes y altos acompañados del
    follaje espeso que formaban las plantas de algodoncillo.

    Era el mismo escenario que vio antes de irse a dormir en su cálido capullo, pero...

    Ahora se sentía diferente.

    Y su cuerpo también era diferente."""

    scene a_crisalida
    narr """Apoyando sus seis patas en la hoja que le dio cobijo durante su transformación, movió sus alas y las extendió
    poco a poco.

    La sangre acumulada en su cuerpo se fue desplazando por sus alas y cuando terminó estas se mostraron en todo
    su esplendor.

    Fue una tarea ardua, que duró casi dos horas. [usuario] estaba exhausta... """

    scene mariposas_saliendo with fade
    narr "Y mirando alrededor se encontró con otras iguales a ella, aún aturdidas y cansadas por el cambio."

    scene mariposa_volando_hacia_mariposas
    narr "Al ser la primera en salir batió sus alas suavemente y se acercó a las otras mariposas mostrándoles cómo debían
    extender sus alas, estas agradecidas copiaron sus movimientos."

    play sound "audio/sonido/notificacion.mp3"
    $ texto = usuario + " tienes bajo tu cuidado a 400 mariposas Monarca" #Numero de huevecillos que puede llegar a poner una mariposa Monarca
    $ etiqueta = "escena_1"
    call screen final_cap_info


################################################################################
label escena_1:
    scene sol with fade
    show screen num_mariposas #item
    narr """Para cuando la última mariposa Monarca terminó de extender sus alas, el sol estaba en su punto más alto.

    [usuario] se debatió entre comer el néctar de las plantas que las protegieron durante su metamorfosis o extender
    sus alas y volar por los alrededores antes de que anocheciera."""

    play sound "audio/sonido/notificacion.mp3"
    menu:
        "Comer":
            play sound "audio/sonido/clic.mp3"
            jump comer_parque
        "Volar":
            play sound "audio/sonido/clic.mp3"
            jump volar


################################################################################
label comer_parque:
    scene mariposa_flor with fade
    narr "[usuario] se posó sobre una flor y bebió de su néctar, sus compañeras siguieron su ejemplo."
    scene mariposas_flor
    pause 1

    play sound "audio/sonido/papel.mp3"
    show screen barra_energia #item
    show screen energia_info
    pause 2.0
    hide screen energia_info
    jump escena_2


################################################################################
label volar:
    play sound "audio/sonido/papel.mp3"
    $ energia = 50
    show screen barra_energia #item
    show screen energia_info
    pause 2.0
    hide screen energia_info
    $ persistent.d1_volar.append(usuario)
    jump escena_2


################################################################################
label escena_2:
    $ texto = "La barra se llenará cuando comas, no dejes que la barra baje del 25 \% o las mariposas empezarán a morir por falta de energía."
    $ etiqueta = "escena_3"
    play sound "audio/sonido/papel.mp3"
    call screen info


################################################################################
label escena_3:
    scene hojas_algodoncillo
    narr """Los pequeños arbustos de algodoncillo han sido su alimento desde que eran larvas.

    Las hojas verdes y lechosas, que son venenosas para cualquier otro animal, para ellas son su mayor fuente de
    alimento y son las que pintan sus alas de colores naranjas y negros vibrantes pues ahí se esconden las
    toxinas del algodoncillo que han comido desde bebés.

    Dando a través de esos colores un claro mensaje, para sus depredadores, de lo tóxicas que son.

    Al ser el único alimento que [usuario] conocía desde que nació, decidió buscar más allá de lo que sus ojos
    alcanzaban a ver."""

    scene parque with fade

    narr """Y extendiendo sus alas se alzó tan alto como pudo y vio un mundo totalmente distinto.

    Plantas tan altas que llegaban hasta un manto azul que lo cubría todo y en el cual flotaban motitas blancas
    y esponjosas.

    Y grandes pilares grises se veían más allá de los árboles."""

    scene mariposa_volando_parque
    narr "[usuario] contempló emocionada estás rarezas y aleteando fuertemente sus alas exploró lo que había más allá
    de su pequeño hogar en el arbusto de algodoncillo."

    stop music fadeout 4.0
    narr "Sus compañeras la siguieron en armonía."

    scene campo_cultivo with fade
    play music "audio/musica/suspenso_suave.mp3" loop fadein 3.0
    narr """Después de merodear por un tiempo, las mariposas llegaron a un inmenso campo un tanto peculiar, pues las
    plantas se erigían en filas paralelas en perfecta simetría.

    Sin embargo, arbustos de algodoncillo y otras malezas brotaban aquí y allá rompiendo el orden entre las plantas.
    [usuario] contempló emocionada los arbustos de algodoncillo en flor, pero..."""

    play sound "audio/sonido/avion.mp3"
    narr "Antes de que pudiera volar hacia ellos, un estruendo se hizo presente en el campo."

    scene avioneta
    narr """El sonido provenía de una enorme bestia de metal que sobrevolaba por el campo espaciando un rocío turbio
    sobre este.

    Las flores del algodoncillo parecían un poco más marchitas después de recibir la brisa de la bestia de metal. Y
    [usuario] dudó si deberían comer de ellas."""

    play sound "audio/sonido/notificacion.mp3"
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

    scene flores_contaminadas1 with fade
    narr "Vacilante [usuario] se posó sobre un arbusto aun dudosa de comer."

    scene flores_contaminadas2
    narr "Sin embargo, algunas de sus compañeras se apresuraron a comer gustosas, pero..."

    scene mariposas_muertas_campo with fade
    narr "Tan pronto como bebieron el néctar cayeron al suelo en un profundo sueño del que jamás despertarían."


    scene campo_cultivo with fade
    narr """Asustada, [usuario] se alejó de la planta envenenada y la siguieron las mariposas que aún no probaban bocado.

    La bestia de metal había rociado veneno sobre las plantas rebeldes que rompían la armonía de las plantas
    cultivadas en hileras."""


    scene mariposas_volando_campo
    narr "Dolida por sus compañeras muertas, [usuario] aleteó lejos de ese campo y su bestia de metal, con las sobrevivientes
    a sus espaldas."

    play sound "audio/sonido/papel.mp3"
    $ energia -= 10
    $ menos_ener = 10
    show screen menos_energia_info
    pause 2.0
    hide screen menos_energia_info

    play sound "audio/sonido/papel.mp3"
    $ num_mari -= 20
    $ menos_mari = 20
    show screen menos_mariposas_info
    pause 2.0
    hide screen menos_mariposas_info

    stop music fadeout 15.0
    $ texto = "¿Sabías que?... El uso de plaguicidas, agroquímicos e insecticidas para actividades agrícolas y de control sanitario, han provocado una disminución del 58 \% del algodoncillo, lo que de 1999 a 2010 significó una reducción de 81 \% en la población de Mariposas Monarca."
    $ etiqueta = "escena_4"
    play sound "audio/sonido/papel.mp3"
    $ persistent.d2_comer_campo.append(usuario)
    call screen info


################################################################################
label no_comer_campo:
    scene mariposas_volando_campo
    narr """Observando una vez más el aspecto marchito de las flores de algodoncillo [usuario] decidió retroceder.

    Probablemente el rocío de la bestia de metal las había contaminado, por lo que dando media vuelta [usuario] y las
    otras mariposas se marcharon del campo."""

    stop music fadeout 4.0
    play sound "audio/sonido/papel.mp3"
    $ texto = "Las mariposas Monarca sólo ponen huevos en el algodoncillo y las orugas solo comen algodoncillo, lo que hace a esta planta crucial para la supervivencia de la población monarca. Los habitantes de E.U. y Canadá pueden ayudar a la sustentabilidad de las Monarcas si siembran algodoncillo en sus patios, macetas y jardineras."
    $ etiqueta = "no_comer_campo2"
    call screen info

label no_comer_campo2:
    play sound "audio/sonido/papel.mp3"
    $ texto = "Pistas para encontrar algodoncillo: Búscalo en jardineras"
    show screen pistas_info
    pause 3.0
    hide screen pistas_info
    jump escena_4


################################################################################
label escena_4:
    scene mariposa with fade
    narr "[usuario] se posó sobre la hoja de un árbol exhausta después de volar por un largo tiempo buscando comida."
    play music "audio/musica/musica_piano.mp3" loop fadein 2.0

    scene abeja
    narr "En una hoja más arriba de donde está, una pequeña abeja la observó con curiosidad."
    abe "{i}Mariposita luces cansada {/i}"

    play sound "audio/sonido/notificacion.mp3"
    menu:
        "Interactuar con la abeja":
            play sound "audio/sonido/clic.mp3"
            jump hablar_abeja
        "Alejarse de la abeja":
            play sound "audio/sonido/clic.mp3"
            jump no_hablar_abeja


################################################################################
label hablar_abeja:
    scene mariposa_abeja
    narr """[usuario] la volteó a ver con ojos agotados y un rugido de su panza sonó en medio del silencio.

    La abeja la miró pensativa juntando sus patas delanteras y de repente se iluminó su expresión."""

    abe "{i}Ya sé, los tuyos comen de las flores de algodoncillo, ¿Verdad?{/i}"

    narr"[usuario] asintió."

    abe """{i}Cerca de aquí, donde brotan las torres de piedra hay plantas a sus alrededores, algunas son arbustos
    de algodoncillo llenos de flores con dulce néctar.{/i}

    {i}Anda, vete con tus amigas a buscarlos.{/i}"""

    scene mariposas_volando_arbol
    narr "[usuario] con renovada energía asintió en agradecimiento a la abeja y voló con sus compañeras hacia las
    torres de piedra."
    jump escena_5


################################################################################
label no_hablar_abeja:
    scene mariposas_volando_arbol
    narr """[usuario] se sobresaltó al escuchar la voz y temerosa dejó la hoja en la que estaba, volando lejos
    de la abeja que solo la miraba con la palabra en la boca.

    Sus compañeras la siguieron de cerca."""
    jump escena_5


################################################################################
label escena_5:
    scene ciudad_pradera with fade
    narr """Las mariposas surcaron los cielos y poco a poco las grandes torres grises aparecieron frente a ellas.

    Y un poco más al este se asomaba lo que parecía ser una pradera verde.

    [usuario] debatió a dónde deberían ir cuando vio por el rabillo del ojo algo familiar cerca de las torres grises."""

    play sound "audio/sonido/notificacion.mp3"
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
    scene flor_polen
    narr """Con la chispa de la curiosidad encendida [usuario] se acercó al objeto en el suelo.

    Era un ramito de flores de algodoncillo y más allá de él había un rastro de polen que se adentraba a la zona de
    las torres de piedra. [usuario] contempló si debía seguir el rastro o volar hacia la pradera."""

    play sound "audio/sonido/notificacion.mp3"
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
    scene jardinera with fade
    narr """Con su estómago gruñendo decidió seguir el polen esparcido por el suelo y se adentró a la ciudad de
    piedra junto con sus compañeras.

    Aunque había pocas plantas alrededor de las torres, entre ellas estaban las distintivas plantas de algodoncillo
    presumiendo sus coloridas flores en todo su esplendor."""

    scene mariposa_flor
    narr "Emocionada [usuario] voló rápidamente hacia ellas y probó el dulce néctar hasta saciar su estómago."

    scene mariposas_flor
    narr "Sus compañeras siguieron su ejemplo y comieron contentas después de muchos percances."

    stop music fadeout 4.0

    play sound "audio/sonido/papel.mp3"
    $ energia = 100
    show screen energia_info
    pause 2.0
    hide screen energia_info

    scene mariposas_flor_win with fade
    $ texto = "Felicidades conseguiste que las mariposas encontraran comida."
    $ etiqueta = "escena_7"
    play sound "audio/sonido/win.mp3"
    call screen final_cap_info


################################################################################
label no_seguir_rastro:
    "Temerosa de entrar a la ciudad de piedra, se alejó del objeto y voló con dirección a la pradera."
    $ persistent.d4_no_seguir_rastro.append(usuario)
    jump escena_6


################################################################################
label no_examinar_objeto:
    "Con su estómago gruñendo decidió no perder el tiempo y voló lejos del objeto con dirección a la pradera."
    $ persistent.d3_no_examinar_objeto.append(usuario)
    jump escena_6


################################################################################
label escena_6:
    scene pradera with fade
    play music "audio/musica/campo_de_cultivo.mp3" loop fadein 1.0
    narr """Cuando [usuario] y sus compañeras llegaron fueron recibidas por un paisaje lleno de pasto verde y brilloso,
    con algunos árboles de fondo, pero...

    No se veían plantas de algodoncillo a la vista...

    El pasto, aunque deslumbrante, había sido podado y los hierbajos habían sido arrancados y tirados aún lado para
    que se marchitaran y se hicieran uno con la tierra."""

    scene a_pradera
    narr """Aunque [usuario] y sus compañeras volaron por toda la pradera no encontraron ni el más pequeño retoño de
    algodoncillo brotando del suelo.

    El sol poco a poco se iba escondiendo y con ello las esperanzas de encontrar comida. Así que abatidas volaron al
    árbol más cercano y se acurrucaron para dormir sintiendo los estragos del hambre."""

    stop music fadeout 4.0

    play sound "audio/sonido/papel.mp3"
    $ energia -= 15
    $ menos_ener = 15
    show screen menos_energia_info
    pause 2.0
    hide screen menos_energia_info

    scene pradera_gameover with fade
    $ texto = "Intenta tomar mejores decisiones en el próximo capítulo."
    $ etiqueta = "escena_7"
    play sound "audio/sonido/game_over.mp3"
    call screen final_cap_info


################################################################################
################################   CAPITULO 2   ################################
################################################################################
label escena_7:
    scene fondo_negro
    pause 1
    scene cap2
    pause 5

    scene mariposas_volando_cielo
    play music "audio/musica/piano_relax.mp3" loop fadein 1.0
    narr """[usuario] y compañía volaron por los alrededores, fueron de aquí y allá disfrutando del nuevo mundo que poco a poco
    iban conociendo ahora que podían volar, hasta que...

    Los días comenzaron a hacerse cada vez más cortos y el frío empezó a rozar ligeramente sus alas.

    Su estancia en Canadá, su país natal, estaba por terminar y [usuario] lo sabía."""

    scene sol with fade
    narr "Ella y sus compañeras debían volar siguiendo la calidez del sol hacia un lugar que nunca antes habían visto pero que en el
    fondo sabían que en dicho lugar los días perduraban y el sol entibiaba sus alas todos los días."

    $ texto = "La Monarca se considera una especie cosmopolita por su presencia en muchos lugares del mundo, aunque sólo en Norteamérica tiene lugar su extraordinario fenómeno de migración e hibernación. Las mariposas Monarcas viajan entre 50 y 100 millas por día y pueden tardar hasta dos meses en completar su viaje a los bosques de hibernación."
    $ etiqueta = "escena_7_2"
    play sound "audio/sonido/papel.mp3"
    call screen info

label escena_7_2:
    pause 1
    $ texto = "Sin embargo, este fenómeno está en peligro de extinción puesto que la población de mariposas Monarca Matusalén, la variante que realiza dicho fenómeno, ha disminuido drásticamente durante la última década."
    $ etiqueta = "escena_8"
    play sound "audio/sonido/papel.mp3"
    call screen info


################################################################################
label escena_8:
    scene granja_exterior with fade
    narr """Sin embargo, era un viaje largo lleno de riesgo e incertidumbre por lo que [usuario] dudó.

    Ahora estaban en un lugar seguro y habían encontrado suficiente alimento para algunos días más en una pequeña “granja ecológica”.

    Así que, [usuario] se preguntó si partir ahora, antes de que el frío las alcanzara o quedarse más tiempo en la comodidad que
    tanto les había costado encontrar."""

    play sound "audio/sonido/notificacion.mp3"
    menu:
        "Viajar":
            play sound "audio/sonido/clic.mp3"
            jump escena_viajar
        "Quedarse":
            play sound "audio/sonido/clic.mp3"
            jump escena_quedarse


label escena_viajar:
    scene mariposas_dejando_granja
    narr "Tras pensarlo varios minutos, decidió que era mejor partir ahora que arriesgarse a que el frío llegará, y extendiendo
    sus alas emprendió el vuelo con sus compañeras siguiéndola."

    stop music fadeout 4.0

    $ texto = "¿Sabías que?... Si las temperaturas al final de la temporada son demasiado frías, los músculos de vuelo de las monarcas no pueden calentarse lo suficiente, lo que les hace físicamente imposible volar. Los eventos climáticos extremos pueden desviar a las monarcas, impedirles avanzar o matarlas."
    $ etiqueta = "escena_9"
    play sound "audio/sonido/papel.mp3"
    call screen info


label escena_quedarse:
    stop music fadeout 4.0

    narr "[usuario] decidió permanecer unos días más en aquella granja junto con sus compañeras, sin embargo..."

    scene granja_exterior_mariposas with fade
    narr "Días después mientras dormían agazapadas en un árbol, las temperaturas comenzaron a descender, un escozor helado se arrastró
    por las alas de [usuario] haciéndola despertar de golpe."

    scene granja_exterior_mariposa_despierta
    play music "audio/musica/campo_de_cultivo.mp3" loop fadein 1.0
    narr """Miró a su alrededor y se dió cuenta de que el frío comenzaba a formar pequeños cristales de hielo en las hojas de los árboles.

    Asustada, despertó a sus compañeras para alertar las de la helada que se avecinaba."""

    scene mariposas_entrando_granja
    narr "Y sin perder tiempo buscó un lugar seguro para ellas encontrando un pequeño establo en las cercanías."

    scene granja_interior_gallinas with fade
    narr """Las mariposas entraron al establo con rapidez y se acurrucaron en los montones de paja que había en este.

    Una gallina vieja se despertó con el susurro de las alas de las mariposas y miró a [usuario] que estaba acurrucada en un
    montoncito de paja a su lado."""


    scene mariposa_hablando_gallina
    play sound "audio/sonido/gallina.mp3" volume 0.25
    gall "¿Pequeña te escondes del frío?"

    narr "[usuario] asintió cansada."

    gall "Ya veo, ¿Sabes? es raro ver a tu especie en estos días, por lo regular en esta época ya emigraron hacia el sur."

    narr "[usuario] la miró con curiosidad y la gallina prosiguió."

    gall "Por está época las heladas se hacen presentes y tu especie vuela hacia el sur donde el clima es más cálido... "

    narr "Así la gallina pasó toda la noche relatándole a la mariposa como veía, en años pasados, emigrar a las mariposas
    monarca a finales de septiembre."

    play sound "audio/sonido/gallina.mp3" volume 0.25
    gall """Hace mucho tiempo tu especie migraba en octubre porque el frío tardaba en llegar, pero de un tiempo para acá.

    Cuando el aire comenzó a contaminarse, el frío se hizo presente más temprano y tu especie a tenido que partir con más tiempo
    de anticipación"""

    narr "[usuario] la miró con tristeza."

    gall "¡Oh! parece que ya ha amanecido, ¿Por qué no emprendes tu viaje?"
    stop sound

    narr "[usuario] levantó la cabeza con emoción y cuando miró los primeros rayos del sol colándose por el granero se despidió
    de la gallina y les indicó a sus compañeras que era hora de partir."

    scene mariposas_muertas_hielo
    narr """Cuando salieron del gallinero observaron grandes capas blancas de hielo cubriendo los árboles y el pasto, pero eso no era
    todo...

    Había algo más...

    Entre esas capas de hielo yacían varias de sus compañeras que no pudieron refugiarse a tiempo.

    [usuario] con dolor se disculpó por no haber partido antes y sin volver a mirar a sus compañeras perdidas, voló junto a las
    demás comenzando con su viaje de migración."""

    $ num_mari -= 25
    $ menos_mari = 25
    play sound "audio/sonido/papel.mp3"
    show screen menos_mariposas_info
    pause 2.0
    hide screen menos_mariposas_info

    stop music fadeout 3.0
    $ texto = "¿Sabías que?... Si las temperaturas al final de la temporada son demasiado frías, los músculos de vuelo de las monarcas no pueden calentarse lo suficiente, lo que les hace físicamente imposible volar. Los eventos climáticos extremos pueden desviar a las monarcas, impedirles avanzar o matarlas."
    $ etiqueta = "escena_9"
    $ persistent.d1_quedarse.append(usuario)
    play sound "audio/sonido/papel.mp3"
    call screen info

################################################################################
label escena_9:
    scene mapa1

    play music "audio/musica/musica_piano.mp3" loop fadein 1.0
    narr """Las mariposas volaron del suroeste de Canadá al norte de Estados Unidos.

    Extendiendo sus alas y planearon como ningún otro organismo, dejándose llevar por el viento. Recorriendo así largos tramos sin
    gastar sus reservas de energía."""

    scene mariposas_flor
    $ energia = 100
    narr """Cuando estuvieron demasiado hambrientas hicieron paradas aquí y allá, y bebieron del néctar de las flores que encontraron en
    su camino.

    Dando así inicio a la polinización anual, que hacen las mariposas monarcas, entre las plantas de Canadá, Estados Unidos y
    México.

    Pues a lo largo de su viaje consumirían el néctar de diferentes flores para convertirlo en reservas energéticas que le
    permitirán sobrevivir a la hibernación, cuando no se alimenta."""

    stop music fadeout 5.0

    $ texto = "En su recorrido, de norte a sur y viceversa, la mariposa Monarca pasa por distintos ecosistemas trasladando polen de unos a otros en millones de plantas y flores en las diversas regiones de Canadá, Estados Unidos y México. Sin este aporte se podría llegar a afectar al mantenimiento de la biodiversidad de plantas silvestres, la estabilidad de los ecosistemas y el bienestar humano."
    $ etiqueta = "escena_10"
    play sound "audio/sonido/papel.mp3"
    call screen info

################################################################################
label escena_10:
    scene lluvia

    play music "audio/musica/mystical.mp3" loop fadein 2.0
    play sound "audio/sonido/lluvia.mp3" volume 0.1
    narr """Una tarde cuando [usuario] y sus compañeras atravesaban un bosque de robles ubicado en el centro de Estados Unidos el
    cielo comenzó a oscurecerse, y truenos retumbaron en lo alto, tomando por sorpresa a las mariposas.

    Puesto que toda la mañana el sol brilló en el cielo despejado, sin mencionar que no era época de lluvia."""

    narr """Aún así, no pasó mucho tiempo antes de que grandes gotas de agua cayeran sin cesar mojando las alas de una que otra mariposa
    impidiendo su vuelo.

    [usuario] buscó un lugar para refugiarse, sin embargo, era otoño y los árboles de roble dejaban caer sus hojas en esa época,
    dejando pocos lugares para refugiarse de la lluvia.

    [usuario] miró las opciones que tenía enfrente."""

    scene bosque_lluvia_opciones with fade
    pause 1.0

    play sound "audio/sonido/notificacion.mp3"
    menu:
        "Árbol sin hojas":
            play sound "audio/sonido/clic.mp3"
            jump escena_ArbolSinHojas
        "Árbol con pocas hojas":
            play sound "audio/sonido/clic.mp3"
            jump escena_ArbolConPocasHojas
        "Parada de autobús":
            play sound "audio/sonido/clic.mp3"
            jump escena_ParadaAutobus


label escena_ArbolSinHojas:
    play sound "audio/sonido/lluvia.mp3" volume 0.1
    scene arbol_sin_hojas with fade
    narr """Y eligió el gran árbol sin hojas.

    Las mariposas se posaron sobre este los más juntas posibles para guardar calor, pero la protección que ofrecía el árbol era
    poca y gran parte de las mariposas se vieron expuestas a la lluvia torrencial.

    Con las alas mojadas y el frío pasando entre ellas, se les entumió el cuerpo provocando que cayeran del árbol."""

    scene carretera_mariposas_muertas with fade
    narr "Y en el pasto mojado dormirían para nunca despertar."

    stop sound
    scene mariposas_volando_cielo
    narr "Al día siguiente, la lluvia había terminado y [usuario] y sus compañeras continuaron su viaje siendo un grupo más pequeño."

    $ num_mari -= 50
    $ menos_mari = 50
    play sound "audio/sonido/papel.mp3"
    show screen menos_mariposas_info
    pause 2.0
    hide screen menos_mariposas_info

    $ energia -= 25
    $ menos_ener = 25
    play sound "audio/sonido/papel.mp3"
    show screen menos_energia_info
    pause 2.0
    hide screen menos_energia_info

    $ persistent.d2_ArbolSinHojas.append(usuario)
    jump info_lluvia


label escena_ArbolConPocasHojas:
    play sound "audio/sonido/lluvia.mp3" volume 0.1
    scene arbol_pocas_hojas with fade
    narr """Y eligió un árbol que aún le quedaban unas cuantas hojas.
    Las mariposas se posaron sobre este los más juntas posibles para guardar calor, pero la protección que ofrecía el árbol no
    era suficiente y algunas mariposas se vieron expuestas a la lluvia torrencial.

    Con las alas mojadas y el frío pasando entre ellas, se les entumió el cuerpo provocando que cayeran del árbol"""

    scene carretera_mariposas_muertas with fade
    narr "Y en el pasto mojado dormirían para nunca despertar."

    stop sound
    scene mariposas_volando_cielo
    narr "Al día siguiente, la lluvia había terminado y [usuario] y sus compañeras continuaron su viaje, dejando atrás a sus compañeras
    que no pudieron sobrevivir a la lluvia."

    $ num_mari -= 25
    $ menos_mari = 25
    play sound "audio/sonido/papel.mp3"
    show screen menos_mariposas_info
    pause 2.0
    hide screen menos_mariposas_info

    $ energia -= 15
    $ menos_ener = 15
    play sound "audio/sonido/papel.mp3"
    show screen menos_energia_info
    pause 2.0
    hide screen menos_energia_info

    $ persistent.d3_ArbolConPocasHojas.append(usuario)
    jump info_lluvia


label escena_ParadaAutobus:
    play sound "audio/sonido/lluvia.mp3" volume 0.1
    scene parada_bus with fade
    narr """Y eligió una rara estructura de madera a un lado del camino de piedra, era vieja pero las protegerá de la lluvia.

    Las mariposas se posaron debajo del techo lo más juntas posibles para guardar calor, y así pasaron la noche sin problemas."""

    stop sound
    scene mariposas_volando_cielo
    narr "Al día siguiente, la lluvia había terminado y [usuario] y sus compañeras continuaron su viaje."

    jump info_lluvia


label info_lluvia:
    stop music fadeout 4.0
    $ texto = "¿Sabías que?... Los fuertes vientos y las lluvias pueden impedir que se muevan las mariposas Monarcas reteniéndolas durante días. Si los vientos son demasiado fuertes en una dirección, es posible que las Monarcas no puedan viajar tan lejos."
    $ etiqueta = "escena_11"
    play sound "audio/sonido/papel.mp3"
    call screen info


################################################################################
label escena_11:

    scene mapa2
    play music "audio/musica/musica_piano.mp3" loop fadein 4.0
    narr """Las mariposas volaron por Texas rumbo a México, haciendo una que otra parada para descansar y comer, continuando así
    con la polinización que esto conlleva.

    Conforme se iban acercando a los estados de Coahuila, Nuevo León y Tamaulipas el clima frío y húmedo que estuvieron sintiendo
    desde que partieron comenzó a cambiar por uno seco y caluroso.

    Ellas no lo sabían pero era aún más caluroso que años anteriores y al igual que las frías heladas o lluvias torrenciales, el
    abrumador calor les afectaba agotando las con más rapidez."""

    scene frontera with fade
    $ energia = 100
    narr "Por lo que tomaron descanso para alimentarse en la frontera de México y de esta manera habían polinizado entre sí a las
    plantas nativas de los 3 países."

################################################################################
label info_cambios_climaticos:
    $ texto = "El cambio climático, debido al calentamiento global, puede alterar significativamente la migración, la hibernación y la reproducción de las mariposas Monarcas. Los inviernos más fríos y húmedos pueden ser letales para las monarcas, mientras que los veranos más calurosos y secos alteran sus hábitats en el norte."
    $ etiqueta = "info_cambios_climaticos2"
    play sound "audio/sonido/papel.mp3"
    call screen info

label info_cambios_climaticos2:
    stop music fadeout 10.0
    pause 1
    $ texto = "Las prioridades para la conservación de la Monarca afectada por el clima deben incluir la restauración y el aumento de la extensión del hábitat con especies apropiadas de algodoncillo y fuentes de néctar. También es esencial mantener y restaurar los hábitats de hibernación, reducir el uso de herbicidas y pesticidas y abordar los problemas relacionados con el cambio de uso de la tierra. "
    $ etiqueta = "escena_12"
    play sound "audio/sonido/papel.mp3"
    call screen info


################################################################################
################################   CAPITULO 3   ################################
################################################################################
label escena_12:
    scene fondo_negro
    pause 1
    scene cap3
    pause 5

    play music "audio/musica/mystical.mp3" loop fadein 4.0
    scene mariposas_montañas with fade
    narr """Las mariposas continuaron con su viaje, pasando por Saltillo.

    Sin embargo, el suelo de México era muy diferente al de Estados Unidos o Canadá, pues grandes montañas rocosas se esparcían por
    todo el lugar provocando que las corrientes de aire descendieran y con ello las mariposas también tenían que hacerlo."""

    scene carretera_montañas with fade
    narr"Volando a una altura peligrosamente baja por lo que bestias de metal terrestre podían arrollarlas."

    play music "audio/musica/tension.mp3" loop fadein 15.0
    $ texto = "Esquiva los autos antes de que se llene la barra de tiempo para sobrevivir."
    play sound "audio/sonido/papel.mp3"
    show screen pistas_info
    pause 3.0
    hide screen pistas_info
    $ menos_mari = 0

################################################################################
label auto_1:

    scene auto1
    play sound "audio/sonido/auto1.mp3"
    $ timeout = 5
    $ etiqueta = "timeout_1"
    show screen choice_time

    menu:
        "Izquierda":
            play sound "audio/sonido/clic.mp3"
            hide screen choice_time
            $ num_mari -= 10
            $ menos_mari += 10
            $ persistent.d1_auto1.append(usuario)
            jump auto_2
        "Derecha":
            play sound "audio/sonido/clic.mp3"
            hide screen choice_time
            jump auto_2

    label timeout_1:
        $ num_mari -= 20
        $ menos_mari += 20
        $ persistent.d1_auto1.append(usuario)
        jump auto_2

################################################################################
label auto_2:
    pause 1.0

    scene auto2 with fade
    play sound "audio/sonido/auto2.mp3"
    $ timeout = 4
    $ etiqueta = "timeout_2"
    show screen choice_time

    menu:
        "Arriba":
            play sound "audio/sonido/clic.mp3"
            hide screen choice_time
            jump auto_3
        "Abajo":
            play sound "audio/sonido/clic.mp3"
            hide screen choice_time
            $ num_mari -= 10
            $ menos_mari += 10
            $ persistent.d2_auto2.append(usuario)
            jump auto_3

    label timeout_2:
        $ num_mari -= 20
        $ menos_mari += 20
        $ persistent.d2_auto2.append(usuario)
        jump auto_3

################################################################################
label auto_3:
    pause 1.0

    scene auto3 with fade
    play sound "audio/sonido/auto4.mp3"
    $ timeout = 4
    $ etiqueta = "timeout_3"
    show screen choice_time

    menu:
        "Derecha":
            play sound "audio/sonido/clic.mp3"
            hide screen choice_time
            jump auto_4
        "Abajo":
            play sound "audio/sonido/clic.mp3"
            hide screen choice_time
            $ num_mari -= 10
            $ menos_mari += 10
            $ persistent.d3_auto3.append(usuario)
            jump auto_4

    label timeout_3:
        $ num_mari -= 20
        $ menos_mari += 20
        $ persistent.d3_auto3.append(usuario)
        jump auto_4

################################################################################
label auto_4:
    pause 1.0

    scene auto4 with fade
    play sound "audio/sonido/auto3.mp3"
    $ timeout = 3
    $ etiqueta = "timeout_4"
    show screen choice_time

    menu:
        "Derecha":
            play sound "audio/sonido/clic.mp3"
            hide screen choice_time
            $ num_mari -= 10
            $ menos_mari += 10
            $ persistent.d4_auto4.append(usuario)
            jump auto_5_6
        "Izquierda":
            play sound "audio/sonido/clic.mp3"
            hide screen choice_time
            jump auto_5_6

    label timeout_4:
        $ num_mari -= 20
        $ menos_mari += 20
        $ persistent.d4_auto4.append(usuario)
        jump auto_5_6

################################################################################
label auto_5_6:
    pause 1.0

    scene auto5y6 with fade
    play sound "audio/sonido/auto3.mp3"
    $ timeout = 3
    $ etiqueta = "timeout_5_6"
    show screen choice_time

    menu:
        "Arriba":
            play sound "audio/sonido/clic.mp3"
            hide screen choice_time
            jump auto_7
        "En medio":
            play sound "audio/sonido/clic.mp3"
            hide screen choice_time
            $ num_mari -= 10
            $ menos_mari += 10
            $ persistent.d5_auto5y6.append(usuario)
            jump auto_7

    label timeout_5_6:
        $ num_mari -= 20
        $ menos_mari += 20
        $ persistent.d5_auto5y6.append(usuario)
        jump auto_7

################################################################################
label auto_7:
    pause 1.0

    scene auto7 with fade
    play sound "audio/sonido/auto4.mp3"
    $ timeout = 2
    $ etiqueta = "timeout_7"
    show screen choice_time

    menu:
        "Abajo":
            play sound "audio/sonido/clic.mp3"
            hide screen choice_time
            $ num_mari -= 10
            $ menos_mari += 10
            $ persistent.d6_auto7.append(usuario)
            jump escena_13
        "Izquierda":
            play sound "audio/sonido/clic.mp3"
            hide screen choice_time
            jump escena_13

    label timeout_7:
        $ num_mari -= 20
        $ menos_mari += 20
        $ persistent.d6_auto7.append(usuario)
        jump escena_13

################################################################################
label escena_13:

    scene carretera_montañas
    stop music fadeout 10
    narr "Cuando llegaron al estado de Zacatecas el suelo era más uniforme por lo que las mariposas podían seguir tranquilas su
    viaje. "

    play sound "audio/sonido/papel.mp3"
    show screen menos_mariposas_info
    pause 2.0
    hide screen menos_mariposas_info

    if menos_mari > 0:
        $ texto = "¿Sabías que?... Las Mariposas Monarca se ven obligadas a pasar por algunos tramos carreteros con alto flujo vehicular. Las altas velocidades de circulación permitidas y el desconocimiento de los ciudadanos ocasionan una gran mortandad de ejemplares durante los días más intensos de la migración. Esto da lugar a una disminución considerable de la población migratoria."
        $ etiqueta = "final_malo_cap3"
        play sound "audio/sonido/papel.mp3"
        call screen info
    else:
        $ texto = "Se han colocado letreros en carretera con avisos e imágenes de la mariposa monarca para que los automovilistas sepan que pasa por ahí y reduzcan la velocidad a 60 km/h."
        $ etiqueta = "final_bueno_cap3"
        play sound "audio/sonido/papel.mp3"
        call screen info

################################################################################
label final_malo_cap3:
    scene carretera_montañas_gameover with fade
    $ texto = "Intenta tomar mejores decisiones en el próximo capítulo."
    $ etiqueta = "escena_14"
    play sound "audio/sonido/game_over.mp3"
    call screen final_cap_info

label final_bueno_cap3:
    scene carretera_montañas_win with fade
    $ texto = "Felicidades esquivaste todos los autos"
    $ etiqueta = "escena_14"
    play sound "audio/sonido/win.mp3"
    call screen final_cap_info


################################################################################
################################   CAPITULO 4   ################################
################################################################################
label escena_14:
    scene fondo_negro
    pause 1
    scene cap4
    pause 5

    scene mapa3
    play music "audio/musica/piano_relax.mp3" loop fadein 4.0
    narr "Las mariposas volaron por los estados de San Luis Potosí, Aguascalientes, Querétaro, Guanajuato y Jalisco,
    después de viajar por dos meses, finalmente habían llegado a la frontera entre Michoacán y el Estado de México."

    scene bosque_lejano with fade
    narr """[usuario] y sus compañeras se sentían atraídas a un punto específico de ese lugar, sabían que ahí se
    encontraban los bosques donde hibernaron algunos de sus ancestros.

    Eran bosques densos en donde se protegerían de los vientos y de los cambios abruptos de temperatura y humedad, ideales para
    pasar el invierno sin ningún problema y por lo que valía la pena el gran viaje que realizaban."""
    stop music fadeout 4.0

    scene campo_cultivo with fade
    play music "audio/musica/Campo_de_cultivo.mp3" loop fadein 4.0
    play sound "audio/sonido/granja.mp3" volume 0.25
    narr """Sin embargo, conforme más se acercaban solo veían zonas ganaderas y campos de cultivo, las mariposas se
    encontraban cansadas y aún no lograban encontrar los bosques donde podían descansar.

    Por lo que [usuario] se preguntó si deberían quedarse en ese lugar agitado y ruidoso para hibernar."""

    play sound "audio/sonido/notificacion.mp3"
    menu:
        "Quedarse":
            play sound "audio/sonido/clic.mp3"
            jump quedarse_zona_ganadera
        "Seguir volando":
            play sound "audio/sonido/clic.mp3"
            jump irse_zona_ganadera


label quedarse_zona_ganadera:
    narr """Tras unos momentos de analizar las situación, [usuario] decidió que deberían asentarse en ese lugar, sin
    embargo, no había árboles donde pudieran acurrucarse y dormir.

    Además el ruido que hacían los animales y las personas era molesto y no las dejaba dormir haciendo imposible que
    se pudieran quedar ahí."""

    scene mariposas_volando_campo_cultivo_ganadero
    narr "Por lo que [usuario] decidió que era mejor seguir volando hasta encontrar el bosque con las pocas energías que les
    quedaban."

    $ energia -= 30
    $ menos_ener = 30
    play sound "audio/sonido/papel.mp3"
    show screen menos_energia_info
    pause 2.0
    hide screen menos_energia_info

    $ persistent.d1_zona_ganadera.append(usuario)
    jump info_zona_ganadera


label irse_zona_ganadera:
    scene mariposas_volando_campo_cultivo_ganadero
    narr "Tras unos momentos de analizar la situación, [usuario] decidió que lo mejor era seguir volando con la energía
    que aún les quedaba, puesto que ese no era un lugar apto para hibernar."

    play sound "audio/sonido/papel.mp3"
    $ texto = "Pistas para encontrar los bosques de hibernación: Busca árboles de oyamel"
    show screen pistas_info
    pause 4.0
    hide screen pistas_info
    jump info_zona_ganadera


label info_zona_ganadera:
    stop sound
    stop music fadeout 4.0
    $ texto = "¿Sabías que?... El aumento de las áreas de cultivo y la intensificación de las prácticas agrícolas y ganaderas han resultado en la reducción del hábitat reproductivo. Se calcula que estas prácticas han provocado una disminución de 58% en la abundancia de algodoncillo, situación que de 1999 a 2010 se tradujo en una reducción de 81% en la abundancia de Mariposas Monarca."
    $ etiqueta = "escena_15"
    play sound "audio/sonido/papel.mp3"
    call screen info

################################################################################
label escena_15:
    scene cultivo_aguacate with fade
    play music "audio/musica/suspenso_suave.mp3" loop fadein 4.0
    narr """Volando más arriba de la zona montañosa, encontraron un raro bosque de árboles de aguacate, plantados en
    hileras simétricas y con el sueño desprovisto de malezas.

    Aunque nunca antes habían estado en los bosques de hibernación, [usuario] sabía que este no era el bosque que ellas
    buscaban, pero el cansancio ya pesaba sobre sus alas y ese bosque era un lugar tentador para descansar."""

    play sound "audio/sonido/notificacion.mp3"
    menu:
        "Quedarse":
            play sound "audio/sonido/clic.mp3"
            jump quedarse_aguacates
        "Seguir volando":
            play sound "audio/sonido/clic.mp3"
            jump irse_aguacates


label quedarse_aguacates:
    scene cultivo_aguacate_mariposas with fade
    play music "audio/musica/triste_violin.mp3" loop
    narr """[usuario] decidió que sería bueno hibernar ahí, no había nadie más cerca por lo que no se preocupaban por el
    ruido, además los árboles les darían cobijo, por lo tanto pasaron la noche acurrucadas debajo de las hojas.

    Pero..."""

    scene cultivo_aguacate_gente with fade
    play sound "audio/sonido/personas_enojadas.mp3" volume 0.25
    narr "Por la mañana del día siguiente, los agricultores arremetieron furiosos contra ellas, echándolas de los
    árboles, lastimadas y desorientadas las mariposas siguieron volando."
    stop sound

    stop music fadeout 15
    $ energia -= 20
    $ menos_ener = 20
    play sound "audio/sonido/papel.mp3"
    show screen menos_energia_info
    pause 2.0
    hide screen menos_energia_info

    play sound "audio/sonido/papel.mp3"
    $ num_mari -= 50
    $ menos_mari = 50
    show screen menos_mariposas_info
    pause 2.0
    hide screen menos_mariposas_info

    $ persistent.d2_aguacates.append(usuario)
    jump info_aguacates


label irse_aguacates:
    narr "Como ese extraño bosque no era apto para hibernar, [usuario] decidió que lo mejor era seguir volando."


label info_aguacates:
    stop music fadeout 4.0
    $ texto = "¿Sabías que?... Hoy en día diversas áreas forestales aledañas al hábitat de hibernación se encuentran fuertemente presionadas para convertirse en zonas de cultivo de aguacate. Este cambio de uso de suelo altera drásticamente el paisaje y ocasiona la pérdida de servicios ecosistémicos como la provisión de agua y la regulación de la temperatura, esenciales durante la hibernación de las Mariposas Monarca."
    $ etiqueta = "escena_16"
    play sound "audio/sonido/papel.mp3"
    call screen info

################################################################################
label escena_16:
    scene arboles_talados with fade
    play music "audio/musica/triste.mp3" loop fadein 4.0
    narr "Siguiendo su camino por las montañas de la sierra madre, las mariposas vieron a lo lejos una pila de troncos
    cortados."

    play sound "audio/sonido/notificacion.mp3"
    menu:
        "Examinar de cerca":
            play sound "audio/sonido/clic.mp3"
            jump examinar_troncos
        "No examinar":
            play sound "audio/sonido/clic.mp3"
            jump escena_17

label examinar_troncos:
    $ texto = "¿Sabías que?... En 2014, la superficie degradada de los bosques de hibernación fue de 2 179 hectáreas, de las cuales 2 057 hectáreas fueron afectadas por tala ilegal."
    $ etiqueta = "escena_17"
    play sound "audio/sonido/papel.mp3"
    call screen info

################################################################################
label escena_17:
    scene bosque_talado with fade
    narr """Más allá de la pila de árboles se encontraban los restos de lo que había sido un bosque.

    Troncos de árboles que habían sido cortados al ras del suelo y este a su vez erosionado e infértil, no era más
    que la cáscara vacía de lo que alguna vez fue un lugar lleno de vida."""

    play sound "audio/sonido/notificacion.mp3"
    menu:
        "Examinar de cerca":
            play sound "audio/sonido/clic.mp3"
            jump examinar_lugar
        "No examinar":
            play sound "audio/sonido/clic.mp3"
            jump escena_18


label examinar_lugar:
    $ texto = "¿Sabías que?... Las primeras evidencias de deforestación (tala ilegal) en la Reserva de la Biósfera Mariposa Monarca (RBMM) se reportaron en 2003 y la superficie talada se duplicó hasta 2007. Sin embargo, de 2008 a 2012, la intensidad de la tala disminuyó, gracias al esfuerzo, trabajo y coordinación de autoridades, los dueños de los territorios (ejidos y comunidades) y organizaciones de la sociedad civil, al punto de llegarse a declarar tala cero en 2012."
    $ etiqueta = "escena_18"
    play sound "audio/sonido/papel.mp3"
    call screen info

################################################################################
label escena_18:
    scene mariposas_volando_bosque_talado
    narr "Volando por sobre ese lugar, [usuario] divisó a lo lejos un objeto extraño."

    stop music fadeout 30
    play sound "audio/sonido/notificacion.mp3"
    menu:
        "Examinar de cerca":
            play sound "audio/sonido/clic.mp3"
            jump examinar_objeto_tala_ilegal
        "No examinar":
            play sound "audio/sonido/clic.mp3"
            jump no_examinar_objeto_tala_ilegal

label examinar_objeto_tala_ilegal:
    scene motosierra
    narr "Era una extraña herramienta de metal con picos filosos."

    $ texto = "¿Sabías que?... Durante la temporada 2014–2015, se registraron algunos sitios talados ilegalmente, lo que dio lugar al establecimiento de operativos en sitios estratégicos, consistentes en la revisión de los vehículos que transportaban madera y la inspección de los aserradores de la región para garantizar la procedencia legal de la madera."
    $ etiqueta = "examinar_objeto_tala_ilegal2"
    play sound "audio/sonido/papel.mp3"
    call screen info

label examinar_objeto_tala_ilegal2:
    narr "Una vez saciada su curiosidad, [usuario] continuó con su camino."
    jump escena_19


label no_examinar_objeto_tala_ilegal:
    narr "[usuario] lo ignoró y continuó con su camino."
    jump escena_19


################################################################################
label escena_19:
    scene puestos_artesanias with fade
    play music "audio/musica/piano_happy.mp3" loop fadein 5.0
    narr """Después de recorrer toda la zona devastada, vislumbraron a lo lejos las copas de los árboles de oyamel y con
    renovado vigor volaron.

    Hasta que poco a poco las pequeñas copas de los árboles que habían visto a lo lejos, se convirtieron en grandes y
    majestuosas árboles frente a ellas

    Habían llegado al bosque de hibernación."""


    stop music fadeout 5.0
    $ texto = "La conservación de los bosques en la Región de la Mariposa Monarca proporciona beneficios locales, regionales, nacionales e internacionales. Además de los importantes beneficios económicos actuales y potenciales del bosque para las comunidades y propietarios de la región, incluyendo el turismo, la conservación de estos ecosistemas es crucial para muchas especies de fauna y flora. "
    $ etiqueta = "escena_19_2"
    play sound "audio/sonido/papel.mp3"
    call screen info

label escena_19_2:
    $ texto = "Cuando viajes por la región de la Monarca, o si vives en ella, reporta los casos de tala ilegal y cualquier tipo de atentado en contra de las especies de los bosques de hibernación. Te puedes comunicar a la Procuraduría Federal de Protección al Ambiente (PROFEPA), así como a la Dirección de la Reserva de la Biosfera Mariposa Monarca(RBMM)."
    $ etiqueta = "escena_20"
    play sound "audio/sonido/papel.mp3"
    call screen info


################################################################################
################################   CAPITULO 5   ################################
################################################################################
label escena_20:
    scene fondo_negro
    pause 1
    scene cap5
    pause 5

    scene puestos_artesanias with fade
    play music "audio/musica/piano_happy.mp3" loop fadein 5.0
    play sound "audio/sonido/personas_caminando.mp3" volume 0.25
    narr "A las afueras del bosque habían bulliciosos visitantes y alegres vendedores de artesanías muy semejantes
    a ellas."

    scene mariposas_volando_turistas
    narr "[usuario] y sus compañeras revolotearon hasta la entrada del bosque siendo observadas por esos ojos
    curiosos."
    stop sound

    $ texto = "Actualmente, muchos pobladores de la región han sido beneficiados por el turismo que visita las mariposas. Durante la temporada de hibernación, gente de las comunidades y de localidades cercanas recibe ingresos por conceptos como el alojamiento y transporte de turistas, ingreso a las colonias de hibernación, la venta de artesanías y de alimentos."
    $ etiqueta = "escena_21"
    play sound "audio/sonido/papel.mp3"
    call screen info


################################################################################
label escena_21:
    scene arboles_orillas_bosque with fade
    narr "[usuario] analizó si debían hibernar en los árboles de las afueras del bosque o adentrarse más."

    play sound "audio/sonido/notificacion.mp3"
    menu:
        "Quedarse":
            play sound "audio/sonido/clic.mp3"
            jump quedarse_afuera_bosque
        "Adentrarse al bosque":
            play sound "audio/sonido/clic.mp3"
            jump adentrarse_bosque

label quedarse_afuera_bosque:
    stop music fadeout 30
    scene arboles_orillas_bosque_mariposas with fade
    narr "Exhausta por el largo viaje decido que deberían hibernar ahí, sin embargo, el ruido de las personas
    alrededor perturbó su sueño, viéndose obligadas a adentrarse más en el bosque."

    $ energia -= 25
    $ menos_ener = 25
    play sound "audio/sonido/papel.mp3"
    show screen menos_energia_info
    pause 2.0
    hide screen menos_energia_info

    $ texto = "¿Sabías que?... Las mariposas Monarca permanecen en estado de hibernación durante los meses de diciembre, enero y parte de febrero. El exceso de ruido las altera e interrumpe su reposo, las hace gastar energía y reduce las posibilidades de que sobrevivan en el vuelo de regreso."
    $ etiqueta = "escena_22"
    $ persistent.d1_quedarse_afuera_bosque.append(usuario)
    play sound "audio/sonido/papel.mp3"
    call screen info

label adentrarse_bosque:
    narr "Después de unos segundos de contemplación decidió que lo mejor era adentrarse al bosque y encontrar un lugar
    tranquilo para hibernar."

    stop music fadeout 4.0
    $ texto = "Se recomienda que los turistas permanezcan en silencio durante su estancia en el santuario."
    $ etiqueta = "escena_22"
    play sound "audio/sonido/papel.mp3"
    call screen info


################################################################################
label escena_22:
    scene mariposas_volando_camino
    play music "audio/musica/musica_piano.mp3" loop fadein 4.0
    narr """En la entrada del bosque había un ancho camino que se ramificaba en diferentes direcciones, desvaneciéndose a lo lejos.

    [usuario] decidió seguir el camino principal para profundizar más en el bosque con sus compañeras detrás de ella."""

    $ texto = "El turismo no planificado erosiona el suelo por los diferentes senderos que se van abriendo en cada temporada para seguir el movimiento de las colonias de mariposas a través del bosque."
    $ etiqueta = "escena_22_2"
    play sound "audio/sonido/papel.mp3"
    call screen info

label escena_22_2:
    pause 1
    $ texto = "Para evitar la degradación del suelo por esta causa, los turistas deben seguir los senderos establecidos durante su recorrido."
    $ etiqueta = "escena_23"
    play sound "audio/sonido/papel.mp3"
    call screen info


################################################################################
label escena_23:
    narr "Después de unos minutos llegaron al final del camino, ahí [usuario] se preguntó si deberían hibernar en el
    árbol a las orillas del camino o ir más allá donde no existía un camino y los árboles estaban rodeados de maleza."

    play sound "audio/sonido/notificacion.mp3"
    menu:
        "Quedarse":
            play sound "audio/sonido/clic.mp3"
            jump quedarse_orilla_camino
        "Adentrarse más al bosque":
            play sound "audio/sonido/clic.mp3"
            jump seguir_adentrandose_bosque

label quedarse_orilla_camino:
    scene mariposas_bosque_camino with fade
    stop music fadeout 4.0
    narr "Eligiendo hibernar ahí se acurrucaron en las hojas de los árboles."

    play music "audio/musica/Campo_de_cultivo.mp3" loop fadein 4.0
    scene mariposas_personas
    narr """Pero, no pasó mucho tiempo para cuando algunos turistas entraron al bosque y al verlas en los árboles cercanos
    intentaron tocarlas y juguetear con ellas interrumpiendo su dulce sueño.

    Sin más remedio volaron buscando un lugar alejado de los turistas."""

    $ energia -= 25
    $ menos_ener = 25
    play sound "audio/sonido/papel.mp3"
    show screen menos_energia_info
    pause 2.0
    hide screen menos_energia_info

    stop music fadeout 4.0
    $ texto = "¿Sabías que?... Las alas de las mariposas Monarca están formadas por miles de escamas que son muy sensibles al tacto y se desprenden con facilidad. Cuando una persona las agarra pierden algunas escamas que las protegen y en consecuencia quedan más expuestas a todos los factores ambientales (frío, luz y viento) que ponen en riesgo su vida. Es similar a una quemadura de tercer grado en humanos."
    $ etiqueta = "escena_24"
    $ persistent.d2_quedarse_orilla_camino.append(usuario)
    play sound "audio/sonido/papel.mp3"
    call screen info

label seguir_adentrandose_bosque:
    scene mariposas_volando_entre_bosque
    narr "Tras pensar detenidamente decidió seguir volando en lo profundo del bosque donde los caminos no podían
    llegar."

    stop music fadeout 4.0
    $ texto = "Los turistas deben respetar los límites de acceso para la observación de las colonias de mariposa Monarca y no deben tocarlas."
    $ etiqueta = "escena_24"
    play sound "audio/sonido/papel.mp3"
    call screen info


################################################################################
label escena_24:
    scene bosque_hibernación_final with fade
    play music "audio/musica/Cap_1.mp3" loop fadein 4.0
    narr """[usuario] y sus compañeras volaron hasta que pronto dieron con un área del bosque donde otras mariposas
    Monarcas ya revoloteaban por ahí.

    Las condiciones de esta área eran las adecuadas y plantas silvestres florecían por doquier, proporcionando a las
    mariposas de comida."""

    scene mariposas_volando_bosque
    narr "[usuario] de inmediato supo que habían llegado al lugar correcto y alentó a sus compañeras a reunirse con
    las otras mariposas que habían llegado antes."

    $ energia = 100
    narr "Sin perder tiempo todas comieron hasta saciarse y tranquilamente volaron a los árboles donde pasarían todo el
    invierno dormidas."

    scene mariposa_despertando
    narr """En febrero, cuando los rayos del sol comienzan a ser más cálidos y el frío invierno se va disipando.

    [usuario] abrió sus ojos y extendió sus alas para revolotear por el lugar hasta encontrar una pareja con la que se
    reproducirá para crear descendencia."""

    scene mariposas_volando_bosque_final
    narr "Y cuando llegue la primavera, también llegará la hora de partir de regreso a Estados Unidos."
    if genero:
        narr """Sin embargo, este viaje solo lo harán [usuario] y las otras hembras con los huevecillos fecundados que
        se convertirán en la próxima generación.

        Mientras los machos caen al suelo sin energía y cierran sus ojos por última vez."""
        jump escena_24_2
    else:
        narr """Sin embargo, este viaje solo lo harán las hembras con los huevecillos fecundados que se convertirán
        en la próxima generación.

        Mientras [usuario] y los otros machos caen al suelo sin energía y cierran sus ojos por última vez."""
        jump escena_24_2

label escena_24_2:
    $ texto = "Los turistas no pueden llevarse las mariposas Monarca, incluso si están muertas, debido a que estas  se convierten en alimento de ratones y aves que consumen su abdomen por la grasa que contienen. La gran cantidad de cadáveres de mariposas Monarca en los santuarios genera una alta concentración de sustancias químicas. Actualmente, los investigadores estudian la posibilidad de que esta alta concentración ayude a las Monarca a ubicar los sitios de hibernación."
    $ etiqueta = "escena_24_3"
    play sound "audio/sonido/papel.mp3"
    call screen info

label escena_24_3:
    pause 1
    stop music fadeout 15
    $ texto = "Cuando visites la Reserva de la Biósfera Mariposa Monarca sigue las reglas que te indiquen las autoridades ambientales y guías turísticos."
    $ etiqueta = "escena_25"
    play sound "audio/sonido/papel.mp3"
    call screen info


################################################################################
label escena_25:
    show screen boton_estadisticas

    if num_mari < 200:
        jump final_malo
    else:
        jump final_bueno


################################################################################
label final_malo:
    $ texto = "Además de las causas de mortandad vistas a lo largo de esta historieta, la mariposa Monarca también se ve afectada por depredadores, parásitos, enfermedades, incendios forestales, contaminación y desecación de los cuerpos de agua dulce, entre otras causas más. Por lo cual es importante tomar conciencia de todos los obstáculos a los que tiene que sobrevivir este pequeño insecto. "
    $ etiqueta = "final_malo_2"
    play sound "audio/sonido/papel.mp3"
    call screen info

label final_malo_2:
    $ texto = "La mayoría de las mariposas a tu cuidado murieron."
    $ etiqueta = "final_malo_3"
    play sound "audio/sonido/papel.mp3"
    call screen final_cap_info

label final_malo_3:
    pause 1
    scene final_malo with fade
    $ texto = "PERDISTE"
    $ etiqueta = "final_juego"
    play sound "audio/sonido/game_over.mp3"
    call screen final


################################################################################
label final_bueno:
    scene mapa4
    play music "audio/musica/final.mp3" loop fadein 4.0
    if genero:
        narr "[usuario] y las otras mariposas sobrevivientes volaron de regreso a Estados Unidos."
    else:
        narr "Las mariposas sobrevivientes, entre ellas la mariposa que cargaba con los huevecillos fecundados por
        [usuario], volaron de regreso a Estados Unidos."

    narr "En donde, después de 9 meses de vida y habiendo recorrido aproximadamente 5000 km."

    scene huevos
    narr """Buscaría una planta de algodoncillo para poner sus huevecillos, los cuales comenzarían un nuevo ciclo de vida."""

    stop music fadeout 2.0
    scene final_bueno with fade
    $ texto = "¡GANASTE!"
    $ etiqueta = "final_juego"
    play sound "audio/sonido/win.mp3"
    play music "audio/sonido/aplausos.mp3" noloop
    call screen final

label final_juego:
    return
