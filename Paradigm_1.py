'''
Author: ProtoDrive000
Date: 2023-04-01 14:06:58
LastEditTime: 2023-04-01 14:07:02
Description: 
FilePath: \BCI_Timer\main.py
Copyright © : 2021年 赛博智能车实验室. All rights reserved. 
'''


from ui.timer_gui import Ui_MainWindow

import sys
import pandas as pd
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt, QPropertyAnimation, QRect, QEasingCurve
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import time
import pandas as pd
import numpy as np
import pyaudio
import wave


def exit():
    if myWin.exitButton.text() == "连接设备":
        if myWin.tri_flag:
            from trigger.trigger_config import TriggerConfig
            myWin.tri_ctrl = TriggerConfig().trig_ctrl
            myWin.tri_ctrl.open()
        myWin.exitButton.setText("关闭")
    else:
        myWin.close()
class TIME(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(TIME, self).__init__()
        self.tri_ctrl = None
        self.setupUi(self)
        self.setWindowTitle("BCI登录")
        self.setWindowIcon(QIcon("mylogo.jpg"))
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #self.setWindowFlags(Qt.FramelessWindowHint)  # 设置窗口标志：隐藏窗口边框
        self.resize(QDesktopWidget().screenGeometry().width(),QDesktopWidget().screenGeometry().height())  # 主窗大小
        self.setWindowFlag(Qt.WindowStaysOnTopHint, True)
        self.startButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.stopButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.resetButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.exitButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_eye.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_eye.clicked.connect(self.eye)
        self.timer = QTimer()
        self.timer.setInterval(10)  # 设置计时器的间隔，单位是毫秒
        self.timer.timeout.connect(self.onTimerOut)
        self.tri_flag = False
        self.min = 0
        self.sec = 0
        self.secondSec = 0
        self.linetext = str(self.min) + ':' + str(self.sec) + ':' + str(self.secondSec)
        self.lcd.display(self.linetext)
        self.lcd.display(str(0) + str(self.min) + ':' + str(0) + str(self.sec) + ':' + str(0) + str(self.secondSec))
        self.count = 0
        self.startButton.clicked.connect(self.start)
        self.stopButton.clicked.connect(self.stop)
        self.resetButton.clicked.connect(self.reset)
        #self.exitButton.clicked.connect(self.exit)


    def eye(self):
        if self.pushButton_eye.text()  ==  "睁眼":
            self.pushButton_eye.setText("闭眼")
        else:
            self.pushButton_eye.setText("睁眼")
    def keyPressEvent(self, QKeyEvent):
        """快捷键"""
        if QKeyEvent.key() == Qt.Key_Escape:  # esc
            sys.exit(app.exec_())
            


    def onTimerOut(self):
        if self.sec < 0:
            self.sec = 59
            self.min -= 1

        if self.secondSec < 0:
            self.secondSec = 99
            self.sec -= 1

        if self.sec == 0 and self.secondSec == 0 and self.min == 0:
            #####百位数 1是 睁眼 ；2是闭眼；
            #####个位数 0是 开始 ；1是暂停；2是结束 
            if self.tri_flag:
                try:
                    if self.pushButton_eye.text() == "睁眼":
                        self.tri_ctrl.send(102)
                    else:
                        self.tri_ctrl.send(202)
                except:
                    QMessageBox.information(self, "提示", "请先连接设备", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            self.lcd.display(str(0) + str(0) + ':' + str(0) + str(0) + ':' + str(0) + str(0))
            now_Time = time.strftime('%Y-%m-%d %H:%M:%S')
            tmp = [now_Time, '计时结束', self.pushButton_eye.text()]
            try:
                df = pd.read_csv('login.csv')
                tmp_data = np.array(df)  # 先将数据框转换为数组
                tmp_data = np.delete(tmp_data, 0, axis=1).tolist()
                tmp_data.append(tmp)
                pd.DataFrame(data=tmp_data).to_csv('login.csv')
            except:
                pd.DataFrame(data=tmp).to_csv('login.csv')
            self.timer.stop()
            chunk = 1024
            wf = wave.open('finish.wav', 'rb')
            p = pyaudio.PyAudio()
            stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                            channels=wf.getnchannels(),
                            rate=wf.getframerate(),
                            output=True)

            data = wf.readframes(chunk)

            while len(data) > 0:
                stream.write(data)
                data = wf.readframes(chunk)
            stream.stop_stream()
            stream.close()

            p.terminate()



        if self.secondSec!=100:
            if self.secondSec<10 and self.sec<10 :
                self.linetext=str(0) + str(self.min) + ':' + str(0) + str(self.sec) + ':' + str(0) + str(self.secondSec)
                self.lcd.display(self.linetext)
            elif self.secondSec>=10 and self.sec<10 :
                self.linetext=str(0) + str(self.min) + ':' +str(0) + str(self.sec) + ':' + str(self.secondSec)
                self.lcd.display(self.linetext)
            elif self.secondSec <10 and self.sec >=10:
                self.linetext=str(0) + str(self.min) + ':'+str(self.sec) + ':' + str(0)+str(self.secondSec)
                self.lcd.display(self.linetext)
            elif self.secondSec >= 10 and self.sec >=10:
                self.linetext=str(0) + str(self.min) + ':' +str(self.sec) + ':' + str(self.secondSec)
                self.lcd.display(self.linetext)
        self.secondSec -= 1



    def start(self):
        if self.sec == 0 and self.secondSec == 0 and self.min == 0:
            self.min = int(self.LineEdit.text())
        self.timer.start()  # 点击开始按钮，计时器开始运行
        now_Time = time.strftime('%Y-%m-%d %H:%M:%S')
        tmp = [now_Time, '开始计时',self.pushButton_eye.text(), self.min, self.sec, self.secondSec]
        if self.tri_flag:
            try:
                if self.pushButton_eye.text() == "睁眼":
                    self.tri_ctrl.send(100)
                else:
                    self.tri_ctrl.send(200)
            except:
                    QMessageBox.information(self, "提示", "请先连接设备", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        try:
            df = pd.read_csv('login.csv')
            tmp_data = np.array(df)  # 先将数据框转换为数组
            tmp_data = np.delete(tmp_data, 0, axis=1).tolist()
            tmp_data.append(tmp)
            pd.DataFrame(data=tmp_data).to_csv('login.csv')
        except:
            pd.DataFrame(data=tmp).to_csv('login.csv')




    def stop(self):
        self.timer.stop()
        self.startButton.setText('继续')
        now_Time = time.strftime('%Y-%m-%d %H:%M:%S')
        tmp = [now_Time, '计时暂停',self.pushButton_eye.text(), self.min, self.sec, self.secondSec]
        try:
            df = pd.read_csv('login.csv')
            tmp_data = np.array(df)  # 先将数据框转换为数组
            tmp_data = np.delete(tmp_data, 0, axis=1).tolist()
            tmp_data.append(tmp)
            pd.DataFrame(data=tmp_data).to_csv('login.csv')
        except:
            pd.DataFrame(data=tmp).to_csv('login.csv')
        if self.tri_flag:
            try:
                if self.pushButton_eye.text() == "睁眼":
                    self.tri_ctrl.send(101)
                else:
                    self.tri_ctrl.send(201)
            except:
                QMessageBox.information(self, "提示", "请先连接设备", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
    def reset(self):
        self.timer.stop()#秒表暂停
        self.sec = 0
        self.secondSec = 0
        self.min = int(self.LineEdit.text())
        now_Time = time.strftime('%Y-%m-%d %H:%M:%S')
        tmp = [now_Time, '计时复位', self.pushButton_eye.text(), self.min, self.sec, self.secondSec]
        try:
            df = pd.read_csv('login.csv')
            tmp_data = np.array(df)  # 先将数据框转换为数组
            tmp_data = np.delete(tmp_data, 0, axis=1).tolist()
            tmp_data.append(tmp)
            pd.DataFrame(data=tmp_data).to_csv('login.csv')
        except:
            pd.DataFrame(data=tmp).to_csv('login.csv')

        #lcd上的数据清零
        self.lcd.display(str(0)+str(0)+':'+str(0)+str(0)+':'+str(0)+str(0))
        self.startButton.setText('开始')






if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = TIME()
    myWin.exitButton.clicked.connect(exit)
    myWin.tri_flag = True
    myWin.show()
    sys.exit(app.exec_())


