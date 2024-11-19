.. note:: 

    您好，欢迎加入 SunFounder Raspberry Pi & Arduino & ESP32 爱好者社区！与其他爱好者一起深入探索 Raspberry Pi、Arduino 和 ESP32 的世界。

    **为什么加入我们？**

    - **专家支持**：通过我们的社区和团队帮助，解决售后问题和技术挑战。
    - **学习与分享**：交流技巧和教程，提升您的技能水平。
    - **独家预览**：抢先获得新产品公告和独家预览机会。
    - **特别折扣**：享受我们最新产品的专属折扣优惠。
    - **节日促销和赠品**：参与节日抽奖和特别促销活动。

    👉 准备好与我们一起探索和创造了吗？点击 [|link_sf_facebook|] 立即加入吧！

6. 启用 I2C 接口（重要）
========================================

我们将使用 Raspberry Pi 的 I2C 接口。在之前安装 ``robot-hat`` 模块时应该已经启用了该接口。为了确保一切正常，让我们检查是否已正确启用。

#. 输入以下命令：

    .. raw:: html

        <run></run>

    .. code-block:: 

        sudo raspi-config

#. 使用键盘上的向下箭头选择 **Interfacing Options**，然后按下 **Enter** 键。

    .. image:: img/image282.png
        :align: center

#. 然后选择 **I2C**。

    .. image:: img/image283.png
        :align: center

#. 使用键盘上的箭头键选择 **<Yes>** -> **<OK>**，完成 I2C 设置。

    .. image:: img/image284.png
        :align: center

#. 选择 **<Finish>** 后，会弹出一个提示，提醒您需要重新启动以使设置生效，选择 **<Yes>**。

    .. image:: img/camera_enable2.png
        :align: center
