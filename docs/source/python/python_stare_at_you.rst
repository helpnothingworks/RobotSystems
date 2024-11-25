.. _py_stare:

8. 注视你
==========================================

本项目基于 :ref:`py_computer_vision` 项目，增加了人脸检测算法。

当您出现在摄像头前时，它会识别您的脸部，并调整云台将您的脸保持在画面的中心。

您可以通过浏览器访问 ``http://<您的 IP>:9000/mjpg`` 查看画面。

**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 8.stare_at_you.py

代码运行后，小车的摄像头将始终注视着您的脸。

**代码**

.. code-block:: python

    from picarx import Picarx
    from time import sleep
    from vilib import Vilib

    px = Picarx()

    def clamp_number(num,a,b):
        return max(min(num, max(a, b)), min(a, b))

    def main():
        Vilib.camera_start()
        Vilib.display()
        Vilib.face_detect_switch(True)
        x_angle =0
        y_angle =0
        while True:
            if Vilib.detect_obj_parameter['human_n']!=0:
                coordinate_x = Vilib.detect_obj_parameter['human_x']
                coordinate_y = Vilib.detect_obj_parameter['human_y']
                
                # 调整云台角度以跟踪目标
                x_angle +=(coordinate_x*10/640)-5
                x_angle = clamp_number(x_angle,-35,35)
                px.set_cam_pan_angle(x_angle)

                y_angle -=(coordinate_y*10/480)-5
                y_angle = clamp_number(y_angle,-35,35)
                px.set_cam_tilt_angle(y_angle)

                sleep(0.05)

            else :
                pass
                sleep(0.05)

    if __name__ == "__main__":
        try:
            main()
        
        finally:
            px.stop()
            print("stop and exit")
            sleep(0.1)

**工作原理**

以下代码段位于 ``while True`` 循环中，用于使摄像头跟踪人脸。

.. code-block:: python

    while True:
        if Vilib.detect_obj_parameter['human_n']!=0:
            coordinate_x = Vilib.detect_obj_parameter['human_x']
            coordinate_y = Vilib.detect_obj_parameter['human_y']
            
            # 调整云台角度以跟踪目标
            x_angle +=(coordinate_x*10/640)-5
            x_angle = clamp_number(x_angle,-35,35)
            px.set_cam_pan_angle(x_angle)

            y_angle -=(coordinate_y*10/480)-5
            y_angle = clamp_number(y_angle,-35,35)
            px.set_cam_tilt_angle(y_angle)

1. 检查是否检测到人脸。

    .. code-block:: python

        Vilib.detect_obj_parameter['human_n'] != 0

2. 如果检测到人脸，获取人脸的坐标（ ``coordinate_x`` 和 ``coordinate_y``）。

3. 根据检测到的人脸位置计算新的云台水平和垂直角度（ ``x_angle`` 和 ``y_angle``），并进行调整以跟随人脸。

4. 使用 ``clamp_number`` 函数限制云台角度在指定范围内。

5. 使用 ``px.set_cam_pan_angle()`` 和 ``px.set_cam_tilt_angle()`` 设置摄像头的云台角度。
