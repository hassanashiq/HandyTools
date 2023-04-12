import mss
from PIL import Image

# Define the second monitor



from pynput.keyboard import Key, Controller
import time


keyboard=Controller()


time.sleep(5)

def type_text(text):
	keyboard.type(text)

def press_enter():
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    
def press_down():
    keyboard.press(Key.down)
    keyboard.release(Key.down)
    
def press_backspace():
    keyboard.press(Key.backspace)
    keyboard.release(Key.backspace)

# Take a screenshot of the second monitor
def take_screenshot(filenum):
    monitor = {"top": -200, "left": 1370, "width": 1180, "height": 1710}
    with mss.mss() as sct:
        imx = sct.grab(monitor)
        imx = Image.frombytes("RGB", imx.size, imx.bgra, "raw", "BGRX")
        filename = 'C:/Users/Data Science/Pictures/asis book/'
        filename += str(filenum)
        filename +='.png'
        imx.save(filename)

for x in range(387):
    
    if x<10:
        type_text(str(x))
        press_enter()
        take_screenshot(x)
        press_backspace()
        time.sleep(0.20)
    
    if x>9 and x<100:
        type_text(str(x))
        press_enter()
        take_screenshot(x)
        press_backspace()
        press_backspace()
        time.sleep(0.20)
    
    if x >100:
        type_text(str(x))
        press_enter()
        take_screenshot(x)
        press_backspace()
        press_backspace()
        press_backspace()
        time.sleep(0.20)
