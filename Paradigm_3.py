from ui.sart_gui import Ui_MainWindow

import sys
import pandas as pd
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt, QPropertyAnimation, QRect, QEasingCurve
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import random
import time
import os
import pandas as pd
import numpy as np
from pynput import mouse
from pynput import keyboard
from qt_material import apply_stylesheet
import win32gui, win32ui, win32api
import win32con  # 系统操作
import datetime


def exit():
    if myWin.exitButton.text() == "连接设备":
        if myWin.tri_flag:
            from trigger.trigger_config import TriggerConfig
            myWin.tri_ctrl = TriggerConfig().trig_ctrl
            myWin.tri_ctrl.open()
        myWin.exitButton.setText("开始")
    elif myWin.exitButton.text() == "开始":
        myWin.my_beg = time.time()
        myWin.exitButton.setText("退出")
        myWin.counter = 0
        myWin.flag = True
        myWin.timer.start()
    else:
        myWin.exitButton.setText("")


class SART(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(SART, self).__init__()

        self.setupUi(self)
        self.setWindowTitle("BCI登录")
        self.setWindowIcon(QIcon("./img/mylogo.jpg"))
        # self.setWindowFlags(Qt.FramelessWindowHint)  # 设置窗口标志：隐藏窗口边框
        self.resize(QDesktopWidget().screenGeometry().width(), QDesktopWidget().screenGeometry().height())  # 主窗大小
        self.setWindowFlag(Qt.WindowStaysOnTopHint, True)
        self.exitButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.tri_flag = False  # 脑电标记flag
        self.mss_flag = False  # 截图flag
        self.flag = False  # 计时开始flag
        self.spaceflag = False  # 空格flag
        self.timer = QTimer()
        self.timer.setInterval(1)  # 设置计时器的间隔，单位是毫秒
        self.timer.timeout.connect(self.onTimerOut)
        self.last_tar = 0
        self.status = 0  # 阶段
        self.ms = 0  # 毫秒数
        self.counter = 0  # 试验次数
        self.score = 100  # 分数
        self.tar_num = 0  # 显示数字
        self.no_go = 0  # 数字3标记
        self.go = 0  # 其余数字标记
        self.no_go_mistake = 0
        self.go_mistake = 0
        self.my_end = None
        self.my_beg = None
        self.resp_end = None
        self.resp_beg = None
        self.sum_resp = 0
        self.timer.stop()
        self.setfont(200)  # 设置字体大小

        self.listener = keyboard.Listener(
            on_press=self.on_press,
        )
        self.listener.start()  # 启动线程

        tmp = ['*', '*', '*', '*', '*', '*', '*', '*', '*']

        try:
            df = pd.read_csv('result.csv')
            tmp_data = np.array(df)  # 先将数据框转换为数组
            tmp_data = np.delete(tmp_data, 0, axis=1).tolist()
            tmp_data.append(tmp)
            pd.DataFrame(data=tmp_data).to_csv('result.csv')
        except:
            pd.DataFrame(data=tmp).to_csv('result.csv')

    def setfont(self, num):
        if num == 1:
            self.label_2.setFont(QFont("微软雅黑", 48, QFont.Bold))
        if num == 2:
            self.label_2.setFont(QFont("微软雅黑", 72, QFont.Bold))
        if num == 3:
            self.label_2.setFont(QFont("微软雅黑", 94, QFont.Bold))
        if num == 4:
            self.label_2.setFont(QFont("微软雅黑", 100, QFont.Bold))
        if num == 5:
            self.label_2.setFont(QFont("微软雅黑", 120, QFont.Bold))

    def on_press(self, key):
        """定义按下时候的响应，参数传入key"""
        if key == keyboard.Key.space:
            self.spaceflag = True
            self.resp_end = time.time()
            self.sum_resp = self.sum_resp + (self.resp_end - self.resp_beg)
            if self.tar_num == 3:
                print(str(self.tar_num) + "按错了！")
                self.no_go_mistake = self.no_go_mistake + 1
                self.label_2.setPixmap(QPixmap("img/mistake_wrong_press.png"))
                self.status = 2
                self.ms = 0
            else:
                print(str(self.tar_num) + "成功！")
                self.label_2.setPixmap(QPixmap("img/mask_green.png"))
            self.savecsv("按下空格")
        else:
            self.spaceflag = False

    def onTimerOut(self):
        # 显示时间
        # QMessageBox.information(self, "提示", "请先连接设备", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        my_Time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        self.label.setText(my_Time)
        if self.no_go > int(self.LineEdit.text()):
            self.label_2.setText("")
            self.exitButton.setText("完成实验！")
            self.close()
        if self.no_go <= int(self.LineEdit.text()):

            ''' 阶段一 '''
            if self.status == 0 and self.ms == 1:
                self.spaceflag = False
                # 随机初始化数字与字体大小
                while self.last_tar == self.tar_num:
                    self.tar_num = random.randint(1, 9)

                self.font_num = random.randint(1, 5)
                # 统计两种标签
                if self.tar_num == 3:
                    self.no_go = self.no_go + 1
                else:
                    self.go = self.go + 1
                self.setfont(self.font_num)

                self.label_2.setText(str(self.tar_num))
                self.resp_beg = time.time()
                if self.tri_flag:
                    self.tri_ctrl.send(1)

            ''' 阶段二 '''
            if self.status == 0 and self.ms == 250:
                self.label_2.setPixmap(QPixmap("img/mask.png"))
                # 更新阶段
                self.status = 1
                self.ms = 0
                if self.tri_flag:
                    self.tri_ctrl.send(2)
            if self.status == 0 and self.spaceflag == True:
                # 更新阶段
                self.status = 1
                self.ms = 0
                if self.tri_flag:
                    self.tri_ctrl.send(2)
            if self.status == 1 and self.ms == 900:
                self.counter = self.counter + 1
                self.last_tar = self.tar_num
                self.progressBar.setValue(int(100 * self.no_go / int(self.LineEdit.text())))
                self.status = 0
                self.ms = 0
                if self.spaceflag == False:
                    self.resp_end = time.time()
                    self.sum_resp = self.sum_resp + (self.resp_end - self.resp_beg)
                    self.savecsv("未按下")
                    if self.tar_num == 3:
                        print("3成功！")

                    if self.tar_num != 3:
                        print(str(self.tar_num) + "错过了！")
                        self.label_2.setPixmap(QPixmap("img/mistake_missed.png"))
                        self.go_mistake = self.go_mistake + 1
                        self.status = 2

            if self.status == 2 and self.ms == 900:
                if self.tri_flag:
                    self.tri_ctrl.send(3)
                self.status = 0
                self.ms = 0
                self.counter = self.counter + 1
                self.last_tar = self.tar_num
            if self.flag:
                self.ms = self.ms + 1
        else:
            print("您的分数为: ", self.score)
            self.my_end = time.time()
            self.timer.stop()
            self.flag = False
            print("time:" + str(self.my_end - self.my_beg))
            print("no_go:" + str(self.no_go))
            print("go:" + str(self.go))
            print("mis_no_go:" + str(self.no_go_mistake))
            print("mis_go:" + str(self.go_mistake))
            t = int(round(time.time() * 1000))
            now_Time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            tmp = ["SART", now_Time, t, self.my_end - self.my_beg, self.no_go, self.go, self.no_go_mistake, self.go_mistake,
                   100 * self.no_go_mistake / int(self.LineEdit.text()), self.sum_resp/(self.counter+1)]
            try:
                df = pd.read_csv('login.csv')
                tmp_data = np.array(df)  # 先将数据框转换为数组
                tmp_data = np.delete(tmp_data, 0, axis=1).tolist()
                tmp_data.append(tmp)
                pd.DataFrame(data=tmp_data).to_csv('login.csv')
            except:
                pd.DataFrame(data=tmp).to_csv('login.csv')

    def savecsv(self, str):
        t = int(round(time.time() * 1000))
        now_Time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        tmp = ["SART", now_Time, t, self.counter, self.font_num, self.tar_num, str, self.status, self.ms,
               self.resp_end - self.resp_beg]
        try:
            df = pd.read_csv('result.csv')
            tmp_data = np.array(df)  # 先将数据框转换为数组
            tmp_data = np.delete(tmp_data, 0, axis=1).tolist()
            tmp_data.append(tmp)
            pd.DataFrame(data=tmp_data).to_csv('result.csv')
        except:
            pd.DataFrame(data=tmp).to_csv('result.csv')

    def window_capture(self, filename):
        hwnd = 0  # 窗口的编号，0号表示当前活跃窗口
        # 根据窗口句柄获取窗口的设备上下文DC（Divice Context）
        hwndDC = win32gui.GetWindowDC(hwnd)
        # 根据窗口的DC获取mfcDC
        mfcDC = win32ui.CreateDCFromHandle(hwndDC)
        # mfcDC创建可兼容的DC
        saveDC = mfcDC.CreateCompatibleDC()
        # 创建bigmap准备保存图片
        saveBitMap = win32ui.CreateBitmap()
        # 获取监控器信息
        MoniterDev = win32api.EnumDisplayMonitors(None, None)
        w = MoniterDev[0][2][2]
        h = MoniterDev[0][2][3]
        # print w,h　　　#图片大小
        # 为bitmap开辟空间
        saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
        # 高度saveDC，将截图保存到saveBitmap中
        saveDC.SelectObject(saveBitMap)
        # 截取从左上角（0，0）长宽为（w，h）的图片
        saveDC.BitBlt((0, 0), (w, h), mfcDC, (0, 0), win32con.SRCCOPY)
        saveBitMap.SaveBitmapFile(saveDC, filename)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # # setup stylesheet
    # apply_stylesheet(app, theme='dark_amber.xml')  # dark_amber
    # stylesheet = app.styleSheet()
    # with open('custom.css') as file:
    #     app.setStyleSheet(stylesheet + file.read().format(**os.environ))
    myWin = SART()
    ###
    myWin.mss_flag = False  # 截图flag
    myWin.tri_flag = True  # 脑电trigger的flag
    ###
    myWin.exitButton.clicked.connect(exit)
    myWin.show()
    sys.exit(app.exec_())
