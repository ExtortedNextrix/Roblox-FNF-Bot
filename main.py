import pyautogui, os, time, keyboard as k, ctypes
from colorama import Fore

"""

Colors:
    purple: R, G, B: (194, 75, 153)
    blue: R, G, B: (0, 255, 255)
    green: R, G, B: (18, 250, 5)
    red: R, G, B: (249, 57, 63)
Positions:
    pos purple: X, Y: (728, 218)
    pos blue: X, Y: (880, 218)
    pos green: X, Y: (1039, 218)
    pos red: X, Y: (1193, 218)

"""

class Main():
    os.system('cls' if os.name == 'nt' else 'clear')
    ctypes.windll.kernel32.SetConsoleTitleW("FNF BOT by nextrix#8446")
    print(f"{Fore.BLUE}FNF Roblox Bot by {Fore.LIGHTMAGENTA_EX}nextrix#8446\n")
    inp = input("Start? (Press Any Key)\t")
    def onStart():
        os.system('cls' if os.name == 'nt' else 'clear')
        # Colors
        purple = 194, 75, 153
        blue = 0, 255, 255
        green = 18, 250, 5
        red = 249, 57, 63

        # Positions
        purpleX, purpleY = 728, 117
        purplePos = purpleX, purpleY
        blueX, blueY = 880, 117
        bluePos = blueX, blueY
        greenX, greenY = 1039, 117
        greenPos = greenX, greenY
        redX, redY = 1193, 117
        redPos = redX, redY
        
        Win32 = True
        pyautogui.PAUSE = 0.0000000000

        
        col1 = pyautogui.pixel(purpleX, purpleY)
        col2 = pyautogui.pixel(blueX, blueY)
        col3 = pyautogui.pixel(greenX, greenY)
        col4 = pyautogui.pixel(redX, redY)

        while Win32:
            if pyautogui.pixelMatchesColor(purpleX, purpleY, (194, 75, 153)):
                print('Pressed Purple!')
                k.press('d')
                if col1 != pyautogui.pixelMatchesColor(purpleX, purpleY, (194, 75, 153)):
                    k.release('d')
                
            if pyautogui.pixelMatchesColor(blueX, blueY, (0, 255, 255)):
                print('Pressed Blue!')
                k.press('f')
                if col1 != pyautogui.pixelMatchesColor(blueX, blueY, (194, 75, 153)):
                    k.release('f')
            if pyautogui.pixelMatchesColor(greenX, greenY, (18, 250, 5)):
                print('Pressed Green!')
                k.press('j')
                if col1 != pyautogui.pixelMatchesColor(greenX, greenY, (194, 75, 153)):
                    k.release('j')
            if pyautogui.pixelMatchesColor(redX, redY, (249, 57, 63)):
                print('Pressed Red!')
                k.press('k')
                if col1 != pyautogui.pixelMatchesColor(redX, redY, (194, 75, 153)):
                    k.release('k')

Main.onStart()
        
