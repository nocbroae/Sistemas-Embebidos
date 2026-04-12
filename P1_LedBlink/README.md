# P1_LedBlink

## Descripción
Esta práctica consiste en el control básico de un LED utilizando la Raspberry Pi. Se implementan dos versiones: una utilizando la numeración de pines BCM (GPIO) y otra utilizando la numeración física (BOARD). El objetivo es comprender el manejo de salidas digitales y las diferencias entre ambos modos.

---

## Materiales utilizados
- Raspberry Pi
- 1 LED
- 1 resistencia (220Ω o 330Ω)
- Cables jumper
- Protoboard

---

## Conexiones GPIO

### Modo BCM
| Elemento | GPIO (BCM) | Pin físico |
|----------|------------|------------|
| LED      | 18         | 12         |

### Modo BOARD
| Elemento | Pin físico |
|----------|------------|
| LED      | 12         |

---

## Funcionamiento del sistema

### Versión 1: Modo BCM
- Se utiliza la numeración de pines GPIO
- El LED se enciende y apaga cada segundo
- Se muestra el estado en la terminal (ENCENDIDO/APAGADO)
- El ciclo se repite indefinidamente

### Versión 2: Modo BOARD
- Se utiliza la numeración física de los pines
- El LED realiza un parpadeo rápido (3 veces)
- Se repite durante 10 ciclos
- Se muestra el número de ciclo en la terminal
