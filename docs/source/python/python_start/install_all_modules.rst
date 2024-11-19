.. note:: 

    您好，欢迎加入 SunFounder Raspberry Pi & Arduino & ESP32 爱好者社区！与其他爱好者一起深入探索 Raspberry Pi、Arduino 和 ESP32 的世界。

    **为什么加入我们？**

    - **专家支持**：通过我们的社区和团队帮助，解决售后问题和技术挑战。
    - **学习与分享**：交流技巧和教程，提升您的技能水平。
    - **独家预览**：抢先获得新产品公告和独家预览机会。
    - **特别折扣**：享受我们最新产品的专属折扣优惠。
    - **节日促销和赠品**：参与节日抽奖和特别促销活动。

    👉 准备好与我们一起探索和创造了吗？点击 [|link_sf_facebook|] 立即加入吧！

.. _install_all_modules:

5. 安装所有模块（重要）
========================================

确保您的设备已连接互联网并更新系统：

.. raw:: html

    <run></run>

.. code-block::

    sudo apt update
    sudo apt upgrade

.. note::

    如果您使用的是 Lite 版本的操作系统，必须安装与 Python3 相关的包。

    .. raw:: html

        <run></run>

    .. code-block::
    
        sudo apt install git python3-pip python3-setuptools python3-smbus


安装 ``robot-hat`` 模块。

.. raw:: html

    <run></run>

.. code-block::

    cd ~/
    git clone -b v2.0 https://github.com/sunfounder/robot-hat.git
    cd robot-hat
    sudo python3 setup.py install


然后下载并安装 ``vilib`` 模块。

.. raw:: html

    <run></run>

.. code-block::

    cd ~/
    git clone -b picamera2 https://github.com/sunfounder/vilib.git
    cd vilib
    sudo python3 install.py

下载并安装 ``picar-x`` 模块。

.. raw:: html

    <run></run>

.. code-block::

    cd ~/
    git clone -b v2.0 https://github.com/sunfounder/picar-x.git
    cd picar-x
    sudo python3 setup.py install

这一步可能需要一些时间，请耐心等待。

最后，您需要运行脚本 ``i2samp.sh`` 来安装 i2s 放大器所需的组件，否则 picar-x 将无法发出声音。

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x
    sudo bash i2samp.sh
	
.. image:: img/i2s.png

输入 ``y`` 并按回车以继续运行脚本。

.. image:: img/i2s2.png

输入 ``y`` 并按回车以在后台运行 ``/dev/zero``。

.. image:: img/i2s3.png

输入 ``y`` 并按回车以重启 Picar-X。

.. note::
    如果重启后仍然没有声音，您可能需要多次运行 i2samp.sh 脚本。
