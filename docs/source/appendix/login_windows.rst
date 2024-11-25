.. _login_windows:

PuTTY
=========================

如果您是 Windows 用户，可以使用一些 SSH 工具。在这里，我们推荐 `PuTTY <https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html>`_。

**步骤 1**

下载 PuTTY。

**步骤 2**

打开 PuTTY，点击左侧树状结构中的 **Session** 。在 **Host Name (or IP address)** 下的文本框中输入树莓派的 IP 地址，在 **Port** 中输入 **22** （默认端口为 22）。

.. image:: img/image25.png
    :align: center

**步骤 3**

点击 **Open**。注意，当您首次使用 IP 地址登录树莓派时，可能会出现安全提醒。
直接点击 **Yes** 即可。

**步骤 4**

当 PuTTY 窗口提示 \"**login as:**\" 时，输入 \"**pi**\"（树莓派的用户名），
然后输入 **password**: \"raspberry\"（默认密码，如果您未更改）。

.. note::

    输入密码时，窗口中不会显示字符，这是正常现象。只需输入正确的密码即可。
    
    如果 PuTTY 显示 inactive，说明连接已中断，需要重新连接。
    
.. image:: img/image26.png
    :align: center

**步骤 5**


现在，树莓派已经成功连接，可以进行下一步操作。
