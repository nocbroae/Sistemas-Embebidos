# RaspberryPi_OLED

Repositorio de prácticas de laboratorio para el uso de pantallas OLED SSD1306 con Raspberry Pi 3 utilizando Python y la biblioteca `luma.oled`.

Basado en el manual de prácticas de Sistemas Embebidos Aplicados a Móviles del TESOEM.

---

# 📚 Contenido del Repositorio

## 🖥️ Prácticas Incluidas

| Práctica | Descripción |
|---|---|
| P1 | Texto estático y dinámico en pantalla OLED |
| P2 | Texto scrolling por software y hardware |
| P3 | Estilos visuales, contraste e inversión |
| P4 | Gráficos e imágenes en pantalla OLED |

---

# 🧠 Temas Aprendidos

- Comunicación I²C
- Uso de pantallas OLED SSD1306
- Programación en Python
- Uso de la biblioteca `luma.oled`
- Manipulación de imágenes con Pillow
- Texto scrolling
- Renderizado gráfico
- Interfaces gráficas embebidas
- Animaciones OLED
- Conversión de imágenes monocromáticas

---

# 🧰 Tecnologías Utilizadas

- Raspberry Pi 3
- Raspberry Pi OS
- Python 3
- luma.oled
- Pillow (PIL)
- smbus2
- I²C

---

# 🔌 Conexión OLED ↔ Raspberry Pi

| OLED SSD1306 | Raspberry Pi |
|---|---|
| VCC | 3.3V (Pin 1) |
| GND | GND (Pin 6) |
| SDA | GPIO2 SDA1 (Pin 3) |
| SCL | GPIO3 SCL1 (Pin 5) |

⚠️ Utilizar únicamente 3.3V para evitar daños en el display OLED.

---

# ⚙️ Configuración del Entorno

## Habilitar I²C

```bash
sudo raspi-config
```

Ir a:

```txt
Interfacing Options → I2C → Enable
```

Reiniciar la Raspberry Pi:

```bash
sudo reboot
```

---

# 📦 Instalación de Dependencias

Actualizar el sistema:

```bash
sudo apt update && sudo apt upgrade -y
```

Instalar herramientas necesarias:

```bash
sudo apt install -y i2c-tools python3-pip python3-dev
sudo apt install -y libfreetype6-dev libjpeg-dev zlib1g-dev
```

Instalar bibliotecas Python:

```bash
pip3 install luma.oled
pip3 install Pillow
pip3 install smbus2
```

---

# 🔍 Verificación del Display OLED

Escanear dispositivos I²C:

```bash
i2cdetect -y 1
```

Salida esperada:

```txt
3c
```

o

```txt
3d
```

---

# 📁 Estructura del Proyecto

```txt
RaspberryPi_OLED/
│
├── P1_Texto_Pantalla/
├── P2_Texto_Scrolling/
├── P3_Estilos_Visuales/
├── P4_Graficos_Imagenes/
│
└── README.md
```

---

# 🎯 Objetivos de Aprendizaje

- Configurar el bus I²C en Raspberry Pi.
- Utilizar pantallas OLED SSD1306.
- Crear interfaces gráficas simples.
- Mostrar texto estático y dinámico.
- Implementar animaciones scrolling.
- Dibujar primitivas gráficas.
- Cargar imágenes monocromáticas.
- Aplicar programación modular en Python.

---

# ✅ Buenas Prácticas Aplicadas

✔️ Código modular  
✔️ Separación por prácticas  
✔️ Organización profesional del repositorio  
✔️ Uso de README por práctica  
✔️ Comentarios descriptivos  
✔️ Manejo básico de errores  

---

# 👨‍💻 Autor

Alan Fernández  
TESOEM — Sistemas Embebidos Aplicados a Móviles

---

# 📖 Referencias

- Raspberry Pi OS
- Python 3
- luma.oled
- Pillow
- SSD1306 Documentation
- TESOEM — Sistemas Embebidos Aplicados a Móviles
