# P2_SemaforoLeds

## Descripción
Esta práctica implementa un sistema de semáforo utilizando una Raspberry Pi y tres LEDs (verde, amarillo y rojo). El objetivo es simular el comportamiento real de un semáforo con tiempos definidos y una secuencia de transición en el estado amarillo.

---

##  Materiales utilizados
- Raspberry Pi
- 3 LEDs (Verde, Amarillo, Rojo)
- 3 resistencias (220Ω o 330Ω)
- Cables jumper
- Protoboard

---

##  Conexiones GPIO

| Color     | GPIO (BCM) |
|----------|------------|
| Verde    | 17         |
| Amarillo | 27         |
| Rojo     | 22         |

---

##  Funcionamiento del sistema

El semáforo funciona en el siguiente ciclo:

1.  Verde:
   - Se mantiene encendido durante 60 segundos
   - Se muestra un contador en la terminal

2.  Amarillo (transición):
   - Apagado inicial de 0.5 segundos
   - Luego realiza 3 parpadeos:
     - 1 segundo encendido
     - 0.5 segundos apagado
   - Se muestra contador en terminal

3.  Rojo:
   - Se mantiene encendido durante 45 segundos
   - Se muestra un contador en la terminal
