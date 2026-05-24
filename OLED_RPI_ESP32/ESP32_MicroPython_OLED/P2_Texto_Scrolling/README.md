# Práctica 2 — Texto con Scrolling

## Nombre de la Práctica
Animaciones de Desplazamiento de Texto por Software y por Hardware

---

## 🎯 Objetivo de la Práctica

Implementar técnicas de scrolling en la pantalla OLED SSD1306 utilizando MicroPython en ESP32.

Se desarrollan dos tipos principales de desplazamiento:

- Scrolling por software usando actualización del FrameBuffer.
- Scrolling por hardware usando comandos directos del controlador SSD1306.

---

## 🧠 Marco Conceptual

El controlador SSD1306 permite realizar desplazamiento de texto de dos maneras:

### Scrolling por Software

El texto se redibuja constantemente en diferentes posiciones del FrameBuffer.

Ventajas:
- Mayor flexibilidad.
- Permite cambiar texto, velocidad y dirección.
- Se puede personalizar fácilmente.

Desventajas:
- Mayor carga para el microcontrolador.
- Requiere actualizar la pantalla constantemente.

### Scrolling por Hardware

El desplazamiento lo realiza directamente el controlador SSD1306 mediante comandos internos.

Ventajas:
- Menor carga para el ESP32.
- El controlador OLED realiza el movimiento automáticamente.

Desventajas:
- Menos flexible.
- El contenido debe estar previamente dibujado.

---

## 🧰 Materiales Utilizados

| Cantidad | Componente |
|---|---|
| 1 | ESP32 DevKit |
| 1 | Pantalla OLED SSD1306 128x64 I2C |
| 4 | Jumpers |
| 1 | Cable USB |
| 1 | PC con Thonny IDE |

---

## 🔌 Diagrama de Conexión

| OLED SSD1306 | ESP32 |
|---|---|
| VCC | 3V3 |
| GND | GND |
| SCL | GPIO22 |
| SDA | GPIO21 |

---

## 📁 Estructura del Proyecto

```txt
P2_Texto_Scrolling/
├── README.md
├── P2A_ticker.py
├── P2B_scroll_vertical.py
└── P2C_hw_scroll.py
```

---

## 📄 Programas Incluidos

### P2A_ticker.py
Muestra un texto desplazándose horizontalmente de derecha a izquierda.

### P2B_scroll_vertical.py
Muestra una lista de noticias o datos simulados desplazándose verticalmente hacia arriba.

### P2C_hw_scroll.py
Utiliza comandos directos del SSD1306 para activar el scroll horizontal por hardware.

---

## ▶️ Ejecución

Ejecutar los archivos desde Thonny con MicroPython en ESP32.

También se pueden subir al dispositivo como archivos `.py` y ejecutarlos desde el entorno MicroPython.

---

## 📊 Resultados Esperados

- Texto desplazándose horizontalmente.
- Lista de información desplazándose verticalmente.
- Scroll por hardware activado desde comandos I2C.

---

## 🧪 Actividades Realizadas

1. Crear un ticker de texto horizontal.
2. Crear un scroll vertical tipo noticias.
3. Activar scroll horizontal por hardware.
4. Comparar scroll por software y scroll por hardware.
5. Manipular posiciones y tiempos de actualización.

---

## ✅ Buenas Prácticas Aplicadas

✔️ Código separado por programa  
✔️ Uso de comentarios descriptivos  
✔️ Control de velocidad con temporizadores  
✔️ Uso del FrameBuffer  
✔️ Uso de comandos internos del SSD1306  

---

## 👨‍💻 Autor

Alan Fernández  
TESOEM — Sistemas Embebidos Aplicados a Móviles
