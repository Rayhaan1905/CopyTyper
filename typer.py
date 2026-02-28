import time
import random
import pyperclip
from pynput.keyboard import Controller, Key
from config import MIN_KEYSTROKE_DELAY, MAX_KEYSTROKE_DELAY, USE_CLIPBOARD_PASTE, WAIT_BEFORE_TYPING

keyboard = Controller()
def human_type(text):
    pyperclip.copy(text)
    content = pyperclip.paste()
    pyperclip.copy("")

    SAFE_TYPE_CHARS = set('abcdefghijklmnopqrstuvwxyz0123456789 .,;-=[\\/]')

    lines = content.split('\n')

    for line_index, line in enumerate(lines):
        stripped = line.lstrip()

        for char in stripped:
            if char == '}':
                continue
            if char in SAFE_TYPE_CHARS:
                keyboard.press(char)
                keyboard.release(char)
            else:
                keyboard.type(char)
                time.sleep(0.05)

            time.sleep(random.uniform(MIN_KEYSTROKE_DELAY, MAX_KEYSTROKE_DELAY))

        if line_index < len(lines) - 1:
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            time.sleep(random.uniform(0.08, 0.15))


def paste_via_clipboard(text):
    original = pyperclip.paste()
    pyperclip.copy(text)
    time.sleep(0.2)
    with keyboard.pressed(Key.ctrl):
        keyboard.press('v')
        keyboard.release('v')
    time.sleep(0.3)
    pyperclip.copy(original)


def type_output(text):
    print("[*] Move cursor to target field...")
    time.sleep(WAIT_BEFORE_TYPING)
        
    if USE_CLIPBOARD_PASTE:
        paste_via_clipboard(text)
    else:
        human_type(text)