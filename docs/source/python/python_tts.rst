.. note::

    欢迎加入 SunFounder Raspberry Pi & Arduino & ESP32 爱好者 Facebook 社区！与志同道合的朋友一起深入探索 Raspberry Pi、Arduino 和 ESP32 的无限可能。

    **为什么要加入？**

    - **专家支持**：社区和团队为您解决售后问题和技术挑战。
    - **学习与分享**：交流技巧和教程，提升您的技能。
    - **独家预览**：抢先获取新产品发布和独家预览。
    - **专属折扣**：享受新品的独家优惠。
    - **节日活动与赠品**：参与节日促销和免费赠品活动。

    👉 准备好与我们一起探索和创造了吗？点击 [|link_sf_facebook|]，立即加入！

.. _py_tts:

3. 文字转语音与音效
=========================================

在此示例中，我们将使用 PiCar-X（更准确地说是 Robot HAT）的音效功能。
它包含三个部分：音乐、音效、文字转语音。

**安装 i2samp**

在使用文字转语音（TTS）和音效功能之前，请先激活扬声器以便使其启用并可以发声。

运行 **picar-x** 文件夹中的 ``i2samp.sh`` 脚本，安装使用 i2s 放大器所需的一切。

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x
    sudo bash i2samp.sh 

.. image:: img/tt_bash.png

执行过程中会有多个确认提示，请全部选择 **Y**。更改应用于 Raspberry Pi 系统后，需要重新启动计算机才能生效。

重启后，再次运行 ``i2samp.sh`` 脚本测试放大器。如果扬声器成功播放声音，配置即完成。

**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 3.tts_example.py
    
代码运行后，请根据终端打印的提示操作。

按下键盘按键以调用功能：

    * 空格键: 播放音效（汽车喇叭）
    * c: 使用线程播放音效
    * t: 文本语音播报（说“Hello”）
    * q: 播放/停止音乐

**代码**

.. code-block:: python

    from time import sleep
    from robot_hat import Music,TTS
    import readchar

    music = Music()
    tts = TTS()

    manual = '''
    Input key to call the function!
        space: Play sound effect (Car horn)
        c: Play sound effect with threads
        t: Text to speak
        q: Play/Stop Music
    '''

    def main():
        print(manual)

        flag_bgm = False
        music.music_set_volume(20)
        tts.lang("en-US")


        while True:
            key = readchar.readkey()
            key = key.lower()
            if key == "q":
                flag_bgm = not flag_bgm
                if flag_bgm is True:
                    music.music_play('../musics/slow-trail-Ahjay_Stelino.mp3')
                else:
                    music.music_stop()

            elif key == readchar.key.SPACE:
                music.sound_play('../sounds/car-double-horn.wav')
                sleep(0.05)

            elif key == "c":
                music.sound_play_threading('../sounds/car-double-horn.wav')
                sleep(0.05)

            elif key == "t":
                words = "Hello"
                tts.say(words)

    if __name__ == "__main__":
        main()

**工作原理**

与背景音乐相关的功能包括：

* ``music = Music()``：声明对象。
* ``music.music_set_volume(20)``：设置音量，范围为 0~100。
* ``music.music_play('../musics/slow-trail-Ahjay_Stelino.mp3')``：播放音乐文件，此处为路径 ``../musics`` 下的 **slow-trail-Ahjay_Stelino.mp3** 文件。
* ``music.music_stop()``：停止播放背景音乐。

.. note::

    您可以通过 :ref:`filezilla` 将不同的音效或音乐添加到 ``musics`` 或 ``sounds`` 文件夹中。

与音效相关的功能包括：

* ``music = Music()``
* ``music.sound_play('../sounds/car-double-horn.wav')``：播放音效文件。
* ``music.sound_play_threading('../sounds/car-double-horn.wav')``：以线程模式播放音效文件，不会阻塞主线程。

文字转语音功能使用了 `eSpeak <http://espeak.sourceforge.net/>`_ 软件。

在 robot_hat 中导入 TTS 模块，该模块封装了将文字转换为语音的功能。

与文字转语音相关的功能包括：

* ``tts = TTS()``
* ``tts.say(words)``：语音播报文本。
* ``tts.lang("en-US")``：设置语言。

.. note:: 

    可以通过设置 ``lang("")`` 参数指定语言，支持以下字符：

.. list-table:: Language
    :widths: 15 50

    *   - zh-CN 
        - 普通话（中文）
    *   - en-US 
        - 美国英语
    *   - en-GB     
        - 英国英语
    *   - de-DE     
        - 德语
    *   - es-ES     
        - 西班牙语
    *   - fr-FR  
        - 法语
    *   - it-IT  
        - 意大利语
