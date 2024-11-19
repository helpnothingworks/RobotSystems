.. note:: 

    您好，欢迎加入 SunFounder Raspberry Pi & Arduino & ESP32 爱好者社区！与其他爱好者一起深入探索 Raspberry Pi、Arduino 和 ESP32 的世界。

    **为什么加入我们？**

    - **专家支持**：通过我们的社区和团队帮助，解决售后问题和技术挑战。
    - **学习与分享**：交流技巧和教程，提升您的技能水平。
    - **独家预览**：抢先获得新产品公告和独家预览机会。
    - **特别折扣**：享受我们最新产品的专属折扣优惠。
    - **节日促销和赠品**：参与节日抽奖和特别促销活动。

    👉 准备好与我们一起探索和创造了吗？点击 [|link_sf_facebook|] 立即加入吧！

.. _openssh_powershell:

通过 Powershell 安装 OpenSSH
===================================

当您尝试使用 ``ssh <username>@<hostname>.local``（或 ``ssh <username>@<IP address>``）连接到 Raspberry Pi 时，出现以下错误信息：

    .. code-block::

        ssh: The term 'ssh' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
        spelling of the name, or if a path was included, verify that the path is correct and try again.


这意味着您的计算机系统版本较旧，没有预装 `OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_。您需要按照以下教程手动安装。

#. 在 Windows 桌面的搜索框中输入 ``powershell``，右键点击 ``Windows PowerShell``，并从出现的菜单中选择 ``以管理员身份运行``。

    .. image:: img/powershell_ssh.png
        :align: center

#. 使用以下命令安装 ``OpenSSH.Client``。

    .. code-block::

        Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

#. 安装完成后，您将看到以下输出：

    .. code-block::

        Path          :
        Online        : True
        RestartNeeded : False

#. 使用以下命令验证安装情况。

    .. code-block::

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. 此时系统会显示 ``OpenSSH.Client`` 已成功安装。

    .. code-block::

        Name  : OpenSSH.Client~~~~0.0.1.0
        State : Installed

        Name  : OpenSSH.Server~~~~0.0.1.0
        State : NotPresent

    .. warning:: 
        如果未出现上述提示，这意味着您的 Windows 系统仍然过于陈旧，建议安装第三方 SSH 工具，例如 :ref:`login_windows`。

#. 现在，重启 PowerShell 并继续以管理员身份运行。在此状态下，您可以使用 ``ssh`` 命令登录到 Raspberry Pi，系统会提示您输入之前设置的密码。

    .. image:: img/powershell_login.png