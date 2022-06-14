import os
import time
import datetime
from datetime import date, time
from datetime import datetime
from time import sleep
import numpy as np
import matplotlib.pyplot as plt
import RPi.GPIO as GPIO
import cv2
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
import mysql.connector
import conexion.py

pin = 11
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)
GPIO.output(pin, GPIO.HIGH)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
cam = cv2.VideoCapture(0)



# Creamos un login

def __init__(self):
    super(Login, self).__init__()
    loadUi("login.ui", self) #Cargamos la interfaz gráfica
    self.loginbutton.clicked.connect(self.loginfunction) #Si apretamos el boton login vamos a la función loginfunction()
    self.password.setEchoMode(QtWidgets.QLineEdit.Password)  # Hace que la contraseña se vea como puntitos
    self.createaccbutton.clicked.connect(self.gotocreate)#Si apretamos el boton createacc vamos a la función gotocreate()


def loginfunction(self):
    emailL = self.email.text()
    passwordL = self.password.text()

    with self.conexion() as mycursor:
        consulta2 =("Select usuario,contrasena from Registro where usuario=? and contrasena=? ")
        mycursor.execute(consulta2,(emailL, passwordL))

        resultado= mycursor.fetchall()

    if resultado:
        for i in resultado:
            loadUi("EFRA PON AQUÍ EL NOMBRE DE LA INTERFAZ PRINCIPAL.ui",self)


def gotocreate(self):
    createacc = CreateAcc()
    widget.addWidget(createacc)
    widget.setCurrentIndex(widget.currentIndex() + 1)


class CreateAcc(QDialog):
    def __init__(self):
        super(CreateAcc, self).__init__()
        loadUi("createacc.ui", self)
        self.signupbutton.clicked.connect(self.createaccfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpass.setEchoMode(QtWidgets.QLineEdit.Password)

    def createaccfunction(self):
        email = self.email.text()
        if self.password.text() == self.confirmpass.text():
            password = self.password.text()
            login = Login()
            widget.addWidget(login)
            widget.setCurrentIndex(widget.currentIndex() + 1)
        with self.conexion() as mycursor:
            consulta = ("INSERT INTO Registro(usuario,constrasena) VALUES(%s,%s)",(email,password)) #Insertamos los valores de email y password en nuestra tabla SQL
            mycursor.execute(consulta, (email,password))

app = QApplication(sys.argv)
mainwindow = Login()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(488)
widget.setFixedHeight(620)
widget.setFixedWidth(308)
widget.setFixedHeight(400)
widget.show()
app.exec_()


def tomar_foto():
    print("Imagen Tomada")
    GPIO.output(pin, GPIO.LOW)
    sleep(0.1)
    GPIO.output(pin, GPIO.HIGH)
    ret, image = cam.read()
    horaf = datetime.now().strftime('%H:%M:%S')
    fechaf = datetime.now().strftime("%d-%m-%y")
    onlyfilesF = next(os.walk('/home/grupo5/Desktop/Fotos'))[2]
    nf = int(len(onlyfilesF)) + 1
    cv2.imwrite("/home/grupo5/Desktop/Fotos/" + str(nf) + "_" + horaf + fechaf + ".jpg", image)


@ @-68

, 9 + 76, 6 @ @


def grabar_video():
    video_cod = cv2.VideoWriter_fourcc(*'XVID')
    video_out = cv2.VideoWriter("/home/grupo5/Desktop/Videos/" + str(nv) + "_" + horav + fechav + '.avi', video_cod, 10,
                                (640, 480))
    print("Grabando ")
    GPIO.output(pin, GPIO.LOW)
    sleep(0.1)
    GPIO.output(pin, GPIO.HIGH)
    while (True):
        ret, frame = cam.read()
        video_out.write(frame)
        if GPIO.input(16) == GPIO.LOW:
            break
    cam.release()
    video_out.release()
    print("Video Guardado en el Directorio")
