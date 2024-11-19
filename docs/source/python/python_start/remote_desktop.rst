.. note:: 

    您好，欢迎加入 SunFounder Raspberry Pi & Arduino & ESP32 爱好者社区！与其他爱好者一起深入探索 Raspberry Pi、Arduino 和 ESP32 的世界。

    **为什么加入我们？**

    - **专家支持**：通过我们的社区和团队帮助，解决售后问题和技术挑战。
    - **学习与分享**：交流技巧和教程，提升您的技能水平。
    - **独家预览**：抢先获得新产品公告和独家预览机会。
    - **特别折扣**：享受我们最新产品的专属折扣优惠。
    - **节日促销和赠品**：参与节日抽奖和特别促销活动。

    👉 准备好与我们一起探索和创造了吗？点击 [|link_sf_facebook|] 立即加入吧！

.. _remote_desktop:

通过远程桌面访问 Raspberry Pi
==================================================

如果您更倾向于使用图形用户界面（GUI）而非命令行访问，Raspberry Pi 支持远程桌面功能。本指南将引导您设置和使用 VNC（虚拟网络计算）进行远程访问。

我们推荐使用 `VNC® Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_。

**在 Raspberry Pi 上启用 VNC 服务**

VNC 服务在 Raspberry Pi OS 中已预装，但默认是禁用的。请按照以下步骤启用它：

#. 在 Raspberry Pi 的终端中输入以下命令：

    .. raw:: html

        <run></run>

    .. code-block:: 

        sudo raspi-config

#. 使用向下箭头键导航至 **Interfacing Options**，然后按下 **Enter**。

    .. image:: img/config_interface.png
        :align: center

#. 从选项中选择 **VNC**。

    .. image:: img/vnc.png
        :align: center

#. 使用箭头键选择 **<Yes>** -> **<OK>** -> **<Finish>**，完成 VNC 服务的激活。

    .. image:: img/vnc_yes.png
        :align: center

**通过 VNC Viewer 登录**

#. 在您的个人电脑上下载并安装 `VNC Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_。

#. 安装完成后，启动 VNC Viewer。在输入框中输入您的 Raspberry Pi 的主机名或 IP 地址，按下 Enter。

    .. image:: img/vnc_viewer1.png
        :align: center

#. 当出现提示时，输入您的 Raspberry Pi 用户名和密码，然后点击 **OK**。

    .. image:: img/vnc_viewer2.png
        :align: center

#. 几秒钟后，您将看到 Raspberry Pi OS 的桌面。现在，您可以打开终端开始输入命令。

    .. image:: img/bookwarm.png
        :align: center
