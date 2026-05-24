# Práctica 3 — Texto y Manejo de Colores / Inversión

## Nombre de la Práctica
Técnicas de Contraste Visual: Inversión, Regiones de Color y Efectos de Atención

---

## 🎯 Objetivo de la Práctica

Explorar las capacidades de manipulación visual del controlador SSD1306 utilizando MicroPython en ESP32.

En esta práctica se implementan:

- Inversión global de pantalla
- Fondos rectangulares
- Texto resaltado
- Efectos de alerta
- Modo oscuro y modo claro

---

## 🧠 Marco Conceptual

La pantalla OLED SSD1306 es monocromática.  
Cada píxel solo puede tener dos estados:

- `1` = encendido
- `0` = apagado

Aunque no existe color real por software, se pueden crear efectos visuales usando:

### Inversión global
Invierte todos los píxeles de la pantalla.

### Fondos rectangulares
Permite crear regiones resaltadas usando `fill_rect()`.

### Texto negro sobre fondo blanco
Se logra dibujando primero un rectángulo blanco y luego texto con color `0`.

### Parpadeo
Alternar entre fondo blanco y fondo negro permite crear alertas visuales.

### Regiones de interés
Se pueden combinar líneas, rectángulos y texto para construir interfaces simples.

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
P3_Inversion_Colores/
├── README.md
├── P3A_inversion.py
├── P3B_paneles.py
└── P3C_modo_oscuro_claro.py
```

---

## 📄 Programas Incluidos

### P3A_inversion.py
Implementa una pantalla de información y una alerta visual con parpadeo.

### P3B_paneles.py
Construye una interfaz con regiones resaltadas, barras de progreso y texto invertido.

### P3C_modo_oscuro_claro.py
Alterna entre modo oscuro y modo claro cada 2 segundos.

---

## ▶️ Ejecución

Ejecutar los archivos desde Thonny con MicroPython en ESP32.

---

## 📊 Resultados Esperados

- Visualización de mensajes con contraste.
- Alerta parpadeante.
- Panel de datos con barras de progreso.
- Alternancia entre modo oscuro y modo claro.

---

## 🧪 Actividades Realizadas

1. Implementar inversión visual.
2. Crear alertas con parpadeo.
3. Diseñar paneles con regiones resaltadas.
4. Usar barras de progreso.
5. Alternar entre modo oscuro y modo claro.

---

## ✅ Buenas Prácticas Aplicadas

✔️ Código separado por programa  
✔️ Uso de funciones  
✔️ Uso de comentarios descriptivos  
✔️ Interfaces visuales simples  
✔️ Manipulación correcta del FrameBuffer  

---

## 👨‍💻 Autor

Alan Fernández  
TESOEM — Sistemas Embebidos Aplicados a Móviles
