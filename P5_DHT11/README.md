# 🌡️ P5 - Lectura de Temperatura y Humedad con DHT11 y Raspberry Pi

Repositorio de práctica para la lectura de temperatura y humedad utilizando un sensor DHT11 conectado a una Raspberry Pi mediante Python.

---

# 📌 Objetivo

Configurar un sistema embebido basado en Raspberry Pi para la lectura de datos de temperatura y humedad utilizando el sensor DHT11, aplicando buenas prácticas de programación como:

- Modularidad
- Reutilización de código
- Manejo de errores
- Separación de responsabilidades

---

# 🧠 Competencias Desarrolladas

- Integración de sensores digitales con Raspberry Pi
- Uso de GPIO en Linux embebido
- Lectura de datos ambientales
- Uso de bibliotecas Python
- Programación modular en Python

---

# 📦 Materiales Utilizados

| Cantidad | Componente | Descripción |
|----------|-------------|-------------|
| 1 | Raspberry Pi 3/4 | Con Raspberry Pi OS |
| 1 | Sensor DHT11 | Sensor digital de temperatura y humedad |
| 1 | Resistencia 10kΩ | Pull-up para línea de datos |
| 1 | Protoboard | Conexiones |
| 3 | Cables jumper | Macho-hembra |
| 1 | Fuente 5V | Alimentación Raspberry Pi |

---

# 🔌 Diagrama de Conexión

## Pinout del DHT11

| DHT11 | Raspberry Pi |
|-------|---------------|
| VCC | Pin 2 (5V) |
| DATA | GPIO4 - Pin 7 |
| GND | Pin 6 (GND) |

⚠️ Se utiliza una resistencia pull-up de 10kΩ entre DATA y VCC.

---

# ⚙️ Configuración del Entorno

## 1. Actualizar sistema

```bash
sudo apt update && sudo apt upgrade -y
```

## 2. Instalar dependencias

```bash
sudo apt install -y python3-pip python3-dev libgpiod2
```

## 3. Instalar librerías necesarias

```bash
pip3 install adafruit-circuitpython-dht
pip3 install --upgrade setuptools
```

---

# 📁 Estructura del Proyecto

```txt
dht11_lab/
├── dht_reader.py
├── sensor_utils.py
└── main.py
```

---

# 🧾 Código Fuente

## sensor_utils.py

```python
import adafruit_dht
import board

class DHT11Sensor:

    def __init__(self, pin=board.D4):
        self.sensor = adafruit_dht.DHT11(pin)

    def read(self):
        try:
            temperature = self.sensor.temperature
            humidity = self.sensor.humidity

            if temperature is None or humidity is None:
                raise ValueError("Valores nulos recibidos")

            return temperature, humidity

        except RuntimeError:
            return None, None

    def close(self):
        self.sensor.exit()
```

---

## dht_reader.py

```python
from sensor_utils import DHT11Sensor
import time

def read_sensor_continuous(interval=2, iterations=10):

    sensor = DHT11Sensor()

    try:
        for i in range(iterations):

            temperature, humidity = sensor.read()

            if temperature is not None:
                print(f"[{i+1}] Temp: {temperature:.1f}°C  Hum: {humidity:.1f}%")

            else:
                print(f"[{i+1}] Error al leer el sensor.")

            time.sleep(interval)

    finally:
        sensor.close()
```

---

## main.py

```python
from dht_reader import read_sensor_continuous

if __name__ == "__main__":

    print("Iniciando lectura del DHT11...\n")

    read_sensor_continuous()
```

---

# ▶️ Ejecución

Ejecutar desde terminal:

```bash
python3 main.py
```

---

# 📊 Resultado Esperado

```txt
Iniciando lectura del DHT11...

[1] Temp: 25.0°C Hum: 40.0%
[2] Temp: 25.0°C Hum: 41.0%
[3] Error al leer el sensor.
[4] Temp: 25.1°C Hum: 40.5%
```

---

# ✅ Buenas Prácticas Aplicadas

- ✔️ Código modular
- ✔️ Reutilización de componentes
- ✔️ Manejo de excepciones
- ✔️ Separación de responsabilidades
- ✔️ Código legible y documentado

---

# 📸 Evidencias

## Conexión del circuito

Agregar imagen en:

```txt
img/conexion.jpg
```

## Funcionamiento

Agregar imagen en:

```txt
img/funcionando.jpg
```

---

# 👨‍💻 Autor

**Alan Fernández**  
Materia: Sistemas Embebidos
