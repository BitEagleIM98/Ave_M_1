# Ave_M_1

Aplicación de sistema de inventarios y logística.

# Pasos para configuración de sistema

# Paso 1: Actualizar sistema

-sudo apt update

-sudo apt upgrade

# Paso 2: Verificar que python 3.12 o superior este einstalado en conjunto con git

-sudo apt install python3 git -y

# Paso 3: Activar servicios bluetooth

-sudo systemctl enable bluetooth

-sudo systemctl start bluetooth

# Paso 4: Instalar dependencias adicionales

-wget http://archive.ubuntu.com/ubuntu/pool/universe/p/python-sounddevice/python3-sounddevice_0.5.3-1_all.deb

-sudo apt install ./python3-sounddevice_0.5.3-1_all.deb

-sudo rm -rf python3-sounddevice_0.5.3-1_all.deb

# Paso 5: Inicializar carpetas de aplicación y glonar repositorio

-mkdir Inv_sys/git/ && cd Inv_sys/git/

-git clone git@github.com:BitEagleIM98/Ave_M_1.git

-cd Ave_M_1

# Paso 6: Dar permisos a archivo .sh e instalar requerimientos

-chmod x+ requirements.sh

-./requirements.sh

# Paso 7: Generar archivo de entorno en carpeta raíz de aplicación con variables de entorno

# Comando para correr aplicación de manera manual:

-sudo python3 app/boot.py

