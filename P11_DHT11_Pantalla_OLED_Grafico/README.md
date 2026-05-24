# P11 - DHT11 Pantalla OLED Grafico

Repositorio de práctica para visualizar temperatura y humedad en tiempo real usando un sensor DHT11 y una pantalla OLED SSD1306 con gráficas dinámicas en Raspberry Pi.

## 🎯 Objetivo

Implementar un sistema de monitoreo ambiental utilizando un sensor DHT11 y una pantalla OLED SSD1306 para visualizar datos en tiempo real mediante gráficos e iconos.

## 🧠 Competencias Desarrolladas

- Lectura de sensores ambientales
- Uso de pantalla OLED SSD1306
- Programación modular en Python
- Visualización gráfica en tiempo real
- Manejo de imágenes BMP
- Manejo de excepciones

## 🛠️ Materiales Requeridos

| Cantidad | Componente |
|----------|------------|
| 1 | Raspberry Pi |
| 1 | Sensor DHT11 |
| 1 | Pantalla OLED SSD1306 128x64 |
| 1 | Protoboard |
| Varios | Jumpers |
| 1 | Fuente de alimentación |
| 2 | Íconos BMP de temperatura y humedad |

## 🔌 Diagrama de Conexión

### DHT11

| DHT11 | Raspberry Pi |
|------|--------------|
| VCC | 3.3V |
| DATA | GPIO17 |
| GND | GND |

### OLED SSD1306

| OLED | Raspberry Pi |
|------|--------------|
| VCC | 3.3V |
| GND | GND |
| SCL | GPIO3 - SCL |
| SDA | GPIO2 - SDA |

## ⚙️ Instalación de Dependencias

Actualizar sistema:

```bash
sudo apt update
sudo apt install python3-pip libgpiod2 -y
```

Instalar librerías:

```bash
pip3 install adafruit-circuitpython-dht
pip3 install adafruit-circuitpython-ssd1306
pip3 install pillow
```

## 📁 Estructura del Proyecto

```txt
P11_DHT11_Pantalla_OLED_Grafico/
├── README.md
├── main.py
├── config.py
├── sensor_dht.py
├── oled_visualizer.py
├── utils.py
└── icons/
    ├── temp.bmp
    └── hum.bmp
```

## 🖼️ Íconos

Los iconos deben colocarse en:

```txt
icons/temp.bmp
icons/hum.bmp
```

Formato recomendado:

- BMP
- Blanco y negro
- 24x24 píxeles

## ▶️ Ejecución

Ejecutar desde terminal:

```bash
python3 main.py
```

## 📊 Resultado Esperado

La pantalla OLED mostrará:

- Temperatura
- Humedad
- Íconos animados
- Gráficas en tiempo real

## 🧪 Actividades Realizadas

- Lectura del sensor DHT11
- Visualización gráfica en OLED
- Historial dinámico de datos
- Animación básica de iconos
- Modularización del sistema

## ✅ Buenas Prácticas Aplicadas

- ✔️ Código orientado a objetos
- ✔️ Separación de responsabilidades
- ✔️ Manejo de excepciones
- ✔️ Código reutilizable
- ✔️ Estructura escalable
<img width="720" height="1280" alt="8554d580-0356-4df5-b355-83a198ecd2bd" src="https://github.com/user-attachments/assets/f8aa6758-c5b5-44e9-9823-24ef699d2010" />

## 👨‍💻 Autor

Alan Fernández  
Materia: Sistemas Embebidos
