#!/usr/bin/env python3
# practica4b_carga_imagen.py

from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306

from PIL import Image
from PIL import ImageDraw

import time
import os


# Inicialización
serial = i2c(port=1, address=0x3C)
device = ssd1306(serial)


def cargar_y_mostrar(ruta_imagen):

    if not os.path.exists(ruta_imagen):

        print(f'ERROR: No existe {ruta_imagen}')
        return

    # Cargar imagen
    img_original = Image.open(ruta_imagen)

    print(f'Imagen cargada: {img_original.size}')

    # Redimensionar
    img_resized = img_original.resize(
        (device.width, device.height),
        Image.Resampling.LANCZOS
    )

    # Escala de grises
    img_gray = img_resized.convert('L')

    # Convertir a monocromático
    img_mono = img_gray.point(
        lambda x: 255 if x > 128 else 0,
        '1'
    )

    # Mostrar
    device.display(img_mono)

    print('Imagen mostrada.')


def generar_imagen_prueba():

    img = Image.new('L', (128, 64), 0)

    draw = ImageDraw.Draw(img)

    # Patrón ajedrez
    for y in range(0, 64, 8):

        for x in range(0, 128, 8):

            if (x // 8 + y // 8) % 2 == 0:

                draw.rectangle(
                    [(x, y), (x + 7, y + 7)],
                    fill=200
                )

    # Logo T
    draw.rectangle([(50, 10), (78, 20)], fill=255)

    draw.rectangle([(60, 10), (68, 55)], fill=255)

    ruta = '/tmp/prueba_oled.png'

    img.save(ruta)

    return ruta


ruta = '/tmp/mi_imagen.png'

if not os.path.exists(ruta):

    print('Generando imagen de prueba...')

    ruta = generar_imagen_prueba()


cargar_y_mostrar(ruta)

time.sleep(10)

device.cleanup()
