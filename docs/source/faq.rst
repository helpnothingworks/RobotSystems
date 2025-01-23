.. note::

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. ¡Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas!

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones especiales.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

FAQ
===========================

P1: Después de instalar Ezblock OS, ¿el servo no gira a 0°?
-------------------------------------------------------------------

1) Verifica si el cable del servo está correctamente conectado y si la fuente de alimentación del Robot HAT está encendida.
2) Presiona el botón de Reinicio.
3) Si ya ejecutaste el programa en Ezblock Studio, el programa personalizado para el P11 ya no estará disponible. Puedes consultar la imagen a continuación para escribir manualmente un programa en Ezblock Studio que ajuste el ángulo del servo a 0°.

.. image:: img/faq_servo.png

P2: Al usar VNC, ¿me aparece un mensaje indicando que no se puede mostrar el escritorio en este momento?
--------------------------------------------------------------------------------------------------------------

En la Terminal, escribe ``sudo raspi-config`` para cambiar la resolución.

P3: ¿Por qué a veces el servo regresa a la posición media sin razón aparente?
----------------------------------------------------------------------------------------------

Cuando el servo está bloqueado por una estructura u objeto y no puede alcanzar su posición deseada, entra en modo de protección de apagado para evitar que el exceso de corriente lo queme.

Después de un periodo de corte de energía, si no se envía ninguna señal PWM al servo, éste volverá automáticamente a su posición original.

P4: ¿Dónde puedo encontrar un tutorial detallado sobre el Robot HAT?
---------------------------------------------------------------------------

Puedes encontrar un tutorial completo sobre el Robot HAT aquí, incluyendo información sobre su hardware y API.

* |link_robot_hat|

P5: Sobre el cargador de batería
-------------------------------------------------------------------

Para cargar la batería, simplemente conecta una fuente de alimentación Type-C de 5V/2A al puerto de alimentación del Robot Hat. No es necesario encender el interruptor de alimentación del Robot Hat durante la carga.
También puedes usar el dispositivo mientras cargas la batería.

.. image:: img/robot_hat_pic.png
    :align: center
    :width: 500

Durante la carga, la energía de entrada es amplificada por el chip de carga para cargar la batería y, al mismo tiempo, alimentar el convertidor DC-DC para uso externo, con una potencia de carga de aproximadamente 10W.
Si el consumo de energía externa se mantiene alto durante un período prolongado, la batería puede complementar el suministro de energía, de manera similar a usar un teléfono mientras se carga. Sin embargo, ten en cuenta la capacidad de la batería para evitar que se agote por completo durante el uso y la carga simultáneos.

P6: ¿La cámara no funciona? 
-----------------------------------------------------

Si la cámara no se muestra o se muestra incorrectamente, sigue estos pasos de solución de problemas:

#. Asegúrate de que el cable FPC de la cámara esté conectado de manera segura. Se recomienda reconectar la cámara y luego encender el dispositivo.

.. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="_static/video/rpi_connect1.mp4" type="video/mp4">
               Tu navegador no admite la etiqueta de video.
           </video>
       </div>

2. Usa el siguiente comando para verificar si la cámara es reconocida.

.. code-block::

    libcamera-hello
