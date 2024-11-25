4. 设置您的 Raspberry Pi
============================

如果您有屏幕
-------------------------

.. note:: 安装在机器人上的 Raspberry Pi ZERO 不便于连接屏幕，请使用无屏幕的设置方法。

如果您有屏幕，操作 Raspberry Pi 会非常简单。



**所需组件**

* Raspberry Pi
* 电源适配器
* Micro SD 卡
* 屏幕电源适配器
* HDMI 线
* 屏幕
* 鼠标
* 键盘

#. 插入鼠标和键盘。

#. 将屏幕连接到 Raspberry Pi 的 HDMI 接口，并确保屏幕已插入电源并打开。

    .. note::

        如果您使用的是 Raspberry Pi 4，请将屏幕连接到 HDMI0（靠近电源接口的端口）。

#. 使用电源适配器为 Raspberry Pi 供电。

#. 几秒钟后，Raspberry Pi OS 的桌面将显示。现在，您可以打开终端开始输入命令。

    .. image:: img/bookwarm.png
        :align: center

如果您没有屏幕
--------------------------

如果您没有显示器，可以远程登录 Raspberry Pi。

**所需组件**

* Raspberry Pi
* 电源适配器
* Micro SD 卡

您可以使用 SSH 命令打开 Raspberry Pi 的 Bash shell。Bash 是 Linux 的默认标准 shell，用户在使用 Unix/Linux 时主要通过 shell 执行指令。大多数任务都可以通过 shell 完成。

如果您对使用命令窗口访问 Raspberry Pi 不满意，还可以通过远程桌面功能，使用图形界面（GUI）轻松管理 Raspberry Pi 上的文件。

请参考下方针对不同系统的详细教程：

.. toctree::

    remote_macosx
    remote_windows
    remote_linux
    remote_desktop

