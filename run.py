'''
Author: ProtoDrive000
Date: 2023-04-01 14:06:58
LastEditTime: 2023-04-01 19:10:03
Description: 
FilePath: \BCI_Timer\run.py
Copyright © : 2021年 赛博智能车实验室. All rights reserved. 
'''

from login import LOGIN
from Paradigm_1 import TIME
from Paradigm_2 import RENZHI
from Paradigm_3 import SART

import sys
import pandas as pd
import numpy as np
from PyQt5.QtWidgets import *
import time
from pynput import mouse
from pynput import keyboard
    
def sign_confirm():
        tmp = [login_Win.reg_name.text(), login_Win.gender.text(), login_Win.age.text(), login_Win.disease.text(), login_Win.reg_password.text()]
        flag = True
        for item in tmp:
            if item == '':
                QMessageBox.information(login_Win, "提示", "请填入完整信息", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                flag = False
        if login_Win.reg_password.text() != login_Win.password_confirm.text():
            QMessageBox.information(login_Win, "提示", "两次密码输入不符", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            flag = False
        if flag:
            now_Time = str(time.strftime('%Y-%m-%d %H:%M:%S'))
            tmp.append(now_Time)
            login_Win.data.append(tmp)
            QMessageBox.information(login_Win, "提示", "注册成功！", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            login_Win.access = True
            pd.DataFrame(data=login_Win.data).to_csv('data.csv')
            tmp2 = []
            tmp1 = [login_Win.reg_name.text(), login_Win.reg_password.text(), now_Time, '成功注册']
            tmp2.append(tmp1)
            try:
                df = pd.read_csv('login.csv')
                tmp_data = np.array(df)  # 先将数据框转换为数组
                tmp_data = np.delete(tmp_data, 0, axis=1).tolist()
                tmp_data.append(tmp1)
                pd.DataFrame(data=tmp_data).to_csv('login.csv')
            except:
                pd.DataFrame(data=tmp2).to_csv('login.csv')

            if login_Win.mode.currentText() == "失眠检测范式":
                if login_Win.checkBox_tri.isChecked():
                    time_Win.tri_flag = True
                    print("check true")
                else:
                    time_Win.tri_flag = False
                    print("check false")
                time_Win.show()
            if login_Win.mode.currentText() == "注意力ANT范式":
                ''''''
                renZ_Win.listener = mouse.Listener(
                    on_move=None,
                    on_click=renZ_Win.on_click,
                    on_scroll=None
                )
                renZ_Win.listener.start()
                ''''''
                if login_Win.checkBox_tri.isChecked():
                    renZ_Win.tri_flag = True
                    print("check true")
                else:
                    renZ_Win.tri_flag = False
                    print("check false")
                renZ_Win.show()
            if login_Win.mode.currentText() == "注意力SART范式":
                ''''''
                sart_Win.keyB_listener = keyboard.Listener(
                    on_press=sart_Win.on_press,
                )
                sart_Win.keyB_listener.start()  # 启动线程
                ''''''
                if login_Win.checkBox_tri.isChecked():
                    sart_Win.tri_flag = True
                    print("check true")
                else:
                    sart_Win.tri_flag = False
                    print("check false")
                sart_Win.show()
            login_Win.close()
def my_login():
    
        sum_data = sum(login_Win.data, [])
        try:
            location = sum_data.index(login_Win.name.text())
            print("找到账号")
            login_Win.access = True
        except:
            print("不存在此帐号")
            QMessageBox.information(login_Win, "提示", "不存在此帐号", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            login_Win.access = False
        
        if login_Win.access:    
            if sum_data[location+4] == login_Win.password.text():
                print("成功登录")
                QMessageBox.information(login_Win, "提示", "成功登录", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                now_Time = time.strftime('%Y-%m-%d %H:%M:%S')

                tmp = []
                tmp1 = [login_Win.name.text(), login_Win.password.text(), now_Time, '成功登录']
                tmp.append(tmp1)
                try:
                    df = pd.read_csv('login.csv')
                    tmp_data = np.array(df)  # 先将数据框转换为数组
                    tmp_data = np.delete(tmp_data, 0, axis=1).tolist()
                    tmp_data.append(tmp1)
                    pd.DataFrame(data=tmp_data).to_csv('login.csv')
                except:
                    pd.DataFrame(data=tmp).to_csv('login.csv')
                if login_Win.mode.currentText()=="失眠检测范式":
                    if login_Win.checkBox_tri.isChecked():
                        time_Win.tri_flag = True
                        print("check true")
                    else:
                        time_Win.tri_flag = False
                        print("check false")
                    time_Win.show()
                if login_Win.mode.currentText()=="注意力ANT范式":
                    ''''''
                    renZ_Win.listener = mouse.Listener(
                        on_move=None,
                        on_click=renZ_Win.on_click,
                        on_scroll=None
                    )
                    renZ_Win.listener.start()
                    ''''''
                    if login_Win.checkBox_tri.isChecked():
                        renZ_Win.tri_flag = True
                        print("check true")
                    else:
                        renZ_Win.tri_flag = False
                        print("check false")
                    renZ_Win.show()
                if login_Win.mode.currentText()=="注意力SART范式":
                    ''''''
                    sart_Win.keyB_listener = keyboard.Listener(
                        on_press=sart_Win.on_press,
                    )
                    sart_Win.keyB_listener.start()  # 启动线程
                    ''''''
                    if login_Win.checkBox_tri.isChecked():
                        sart_Win.tri_flag = True
                        print("check true")
                    else:
                        sart_Win.tri_flag = False
                        print("check false")
                    sart_Win.show()
                login_Win.close()
            else:
                print("密码错误")
                QMessageBox.information(login_Win, "提示", "密码错误", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                login_Win.access = False

def exit_p1():
    if time_Win.exitButton.text() == "连接设备":
        if time_Win.tri_flag:
            from trigger.trigger_config import TriggerConfig
            time_Win.tri_ctrl = TriggerConfig().trig_ctrl
            time_Win.tri_ctrl.open()
        time_Win.exitButton.setText("关闭")
    else:
        if time_Win.tri_flag:
            time_Win.tri_ctrl.close()
        time_Win.close()
        login_Win.show()


def exit_p2():
    if renZ_Win.exitButton.text() == "连接设备":
        if renZ_Win.tri_flag:
            from trigger.trigger_config import TriggerConfig
            renZ_Win.tri_ctrl = TriggerConfig().trig_ctrl
            renZ_Win.tri_ctrl.open()
        renZ_Win.exitButton.setText("开始")
    elif renZ_Win.exitButton.text() == "开始":
        renZ_Win.beg = time.time()
        renZ_Win.exitButton.setText("退出")
        renZ_Win.counter = 0
        renZ_Win.flag = True
        renZ_Win.timer.start()
    else:
        if renZ_Win.tri_flag:
            renZ_Win.tri_ctrl.close()
        renZ_Win.close()
        login_Win.show()
def exit_p3():
    if sart_Win.exitButton.text() == "连接设备":
        if sart_Win.tri_flag:
            from trigger.trigger_config import TriggerConfig
            sart_Win.tri_ctrl = TriggerConfig().trig_ctrl
            sart_Win.tri_ctrl.open()
        sart_Win.exitButton.setText("开始")
    elif sart_Win.exitButton.text() == "开始":
        sart_Win.my_beg = time.time()
        sart_Win.exitButton.setText("退出")
        sart_Win.counter = 0
        sart_Win.flag = True
        sart_Win.timer.start()
    else:
        sart_Win.exitButton.setText("")


if __name__ == "__main__":

    app = QApplication(sys.argv)
    login_Win = LOGIN()
    time_Win = TIME()
    renZ_Win = RENZHI()
    sart_Win = SART()

    login_Win.Login.clicked.connect(my_login)
    login_Win.confirm.clicked.connect(sign_confirm)
    time_Win.exitButton.clicked.connect(exit_p1)
    renZ_Win.exitButton.clicked.connect(exit_p2)
    sart_Win.exitButton.clicked.connect(exit_p3)
    login_Win.show()
    sys.exit(app.exec_())
