
# ESP32 MicroPython OLED SSD1306

Repositorio de prácticas de laboratorio para el uso de pantallas OLED SSD1306 con MicroPython en ESP32.

Este repositorio contiene ejercicios progresivos orientados al aprendizaje de:

- Comunicación I2C
- Manejo de pantallas OLED SSD1306
- Uso de FrameBuffer
- Texto y animaciones
- Scroll por software y hardware
- Inversión de colores
- Interfaces gráficas
- Gráficos vectoriales
- Carga de imágenes bitmap

---

# 📚 Contenido del Repositorio

## 🖥️ Prácticas Incluidas

| Práctica | Descripción |
|---|---|
| P1 | Texto estático y dinámico |
| P2 | Texto con scrolling |
| P3 | Inversión de colores y contraste |
| P4 | Gráficos y carga de imágenes |

---

# 🧰 Tecnologías Utilizadas

- ESP32 DevKit
- MicroPython
- Pantalla OLED SSD1306
- Comunicación I2C
- FrameBuffer

---

# 🔌 Conexión OLED ↔ ESP32

| OLED SSD1306 | ESP32 |
|---|---|
| VCC | 3V3 |
| GND | GND |
| SCL | GPIO22 |
| SDA | GPIO21 |

---

# ⚙️ Requisitos

## Instalar MicroPython en ESP32

```bash
pip install esptool
```

Flashear firmware:

```bash
esptool.py --chip esp32 erase_flash

esptool.py --chip esp32 --baud 460800 write_flash -z 0x1000 firmware.bin
```

---

## Instalar driver SSD1306

```bash
pip install mpremote

mpremote mip install ssd1306
```

---

# 📁 Estructura del Proyecto

```txt
ESP32_MicroPython_OLED/
│
├── P1_Texto_Pantalla/
├── P2_Texto_Scrolling/
├── P3_Inversion_Colores/
├── P4_Graficos_Imagenes/
│
└── README.md
```

---

# 🎯 Objetivos de Aprendizaje

- Comprender el funcionamiento del protocolo I2C.
- Manipular displays OLED SSD1306.
- Utilizar primitivas gráficas.
- Implementar interfaces gráficas embebidas.
- Aplicar buenas prácticas de programación modular.
- Trabajar con imágenes bitmap monocromáticas.

---

# ✅ Buenas Prácticas Aplicadas

✔️ Código modular  
✔️ Separación por prácticas  
✔️ Comentarios descriptivos  
✔️ Organización profesional del repositorio  
✔️ Uso de README por práctica  

---

# 👨‍💻 Autor

Alan Fernández  
TESOEM — Sistemas Embebidos Aplicados a Móviles

---

# 📖 Referencias

- MicroPython
- SSD1306 Documentation
- FrameBuffer API
- TESOEM — Sistemas Embebidos Aplicados a Móviles
