.. note::

    欢迎加入 SunFounder Raspberry Pi & Arduino & ESP32 爱好者社区（Facebook）！与全球的爱好者一起深入探索 Raspberry Pi、Arduino 和 ESP32 的奥秘。

    **为什么要加入？**

    - **专业支持**：在社区和团队的帮助下，快速解决售后问题和技术难题。
    - **学习与分享**：交流技巧与教程，提升您的技能。
    - **独家预览**：抢先了解新产品发布及独家内容。
    - **专属折扣**：享受最新产品的独家优惠。
    - **节日促销与赠品活动**：参与抽奖活动及节日促销。

    👉 准备好与我们一起探索和创造了吗？点击 [|link_sf_facebook|] 马上加入！

.. _py_avoid:

4. 避障功能
=============================

在本项目中，PiCar-X 将在向前移动时检测前方障碍物，当障碍物距离过近时，会自动改变前进方向。

**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 4.avoiding_obstacles.py

运行代码后，PiCar-X 将开始向前移动。

如果检测到前方障碍物距离小于 20cm，PiCar-X 会倒退。

如果检测到障碍物距离在 20 到 40cm 之间，它将向左转弯。

如果左转后方向没有障碍物或障碍物距离大于 25cm，PiCar-X 将继续向前移动。

**代码**

.. note::
    您可以 **修改/重置/复制/运行/停止** 以下代码。但在此之前，需进入源码路径，例如 ``picar-x/example``。修改代码后，您可以直接运行以查看效果。

.. raw:: html

    <run></run>

.. code-block:: python

    from picarx import Picarx
    import time
    
    POWER = 50
    SafeDistance = 40   # > 40 安全距离
    DangerDistance = 20 # > 20 && < 40 转弯,
                        # < 20 倒退
    
    def main():
        try:
            px = Picarx()
            # px = Picarx(ultrasonic_pins=['D2','D3']) # trigger, echo
           
            while True:
                distance = round(px.ultrasonic.read(), 2)
                print("distance: ",distance)
                if distance >= SafeDistance:
                    px.set_dir_servo_angle(0)
                    px.forward(POWER)
                elif distance >= DangerDistance:
                    px.set_dir_servo_angle(30)
                    px.forward(POWER)
                    time.sleep(0.1)
                else:
                    px.set_dir_servo_angle(-30)
                    px.backward(POWER)
                    time.sleep(0.5)
    
        finally:
            px.forward(0)
    
    
    if __name__ == "__main__":
        main()

**工作原理**

* 导入 Picarx 模块并初始化常量：

    此部分代码从 ``picarx`` 模块中导入 ``Picarx`` 类，这是控制 Picarx 机器人的核心。代码中定义了常量 ``POWER``、 ``SafeDistance`` 和 ``DangerDistance`` ，用于根据距离测量结果控制机器人运动。

    .. code-block:: python

        from picarx import Picarx
        import time

        POWER = 50
        SafeDistance = 40 # > 40 安全
        DangerDistance = 20 # > 20 && < 40 转弯,
        # < 20 倒退

* 主函数定义和超声波传感器读取：

    ``main`` 函数是控制 Picarx 机器人的核心逻辑。代码中创建了 ``Picarx`` 的实例，激活机器人的功能。程序进入无限循环，不断读取超声波传感器的距离数据，并根据数据控制机器人的运动。

    .. code-block:: python
        
        def main():
        try:
        px = Picarx()

            while True:
                distance = round(px.ultrasonic.read(), 2)
                # [其余逻辑]

* 基于距离的运动逻辑：

    根据超声波传感器读取的 ``distance`` 值控制机器人运动。如果 ``distance`` 大于 ``SafeDistance``，机器人向前移动；如果在 ``DangerDistance`` 和 ``SafeDistance`` 之间，机器人略微转向后前进；如果小于 ``DangerDistance``，机器人倒退并转向。

    .. code-block:: python

        if distance >= SafeDistance:
            px.set_dir_servo_angle(0)
            px.forward(POWER)
        elif distance >= DangerDistance:
            px.set_dir_servo_angle(30)
            px.forward(POWER)
            time.sleep(0.1)
        else:
            px.set_dir_servo_angle(-30)
            px.backward(POWER)
            time.sleep(0.5)

* 使用 'finally' 块保障安全：

    ``try...finally`` 块确保在程序中断或出现错误时停止机器人的动作，这是防止机器人失控的重要措施。

    .. code-block:: python
        
        try:
        # [控制逻辑]
        finally:
        px.forward(0)

* 脚本的执行入口：

    使用标准的 Python 入口点 ``if __name__ == "__main__":``，在脚本作为独立程序运行时执行主函数。

    .. code-block:: python
        
        if name == "main":
            main()

总结，代码通过 Picarx 模块控制机器人，利用超声波传感器测量距离，根据测量结果调整机器人的运动方向，并通过 ``finally`` 块确保安全运行。
