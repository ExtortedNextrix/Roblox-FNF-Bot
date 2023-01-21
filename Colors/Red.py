import pyautogui, os, pydirectinput as d, keyboard as k, ctypes
from colorama import Fore
class Main():
    ctypes.windll.kernel32.SetConsoleTitleW("FNF Bot : Red")
    def onStart():
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{Fore.RED}Red{Fore.WHITE} Listening...")
        redX, redY = 1193, 155
        redPos = redX, redY 
        OutX, OutY = 1193, 2
        pyautogui.PAUSE = 0.0
        d.PAUSE = 0.0
        Missed = 0
        col4 = pyautogui.pixel(redX, redY)
        while True:
            if pyautogui.pixelMatchesColor(redX, redY, (249, 57, 63)):
                print(f'{Fore.GREEN}Missed{Fore.BLUE}:{Fore.LIGHTRED_EX} {Missed}{Fore.RESET}\n{Fore.LIGHTYELLOW_EX}Pressed {Fore.LIGHTRED_EX}Red{Fore.LIGHTYELLOW_EX} at Position{Fore.CYAN}: {Fore.WHITE}{redPos}!')
                d.keyDown('k')
                if col4 != pyautogui.pixelMatchesColor(redX, redY, (194, 75, 153)):
                    d.keyUp('k')
            #if pyautogui.pixelMatchesColor(OutX, OutY, (249, 57, 63)):
               # print(f"\t{Fore.RED}Missed A Note!")
                #Missed = Missed+1
Main.onStart()
        
