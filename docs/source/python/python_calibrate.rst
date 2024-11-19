.. note::

    欢迎加入 SunFounder Raspberry Pi & Arduino & ESP32 爱好者社区（Facebook）！与全球的爱好者一起深入探索 Raspberry Pi、Arduino 和 ESP32 的奥秘。

    **为什么要加入？**

    - **专业支持**：在社区和团队的帮助下，快速解决售后问题和技术难题。
    - **学习与分享**：交流技巧与教程，提升您的技能。
    - **独家预览**：抢先了解新产品发布及独家内容。
    - **专属折扣**：享受最新产品的独家优惠。
    - **节日促销与赠品活动**：参与抽奖活动及节日促销。

    👉 准备好与我们一起探索和创造了吗？点击 [|link_sf_facebook|] 马上加入！

.. _py_calibrate:

0. 校准 PiCar-X
=================================

校准电机和舵机
---------------------------

由于 PiCar-X 安装过程中可能存在偏差，或者舵机本身存在局限性，某些舵机角度可能会稍有倾斜，
因此可以对其进行校准。

当然，如果您认为安装非常完美且无需校准，可以跳过本章。

#. 运行 ``calibration.py``。

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/picar-x/example/calibration
        sudo python3 calibration.py

#. 运行代码后，终端会显示以下界面：

    .. image:: img/calibrate1.png

#. 按 ``R`` 键测试 3 个舵机是否正常工作。使用 ``1``、 ``2`` 或 ``3`` 键选择舵机后，再按 ``R`` 键测试对应舵机。

#. 按数字键 ``1`` 选择前轮舵机，然后按 ``W/S`` 键调整前轮方向，使其尽量保持正前方且不偏左或偏右。

    .. image:: img/calibrate2.png

#. 按数字键 ``2`` 选择 **水平舵机**，然后按 ``W/S`` 键调整云台水平，使其正对前方且不倾斜左右。

    .. image:: img/calibrate3.png

#. 按数字键 ``3`` 选择 **俯仰舵机**，然后按 ``W/S`` 键调整云台俯仰角度，使其正对前方且不向上或向下倾斜。

    .. image:: img/calibrate4.png

#. 如果在安装过程中电机接线发生了反转，您可以按 ``E`` 键测试小车是否可以正常向前移动。如果不能，使用数字键 ``4`` 和 ``5`` 选择左右电机，然后按 ``Q`` 键校准旋转方向。

    .. image:: img/calibrate6.png

#. 校准完成后，按 ``空格键`` 保存校准参数。根据提示输入 ``y`` 确认，最后按 ``Ctrl+C`` 退出程序完成校准。

    .. image:: img/calibrate5.png


校准灰度模块
---------------------------

由于环境条件和光线情况的不同，灰度模块的预设参数可能无法达到最佳效果。
通过此程序，您可以对参数进行微调以获得更好的性能。


#. 在浅色地板上贴一条约 15 厘米长的黑色电工胶带。将 PiCar-X 放置在胶带上，使其跨越胶带。此时，灰度模块的中间传感器应正对胶带，而两侧传感器应悬空在浅色地面上。

#. 运行 ``grayscale_calibration.py``。

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/picar-x/example/calibration
        sudo python3 grayscale_calibration.py

#. 运行代码后，终端会显示以下界面：

    .. image:: img/calibrate_g1.png

#. 按 ``Q`` 键开始灰度校准。您会看到 PiCar-X 轻微向左和向右移动。在此过程中，三个传感器应至少一次扫过电工胶带。

#. 在 "threshold value" 区域，您将看到三组明显不同的数值，而 "line reference" 将显示两组中间值，分别表示每组数值的平均值。

    .. image:: img/calibrate_g2.png

#. 接下来，将 PiCar-X 悬空（或放置在悬崖边缘）并按下 ``E`` 键，您会发现 "cliff reference" 的值也会相应更新。

    .. image:: img/calibrate_g3.png

#. 确认所有数值准确无误后，按 ``空格键`` 保存数据。然后按 ``Ctrl+C`` 退出程序。
