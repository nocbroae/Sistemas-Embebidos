# Práctica 1 — Texto en Pantalla OLED SSD1306

## Nombre de la Práctica
Texto Estático y Dinámico en Pantalla OLED SSD1306 con Raspberry Pi 3

---

## 🎯 Objetivo de la Práctica

Desarrollar programas en Python para desplegar texto estático y dinámico en una pantalla OLED SSD1306 utilizando Raspberry Pi 3 y comunicación I²C.

Se trabajan conceptos como:

- Sistema de coordenadas
- Tipografías
- Texto dinámico
- Renderizado de información del sistema
- Uso de la biblioteca `luma.oled`

---

## 🧠 Fundamento Teórico

La pantalla OLED SSD1306 utiliza un sistema de coordenadas donde:

- `(0,0)` se encuentra en la esquina superior izquierda.
- El eje X aumenta hacia la derecha.
- El eje Y aumenta hacia abajo.

La biblioteca Pillow trabaja en modo monocromático:

- `0` = negro
- `255` = blanco

Las fuentes pueden ser:
- Bitmap por defecto
- Fuentes TrueType (.ttf)

---

## 🧰 Materiales Utilizados

| Cantidad | Componente |
|---|---|
| 1 | Raspberry Pi 3 |
| 1 | Pantalla OLED SSD1306 I²C |
| 4 | Jumpers |
| 1 | Protoboard |
| 1 | Fuente de alimentación |

---

## 🔌 Diagrama de Conexión

| OLED SSD1306 | Raspberry Pi |
|---|---|
| VCC | 3.3V |
| GND | GND |
| SDA | GPIO2 - Pin 3 |
| SCL | GPIO3 - Pin 5 |

---

## ⚙️ Configuración del Entorno

Actualizar el sistema:

```bash
sudo apt update && sudo apt upgrade -y
```

Instalar dependencias:

```bash
sudo apt install -y python3-pip i2c-tools python3-dev
```

Instalar bibliotecas:

```bash
pip3 install luma.oled
pip3 install Pillow
pip3 install smbus2
```

Habilitar I²C:

```bash
sudo raspi-config
```

Ruta:

```txt
Interfacing Options → I2C → Enable
```

---

## 🔍 Verificación del OLED

```bash
i2cdetect -y 1
```

Dirección esperada:

```txt
0x3C
```

---

## 📁 Estructura del Proyecto

```txt
P1_Texto_Pantalla/
├── README.md
├── practica1a_texto_basico.py
├── practica1b_texto_fuentes.py
└── practica1c_info_dinamica.py
```

---

## 📄 Programas Incluidos

### practica1a_texto_basico.py
Muestra texto estático organizado en distintas posiciones.

### practica1b_texto_fuentes.py
Utiliza fuentes TrueType con distintos tamaños.

### practica1c_info_dinamica.py
Muestra información dinámica del sistema:
- Hora
- Temperatura CPU
- Dirección IP

---

## ▶️ Ejecución

Ejecutar desde terminal:

```bash
python3 practica1a_texto_basico.py
```

o

```bash
python3 practica1b_texto_fuentes.py
```

o

```bash
python3 practica1c_info_dinamica.py
```

---

## 📊 Resultados Esperados

- Visualización correcta de texto.
- Diferentes tamaños de fuente.
- Información dinámica actualizada en tiempo real.

---

## 🧪 Actividades Realizadas

1. Mostrar texto estático.
2. Utilizar fuentes TrueType.
3. Mostrar información dinámica.
4. Comprender el sistema de coordenadas.
5. Usar renderizado con Pillow.

---

## ✅ Buenas Prácticas Aplicadas

✔️ Código modular  
✔️ Uso de funciones  
✔️ Manejo de excepciones  
✔️ Separación de programas  
✔️ Uso correcto de luma.oled  

---

## 👨‍💻 Autor

Alan Fernández  
TESOEM — Sistemas Embebidos Aplicados a Móviles
