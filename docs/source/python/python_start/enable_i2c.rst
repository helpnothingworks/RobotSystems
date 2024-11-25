6. 启用 I2C 接口（重要）
========================================

我们将使用 Raspberry Pi 的 I2C 接口。在之前安装 ``robot-hat`` 模块时应该已经启用了该接口。为了确保一切正常，让我们检查是否已正确启用。

#. 输入以下命令：

    .. raw:: html

        <run></run>

    .. code-block:: 

        sudo raspi-config

#. 使用键盘上的向下箭头选择 **Interfacing Options** ，然后按下 **Enter** 键。

    .. image:: img/image282.png
        :align: center

#. 然后选择 **I2C**。

    .. image:: img/image283.png
        :align: center

#. 使用键盘上的箭头键选择 **<Yes>** ->  **<OK>** ，完成 I2C 设置。

    .. image:: img/image284.png
        :align: center

#. 选择 **<Finish>** 后，会弹出一个提示，提醒您需要重新启动以使设置生效，选择 **<Yes>** 。

    .. image:: img/camera_enable2.png
        :align: center
