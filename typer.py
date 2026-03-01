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

        if not stripped:
            if line_index < len(lines) - 1:
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)
                time.sleep(0.05)
                keyboard.press(Key.home)
                keyboard.release(Key.home)
            continue

        # Type each character
        for char in stripped:
            if char in SAFE_TYPE_CHARS:
                keyboard.press(char)
                keyboard.release(char)
            else:
                keyboard.type(char)
                time.sleep(0.05)
            time.sleep(random.uniform(MIN_KEYSTROKE_DELAY, MAX_KEYSTROKE_DELAY))

        # If line ends with { move cursor to end to get past auto-inserted }
        # Then delete everything after our typed content
        keyboard.press(Key.end)
        keyboard.release(Key.end)
        time.sleep(0.05)

        # Only delete auto-inserted content if line ends with {
        if stripped.rstrip().endswith('{'):
            # Move back one position to sit between { and auto-inserted }
            keyboard.press(Key.left)
            keyboard.release(Key.left)
            time.sleep(0.03)
            # Select and delete the auto-inserted }
            keyboard.press(Key.shift)
            keyboard.press(Key.end)
            keyboard.release(Key.end)
            keyboard.release(Key.shift)
            time.sleep(0.03)
            keyboard.press(Key.delete)
            keyboard.release(Key.delete)
            time.sleep(0.03)

        # Press Enter and Home
        if line_index < len(lines) - 1:
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            time.sleep(random.uniform(0.08, 0.15))
            keyboard.press(Key.home)
            keyboard.release(Key.home)
            time.sleep(0.03)


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

    # Clear everything first
    with keyboard.pressed(Key.ctrl):
        keyboard.press('a')
        keyboard.release('a')
    time.sleep(0.1)
    keyboard.press(Key.delete)
    keyboard.release(Key.delete)
    time.sleep(0.2)

    if USE_CLIPBOARD_PASTE:
        paste_via_clipboard(text)
    else:
        human_type(text)