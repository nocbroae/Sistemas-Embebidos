# Práctica 4 — Gráficos Simples y Carga de Imágenes

## Nombre de la Práctica
Gráficos Vectoriales, Primitivas de Dibujo y Carga de Imágenes Bitmap Monocromas

---

## 🎯 Objetivo de la Práctica

Implementar primitivas gráficas utilizando la pantalla OLED SSD1306 y MicroPython en ESP32.

Además, se trabaja con imágenes bitmap monocromas utilizando `bytearray()` y `FrameBuffer`.

---

## 🧠 Marco Conceptual

La pantalla OLED SSD1306 es monocromática (1 bit por píxel).

Cada píxel puede estar:

- Encendido (`1`)
- Apagado (`0`)

Esto permite construir:

- Líneas
- Rectángulos
- Elipses
- Barras de progreso
- Interfaces gráficas
- Imágenes bitmap

Las imágenes deben convertirse a formato monocromático antes de ser utilizadas.

---

## 🧰 Materiales Utilizados

| Cantidad | Componente |
|---|---|
| 1 | ESP32 DevKit |
| 1 | Pantalla OLED SSD1306 128x64 |
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
P4_Graficos_Imagenes/
├── README.md
├── P4A_graficos.py
├── P4B_dashboard.py
└── P4C_imagen.py
```

---

## 📄 Programas Incluidos

### P4A_graficos.py
Demostración de primitivas gráficas:
- Líneas
- Rectángulos
- Elipses
- Círculos

### P4B_dashboard.py
Dashboard gráfico con barras de progreso simulando sensores.

### P4C_imagen.py
Carga y visualización de imágenes bitmap utilizando `FrameBuffer`.

---

## ▶️ Ejecución

Ejecutar los archivos desde Thonny usando MicroPython en ESP32.

---

## 📊 Resultados Esperados

- Visualización de figuras geométricas.
- Dashboard con barras dinámicas.
- Carga de logos o imágenes monocromáticas.

---

## 🧪 Actividades Realizadas

1. Dibujar líneas y figuras.
2. Crear interfaces gráficas.
3. Implementar barras de progreso.
4. Mostrar imágenes bitmap.
5. Manipular FrameBuffer.

---

## ✅ Buenas Prácticas Aplicadas

✔️ Código modular  
✔️ Uso de funciones  
✔️ Comentarios descriptivos  
✔️ Separación de responsabilidades  
✔️ Uso correcto de FrameBuffer  

---

## 👨‍💻 Autor

Alan Fernández  
TESOEM — Sistemas Embebidos Aplicados a Móviles
