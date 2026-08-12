import serial
import cv2


class Bascula:
    def __init__(self):
        self.com_bascula = serial.Serial('/dev/tty0', baudrate=115200, timeout=1)

    def leer_bascula(self):
        self.dato_bascula = self.com_bascula.readline().decode('utf-8').strip()
        if self.dato_bascula:
            print("Dato recibido: ", self.dato_bascula)
        else:
            print("No se recibió dato de báscula")


class Camara:
    def __init__(self):
        self.captura_camara = cv2.VideoCapture(0)

    def ver_camara(self):
        self.ret, self.frame = self.captura_camara.read()  # Crea un frame con la imagen obtenida y ret es un retorno booleano que dice si la imagen se capturó o no
        # cv2.imshow("Camara Pi", frame)  # Para mostrar la imagen
