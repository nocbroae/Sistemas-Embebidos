



# P9 - Pantalla OLED con Texto Scroll

Repositorio de práctica para mostrar texto desplazable en una pantalla OLED SSD1306 conectada a una Raspberry Pi mediante Python.

## 🎯 Objetivo General

Configurar y programar una pantalla OLED utilizando Raspberry Pi y Python para mostrar texto desplazable, aplicando buenas prácticas de desarrollo de software embebido.

## 🧠 Competencias Desarrolladas

- Uso de pantalla OLED SSD1306 con Raspberry Pi
- Comunicación mediante protocolo I2C
- Visualización de texto dinámico
- Programación modular en Python
- Uso de bibliotecas Adafruit y Pillow

## 🧰 Materiales Requeridos

| Cantidad | Componente | Observaciones |
|----------|------------|---------------|
| 1 | Raspberry Pi | Recomendado Raspberry Pi 3 o 4 |
| 1 | Pantalla OLED 0.96" I2C SSD1306 | Resolución 128x64 |
| 4 | Jumpers Dupont macho-hembra | Para conexión I2C |
| 1 | Protoboard | Opcional |
| 1 | Fuente de alimentación | USB-C o MicroUSB |
| 1 | Conexión a Internet | Opcional para instalar librerías |

## 🔌 Diagrama de Conexión

| OLED SSD1306 | Raspberry Pi |
|-------------|--------------|
| VCC | 3.3V - Pin físico 1 |
| GND | GND - Pin físico 6 |
| SCL | GPIO3 - Pin físico 5 |
| SDA | GPIO2 - Pin físico 3 |

> Asegúrate de que I2C esté habilitado en la Raspberry Pi.

## ⚙️ Configuración del Entorno

Actualizar sistema:

```bash
sudo apt update && sudo apt upgrade -y
```

Habilitar I2C:

```bash
sudo raspi-config
```

Ruta:

```txt
Interfacing Options -> I2C -> Enable
```

Instalar librerías necesarias:

```bash
sudo apt install python3-pip i2c-tools -y
pip3 install adafruit-circuitpython-ssd1306
pip3 install pillow
pip3 install adafruit-blinka
```

Verificar dirección I2C:

```bash
i2cdetect -y 1
```

Dirección común esperada:

```txt
0x3c
```

## 📁 Estructura del Proyecto

```txt
P9_Pantalla_OLED_TextoScroll/
├── README.md
├── main.py
├── oled_display.py
└── config.py
```

## ▶️ Ejecución

Ejecutar desde terminal:

```bash
python3 main.py
```

## 📊 Resultado Esperado

Al ejecutar el programa, el mensaje definido en `config.py` se desplazará continuamente de derecha a izquierda en la pantalla OLED.

## 🧪 Actividades Realizadas

- Mostrar texto desplazable en pantalla OLED
- Configurar velocidad de desplazamiento
- Separar configuración y lógica en archivos diferentes
- Implementar limpieza de pantalla al finalizar

## ✅ Buenas Prácticas Aplicadas

- ✔️ Código modular
- ✔️ Separación de responsabilidades
- ✔️ Uso de constantes en archivo de configuración
- ✔️ Manejo de interrupción con teclado
- ✔️ Código limpio y legible
 

https://github.com/user-attachments/assets/888daf36-af51-4b79-824a-2bc660c9b852



## 👨‍💻 Autor

Alan Fernández  
Materia: Sistemas Embebidos
