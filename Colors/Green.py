import pyautogui, os, pydirectinput as d, keyboard as k, ctypes
from colorama import Fore
class Main():
    ctypes.windll.kernel32.SetConsoleTitleW("FNF Bot : Green")
    def onStart():
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{Fore.GREEN}GREEN{Fore.WHITE} Listening...")
        greenX, greenY = 1039, 155
        greenPos = greenX, greenY
        OutX, OutY = 1039, 2
        pyautogui.PAUSE = 0.0
        d.PAUSE = 0.0
        Missed = 0
        col3 = pyautogui.pixel(greenX, greenY)
        while True:
            if pyautogui.pixelMatchesColor(greenX, greenY, (18, 250, 5)):
                print(f'{Fore.GREEN}Missed{Fore.BLUE}:{Fore.LIGHTRED_EX} {Missed}{Fore.RESET}\n{Fore.LIGHTYELLOW_EX}Pressed {Fore.LIGHTGREEN_EX}Green{Fore.LIGHTYELLOW_EX} at Position{Fore.CYAN}: {Fore.WHITE}{greenPos}!')
                d.keyDown('j')
                if col3 != pyautogui.pixelMatchesColor(greenX, greenY, (194, 75, 153)):
                    d.keyUp('j')
            #if pyautogui.pixelMatchesColor(OutX, OutY, (18, 250, 5)):
             #   print(f"\t{Fore.RED}Missed A Note!")
                #Missed = Missed+1
Main.onStart()
        
