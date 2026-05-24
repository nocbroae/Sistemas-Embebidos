from RPLCD.i2c import CharLCD


class LCDDisplay:
    def __init__(self, address=0x27):
        self.lcd = CharLCD("PCF8574", address)
        self.lcd.clear()

    def show_message(self, line1, line2=""):
        self.lcd.clear()
        self.lcd.write_string(str(line1).ljust(16)[:16])

        if line2:
            self.lcd.crlf()
            self.lcd.write_string(str(line2).ljust(16)[:16])

    def clear(self):
        self.lcd.clear()
