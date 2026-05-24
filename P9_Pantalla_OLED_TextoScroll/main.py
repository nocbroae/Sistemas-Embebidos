from oled_display import OLEDScroller
from config import MESSAGE


def main():
    scroller = OLEDScroller()

    try:
        while True:
            scroller.scroll_text(MESSAGE)

    except KeyboardInterrupt:
        scroller.clear()
        print("\nEjecución finalizada por el usuario.")


if __name__ == "__main__":
    main()
