# Práctica 2 — Texto Scrolling en Pantalla OLED

## Nombre de la Práctica
Animación de Texto en Pantalla OLED SSD1306

---

## 🎯 Objetivo de la Práctica

Implementar diferentes técnicas de scrolling de texto utilizando una pantalla OLED SSD1306 con Raspberry Pi y Python.

Se trabaja con:

- Scrolling horizontal
- Scrolling vertical
- Scroll por hardware SSD1306
- Optimización de framerate
- Renderizado dinámico

---

## 🧠 Fundamento Teórico

El scrolling de texto se realiza desplazando continuamente la posición del texto en cada frame.

Proceso básico:

1. Dibujar el texto.
2. Cambiar posición.
3. Actualizar pantalla.
4. Repetir.

Existen dos métodos:

- Scroll por software
- Scroll por hardware del SSD1306

El scrolling por hardware reduce carga del CPU y mejora rendimiento.

---

## 🧰 Materiales Utilizados

| Cantidad | Componente |
|---|---|
| 1 | Raspberry Pi 3 |
| 1 | Pantalla OLED SSD1306 |
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

## ⚙️ Librerías Necesarias

```bash
pip3 install luma.oled
pip3 install Pillow
pip3 install smbus2
```

---

## 📁 Estructura del Proyecto

```txt
P2_Texto_Scrolling/
├── README.md
├── practica2a_scroll_horizontal.py
├── practica2b_scroll_vertical.py
└── practica2c_scroll_hardware.py
```

---

## 📄 Programas Incluidos

### practica2a_scroll_horizontal.py
Scrolling horizontal de derecha a izquierda.

### practica2b_scroll_vertical.py
Scrolling vertical estilo créditos o ticker.

### practica2c_scroll_hardware.py
Uso del scroll por hardware integrado en el SSD1306.

---

## ▶️ Ejecución

```bash
python3 practica2a_scroll_horizontal.py
```

```bash
python3 practica2b_scroll_vertical.py
```

```bash
python3 practica2c_scroll_hardware.py
```

---

## 📊 Resultados Esperados

- Texto desplazándose fluidamente.
- Animaciones dinámicas.
- Comparación entre scrolling software y hardware.

---

## 🧪 Actividades Realizadas

1. Scrolling horizontal.
2. Scrolling vertical.
3. Scroll hardware SSD1306.
4. Manipulación de frames.
5. Optimización visual.

---

## ✅ Buenas Prácticas Aplicadas

✔️ Código modular  
✔️ Animaciones optimizadas  
✔️ Uso correcto de canvas  
✔️ Manejo de renderizado  
✔️ Comentarios descriptivos  

---

## 👨‍💻 Autor

Alan Fernández  
TESOEM — Sistemas Embebidos Aplicados a Móviles
