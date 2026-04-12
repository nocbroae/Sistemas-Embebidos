# P3_RecorridoLedVector

## Descripción
Esta práctica consiste en controlar una serie de 5 LEDs conectados a una Raspberry Pi para generar una secuencia de encendido tipo recorrido. El objetivo es simular un efecto de desplazamiento (ida y vuelta), similar a luces secuenciales, utilizando salidas digitales.

---

## Materiales utilizados
- Raspberry Pi
- 5 LEDs
- 5 resistencias (220Ω o 330Ω)
- Cables jumper
- Protoboard

---

## Conexiones GPIO

| LED | GPIO (BCM) | Pin físico |
|-----|------------|------------|
| 1   | 17         | 11         |
| 2   | 27         | 13         |
| 3   | 22         | 15         |
| 4   | 23         | 16         |
| 5   | 24         | 18         |

Todos los LEDs están conectados con una resistencia en serie hacia GND.

---

## Funcionamiento del sistema

El sistema realiza una secuencia continua de encendido de LEDs en dos direcciones:
ida y vuelta

### Características
- Cada LED permanece encendido por un corto intervalo de tiempo
- Solo un LED está encendido a la vez
- La secuencia se repite de manera indefinida

---

## Conclusión
Se logró implementar un sistema de recorrido de LEDs utilizando la Raspberry Pi, aplicando conceptos de programación como ciclos, listas y control de salidas digitales. Esta práctica permite comprender cómo generar patrones visuales secuenciales en sistemas embebidos.

---
