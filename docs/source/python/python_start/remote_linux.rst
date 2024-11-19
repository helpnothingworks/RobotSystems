.. note::

    欢迎加入 SunFounder Raspberry Pi & Arduino & ESP32 爱好者 Facebook 社区！与全球的爱好者一起深入探索 Raspberry Pi、Arduino 和 ESP32 的无限可能。

    **加入我们的理由？**

    - **专业支持**：在社区和团队的帮助下解决售后问题及技术难题。
    - **学习与分享**：交换技能提升技巧的秘籍和教程。
    - **新品预览**：抢先获取新产品发布和独家预览。
    - **专属折扣**：享受我们最新产品的独家优惠。
    - **节日促销与赠品活动**：参与赠品抽奖及节日促销活动。

    👉 准备好与我们一起探索和创造了吗？点击 [|link_sf_facebook|] 马上加入！

Linux/Unix 用户指南
==========================

#. 找到并打开 Linux/Unix 系统中的 **终端**。

#. 确保您的 Raspberry Pi 已连接到同一网络。通过输入以下命令验证连接状态： ``ping <hostname>.local``。例如：

    .. code-block::

        ping raspberrypi.local

    如果 Raspberry Pi 已连接到网络，您将看到其 IP 地址。

    * 如果终端显示类似 ``Ping request could not find host pi.local. Please check the name and try again.`` 的消息，请仔细检查输入的主机名。
    * 如果仍无法获取 IP 地址，请检查 Raspberry Pi 的网络或 WiFi 设置。

#. 使用以下命令启动 SSH 连接：``ssh <username>@<hostname>.local`` 或 ``ssh <username>@<IP address>``。例如：

    .. code-block::

        ssh pi@raspberrypi.local

#. 首次登录时，您会看到一条安全提示消息。输入 ``yes`` 继续。

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. 输入您之前设置的密码。请注意，为了安全起见，输入时密码字符不会显示。

    .. note::
        终端中不显示密码字符是正常现象。只需确保输入正确的密码即可。

#. 登录成功后，您的 Raspberry Pi 已连接，您可以开始进行下一步操作。
