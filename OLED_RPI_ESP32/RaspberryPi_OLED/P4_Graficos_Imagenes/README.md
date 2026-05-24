# Práctica 4 — Gráficos y Carga de Imágenes

## Nombre de la Práctica
Gráficos Vectoriales y Visualización de Imágenes en Pantalla OLED SSD1306

---

## 🎯 Objetivo de la Práctica

Implementar primitivas gráficas y visualización de imágenes utilizando Python y Raspberry Pi con una pantalla OLED SSD1306.

Se trabajan:

- Líneas
- Rectángulos
- Círculos
- Arcos
- Polígonos
- Conversión de imágenes
- Slideshow animado

---

## 🧠 Fundamento Teórico

La biblioteca Pillow permite dibujar primitivas gráficas mediante `ImageDraw`.

Las imágenes RGB deben convertirse a:

```txt
Modo monocromático 1-bit
```

para ser compatibles con el SSD1306.

La calidad depende de:
- Contraste
- Umbralización
- Resolución

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
P4_Graficos_Imagenes/
├── README.md
├── practica4a_primitivas.py
├── practica4b_carga_imagen.py
└── practica4c_slideshow.py
```

---

## 📄 Programas Incluidos

### practica4a_primitivas.py
Demostración de primitivas gráficas:
- Líneas
- Rectángulos
- Círculos
- Reloj analógico

### practica4b_carga_imagen.py
Carga y conversión de imágenes externas al formato OLED.

### practica4c_slideshow.py
Presentación animada con múltiples pantallas y efectos visuales.

---

## ▶️ Ejecución

```bash
python3 practica4a_primitivas.py
```

```bash
python3 practica4b_carga_imagen.py
```

```bash
python3 practica4c_slideshow.py
```

---

## 📊 Resultados Esperados

- Renderizado de gráficos.
- Visualización de imágenes monocromáticas.
- Animaciones y efectos dinámicos.
- Interfaces gráficas OLED.

---

## 🧪 Actividades Realizadas

1. Dibujar primitivas gráficas.
2. Crear reloj analógico.
3. Convertir imágenes a monocromático.
4. Mostrar imágenes en OLED.
5. Implementar slideshow animado.

---

## ✅ Buenas Prácticas Aplicadas

✔️ Código modular  
✔️ Uso de funciones  
✔️ Renderizado optimizado  
✔️ Conversión correcta de imágenes  
✔️ Uso profesional de Pillow  

---

## 👨‍💻 Autor

Alan Fernández  
TESOEM — Sistemas Embebidos Aplicados a Móviles
