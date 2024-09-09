.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete más en Raspberry Pi, Arduino y ESP32 junto con otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas técnicos y de posventa con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Accede anticipadamente a anuncios de nuevos productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones especiales en días festivos.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

Para usuarios de Windows
==========================

Para los usuarios de Windows 10 o superior, el inicio de sesión remoto en una Raspberry Pi se puede lograr a través de los siguientes pasos:

#. Busca ``powershell`` en el cuadro de búsqueda de Windows. Haz clic derecho en ``Windows PowerShell`` y selecciona ``Ejecutar como administrador``.

    .. image:: img/powershell_ssh.png
        :align: center

#. Determina la dirección IP de tu Raspberry Pi escribiendo ``ping -4 <hostname>.local`` en PowerShell.

    .. code-block::

        ping -4 raspberrypi.local

    .. image:: img/sp221221_145225.png
        :width: 550
        :align: center

    La dirección IP de la Raspberry Pi se mostrará una vez que esté conectada a la red.

    * Si la terminal muestra ``Ping request could not find host pi.local. Please check the name and try again.``, verifica que el nombre del host que has introducido sea correcto.
    * Si aún no puedes obtener la dirección IP, revisa la configuración de red o WiFi en la Raspberry Pi.

#. Una vez confirmada la dirección IP, inicia sesión en tu Raspberry Pi usando ``ssh <username>@<hostname>.local ``ssh <username>@<IP address>``.

    .. code-block::

        ssh pi@raspberrypi.local

    .. warning::

        Si aparece un error indicando ``The term 'ssh' is not recognized as the name of a cmdlet...``, es posible que tu sistema no tenga las herramientas SSH instaladas. En este caso, deberás instalar manualmente OpenSSH siguiendo :ref:`openssh_powershell`, o utilizar una herramienta de terceros como se describe en :ref:`login_windows`.

#. Aparecerá un mensaje de seguridad en tu primer inicio de sesión. Introduce ``yes`` para continuar.

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. Introduce la contraseña que estableciste previamente. Ten en cuenta que los caracteres de la contraseña no se mostrarán en pantalla, lo cual es una característica de seguridad estándar.

    .. note::
        La ausencia de caracteres visibles al escribir la contraseña es normal. Asegúrate de ingresar la contraseña correctamente.

#. Una vez conectado, tu Raspberry Pi está lista para operaciones remotas.

    .. image:: img/sp221221_140628.png
        :width: 550
        :align: center
