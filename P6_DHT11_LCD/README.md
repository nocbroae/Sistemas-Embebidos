# 🌡️ P6 - DHT11 con Pantalla LCD 16x2

Repositorio de práctica para leer temperatura y humedad con un sensor DHT11 conectado a una Raspberry Pi, mostrando los resultados en una pantalla LCD 16x2 mediante Python.

## 🎯 Objetivo General

Desarrollar una aplicación embebida básica con Raspberry Pi para leer datos ambientales usando un sensor DHT11 y mostrar los resultados en una pantalla LCD 16x2, empleando programación modular y buenas prácticas de desarrollo.

## 🧠 Competencias Desarrolladas

- Integración de sensores digitales con Raspberry Pi
- Uso de pantallas LCD 16x2 con interfaz I2C
- Uso de GPIO en Linux embebido
- Programación modular en Python
- Manejo básico de errores

## 🧰 Materiales Requeridos

| Cantidad | Componente |
|----------|------------|
| 1 | Raspberry Pi 3/4 |
| 1 | Sensor DHT11 |
| 1 | Pantalla LCD 16x2 |
| 1 | Módulo adaptador I2C para LCD |
| 1 | Resistencia 10kΩ |
| 1 | Protoboard |
| Varios | Cables jumper |
| 1 | Fuente de alimentación 5V |

## 🔌 Diagrama de Conexión

### DHT11

| DHT11 | Raspberry Pi |
|------|--------------|
| VCC | 5V - Pin físico 2 |
| GND | GND - Pin físico 6 |
| DATA | GPIO17 - Pin físico 11 |

> Se utiliza una resistencia pull-up de 10kΩ entre DATA y 5V.

### LCD 16x2 con I2C

| LCD I2C | Raspberry Pi |
|--------|--------------|
| VCC | 5V - Pin físico 2 |
| GND | GND - Pin físico 6 |
| SDA | GPIO2 - Pin físico 3 |
| SCL | GPIO3 - Pin físico 5 |

## ⚙️ Configuración del Entorno

Actualizar sistema:

```bash
sudo apt update && sudo apt upgrade -y
```

Instalar dependencias:

```bash
sudo apt install python3-pip python3-smbus i2c-tools -y
```

Instalar librerías:

```bash
pip3 install adafruit-circuitpython-dht
pip3 install RPLCD
pip3 install adafruit-blinka
```

Activar I2C:

```bash
sudo raspi-config
```

Ruta:

```txt
Interfacing Options -> I2C -> Enable
```

Verificar dirección I2C del LCD:

```bash
i2cdetect -y 1
```

Dirección común del LCD:

```txt
0x27
```

## 📁 Estructura del Proyecto

```txt
P6_DHT11_LCD/
├── README.md
├── main.py
├── sensor.py
├── display.py
└── utils.py
```

## ▶️ Ejecución

Ejecutar desde terminal:

```bash
python3 main.py
```

## 📊 Resultado Esperado

En la pantalla LCD se mostrará la temperatura y humedad:

```txt
T:25.0C
H:40.0%
```

Si ocurre un error de lectura:

```txt
Sensor
sin lectura
```

## ✅ Buenas Prácticas Aplicadas

- ✔️ Código modular
- ✔️ Separación de responsabilidades
- ✔️ Manejo de excepciones
- ✔️ Uso de clases
- ✔️ Reutilización de componentes
- ✔️ Código limpio y legible

## 👨‍💻 Autor

Alan Fernández  
Materia: Sistemas Embebidos
