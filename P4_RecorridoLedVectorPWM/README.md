P4_RecorridoLedVectorPWM
Descripción
Esta práctica consiste en controlar una serie de 5 LEDs utilizando modulación por ancho de pulso (PWM) en una Raspberry Pi, generando un efecto de encendido suave (fade) en secuencia. El objetivo es simular un desplazamiento de luz con variación de intensidad, en lugar de un encendido y apagado directo.

Materiales utilizados
Raspberry Pi
5 LEDs
5 resistencias (220Ω o 330Ω)
Cables jumper
Protoboard

Conexiones GPIO
LED	GPIO (BCM)	Pin físico
1	17	11
2	27	13
3	22	15
4	23	16
5	24	18
Todos los LEDs están conectados con una resistencia en serie hacia GND.

Funcionamiento del sistema
El sistema realiza una secuencia continua de encendido de LEDs en dos direcciones: ida y vuelta, utilizando PWM.

Características
Cada LED aumenta y disminuye su intensidad de forma gradual (efecto fade)
Se utiliza PWM para simular niveles de brillo
Solo un LED cambia de intensidad a la vez
La secuencia se repite de manera indefinida
Se aplica recorrido en ambos sentidos (1→5 y 5→1)

Conclusión
Se logró implementar un sistema de recorrido de LEDs con control de intensidad utilizando PWM en la Raspberry Pi. Esta práctica permitió comprender la diferencia entre control digital y control por modulación, así como la generación de efectos visuales más suaves en sistemas embebidos.
