.. note::

    Bonjour et bienvenue dans la communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Plongez-vous dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et relevez les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprenez & Partagez** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et à des avant-premières.
    - **Remises spéciales** : Profitez de réductions exclusives sur nos nouveaux produits.
    - **Promotions festives et concours** : Participez à des tirages au sort et à des promotions durant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

Pour les utilisateurs de Windows
=======================================

Pour les utilisateurs de Windows 10 ou version supérieure, la connexion à distance à un Raspberry Pi peut être réalisée en suivant les étapes suivantes :

#. Recherchez ``powershell`` dans votre barre de recherche Windows. Faites un clic droit sur ``Windows PowerShell`` et sélectionnez ``Run as administrator`` .

    .. image:: img/powershell_ssh.png
        :align: center

#. Déterminez l'adresse IP de votre Raspberry Pi en tapant ``ping -4 <hostname>.local`` dans PowerShell.

    .. code-block::

        ping -4 raspberrypi.local

    .. image:: img/sp221221_145225.png
        :width: 550
        :align: center

    L'adresse IP du Raspberry Pi s'affichera une fois qu'il sera connecté au réseau.

    * Si le terminal affiche ``Ping request could not find host pi.local. Please check the name and try again.``, vérifiez que le nom d'hôte que vous avez saisi est correct.
    * Si vous ne parvenez toujours pas à récupérer l'adresse IP, vérifiez les paramètres réseau ou WiFi sur le Raspberry Pi.

#. Une fois l'adresse IP confirmée, connectez-vous à votre Raspberry Pi en utilisant ``ssh <username>@<hostname>.local`` ou ``ssh <username>@<IP address>``.

    .. code-block::

        ssh pi@raspberrypi.local

    .. warning::

        Si une erreur apparaît indiquant ``The term 'ssh' is not recognized as the name of a cmdlet...``, il se peut que votre système n'ait pas les outils SSH pré-installés. Dans ce cas, vous devrez installer OpenSSH manuellement en suivant :ref:`openssh_powershell`, ou utiliser un outil tiers comme décrit dans :ref:`login_windows`.

#. Un message de sécurité apparaîtra lors de votre première connexion. Saisissez ``yes`` pour continuer.

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. Entrez le mot de passe que vous avez défini précédemment. Notez que les caractères du mot de passe ne s'afficheront pas à l'écran, ce qui est une fonctionnalité de sécurité standard.

    .. note::
        L'absence de caractères visibles lors de la saisie du mot de passe est normale. Assurez-vous d'entrer le bon mot de passe.

#. Une fois connecté, votre Raspberry Pi est prêt pour des opérations à distance.

    .. image:: img/sp221221_140628.png
        :width: 550
        :align: center

