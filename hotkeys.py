from pynput import keyboard
from config import CAPTURE_HOTKEY, TYPE_HOTKEY, CANCEL_HOTKEY

class HotkeyManager:
    def __init__(self, on_capture, on_type, on_cancel):
        self.on_capture = on_capture
        self.on_type    = on_type
        self.on_cancel  = on_cancel
        self._listener  = None

    def start(self):
        hotkeys = {
            CAPTURE_HOTKEY : self.on_capture,
            TYPE_HOTKEY    : self.on_type,
            CANCEL_HOTKEY  : self.on_cancel,
        }

        self._listener = keyboard.GlobalHotKeys(hotkeys)
        self._listener.start()
        print("[Hotkeys] Listening...")
        print(f"  {CAPTURE_HOTKEY} → Capture + Analyze")
        print(f"  {TYPE_HOTKEY}    → Type output at cursor")
        print(f"  {CANCEL_HOTKEY}  → Cancel")

    def stop(self):
        if self._listener:
            self._listener.stop()