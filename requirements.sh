#! /bin/bash
# Para dar permisos:
# chmod +x requirements.sh

echo "Actualizando repositiorios..."
echo "Instalando requerimientos..."
sudo apt install python3-dev build-essential swig liblgpio-dev -y
sudo apt install python3-dotenv -y
sudo apt install python3-numpy -y
sudo apt install python3-tflite-runtime -y
sudo apt install python3-pyserial -y
sudo apt install python3-opencv -y
sudo apt install pulseaudio pulseaudio-module-bluetooth bluez bluetooth bluez-tools pavucontrol python3-bluez sounddevice -y
sudo apt install python3-pytest -y
sudo apt install python3-pytest-cov -y
echo "Instalación completada con éxito"