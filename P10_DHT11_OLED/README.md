# P10 - DHT11 OLED

Repositorio de práctica para medir temperatura y humedad con un sensor DHT11 y mostrar los datos en una pantalla OLED SSD1306 conectada a una Raspberry Pi.

## 🎯 Objetivo

Configurar y utilizar un sensor DHT11 para medir temperatura y humedad, mostrando los datos en tiempo real en una pantalla OLED con iconos representativos.

## 🧠 Competencias Desarrolladas

- Integración de sensor DHT11 con Raspberry Pi
- Uso de pantalla OLED SSD1306 mediante I2C
- Visualización de datos ambientales
- Programación modular en Python
- Manejo de imágenes con Pillow

## 🧰 Materiales Requeridos

| Cantidad | Componente |
|----------|------------|
| 1 | Raspberry Pi 3B+, 4 o Zero W |
| 1 | Sensor DHT11 |
| 1 | Pantalla OLED 128x64 SSD1306 |
| 1 | Protoboard |
| Varios | Jumpers |
| 1 | Fuente de alimentación 5V |
| 2 | Iconos PNG de temperatura y humedad |

## 🔌 Diagrama de Conexión

### DHT11

| DHT11 | Raspberry Pi |
|------|--------------|
| VCC | 5V |
| GND | GND |
| DATA | GPIO17 |

### OLED SSD1306 I2C

| OLED | Raspberry Pi |
|------|--------------|
| VCC | 3.3V |
| GND | GND |
| SCL | GPIO3 - SCL |
| SDA | GPIO2 - SDA |

## ⚙️ Instalación de Librerías

Actualizar sistema:

```bash
sudo apt update && sudo apt install -y python3-pip libgpiod2 i2c-tools
```

Instalar librerías:

```bash
pip3 install adafruit-circuitpython-dht
pip3 install adafruit-circuitpython-ssd1306
pip3 install pillow
pip3 install adafruit-blinka
```

Verificar OLED por I2C:

```bash
i2cdetect -y 1
```

Dirección común:

```txt
0x3c
```

## 📁 Estructura del Proyecto

```txt
P10_DHT11_OLED/
├── README.md
├── main.py
├── sensors/
│   ├── __init__.py
│   └── dht11_reader.py
├── display/
│   ├── __init__.py
│   ├── oled_display.py
│   └── icons/
│       ├── temp.png
│       └── humidity.png
└── utils/
    ├── __init__.py
    └── data_logger.py
```

## 🖼️ Iconos

Los iconos deben colocarse en:

```txt
display/icons/temp.png
display/icons/humidity.png
```

Se recomienda usar imágenes de 16x16 píxeles en formato PNG.

## ▶️ Ejecución

Ejecutar desde terminal:

```bash
python3 main.py
```

## 📊 Resultado Esperado

La pantalla OLED mostrará la temperatura y humedad medidas por el sensor DHT11.

Ejemplo:

```txt
Temp: 25.0 C
Hum: 40.0 %
```

## 🧪 Actividades Realizadas

- Lectura del sensor DHT11
- Visualización de temperatura en OLED
- Visualización de humedad en OLED
- Uso de iconos para representar los datos
- Organización del proyecto en carpetas

## ✅ Buenas Prácticas Aplicadas

- ✔️ Código modular
- ✔️ Separación de lógica de sensor y pantalla
- ✔️ Manejo de errores del sensor
- ✔️ Uso de clases
- ✔️ Estructura escalable de carpetas
  <img width="1280" height="720" alt="e89b4dd7-108b-4a76-adc4-f5bbb8d45003" src="https://github.com/user-attachments/assets/b14f2407-c4e7-4d2a-b3c4-cc541600f1ab" />


## 👨‍💻 Autor

Alan Fernández  
Materia: Sistemas Embebidos
