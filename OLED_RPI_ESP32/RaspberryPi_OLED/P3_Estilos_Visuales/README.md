# Práctica 3 — Texto y Manejo de Estilos Visuales

## Nombre de la Práctica
Texto, Contraste y Efectos Visuales en Pantalla OLED SSD1306

---

## 🎯 Objetivo de la Práctica

Aplicar técnicas visuales avanzadas en una pantalla OLED monocromática SSD1306 utilizando Python y Raspberry Pi.

Se implementan:

- Texto invertido
- Fondos rellenos
- Bordes
- Contraste dinámico
- Layouts complejos
- Simulación visual de estilos

---

## 🧠 Fundamento Teórico

Aunque la pantalla OLED SSD1306 es monocromática, es posible crear interfaces visualmente atractivas utilizando:

- Inversión de colores
- Rectángulos rellenos
- Contraste
- Sombras
- Bordes
- Regiones diferenciadas

La biblioteca Pillow permite manipular imágenes y renderizar texto dinámicamente.

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
P3_Estilos_Visuales/
├── README.md
├── practica3a_estilos_texto.py
├── practica3b_contraste.py
└── practica3c_tarjeta_presentacion.py
```

---

## 📄 Programas Incluidos

### practica3a_estilos_texto.py
Demostración de:
- Texto normal
- Texto invertido
- Texto con borde
- Texto con sombra

### practica3b_contraste.py
Control dinámico del brillo y contraste del SSD1306.

### practica3c_tarjeta_presentacion.py
Diseño de una interfaz tipo tarjeta de presentación.

---

## ▶️ Ejecución

```bash
python3 practica3a_estilos_texto.py
```

```bash
python3 practica3b_contraste.py
```

```bash
python3 practica3c_tarjeta_presentacion.py
```

---

## 📊 Resultados Esperados

- Visualización de estilos visuales.
- Manipulación del contraste.
- Interfaces con regiones diferenciadas.
- Uso de layouts profesionales.

---

## 🧪 Actividades Realizadas

1. Texto invertido.
2. Texto con fondo.
3. Efectos de sombra.
4. Contraste dinámico.
5. Tarjetas de presentación visuales.

---

## ✅ Buenas Prácticas Aplicadas

✔️ Código modular  
✔️ Renderizado organizado  
✔️ Separación visual por regiones  
✔️ Uso correcto de Pillow  
✔️ Interfaces gráficas legibles  

---

## 👨‍💻 Autor

Alan Fernández  
TESOEM — Sistemas Embebidos Aplicados a Móviles
