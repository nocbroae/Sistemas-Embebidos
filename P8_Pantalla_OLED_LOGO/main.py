from display_manager import OLEDDisplay
from utils import get_timestamp
import time
import os


def main():
    oled = OLEDDisplay()

    oled.show_text("Inicializando...")
    time.sleep(1)

    logo_path = "assets/logo.pbm"

    if os.path.exists(logo_path):
        oled.show_logo(logo_path)
        time.sleep(2)
    else:
        oled.show_text("Logo no\nencontrado")
        time.sleep(2)

    try:
        while True:
            now = get_timestamp()
            oled.show_text(f"Hora:\n{now}")
            time.sleep(1)

    except KeyboardInterrupt:
        oled.clear()
        oled.update()
        print("Programa finalizado.")


if __name__ == "__main__":
    main()
