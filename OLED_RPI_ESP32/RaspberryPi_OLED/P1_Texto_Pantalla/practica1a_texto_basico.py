#!/usr/bin/env python3
# practica1a_texto_basico.py
# Muestra texto estático en distintas posiciones

from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306
from luma.core.render import canvas
from PIL import ImageFont
import time


# Inicialización del dispositivo
serial = i2c(port=1, address=0x3C)
device = ssd1306(serial)

# Fuente por defecto
font_default = ImageFont.load_default()


# Dibujar contenido
with canvas(device) as draw:

    # Título
    draw.text(
        (10, 0),
        'TESOEM - OLED',
        font=font_default,
        fill=255
    )

    # Línea separadora
    draw.line(
        [(0, 12), (127, 12)],
        fill=255,
        width=1
    )

    # Información
    draw.text(
        (0, 16),
        'Alumno:',
        font=font_default,
        fill=255
    )

    draw.text(
        (50, 16),
        'Alan Fernandez',
        font=font_default,
        fill=255
    )

    draw.text(
        (0, 28),
        'Grupo:',
        font=font_default,
        fill=255
    )

    draw.text(
        (50, 28),
        '8S22',
        font=font_default,
        fill=255
    )

    draw.text(
        (0, 40),
        'Materia:',
        font=font_default,
        fill=255
    )

    draw.text(
        (50, 40),
        'Embebidos',
        font=font_default,
        fill=255
    )

    draw.text(
        (0, 52),
        'Status:',
        font=font_default,
        fill=255
    )

    draw.text(
        (50, 52),
        '[ OK ]',
        font=font_default,
        fill=255
    )

    # Mostrar durante 10 segundos
    time.sleep(10)
