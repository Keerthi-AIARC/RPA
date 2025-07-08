import subprocess
import time
import pyautogui

# ---------- SAFETY SETTINGS ----------
pyautogui.FAILSAFE = True      # Mouse to any screen corner → abort
pyautogui.PAUSE = 0.2          # Tiny delay after every PyAutoGUI call

# ---------- STEP 1 — launch Chrome ----------
# Adjust the path if Chrome is installed somewhere else
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
subprocess.Popen(chrome_path)

# ---------- STEP 2 — wait for Chrome to appear ----------
time.sleep(3)                  # tweak if your PC is slower/faster

# ---------- STEP 3 — open ChatGPT ----------
pyautogui.hotkey('ctrl', 'l')  # focus the address bar
pyautogui.typewrite('https://chat.openai.com\n', interval=0.05)

# ---------- STEP 4 — wait for page load / (manual) login ----------
# If you are not already signed in, log in manually,
# then press Ctrl+Alt+R to resume the script.
time.sleep(8)                  # enough for most broadband connections

# ---------- STEP 5 — ask for trending social updates ----------
pyautogui.typewrite('Digital Marketing strategies using AI\n',
                    interval=0.05)
# Done! ChatGPT will reply in the browser tab.
