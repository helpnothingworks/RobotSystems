.. _py_cliff:

6. 悬崖检测
===========================

让我们为 PiCar-X 增加一些自我保护意识，让它学会使用自身的灰度模块避免冲下悬崖。

在本示例中，小车将处于休眠状态。如果您将它推到悬崖边缘，它会紧急唤醒，
然后倒退，并说出“危险”。

**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 6.cliff_detection.py
    

**代码**

.. note::
    您可以 **修改/重置/复制/运行/停止** 以下代码。但在此之前，需进入源码路径，例如 ``picar-x/example``。修改代码后，您可以直接运行以查看效果。

.. raw:: html

    <run></run>

.. code-block:: python

    from picarx import Picarx
    from time import sleep
    from robot_hat import TTS

    tts = TTS()
    tts.lang("en-US")

    px = Picarx()
    # px = Picarx(grayscale_pins=['A0', 'A1', 'A2'])
    # 手动修改参考值
    px.set_cliff_reference([200, 200, 200])

    current_state = None
    px_power = 10
    offset = 20
    last_state = "safe"

    if __name__=='__main__':
        try:
            while True:
                gm_val_list = px.get_grayscale_data()
                gm_state = px.get_cliff_status(gm_val_list)
                # print("悬崖状态是:  %s" % gm_state)

                if gm_state is False:
                    state = "safe"
                    px.stop()
                else:
                    state = "danger"   
                    px.backward(80)
                    if last_state == "safe":
                        tts.say("danger")
                        sleep(0.1)
                last_state = state

        finally:
            px.stop()
            print("stop and exit")
            sleep(0.1)

**工作原理**

检测悬崖的功能如下：

* ``get_grayscale_data()``：此方法直接输出从右到左的三个传感器读数。区域越亮，获得的数值越大。

* ``get_cliff_status(gm_val_list)``：此方法比较三个探头的读数并输出结果。如果结果为 True，则表示检测到小车前方存在悬崖。
