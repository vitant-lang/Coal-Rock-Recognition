# 有关环境配置
## 推荐anaconda py3.7
conda install --file requirements.txt
网络架构是deeplabv3+
# Coal-Rock-Recognition
# 模拟测试与振动传感器
传感器的型号是 正点原子的9050 6050也可以用，通过串口读取数据。
![demo1](https://github.com/vitant-lang/Coal-Rock-Recognition/assets/75409802/abeddd22-db85-4630-b8a9-bc84bfb84c4c)
![demo2](https://github.com/vitant-lang/Coal-Rock-Recognition/assets/75409802/ec48d4c3-538e-4f62-be85-3f921741fee1)
## 振动传感器应该是配备在底下开采机器当中的，此部分仅仅做为模拟。
# 保存至本地xls
![save to xls ](https://github.com/vitant-lang/Coal-Rock-Recognition/assets/75409802/d2776146-f17b-4e58-8708-8e8c1aa762ec)
# 同步人员与煤炭数据
![人员及数据同步数据库 00_00_00-00_00_30](https://github.com/vitant-lang/Coal-Rock-Recognition/assets/75409802/1cb6a89b-b02b-493a-8725-8bd6a8641d99)
# 摄像头监控
![摄像头监控](https://github.com/vitant-lang/Coal-Rock-Recognition/assets/75409802/ae00ead5-c0a4-4c33-85b4-f4a0aebccd59)
![摄像头实时模拟 00_00_00-00_00_30](https://github.com/vitant-lang/Coal-Rock-Recognition/assets/75409802/a4a1da08-bb37-4e4c-ae14-f958a13fbd83)
# 摄像头监控
![文件夹遍历 00_00_00-00_00_30](https://github.com/vitant-lang/Coal-Rock-Recognition/assets/75409802/2d464076-5f5d-44c0-bd69-8a323d947df0)
![文件夹遍历2 00_00_00-00_00_30](https://github.com/vitant-lang/Coal-Rock-Recognition/assets/75409802/3cead8b7-37bf-4d1b-8355-b91cc71f6ddb)
# 预估开采量
![预估开采量 00_00_00-00_00_30](https://github.com/vitant-lang/Coal-Rock-Recognition/assets/75409802/116101c0-d059-4668-b1d5-815450ebfa58)
# 硬件视频
https://github.com/vitant-lang/Coal-Rock-Recognition/assets/75409802/7554925d-6c12-44a2-91d4-d3d10bccd31c
## 传输方式上位机将坐标发至控制板，控制板坐标换算后使机械臂靠近，开发板的算力不够，之前也尝试过利用无线传输，干扰太多，可用串口线模拟防干扰电缆进行传输。

# Reference
## 训练过程可以参考B导  dog.jpg
https://github.com/bubbliiiing/deeplabv3-plus-pytorch#reference


# 未来更新计划
会放出加了eca cbam se的deeplabv3+和pspnet 
