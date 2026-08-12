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

## Paso 3: Activar servicios bluetooth

```bash
sudo systemctl enable bluetooth
sudo systemctl start bluetooth
```

## Paso 4: Instalar dependencias adicionales

```bash
wget http://archive.ubuntu.com/ubuntu/pool/universe/p/python-sounddevice/python3-sounddevice_0.5.3-1_all.deb
```

```bash
sudo apt install ./python3-sounddevice_0.5.3-1_all.deb
```

```bash
sudo rm -rf python3-sounddevice_0.5.3-1_all.deb
```

## Paso 5: Inicializar carpetas de aplicación y clonar repositorio

```bash
mkdir Inv_sys/git/ && cd Inv_sys/git/
```

```bash
git clone git@github.com:BitEagleIM98/Ave_M_1.git
```

```bash
cd Ave_M_1
```

## Paso 6: Dar permisos a archivo .sh e instalar requerimientos

```bash
chmod x+ requirements.sh
```

```bash
./requirements.sh
```
## Paso 7: Generar archivo de entorno en carpeta raíz de aplicación

## Comando para correr aplicación de manera manual:

```bash
sudo python3 app/boot.py
```
