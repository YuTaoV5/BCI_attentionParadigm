'''
Author: ProtoDrive000
Date: 2023-04-01 14:06:58
LastEditTime: 2023-04-01 19:31:50
Description: 
FilePath: \BCI_Timer\test.py
Copyright © : 2021年 赛博智能车实验室. All rights reserved. 
'''

from ui.ant_gui import Ui_MainWindow

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
import pandas as pd
import numpy as np
from pynput import mouse

import win32gui, win32ui, win32api
import win32con  # 系统操作
import datetime


# 鼠标点击响应事件


# def listen_mouse_nblock():
#     listener = mouse.Listener(
#         on_move=None,
#         on_click=on_click,
#         on_scroll=None
#     )
#     listener.start()


def exit():
    if myWin.exitButton.text() == "连接设备":
        if myWin.tri_flag:
            from trigger.trigger_config import TriggerConfig
            myWin.tri_ctrl = TriggerConfig().trig_ctrl
            myWin.tri_ctrl.open()
        myWin.exitButton.setText("开始")
    elif myWin.exitButton.text() == "开始":
        myWin.beg = time.time()
        myWin.exitButton.setText("退出")
        myWin.counter = 0
        myWin.flag = True
        myWin.timer.start()
    else:
        myWin.close()


class RENZHI(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(RENZHI, self).__init__()
        self.tri_ctrl = None
        self.my_end = None
        self.beg = None
        self.setupUi(self)
        self.setWindowTitle("BCI登录")
        self.setWindowIcon(QIcon("./img/mylogo.jpg"))
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # self.setWindowFlags(Qt.FramelessWindowHint)  # 设置窗口标志：隐藏窗口边框
        self.resize(QDesktopWidget().screenGeometry().width(), QDesktopWidget().screenGeometry().height())  # 主窗大小
        self.setWindowFlag(Qt.WindowStaysOnTopHint, True)
        self.exitButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.progressBar.setValue(0)
        self.tri_flag = False
        self.mss_flag = False  # 截图flag
        self.press_flag = False
        self.flag = 0
        self.status = 0
        self.timer = QTimer()
        self.timer.setInterval(1)  # 设置计时器的间隔，单位是毫秒
        self.timer.timeout.connect(self.onTimerOut)
        self.ms = 0
        self.dir = 0
        self.counter = 0
        self.score = 100
        self.last_count = 0
        self.Fix_time = random.randint(400, 1600)
        self.cue_num = random.randint(1, 5)
        self.tar_num = random.randint(1, 3)
        self.dir_num = random.randint(1, 2)
        self.cue_list = [" ", "无cue", "中央位置", "双提示", "空间信息（下）", "空间信息（上）"]
        self.tar_list = [" ", "一致刺激", "中性", "非一致刺激"]
        self.dir_list = [" ", "左", "右"]

        # self.exitButton.clicked.connect(self.exit)
        self.timer.stop()
        self.setfont(200)

        self.no_cue_ms = 0
        self.center_ms = 0
        self.space_ms = 0
        self.no_same_ms = 0
        self.same_ms = 0


        tmp = ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*']
        self.no_cue_list = ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*']
        self.center_list = ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*']
        self.space_list = ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*']
        self.no_same_list = ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*']
        self.same_list = ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*']
        self.data = ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*']
        self.tmp_count = len(tmp)

        try:
            df = pd.read_csv('result.csv')
            tmp_data = np.array(df)  # 先将数据框转换为数组
            tmp_data = np.delete(tmp_data, 0, axis=1).tolist()
            tmp_data.append(tmp)
            pd.DataFrame(data=tmp_data).to_csv('result.csv')
        except:
            pd.DataFrame(data=tmp).to_csv('result.csv')

    def Fix_ISI(self):
        self.label_11.setText(" ")
        self.label_12.setText(" ")
        self.label_13.setText(" ")
        self.label_14.setText(" ")
        self.label_15.setText(" ")

        self.label_21.setText(" ")
        self.label_22.setText(" ")
        self.label_23.setText("+")
        self.label_24.setText(" ")
        self.label_25.setText(" ")

        self.label_31.setText(" ")
        self.label_32.setText(" ")
        self.label_33.setText(" ")
        self.label_34.setText(" ")
        self.label_35.setText(" ")

    def cue(self, num):
        if num == 1:  # 无cue
            self.Fix_ISI()
        if num == 2:  # 中央位置
            self.label_23.setText("*")
        if num == 3:  # 双提示
            self.label_13.setText("*")
            self.label_33.setText("*")
        if num == 4:  # 空间信息（下）
            self.label_33.setText("*")
        if num == 5:  # 空间信息（上）
            self.label_13.setText("*")

    def tar(self, num, event):
        self.dir = 0
        if num == 5:
            self.dir = 1
        if num == 4:
            self.dir = 2
        if num == 1 or num == 2 or num == 3:
            self.dir = random.randint(1, 2)
        self.dir_num = random.randint(1, 2)
        '''
        ←←←←←
          |
        -----
          |
        '''
        if event == 1:  # 一致刺激
            if self.dir == 1:
                if self.dir_num == 1:
                    self.label_11.setText("←")
                    self.label_12.setText("←")
                    self.label_13.setText("←")
                    self.label_14.setText("←")
                    self.label_15.setText("←")
                if self.dir_num == 2:
                    self.label_11.setText("→")
                    self.label_12.setText("→")
                    self.label_13.setText("→")
                    self.label_14.setText("→")
                    self.label_15.setText("→")
            if self.dir == 2:
                if self.dir_num == 2:
                    self.label_31.setText("→")
                    self.label_32.setText("→")
                    self.label_33.setText("→")
                    self.label_34.setText("→")
                    self.label_35.setText("→")
                if self.dir_num == 1:
                    self.label_31.setText("←")
                    self.label_32.setText("←")
                    self.label_33.setText("←")
                    self.label_34.setText("←")
                    self.label_35.setText("←")

        if event == 2:  # 中性
            if self.dir == 1:
                if self.dir_num == 1:
                    self.label_11.setText("—")
                    self.label_12.setText("—")
                    self.label_13.setText("←")
                    self.label_14.setText("—")
                    self.label_15.setText("—")
                if self.dir_num == 2:
                    self.label_11.setText("—")
                    self.label_12.setText("—")
                    self.label_13.setText("→")
                    self.label_14.setText("—")
                    self.label_15.setText("—")
            if self.dir == 2:
                if self.dir_num == 2:
                    self.label_31.setText("—")
                    self.label_32.setText("—")
                    self.label_33.setText("→")
                    self.label_34.setText("—")
                    self.label_35.setText("—")
                if self.dir_num == 1:
                    self.label_31.setText("—")
                    self.label_32.setText("—")
                    self.label_33.setText("←")
                    self.label_34.setText("—")
                    self.label_35.setText("—")

        if event == 3:  # 非一致刺激
            if self.dir == 1:
                if self.dir_num == 1:
                    self.label_11.setText("→")
                    self.label_12.setText("→")
                    self.label_13.setText("←")
                    self.label_14.setText("→")
                    self.label_15.setText("→")
                if self.dir_num == 2:
                    self.label_11.setText("←")
                    self.label_12.setText("←")
                    self.label_13.setText("→")
                    self.label_14.setText("←")
                    self.label_15.setText("←")
            if self.dir == 2:
                if self.dir_num == 2:
                    self.label_31.setText("←")
                    self.label_32.setText("←")
                    self.label_33.setText("→")
                    self.label_34.setText("←")
                    self.label_35.setText("←")
                if self.dir_num == 1:
                    self.label_31.setText("→")
                    self.label_32.setText("→")
                    self.label_33.setText("←")
                    self.label_34.setText("→")
                    self.label_35.setText("→")

    def setfont(self, num):
        self.label_11.setFont(QFont("微软雅黑", num, QFont.Bold))
        self.label_12.setFont(QFont("微软雅黑", num, QFont.Bold))
        self.label_13.setFont(QFont("微软雅黑", num, QFont.Bold))
        self.label_14.setFont(QFont("微软雅黑", num, QFont.Bold))
        self.label_15.setFont(QFont("微软雅黑", num, QFont.Bold))

        self.label_21.setFont(QFont("微软雅黑", num, QFont.Bold))
        self.label_22.setFont(QFont("微软雅黑", num, QFont.Bold))
        self.label_23.setFont(QFont("微软雅黑", num, QFont.Bold))
        self.label_24.setFont(QFont("微软雅黑", num, QFont.Bold))
        self.label_25.setFont(QFont("微软雅黑", num, QFont.Bold))

        self.label_31.setFont(QFont("微软雅黑", num, QFont.Bold))
        self.label_32.setFont(QFont("微软雅黑", num, QFont.Bold))
        self.label_33.setFont(QFont("微软雅黑", num, QFont.Bold))
        self.label_34.setFont(QFont("微软雅黑", num, QFont.Bold))
        self.label_35.setFont(QFont("微软雅黑", num, QFont.Bold))

    def on_click(self, x, y, button, pressed):
        # self.status == 3
        if pressed and self.flag:
            self.press_flag = True
            t = int(round(time.time() * 1000))
            now_Time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            self.my_tmp = []
            # if self.tri_flag:
            #     if button.name == "left":
            #         self.tri_ctrl.send(88)
            #     if button.name == "right":
            #         self.tri_ctrl.send(99)
            self.my_tmp = [now_Time, t, self.counter, "成功", self.cue_list[self.cue_num], self.dir_list[self.dir_num],
                           self.tar_list[self.tar_num], self.ms, "鼠标事件", button]
            if button.name == "left" and self.dir_num == 2:
                self.score = self.score - 5
                self.my_tmp = [now_Time, t, self.counter, "失败", self.cue_list[self.cue_num], self.dir_list[self.dir_num],
                               self.tar_list[self.tar_num], self.ms, "鼠标事件", button]
                print("扣5分：", "按了左键", self.my_tmp)
            if button.name == "right" and self.dir_num == 1:
                self.score = self.score - 5
                self.my_tmp = [now_Time, t, self.counter, "失败", self.cue_list[self.cue_num], self.dir_list[self.dir_num],
                               self.tar_list[self.tar_num], self.ms, "鼠标事件", button]
                print("扣5分：", "按了右键", self.my_tmp)

            # print('click at', x, y, button, pressed, tmp)
            if self.cue_num == 1:
                self.no_cue_list.append(self.my_tmp)
                self.no_cue_ms = self.no_cue_ms + self.ms
            if self.cue_num == 2:
                self.center_list.append(self.my_tmp)
                self.center_ms = self.center_ms + self.ms
            if self.cue_num == 4 or self.cue_num == 5:
                self.space_list.append(self.my_tmp)
                self.space_ms = self.space_ms + self.ms
            if self.tar_num == 3:
                self.no_same_list.append(self.my_tmp)
                self.no_same_ms = self.no_same_ms + self.ms
            if self.tar_num == 1:
                self.same_list.append(self.my_tmp)
                self.same_ms = self.same_ms + self.ms
            self.data.append(self.my_tmp)

            # self.cue_list = [" ", "无cue", "中央位置", "双提示", "空间信息（下）", "空间信息（上）"]
            # self.tar_list = [" ", "一致刺激", "中性", "非一致刺激"]
            # self.dir_list = [" ", "左", "右"]

            # tmp = [self.cue_list[self.cue_num], self.dir_list[self.dir_num], self.tar_list[self.tar_num], self.ms]
            self.last_count = self.counter
    def onTimerOut(self):
        self.progressBar.setValue(int(100*self.counter/int(self.LineEdit.text())))
        # QMessageBox.information(self, "提示", "请先连接设备", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        my_Time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        self.label.setText(my_Time)
        if self.counter < int(self.LineEdit.text()):

            ''' 阶段一 '''
            if self.status == 0 and self.ms == 1:
                # random int the cue and tar
                self.Fix_time = random.randint(400, 1600)
                self.cue_num = random.randint(1, 5)
                self.tar_num = random.randint(1, 3)

                if self.tri_flag:
                    self.tri_ctrl.send(7)
                if self.mss_flag:
                    tmp_name = "./outputIMG/" + str(self.counter) + "_status_1_" + str(
                        self.cue_num * 10 + self.tar_num) + ".png"
                    self.window_capture(tmp_name)

            ''' 阶段二 '''
            if self.status == 0 and self.ms == self.Fix_time:

                if self.tri_flag:
                    self.tri_ctrl.send(8)
                if self.mss_flag:
                    tmp_name = "./outputIMG/" + str(self.counter) + "_status_2_" + str(
                        self.cue_num * 10 + self.tar_num) + ".png"
                    self.window_capture(tmp_name)
                self.ms = 0
                self.status = 1
                self.cue(self.cue_num)

            ''' 阶段三 '''
            if self.status == 1 and self.ms == 100:

                if self.tri_flag:
                    self.tri_ctrl.send(9)
                if self.mss_flag:
                    tmp_name = "./outputIMG/" + str(self.counter) + "_status_3_" + str(
                        self.cue_num * 10 + self.tar_num) + ".png"
                    self.window_capture(tmp_name)
                self.Fix_ISI()
                self.ms = 0
                self.status = 2

            ''' 阶段四 开始 '''
            if self.status == 2 and self.ms == 400:
                self.press_flag = False

                if self.tri_flag:
                    self.tri_ctrl.send(10)
                if self.mss_flag:
                    tmp_name = "./outputIMG/" + str(self.counter) + "_status_4_" + str(
                        self.cue_num * 10 + self.tar_num) + ".png"
                    self.window_capture(tmp_name)
                self.tar(self.cue_num, self.tar_num)
                self.ms = 0
                self.status = 3

            ''' 阶段四 结束'''
            if self.status == 3 and self.ms == 1700:
                if self.tri_flag:
                    if not self.press_flag:
                        t = int(round(time.time() * 1000))
                        now_Time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
                        tmp = [now_Time, t, self.counter, 11, self.cue_list[self.cue_num], self.tar_list[self.tar_num],
                               "没有按下", self.ms, "鼠标事件"]
                        self.score = self.score - 5
                        print("没有按下扣5分！")
                        try:
                            df = pd.read_csv('result.csv')
                            tmp_data = np.array(df)  # 先将数据框转换为数组
                            tmp_data = np.delete(tmp_data, 0, axis=1).tolist()
                            tmp_data.append(tmp)
                            pd.DataFrame(data=tmp_data).to_csv('result.csv')
                        except:
                            pd.DataFrame(data=tmp).to_csv('result.csv')
                self.press_flag = False
                if self.tri_flag:
                    self.tri_ctrl.send(11)
                self.Fix_ISI()
                self.ms = 0
                self.status = 0
                self.counter = self.counter + 1

            if self.flag:
                self.ms = self.ms + 1
        if self.counter == int(self.LineEdit.text()):
            print("您的分数为: ", self.score)
            self.my_end = time.time()
            self.timer.stop()
            self.flag = False
            print(self.my_end - self.beg)
            if self.tri_flag:
                score_1 = self.no_cue_ms / (len(self.no_cue_list) - self.tmp_count) - self.center_ms / (len(self.center_list) - self.tmp_count)
                score_2 = self.center_ms / (len(self.center_list)-self.tmp_count) - self.space_ms / (len(self.space_list) - self.tmp_count)
                score_3 = self.no_same_ms / (len(self.no_same_list)-self.tmp_count) - self.same_ms / (len(self.same_list) - self.tmp_count)

                res = ["ANT分数：", score_1, score_2, score_3]
                print(res)
                try:
                    df = pd.read_csv('login.csv')
                    tmp_data = np.array(df)  # 先将数据框转换为数组
                    tmp_data = np.delete(tmp_data, 0, axis=1).tolist()
                    # tmp_data.extend(self.data)
                    tmp_data.append(res)
                    pd.DataFrame(data=tmp_data).to_csv('login.csv')
                except:
                    pd.DataFrame(data=self.data).to_csv('login.csv')
                try:
                    df = pd.read_csv('result.csv')
                    tmp_data = np.array(df)  # 先将数据框转换为数组
                    tmp_data = np.delete(tmp_data, 0, axis=1).tolist()

                    tmp_data.extend(self.no_cue_list)
                    tmp_data.extend(self.center_list)
                    tmp_data.extend(self.space_list)
                    tmp_data.extend(self.no_same_list)
                    tmp_data.extend(self.same_list)
                    tmp_data.append(res)
                    pd.DataFrame(data=tmp_data).to_csv('result.csv')
                except:
                    pd.DataFrame(data=['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', ]).to_csv('result.csv')
            self.close()

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
    myWin = RENZHI()
    ###
    myWin.mss_flag = False  # 截图flag
    myWin.tri_flag = True  # 脑电trigger的flag
    ###
    myWin.listener = mouse.Listener(
        on_move=None,
        on_click=myWin.on_click,
        on_scroll=None
    )
    myWin.listener.start()
    myWin.exitButton.clicked.connect(exit)
    myWin.show()
    sys.exit(app.exec_())
