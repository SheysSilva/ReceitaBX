import pyautogui

func = pyautogui

w, h = func.size()
x, y = func.position()
pyautogui.onScreen(x, y)

print(x)
print(y)
