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
        filename = 'C:/Users/Data Science/Pictures/asis book/pre pages/'
        filename += str(filenum)
        filename +='.png'
        imx.save(filename)


roman_numerals = ["i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x", "xi", "xii",    "xiii", "xiv", "xv", "xvi", "xvii", "xviii", "xix", "xx", "xxi", "xxii",    "xxiii", "xxiv", "xxv", "xxvi", "xxvii"]
for x in roman_numerals:
    
    if len(x)==1:
        type_text(x)
        press_enter()        
        press_enter()
        time.sleep(2)
        take_screenshot(x)
        press_backspace()

    
    if len(x)==2:
        type_text(x)
        press_enter()        
        press_enter()
        time.sleep(2)
        take_screenshot(x)
        press_backspace()
        press_backspace()

    
    if len(x)==3:
        type_text(x)
        press_enter()
        press_enter()
        time.sleep(2)
        take_screenshot(x)
        press_backspace()
        press_backspace()
        press_backspace()
    
    if len(x)==4:
        type_text(x)
        press_enter()
        press_enter()
        time.sleep(2)
        take_screenshot(x)
        press_backspace()
        press_backspace()
        press_backspace()
        press_backspace()
    
    if len(x)==5:
        type_text(x)
        press_enter()
        press_enter()
        time.sleep(2)
        take_screenshot(x)
        press_backspace()
        press_backspace()
        press_backspace()
        press_backspace()
        press_backspace()
    
    