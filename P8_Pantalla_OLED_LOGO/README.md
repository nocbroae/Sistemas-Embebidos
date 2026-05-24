# P8 - Pantalla OLED con LOGO

Repositorio de práctica para utilizar una pantalla OLED SSD1306 con Raspberry Pi mediante Python, mostrando texto, hora actual y un logo en pantalla.

## 🎯 Objetivo

Configurar y utilizar una pantalla OLED basada en el controlador SSD1306 con Raspberry Pi, aplicando programación modular para mostrar información básica como texto, símbolos, valores dinámicos y un logo.

## 🧠 Competencias Desarrolladas

- Uso de pantalla OLED SSD1306 con Raspberry Pi
- Comunicación mediante protocolo I2C
- Programación modular en Python
- Manejo de imágenes en pantalla OLED
- Uso de bibliotecas Adafruit y Pillow

## 📦 Materiales Utilizados

| Cantidad | Componente | Descripción |
|----------|------------|-------------|
| 1 | Raspberry Pi 3/4 o Zero W | Con Raspberry Pi OS |
| 1 | Pantalla OLED 0.96" SSD1306 | Resolución 128x64, interfaz I2C |
| 1 | Protoboard | Para conexión |
| Varios | Cables jumper | Para conexiones |
| 1 | Fuente de alimentación | Micro-USB o USB-C |

## 🔌 Diagrama de Conexión

| OLED I2C | Raspberry Pi |
|---------|--------------|
| VCC | Pin físico 1 - 3.3V |
| GND | Pin físico 6 - GND |
| SCL | Pin físico 5 - GPIO3 |
| SDA | Pin físico 3 - GPIO2 |

## ⚙️ Configuración del Sistema

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

Instalar dependencias:

```bash
sudo apt install python3-pip i2c-tools -y
```

Instalar bibliotecas necesarias:

```bash
pip3 install adafruit-circuitpython-ssd1306
pip3 install adafruit-blinka
pip3 install pillow
```

Verificar conexión I2C:

```bash
i2cdetect -y 1
```

Dirección común esperada:

```txt
0x3c
```

## 📁 Estructura del Proyecto

```txt
P8_Pantalla_OLED_LOGO/
├── README.md
├── main.py
├── display_manager.py
├── utils.py
├── convertir_logo.py
└── assets/
    └── logo.pbm
```

## 🖼️ Conversión de Logo

Para convertir una imagen PNG o JPG a formato PBM:

```bash
python3 convertir_logo.py
```

El archivo generado debe quedar en:

```txt
assets/logo.pbm
```

## ▶️ Ejecución

Ejecutar desde terminal:

```bash
python3 main.py
```

## 📊 Resultado Esperado

La pantalla OLED mostrará:

```txt
Inicializando...
```

Después mostrará el logo y finalmente actualizará la hora en tiempo real.

## 🧪 Actividades Realizadas

- Mostrar texto en pantalla OLED
- Mostrar un logo en formato PBM
- Actualizar hora en tiempo real
- Organizar el código por módulos

## ✅ Buenas Prácticas Aplicadas

- ✔️ Código modular
- ✔️ Uso de clases y encapsulación
- ✔️ Separación lógica en archivos
- ✔️ Reutilización de componentes
- ✔️ Código claro y legible
- <img width="1280" height="720" alt="image" src="https://github.com/user-attachments/assets/13665383-218e-43ee-8469-3812928e7f0f" />


## 👨‍💻 Autor

Alan Fernández  
Materia: Sistemas Embebidos
