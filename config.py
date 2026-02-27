CAPTURE_HOTKEY        = "<ctrl>+r+a+y"
TYPE_HOTKEY           = "<ctrl>+<shift>+v"
CANCEL_HOTKEY         = "<ctrl>+<shift>+x"

WAIT_BEFORE_TYPING    = 4
MIN_KEYSTROKE_DELAY   = 0.08
MAX_KEYSTROKE_DELAY   = 0.15
USE_CLIPBOARD_PASTE   = False

GEMINI_MODEL          = "gemini-3-flash-preview"
MONITOR_INDEX         = 1

GEMINI_PROMPT = """
You are an expert coding assistant. Analyze this screenshot carefully.

STRICT RULES:
- Return ONLY the complete, correct, compilable code
- Every single character must be exactly correct
- No missing brackets, parentheses, or quotation marks
- No truncated words or method names
- No markdown, no backticks, no comments, no explanation
- Double check every line before returning
- If it is Java, the class must be named Main
- Use correct case for every keyword — boolean not Boolean, int not Int
- Variable names must match exactly — use i not I in for loops
- Return the raw code only, nothing else
"""