# 使用指南
## 快速开始
左侧`realse`中下载`.exe`文件可以直接运行
## 界面介绍
首先是登陆界面，点击登录会自动访问同级文件夹里面的`data.csv`，注册也是同理。
在配置页面可以选择串口号，先点击检测串口，再点保存，就会自动生成`port.txt`。
其次，在登录或者注册前，需要在配置界面选择`是否启用trigger信号`，以及选择范式界面。
## 备注
整个项目仓促完成，多有漏洞，欢迎在issue里面提问

## 前期准备
### 软件安装

|安装软件|版本要求|
|-|-|
|PyCharm|社区版|
|Start Neusen W|V2.0|
|SubmarineHTC|-|
|SteamVR|最新版本|
|VIVE|最新版本|

### 环境配置
==运行“pip install requirement.txt”即可==
### VR软件硬件配置
[参考网站](https://www.vive.com/cn/setup/vive-pro-hmd/)
## 实验操作
### 实验前准备
- 准备清洗过的干净脑电帽
- 脑电放大器电池，VR操作手柄充电
- 提前对被试进行基本游戏规则描述
- 签写知情同意书
### VR准备
- 在房间对角架设三脚架
- 分别安装两台定位器到三脚架上，并连接电源
- 串流盒连接电源，usb线以及头显设备接口，点击一侧的启动按钮
- 笔记本电脑启动SteamVR
- 在SteamVR界面左上角选择'房间设置'
- 选择站立校准，完成校准步骤
- 短按左右手柄开关进行上电

### 脑电准备
- 路由器上电
- 安装标签记录器天线并上电
- USB线连接标签记录器与笔记本电脑
- 放大器装入电池
- 长按开关键启动
- 笔记本电脑连接'Neusen W'名称的wifi
- 打开'Start Neusen W'软件
- 点击'Tools'-'Device Settings'
- 点击'AutoDiscover'
- 在'Device Discover'界面，'TriggerBoxs Available'与'DevicesAvailable'均出现IP地址
    - 如果未出现IP地址
        - 尝试'ReScan'
        - 检查路由器，标签记录器以及放大器是否上电
        - 检查usb线是否连接
- 点击'DevicesAvailable'下的IP地址，点击'Save'
- 再次点击'Save'，点击'Close'
- 在'Device Settings'界面点击'Close'
- 如果是新被试
    - 点击主界面中'New Subjects'下的符号按钮
    - 输入'SubjectID'，以't000'为模板，'t000'就是1号被试，'t001'就是2号被试，以此类推
    - 在'Name'输入被试中文姓名
    - 在'AdmissionID'输入当前实验名称
    - 点击'OK'
- 如果是已注册过的被试
    - 点击主界面中'Select Subjects'下的符号按钮
    - 选择被试，点击'OK'
    - 在'AdmissionID'输入当前实验名称
    - 点击'OK'
- 点击弹出来的界面右上角'Impedance'查看阻抗
- 给被试戴脑电帽
- 打脑电膏，保证阻抗小于50KΩ
- 完成后，关闭'Impedance'
- 点击'DataService'选择16导联
- 点击'StartRecord'
### 精神状态量表评估
- 向被试询问汉密尔顿焦虑抑郁量表，并打分
- 向被试询问匹兹堡睡眠质量量表，并打分
>若有两位操作员，可以在打脑电膏的同时，进行量表打分，节省时间
### 实验1-ANT实验
- 点击'StartRecord'，在'AdmissionID'输入当前实验名称
- 在桌面右击'BCI_attentionParadigm'文件夹，在展开选项里面选择'Open Folder as PyCharm Project'
- 在右下角选择解释器，点击后选择'PyQt'
- 运行'run.py'
- 点击配置界面，点击“串口检测”，系统检测具体串口号并显示到界面上，点击“保存”
- 点击“范式选择”下拉框，选择"认知"范式
- 如果是已注册被试
    - 填写被试账号密码，点击“登陆”
- 如未注册则跳到第三点
    - 点击注册按钮，根据需求填写注册信息，点击完成
- 在弹出的相应范式界面中，填写实验轮次100，点击“连接设备”，再次点击“开始”
- 结束后，在'Recorder'界面点击'StopRecord'
### 实验2-SART实验
- 点击'StartRecord'，在'AdmissionID'输入当前实验名称
- 在桌面右击'BCI_attentionParadigm'文件夹，在展开选项里面选择'Open Folder as PyCharm Project'
- 在右下角选择解释器，点击后选择'PyQt'
- 运行'run.py'
- 点击配置界面，点击“串口检测”，系统检测具体串口号并显示到界面上，点击“保存”
- 点击“范式选择”下拉框，选择"SART"范式
- 如果是已注册被试
    - 填写被试账号密码，点击“登陆”
- 如未注册则跳到第三点
    - 点击注册按钮，根据需求填写注册信息，点击完成
- 在弹出的相应范式界面中，填写实验轮次100，点击“连接设备”，再次点击“开始”
- 结束后，在'Recorder'界面点击'StopRecord'
### 实验3-VR潜艇实验
- 点击'StartRecord'，在'AdmissionID'输入当前实验名称
- 佩戴VR头显
- 点击运行'SubmarineHTC'
- 点击运行'VR潜艇脑电控制端'
- 在'VR潜艇脑电控制端'界面输入被试基本信息，时间间隔为2000-2500-5000-15000
- 点击'下一步'，选择'主动'，'鱼雷舱'，系统配置为'COM4'，'115200'，点击'开始测试'
- 点击'事件测试'
- 点击'开始测试'
- 每完成12轮事件，点击'结束测试'
- 再次点击'开始测试'
- 重复五轮，即完成实验
### 实验4-静息态采集
- 点击'情绪舒缓'
- 点击'睁眼'，1分钟后，点击'闭眼'，1分钟后，点击'睁眼'，1分钟后即完成静息态采集
### 实验5-视频音乐舒缓
- 点击'视频播放'，10分钟后点击'视频停止'
- 点击'音乐播放'，3分钟后点击'音乐停止'
>此模块可以自动播放，即点击'视频播放'后13分钟后点击'音乐停止'即可
### 实验6-静息态采集
- 点击'睁眼'，1分钟后，点击'闭眼'，1分钟后，点击'睁眼'，1分钟后即完成静息态采集
- 摘下VR头显
### 实验7-ANT实验
- 点击'StartRecord'，在'AdmissionID'输入当前实验名称
- 在桌面右击'BCI_attentionParadigm'文件夹，在展开选项里面选择'Open Folder as PyCharm Project'
- 在右下角选择解释器，点击后选择'PyQt'
- 运行'run.py'
- 点击配置界面，点击“串口检测”，系统检测具体串口号并显示到界面上，点击“保存”
- 点击“范式选择”下拉框，选择"认知"范式
- 如果是已注册被试
    - 填写被试账号密码，点击“登陆”
- 如未注册则跳到第三点
    - 点击注册按钮，根据需求填写注册信息，点击完成
- 在弹出的相应范式界面中，填写实验轮次100，点击“连接设备”，再次点击“开始”
- 结束后，在'Recorder'界面点击'StopRecord'
### 实验8-SART实验
- 点击'StartRecord'，在'AdmissionID'输入当前实验名称
- 在桌面右击'BCI_attentionParadigm'文件夹，在展开选项里面选择'Open Folder as PyCharm Project'
- 在右下角选择解释器，点击后选择'PyQt'
- 运行'run.py'
- 点击配置界面，点击“串口检测”，系统检测具体串口号并显示到界面上，点击“保存”
- 点击“范式选择”下拉框，选择"SART"范式
- 如果是已注册被试
    - 填写被试账号密码，点击“登陆”
- 如未注册则跳到第三点
    - 点击注册按钮，根据需求填写注册信息，点击完成
- 在弹出的相应范式界面中，填写实验轮次100，点击“连接设备”，再次点击“开始”
- 结束后，在'Recorder'界面点击'StopRecord'

## 附录
requirement.txt具体如下：
>altgraph\==0.17.3
auto-py-to-exe\==2.33.0
bottle\==0.12.25
bottle-websocket\==0.2.9
Bottleneck\==1.3.5
brotlipy\==0.7.0
certifi\==2022.12.7
cffi\==1.15.1
charset-normalizer\==2.0.4
cloudpickle\==2.2.1
colorama\==0.4.6
cryptography\==39.0.1
Eel\==0.16.0
future\==0.18.3
gevent\==22.10.2
gevent-websocket\==0.10.1
greenlet\==2.0.2
gym\==0.26.2
gym-notices\==0.0.8
idna\==3.4
importlib-metadata\==6.3.0
Jinja2\==3.1.2
MarkupSafe\==2.1.3
mkl-fft\==1.3.1
mkl-random\==1.2.2
mkl-service\==2.4.0
mss\==8.0.2
nes-py\==8.2.1
numexpr\==2.8.4
numpy\==1.23.5
opencv-python\==4.7.0.72
packaging\==23.0
pandas\==1.5.3
pefile\==2023.2.7
Pillow\==9.4.0
pip\==23.0.1
PyAudio\==0.2.11
pycparser\==2.21
pyglet\==1.5.21
pyinstaller\==5.10.0
pyinstaller-hooks-contrib\==2023.2
pynput\==1.7.6
pyOpenSSL\==23.0.0
pyparsing\==3.0.9
pypiwin32\==223
PyQt5\==5.15.9
PyQt5-Qt5\==5.15.2
PyQt5-sip\==12.11.1
pyserial\==3.5
PySocks\==1.7.1
python-dateutil\==2.8.2
pytz\==2022.7
pywin32\==306
pywin32-ctypes\==0.2.0
QDarkStyle\==3.1
QScintilla\==2.13.4
qt-material\==2.14
QtPy\==2.3.1
requests\==2.29.0
setuptools\==67.8.0
six\==1.16.0
tqdm\==4.65.0
urllib3\==1.26.16
wheel\==0.40.0
whichcraft\==0.6.1
win-inet-pton\==1.1.0
wincertstore\==0.2
zipp\==3.15.0
zope.event\==4.6
zope.interface\==6.0
