import os
import board
import busio
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont


class OLEDDisplay:
    def __init__(self, width=128, height=64):
        self.width = width
        self.height = height

        i2c = busio.I2C(board.SCL, board.SDA)

        self.display = adafruit_ssd1306.SSD1306_I2C(
            width,
            height,
            i2c
        )

        self.display.fill(0)
        self.display.show()

        self.font = ImageFont.load_default()
        self.temp_icon = None
        self.humidity_icon = None

        self.load_icons()

    def load_icons(self):
        base_path = os.path.dirname(__file__)
        icons_path = os.path.join(base_path, "icons")

        temp_path = os.path.join(icons_path, "temp.png")
        humidity_path = os.path.join(icons_path, "humidity.png")

        if os.path.exists(temp_path):
            self.temp_icon = Image.open(temp_path).resize((16, 16)).convert("1")

        if os.path.exists(humidity_path):
            self.humidity_icon = Image.open(humidity_path).resize((16, 16)).convert("1")

    def update(self, temperature, humidity):
        image = Image.new("1", (self.width, self.height))
        draw = ImageDraw.Draw(image)

        if self.temp_icon:
            image.paste(self.temp_icon, (0, 4))
        else:
            draw.text((0, 4), "T", font=self.font, fill=255)

        draw.text(
            (22, 4),
            f"Temp: {temperature:.1f} C",
            font=self.font,
            fill=255
        )

        if self.humidity_icon:
            image.paste(self.humidity_icon, (0, 32))
        else:
            draw.text((0, 32), "H", font=self.font, fill=255)

        draw.text(
            (22, 32),
            f"Hum: {humidity:.1f} %",
            font=self.font,
            fill=255
        )

        self.display.image(image)
        self.display.show()

    def show_error(self):
        image = Image.new("1", (self.width, self.height))
        draw = ImageDraw.Draw(image)

        draw.text((10, 20), "Error sensor", font=self.font, fill=255)
        draw.text((10, 35), "Sin lectura", font=self.font, fill=255)

        self.display.image(image)
        self.display.show()

    def clear(self):
        self.display.fill(0)
        self.display.show()
