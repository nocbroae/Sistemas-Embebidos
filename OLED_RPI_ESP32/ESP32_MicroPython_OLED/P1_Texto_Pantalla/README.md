# Práctica 1 — Texto en Pantalla OLED SSD1306

## Nombre de la Práctica
Despliegue de Texto Estático y Dinámico en Pantalla OLED SSD1306

---

## 🎯 Objetivo de la Práctica

Programar la pantalla OLED SSD1306 para mostrar información textual estática y dinámica utilizando MicroPython en ESP32, comprendiendo el sistema de coordenadas de la pantalla y el funcionamiento de la fuente bitmap 8×8 del FrameBuffer.

---

## 🧠 Marco Conceptual

La fuente integrada en MicroPython utiliza una fuente bitmap monoespaciada de 8×8 píxeles.

Esto significa que:
- Cada carácter ocupa exactamente 8×8 píxeles.
- La pantalla OLED de 128×64 px puede mostrar:
  - 16 columnas de caracteres
  - 8 filas de caracteres

### Sistema de Coordenadas

- El origen `(0,0)` se encuentra en la esquina superior izquierda.
- El eje X aumenta hacia la derecha.
- El eje Y aumenta hacia abajo.

Ejemplo:

```python
oled.text("Hola", x, y, color)
```

Donde:
- `x` = posición horizontal
- `y` = posición vertical
- `color`:
  - `1` = píxel encendido
  - `0` = píxel apagado

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

## ⚙️ Configuración del Entorno

Instalar MicroPython y el driver SSD1306.

Instalar el driver usando:

```bash
pip install mpremote
mpremote mip install ssd1306
```

---

## 📁 Estructura del Proyecto

```txt
P1_Texto_Pantalla/
├── README.md
├── P1A_texto_basico.py
├── P1B_contador.py
└── P1C_contraste.py
```

---

## 📄 Programas Incluidos

### P1A_texto_basico.py
Muestra texto estático organizado en varias líneas.

### P1B_contador.py
Actualiza un contador dinámicamente en tiempo real.

### P1C_contraste.py
Modifica el brillo de la pantalla OLED usando diferentes niveles de contraste.

---

## ▶️ Ejecución

Ejecutar desde Thonny o cargar el archivo al ESP32 y ejecutarlo.

---

## 📊 Resultados Esperados

- Visualización correcta del texto
- Actualización dinámica del contador
- Cambios visibles de brillo/contraste

---

## 🧪 Actividades Realizadas

1. Mostrar texto estático.
2. Mostrar texto dinámico.
3. Controlar el brillo de la pantalla.
4. Comprender el sistema de coordenadas.
5. Manipular el FrameBuffer del SSD1306.

---

## ✅ Buenas Prácticas Aplicadas

✔️ Código organizado  
✔️ Separación de programas  
✔️ Uso de comentarios  
✔️ Manejo correcto del display OLED  
✔️ Uso de funciones del FrameBuffer  

---
<img width="720" height="1280" alt="e21642db-749b-436c-933f-31eac960c38f" src="https://github.com/user-attachments/assets/0b2d2a90-05e7-4f57-9183-547b10edaa31" />


https://github.com/user-attachments/assets/c12d0925-c5f2-4559-ad3e-8415cbc08890



https://github.com/user-attachments/assets/c9f83a8d-2da3-4f72-b3a0-4b38af767c2c
<img width="720" height="1280" alt="26fb62ed-0946-4c0c-9238-edf3533a5cd0" src="https://github.com/user-attachments/assets/39d7e876-976a-4eef-9047-eed0e96de70d" />





## 👨‍💻 Autor

Alan Fernández  
TESOEM — Sistemas Embebidos Aplicados a Móviles
