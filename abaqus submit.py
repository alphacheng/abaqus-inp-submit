# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 16:01:20 2023

@author: 2182
"""

# MyWindow.py
from PyQt5 import QtCore, QtGui, QtWidgets
import os


class NewQLineEdit(QtWidgets.QLineEdit):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setAcceptDrops(True)  # 删除没有影响，目前不确定（因为True和False测试结果一样）
        self.setDragEnabled(True)  # 删除没有影响，（因为True和False测试结果一样）

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():  # 当文件拖入此区域时为True
            event.accept()  # 接受拖入文件
        else:
            event.ignore()  # 忽略拖入文件

    def dropEvent(self, event):    # 本方法为父类方法，本方法中的event为鼠标放事件对象
        urls = [u for u in event.mimeData().urls()]  # 范围文件路径的Qt内部类型对象列表，由于支持多个文件同时拖入所以使用列表存放
        for url in urls:
            self.setText(url.path()[1:])   # 将Qt内部类型转换为字符串类型
            

            
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 400)
        Form.setAcceptDrops(True)

        self.interactive=' int'
        V_layout1=QtWidgets.QVBoxLayout(Form)
        # V_layout1.setContentsMargins(0,0,0,0)
        # V_layout1.setSpacing(0)     
         
           


        H_layout1=QtWidgets.QHBoxLayout()
        self.lineEdit_path = NewQLineEdit() # 此处更改
        # self.lineEdit.setGeometry(QtCore.QRect(70, 230, 881, 41))
        self.lineEdit_path.setAcceptDrops(True)
        self.lineEdit_path.setStyleSheet("font: 12pt \"Arial\";")
        self.lineEdit_path.setText("")
        self.lineEdit_path.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel()
        # self.label.setGeometry(QtCore.QRect(430, 160, 311, 41))
        self.label.setStyleSheet(
            "font: 12pt \"黑体\";\n"
            "font: 14pt \"微软雅黑\";"
                                )
        self.label.setObjectName("label")
        H_layout1.addWidget(self.label)  
        H_layout1.addWidget(self.lineEdit_path)
        V_layout1.addLayout(H_layout1)  



        H_layout2=QtWidgets.QHBoxLayout()
        self.label_cpus = QtWidgets.QLabel()
        # self.label_cpus.setGeometry(QtCore.QRect(70, 330, 311, 41))
        self.label_cpus.setStyleSheet(
            "font: 12pt \"黑体\";\n"
            "font: 14pt \"微软雅黑\";"
                                )
        self.label_cpus.setObjectName("label")

        self.lineEdit_cpus = QtWidgets.QLineEdit() # 此处更改
        # self.lineEdit_cpus.setGeometry(QtCore.QRect(200, 330, 100, 41))
        self.lineEdit_cpus.setAcceptDrops(False)
        self.lineEdit_cpus.setStyleSheet("font: 12pt \"Arial\";")
        self.lineEdit_cpus.setText("6")
        self.lineEdit_cpus.setObjectName("lineEdit")
        
        H_layout2.addWidget(self.label_cpus)      
        H_layout2.addWidget(self.lineEdit_cpus)
        V_layout1.addLayout(H_layout2)                



        #水平布局
        H_layout3=QtWidgets.QHBoxLayout()
 
        self.btn1=QtWidgets.QRadioButton('无交互')
        self.btn1.setStyleSheet("font: 12pt \"Arial\";")
        # 设为默认是选中状态
        #toggled是状态切换的信号
        # self.btn1.toggled.connect(self.buttonState)
        H_layout3.addWidget(self.btn1)
 
        self.btn2=QtWidgets.QRadioButton('有交互')
        self.btn2.setStyleSheet("font: 12pt \"Arial\";")        
        self.btn2.setChecked(True)
        # self.btn2.toggled.connect(self.buttonState)
        H_layout3.addWidget(self.btn2)
        V_layout1.addLayout(H_layout3)            
   
        self.btn_submit = QtWidgets.QPushButton('提交')
        self.btn_submit.clicked.connect(self.clickButton)
        self.btn_submit.setStyleSheet("font: 12pt \"Arial\";") 
        V_layout1.addWidget(self.btn_submit)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        self.btn1.clicked.connect(self.slot_radio_button_1)
        self.btn2.clicked.connect(self.slot_radio_button_2)


    def clickButton(self):
        cpus=self.lineEdit_cpus.text()
        file_path=self.lineEdit_path.text()
        inp_name=file_path.split('/')[-1]
        path=file_path.replace(inp_name,'')
        job_name=inp_name.split('.')[0]
        cmd_str='cd '+path+'&&'+path[0:2]+'&&'+'call abaqus job='+job_name+' inp='+inp_name+' cpus='+cpus+self.interactive
        # cmd_str='cd '+path+'&&'+path[0:2]+'&&'+'cd'        
        print(cmd_str)
        os.system(cmd_str)


    def slot_radio_button_1(self):
        self.interactive=' '
    def slot_radio_button_2(self):
        self.interactive=' int'


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "拖放提交inp"))
        self.label.setText(_translate("Form", "inp路径"))
        self.label_cpus.setText(_translate("Form", "cpus"))


# main.py
# 注入口文件不再注释，仅提供读者测试使用

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QCoreApplication
import os
# from MyWindow import *
class Main:

    def __init__(self, ui, root):
        QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
        self.__app = QApplication(sys.argv)
        self.__ui = ui()
        self.__root = root()

    def __close(self):
        os._exit(520)

    def __main(self):
        self.__app.setQuitOnLastWindowClosed(False)
        self.__app.lastWindowClosed.connect(self.__close)  # 设置关闭程序
        self.__ui.setupUi(self.__root)

        self.__root.show()
        sys.exit(self.__app.exec_())

    def run(self):
        self.__main()


if __name__ == '__main__':
    app = Main(Ui_Form, QWidget)
    app.run()
