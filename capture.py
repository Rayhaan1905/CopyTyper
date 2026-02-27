import mss
from PIL import Image
from config import MONITOR_INDEX

def capture_screen():
    with mss.mss() as sct:
        monitor = sct.monitors[MONITOR_INDEX]
        raw = sct.grab(monitor)
        img = Image.frombytes("RGB", raw.size, raw.bgra, "raw", "BGRX")
        return img

def capture_region(x, y, width, height):
    with mss.mss() as sct:
        region = {"top": y, "left": x, "width": width, "height": height}
        raw = sct.grab(region)
        img = Image.frombytes("RGB", raw.size, raw.bgra, "raw", "BGRX")
        return img