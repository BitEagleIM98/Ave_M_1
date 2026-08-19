## Ave_M_1

Aplicación de sistema de inventarios y logística.

## Pasos para configuración de sistema

## Paso 1: Actualizar sistema

```bash
sudo apt update
```
```bash
sudo apt upgrade
```

## Paso 2: Verificar que python 3.12 o superior este instalado en conjunto con git

```bash
sudo apt install python3 git -y
```

## Paso 3: Inicializar carpetas de aplicación y clonar repositorio

```bash
mkdir -p Inv_sys/git/ && cd Inv_sys/git/
```

```bash
git clone git@github.com:BitEagleIM98/Ave_M_1.git
```

## Paso 4: Instalar dependencias adicionales

```bash
cd ..
```

```bash
pip install vosk
```

```bash
mkdir dependencias && cd dependencias
```

```bash
wget http://archive.ubuntu.com/ubuntu/pool/universe/p/python-sounddevice/python3-sounddevice_0.5.3-1_all.deb
```

```bash
wget https://alphacephei.com/vosk/models/vosk-model-small-es-0.42.zip
```

```bash
sudo apt install ./python3-sounddevice_0.5.3-1_all.deb
```

```bash
unzip vosk-model-small-es-0.42.zip
```

```bash
sudo rm -rf python3-sounddevice_0.5.3-1_all.deb
```

```bash
cd .. && cd git/Ave_M_1
```

## Paso 5: Dar permisos a archivo .sh e instalar requerimientos

```bash
chmod +x requirements.sh
```

```bash
./requirements.sh
```

## Paso 6: Activar servicios bluetooth y configurar servicios

```bash
sudo systemctl enable bluetooth
sudo systemctl start bluetooth
```

Posteriormente, configurar bluetooth para establecer una conexión.
```bash
bluetoothctl
```
dentro del control ingresar los siguientes comandos:

```bash
power on
```

```bash
agent on
```

```bash
default-agent
```

```bash
scan on
```

```bash
pair XX:XX:XX:XX:XX:XX
```

```bash
trust XX:XX:XX:XX:XX:XX
```

```bash
connect XX:XX:XX:XX:XX:XX
```

```bash
exit
```

## Paso 7: Generar archivo de entorno en carpeta raíz de aplicación

## Comando para correr aplicación de manera manual:

```bash
sudo python3 app/boot.py
```
