.. _py_treasure:

12. 寻宝游戏
============================

在您的房间里布置一个迷宫，并在六个角落分别放置六张不同颜色的卡片。然后控制 PiCar-X 逐一寻找这些颜色卡片！

.. note:: 您可以下载并打印色卡 :download:`PDF Color Cards <https://github.com/sunfounder/sf-pdf/raw/master/prop_card/object_detection/color-cards.pdf>` 用于颜色检测。

**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 12.treasure_hunt.py

**查看画面**

运行代码后，终端将显示以下提示：

.. code-block::

    No desktop !
    * Serving Flask app "vilib.vilib" (lazy loading)
    * Environment: production
    WARNING: Do not use the development server in a production environment.
    Use a production WSGI server instead.
    * Debug mode: off
    * Running on http://0.0.0.0:9000/ (Press CTRL+C to quit)

然后，您可以在浏览器中输入 ``http://<您的 IP>:9000/mjpg`` 查看视频画面，例如： ``http://192.168.18.113:9000/mjpg``

.. image:: img/display.png

**代码**

.. code-block:: python

    from picarx import Picarx
    from time import sleep
    from robot_hat import Music,TTS
    from vilib import Vilib
    import readchar
    import random
    import threading
    
    px = Picarx()
    
    music = Music()
    tts = TTS()
    
    manual = '''
    Press keys on keyboard to control Picar-X!
        w: Forward
        a: Turn left
        s: Backward
        d: Turn right
        space: Say the target again
        ctrl+c: Quit
    '''
    
    color = "red"
    color_list=["red","orange","yellow","green","blue","purple"]
    
    def renew_color_detect():
        global color
        color = random.choice(color_list)
        Vilib.color_detect(color)
        tts.say("Look for " + color)
    
    key = None
    lock = threading.Lock()
    def key_scan_thread():
        global key
        while True:
            key_temp = readchar.readkey()
            print('\r',end='')
            with lock:
                key = key_temp.lower()
                if key == readchar.key.SPACE:
                    key = 'space'
                elif key == readchar.key.CTRL_C:
                    key = 'quit'
                    break
            sleep(0.01)
    
    def car_move(key):
        if 'w' == key:
            px.set_dir_servo_angle(0)
            px.forward(80)
        elif 's' == key:
            px.set_dir_servo_angle(0)
            px.backward(80)
        elif 'a' == key:
            px.set_dir_servo_angle(-30)
            px.forward(80)
        elif 'd' == key:
            px.set_dir_servo_angle(30)
            px.forward(80)
    
    
    def main():
        global key
        Vilib.camera_start(vflip=False,hflip=False)
        Vilib.display(local=False,web=True)
        sleep(0.8)
        print(manual)
    
        sleep(1)
        _key_t = threading.Thread(target=key_scan_thread)
        _key_t.setDaemon(True)
        _key_t.start()
    
        tts.say("game start")
        sleep(0.05)
        renew_color_detect()
        while True:
    
            if Vilib.detect_obj_parameter['color_n']!=0 and Vilib.detect_obj_parameter['color_w']>100:
                tts.say("will done")
                sleep(0.05)
                renew_color_detect()
    
            with lock:
                if key != None and key in ('wsad'):
                    car_move(key)
                    sleep(0.5)
                    px.stop()
                    key =  None
                elif key == 'space':
                    tts.say("Look for " + color)
                    key =  None
                elif key == 'quit':
                    _key_t.join()
                    print("\n\rQuit")
                    break
    
            sleep(0.05)
    
    if __name__ == "__main__":
        try:
            main()
        except KeyboardInterrupt:
            pass
        except Exception as e:
            print(f"ERROR: {e}")
        finally:
            Vilib.camera_close()
            px.stop()
            sleep(.2)


**工作原理**

要理解此代码的基本逻辑，您可以关注以下关键部分：

1. **初始化与导入：**
   代码开头的导入语句用于了解所使用的库和模块。

2. **全局变量：**
   定义全局变量，例如 ``color`` 和 ``key``，这些变量贯穿整个代码，用于跟踪目标颜色和键盘输入。

3. ``renew_color_detect()`` ：
   该函数从颜色列表中随机选择一个颜色，并将其设置为检测目标。同时，使用语音合成功能播报所选颜色。

4. ``key_scan_thread()`` ：
   该函数运行在单独的线程中，不断扫描键盘输入，并更新 ``key`` 变量为按下的键值。它使用锁机制确保线程访问的安全性。

5. ``car_move(key)`` ：
   根据键盘输入（ ``key`` ）控制 PiCar-X 的移动。该函数设置机器人的方向和移动速度。

6. ``main()`` ： 代码的主要逻辑协调函数，其功能包括：

    * 初始化摄像头并开始显示实时画面。
    * 创建独立线程以扫描键盘输入。
    * 通过语音播报宣布游戏开始。
    * 进入一个循环：

        * 检查是否检测到颜色目标对象，并在检测到有效对象时触发相应动作。
        * 处理键盘输入以控制机器人并与游戏交互。
    * 处理游戏退出逻辑和诸如 ``KeyboardInterrupt`` 的异常情况。
    * 确保退出时关闭摄像头并停止 PiCar-X。

通过理解代码的这些关键部分，您可以掌握 PiCar-X 机器人如何响应键盘输入，
以及如何利用摄像头和音频输出功能检测并与特定颜色的目标对象进行交互。

