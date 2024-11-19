.. note::

    欢迎加入 SunFounder Raspberry Pi & Arduino & ESP32 爱好者社区（Facebook）！与其他爱好者一起深入探索 Raspberry Pi、Arduino 和 ESP32 的乐趣。

    **为什么要加入？**

    - **专家支持**：在社区和团队的帮助下解决售后问题和技术挑战。
    - **学习与分享**：交流技巧和教程，提升您的技能。
    - **独家预览**：抢先了解新产品发布和独家预览。
    - **专属折扣**：享受新品的独家优惠。
    - **节日活动与赠品**：参与赠品活动和节日促销。

    👉 准备好与我们一起探索和创造了吗？点击 [|link_sf_facebook|] 立即加入！

.. _video_car:

11. 视频小车
==========================================

此程序为您提供 PiCar-X 的第一视角体验！通过键盘上的 WSAD 键控制方向，
使用 O 和 P 键调整速度。

**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 11.video_car.py

代码运行后，您可以看到 PiCar-X 拍摄的画面，并通过以下按键进行控制：

* O: 加速
* P: 减速
* W: 前进  
* S: 后退
* A: 左转
* D: 右转
* F: 停止
* T: 拍照
* Ctrl+C: 退出

**查看画面**

代码运行后，终端将显示以下提示：

.. code-block::

    No desktop !
    * Serving Flask app "vilib.vilib" (lazy loading)
    * Environment: production
    WARNING: Do not use the development server in a production environment.
    Use a production WSGI server instead.
    * Debug mode: off
    * Running on http://0.0.0.0:9000/ (Press CTRL+C to quit)

然后您可以在浏览器中输入 ``http://<你的IP>:9000/mjpg`` 查看视频画面，例如： ``https://192.168.18.113:9000/mjpg``

.. image:: img/display.png

**代码**

.. code-block:: python
    
    #!/usr/bin/env python3

    from robot_hat.utils import reset_mcu
    from picarx import Picarx
    from vilib import Vilib
    from time import sleep, time, strftime, localtime
    import readchar

    import os
    user = os.getlogin()
    user_home = os.path.expanduser(f'~{user}')

    reset_mcu()
    sleep(0.2)

    manual = '''
    按下键盘按键以调用功能（不区分大小写）：

        O: 加速
        P: 减速
        W: 前进  
        S: 后退
        A: 左转
        D: 右转
        F: 停止
        T: 拍照

        Ctrl+C: 退出
    '''


    px = Picarx()

    def take_photo():
        _time = strftime('%Y-%m-%d-%H-%M-%S',localtime(time()))
        name = 'photo_%s'%_time
        path = f"{user_home}/Pictures/picar-x/"
        Vilib.take_photo(name, path)
        print('\nphoto save as %s%s.jpg'%(path,name))


    def move(operate:str, speed):

        if operate == 'stop':
            px.stop()  
        else:
            if operate == 'forward':
                px.set_dir_servo_angle(0)
                px.forward(speed)
            elif operate == 'backward':
                px.set_dir_servo_angle(0)
                px.backward(speed)
            elif operate == 'turn left':
                px.set_dir_servo_angle(-30)
                px.forward(speed)
            elif operate == 'turn right':
                px.set_dir_servo_angle(30)
                px.forward(speed)
            


    def main():
        speed = 0
        status = 'stop'

        Vilib.camera_start(vflip=False,hflip=False)
        Vilib.display(local=True,web=True)
        sleep(2)  # 等待启动
        print(manual)
        
        while True:
            print("\rstatus: %s , speed: %s    "%(status, speed), end='', flush=True)
            # 读取按键
            key = readchar.readkey().lower()
            # 操作处理
            if key in ('wsadfop'):
                # 油门
                if key == 'o':
                    if speed <=90:
                        speed += 10           
                elif key == 'p':
                    if speed >=10:
                        speed -= 10
                    if speed == 0:
                        status = 'stop'
                # 方向控制
                elif key in ('wsad'):
                    if speed == 0:
                        speed = 10
                    if key == 'w':
                        # 倒车时限速，避免瞬间电流过大
                        if status != 'forward' and speed > 60:  
                            speed = 60
                        status = 'forward'
                    elif key == 'a':
                        status = 'turn left'
                    elif key == 's':
                        if status != 'backward' and speed > 60: # 倒车时限速
                            speed = 60
                        status = 'backward'
                    elif key == 'd':
                        status = 'turn right' 
                # 停止
                elif key == 'f':
                    status = 'stop'
                # 移动
                move(status, speed)  
            # 拍照
            elif key == 't':
                take_photo()
            # 退出
            elif key == readchar.key.CTRL_C:
                print('\nquit ...')
                px.stop()
                Vilib.camera_close()
                break 

            sleep(0.1)


    if __name__ == "__main__":
        try:
            main()
        except Exception as e:    
            print("error:%s"%e)
        finally:
            px.stop()
            Vilib.camera_close()

