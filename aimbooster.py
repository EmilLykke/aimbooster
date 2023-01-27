import win32api
import win32con
import time
import pyautogui
import keyboard

time.sleep(2)


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


while keyboard.is_pressed('q') == False:
    center = pyautogui.locateCenterOnScreen("Time.png",confidence=0.7)

    x_off = center.x-25
    y_off=center.y+20

    pic = pyautogui.screenshot(region=(x_off,y_off,600,420))
    pic.save("savedimage.png")

    width, height = pic.size

    for x in range(0,width,5):
        for y in range(0,height,5):
            # 255,219,195

            r,g,b = pic.getpixel((x,y))
            
            if g == 219:
                click(x_off+x,y_off+y)
                time.sleep(0.03)
                break