# P4_RecorridoLedVectorPWM

## Descripción
Esta práctica consiste en controlar una serie de 5 LEDs utilizando modulación por ancho de pulso (PWM) en una Raspberry Pi, generando un efecto de encendido suave (fade) en secuencia. El objetivo es simular un desplazamiento de luz con variación de intensidad, en lugar de un encendido y apagado directo.

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

El sistema realiza una secuencia continua de encendido de LEDs en dos direcciones (ida y vuelta) utilizando PWM.

### Secuencia de ida
- Los LEDs aumentan y disminuyen su intensidad en orden:
  1 → 2 → 3 → 4 → 5

### Secuencia de regreso
- Luego se realiza el mismo efecto en orden inverso:
  5 → 4 → 3 → 2 → 1

---

## Características
- Uso de PWM para controlar la intensidad del LED
- Efecto de encendido y apagado suave (fade)
- Solo un LED cambia de intensidad a la vez
- Secuencia continua en ambos sentidos

---

## Resultados
- Implementación de control de intensidad mediante PWM
- Generación de efectos visuales suaves
- Uso de ciclos y listas para control secuencial

---

## Conclusión
Se logró implementar un sistema de recorrido de LEDs con control de intensidad utilizando PWM en la Raspberry Pi. Esta práctica permitió comprender la diferencia entre control digital y control por modulación, así como la generación de efectos visuales más avanzados en sistemas embebidos.
