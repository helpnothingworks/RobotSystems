.. note::

    欢迎加入 SunFounder Raspberry Pi & Arduino & ESP32 爱好者社区（Facebook）！与其他爱好者一起深入探索 Raspberry Pi、Arduino 和 ESP32 的乐趣。

    **为什么要加入？**

    - **专家支持**：通过社区和团队的帮助解决售后问题和技术挑战。
    - **学习与分享**：交流技巧和教程，提升您的技能。
    - **独家预览**：抢先获取新产品发布信息和独家预览。
    - **专属折扣**：享受新品的独家优惠。
    - **节日活动与赠品**：参与赠品活动和节日促销。

    👉 准备好与我们一起探索和创造了吗？点击 [|link_sf_facebook|] 立即加入！

简介
====================


自动驾驶汽车的历史
----------------------------------------

自1920年代以来，人们就开始对自动驾驶汽车进行实验。1950年代出现了初步的成功试验，
此后研究工作不断推进。1980年代，首批真正自给自足且完全自主的车辆问世，例如
卡内基梅隆大学的 Navlab 和 ALV 项目（1984年）以及梅赛德斯-奔驰和慕尼黑联邦国防军大学
的 Eureka Prometheus 项目（1987年）。自1980年代后期以来，许多研究机构和主要汽车制造商开发了实用的自动驾驶车辆，包括：梅赛德斯-奔驰、通用汽车、大陆汽车系统、Autoliv、博世、日产、丰田、奥迪、沃尔沃、帕尔马大学 Vislab、牛津大学和谷歌。

2013年7月，Vislab 展示了 BRAiVE，这是一辆能够在开放的混合交通路线上自主行驶的车辆。截至2019年，美国已有29个州通过了允许自动驾驶汽车在公共道路上行驶的法律。

一些联合国欧洲经济委员会成员和欧盟成员（包括英国）也颁布了与自动驾驶汽车相关的法规。在欧洲，比利时、法国、意大利和英国的城市已制定计划，运营无人驾驶汽车的交通系统，而德国、荷兰和西班牙则已允许在公共道路上测试机器人汽车。到2020年，英国、欧盟和日本已经着手制定自动驾驶汽车的相关法规。

* 参考文献： `自动驾驶汽车历史 - 维基百科 <https://en.wikipedia.org/wiki/History_of_self-driving_cars>`_

如今，自动驾驶汽车是最接近我们生活的技术革命之一。一些专家预测，到2025年，4级自动驾驶汽车可能进入市场。4级自动驾驶汽车将允许驾驶员完全专注于其他事情，只要系统正常运行，就无需关注交通状况。

4级自动驾驶参考：

* `SAE 自动驾驶等级 <https://www.sae.org/blog/sae-j3016-update>`_
* `ABI 研究预测到2025年将有800万辆配备SAE 3、4、5级自动驾驶技术的车辆问世 <https://www.abiresearch.com/press/abi-research-forecasts-8-million-vehicles-ship-sae-level-3-4-and-5-autonomous-technology-2025/>`_

.. image:: img/self_driving_car.jpeg

近年来，软件（人工智能、机器学习）、硬件（GPU、FPGA、加速度计等）和云计算的快速发展推动了这一技术革命的进程。

* 2010年10月，由意大利技术公司 **Vislab** 设计的无人驾驶卡车用三个月时间完成了从 `意大利到中国的行程 <http://edition.cnn.com/2010/TECH/innovation/10/27/driverless.car/>`_，总行程达8,077英里。
* 2015年4月，由 **Delphi Automotive** 设计的一辆汽车从 `旧金山开往纽约 <https://money.cnn.com/2015/04/03/autos/delphi-driverless-car-cross-country-trip/>`_，全程3,400英里，其中99%的距离由计算机控制完成。
* 2018年12月，**Alphabet** 的 **Waymo** 在亚利桑那州推出了 `4级自动驾驶出租车服务 <https://www.reuters.com/article/us-waymo-selfdriving-focus/waymo-unveils-self-driving-taxi-service-in-arizona-for-paying-customers-idUSKBN1O41M2>`_，车辆自2008年起已进行无人驾驶测试，超过10万英里无驾驶员操作。
* 2020年10月，**百度** 在北京正式开放 `Apollo Robotaxi 无人驾驶出租车服务 <http://autonews.gasgoo.com/icv/70017615.html>`_，其行驶路线覆盖住宅区、商业区、休闲区及工业园区，提供完全自主驾驶体验。

然而，尽管每天收集了海量的驾驶数据，包括真实驾驶记录和模拟场景，自动驾驶汽车的人工智能模型的复杂性需求仍未完全满足。

根据 `RAND 报告 <https://www.rand.org/pubs/research_reports/RR1478.html>`_，要达到足够的自主学习水平，需要数亿甚至数千亿英里的训练数据以建立可靠性。

因此，尽管自动驾驶汽车的未来充满希望且令人兴奋，但距离技术完全成熟并广泛应用于市场仍需多年发展。

一种让新兴技术快速成熟的有效方法是通过降低市场准入门槛，让其更易为大众所用。这正是 SunFounder 推出 PiCar-X 的初衷。

SunFounder 的目标是帮助初学者、爱好者以及那些希望了解自动驾驶开发过程、技术和最新创新的人，理解自动驾驶汽车的研发流程与技术。

关于 PiCar-X
-------------------

.. .. image:: img/picar-x.jpg

PiCar-X 是一款基于 Raspberry Pi 平台的人工智能自驾机器人小车，Raspberry Pi 作为其控制中心。PiCar-X 的双轴摄像头模块、超声波模块和巡线模块支持色彩/人脸/交通标志识别、自动避障和自动巡线等功能。

通过 SunFounder 设计的 Robot HAT 板，PiCar-X 集成了左右驱动电机、负责转向和摄像头云台的舵机，并预置了 Robot HAT 的 ADC、PWM 和 I2C 数字引脚，使 Raspberry Pi 的标准功能得到扩展。Robot HAT 还配备了扬声器和蓝牙芯片，用于远程控制文字转语音、音效甚至背景音乐功能。

PiCar-X 的所有功能，包括 GPIO 控制、计算机视觉和深度学习，均通过开源的 Python 编程语言、OpenCV 计算机视觉库软件以及 Google 的 TensorFlow 深度学习框架实现。其他软件进一步优化了 PiCar-X 的功能，为用户提供几乎无限的学习环境。


深度学习与神经网络
-------------------------------------------------
要了解更多关于深度学习和神经网络的信息，SunFounder 推荐以下资源：



`机器学习 - Andrew Ng <https://www.coursera.org/learn/machine-learning>`_：本课程全面介绍了机器学习、数据挖掘和统计模式识别。

`神经网络与深度学习 <http://neuralnetworksanddeeplearning.com/>`_：本电子书涵盖了神经网络（一种启发自生物的编程范式，使计算机能够从观测数据中学习）和深度学习（用于神经网络机器学习的一组强大技术）。

`重新思考计算机视觉的 Inception 架构 <https://arxiv.org/abs/1512.00567>`_：这篇高水平论文探讨了通过因式分解卷积和激进正则化方法，用户如何高效利用额外计算资源扩展网络。
