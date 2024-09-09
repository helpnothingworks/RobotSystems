.. note::

    Hola, bienvenido a la Comunidad de Entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. ¡Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 con otros entusiastas!

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo!

3. Fuente de Alimentación para Raspberry Pi (Importante)
============================================================

Carga
--------

Inserta el cable de la batería. A continuación, conecta el cable USB-C para cargar la batería.
Deberás utilizar tu propio cargador; recomendamos un cargador de 5V 3A, o bien puedes usar el cargador de tu smartphone habitual.

.. image:: img/BTR_IMG_1096.png

.. note::
    Conecta una fuente de alimentación externa de tipo C al puerto tipo C en el sombrero del robot; la batería comenzará a cargarse inmediatamente y se encenderá una luz indicadora roja.\
    Cuando la batería esté completamente cargada, la luz roja se apagará automáticamente.


Encendido
-------------

Enciende el interruptor de alimentación. Se iluminarán la luz indicadora de encendido y la luz indicadora del nivel de batería.

.. image:: img/BTR_IMG_1097.png

Espera unos segundos y escucharás un leve pitido, lo que indica que la Raspberry Pi ha arrancado correctamente.

.. note::
    Si ambas luces indicadoras del nivel de batería están apagadas, carga la batería.
    Cuando necesites sesiones prolongadas de programación o depuración, puedes mantener la Raspberry Pi operativa conectando el cable USB-C para cargar la batería simultáneamente.

Batería 18650
----------------

.. image:: img/3pin_battery.jpg

* VCC: Terminal positivo de la batería, aquí hay dos conjuntos de VCC y GND para aumentar la corriente y reducir la resistencia.
* Medio: Para equilibrar el voltaje entre las dos celdas y así proteger la batería.
* GND: Terminal negativo de la batería.

Este es un paquete de batería personalizado fabricado por SunFounder, que consta de dos baterías 18650 con una capacidad de 2000mAh. El conector es XH2.54 3P, que puede cargarse directamente después de insertarlo en el escudo.

**Características**

* Carga de batería: 5V/2A
* Salida de batería: 5V/5A
* Capacidad de batería: 3.7V 2000mAh x 2
* Duración de la batería: 90 minutos
* Tiempo de carga de la batería: 130 minutos
* Conector: XH2.54 3P

