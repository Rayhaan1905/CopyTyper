import threading
import time
from capture import capture_screen
from analyzer import analyze_screenshot
from typer import type_output
from hotkeys import HotkeyManager
from agent_state import state

def handle_capture():
    if state.is_analyzing:
        return

    state.is_analyzing = True
    state.status = "capturing"

    def run():
        try:
            img = capture_screen()
            state.status = "analyzing"
            result = analyze_screenshot(img)
            if result:
                state.last_output = result
                state.status = "ready"
                type_output(result)
                state.status = "idle"
                state.last_output = None
            else:
                state.status = "idle"
        except Exception:
            state.status = "idle"
        finally:
            state.is_analyzing = False

    threading.Thread(target=run, daemon=True).start()


def handle_cancel():
    state.is_analyzing = False
    state.is_ready_to_type = False
    state.last_output = None
    state.status = "idle"


def main():
    manager = HotkeyManager(
        on_capture = handle_capture,
        on_type    = handle_cancel,
        on_cancel  = handle_cancel
    )
    manager.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        manager.stop()

if __name__ == "__main__":
    main()