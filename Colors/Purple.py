import pyautogui, os, pydirectinput as d, keyboard as k, ctypes
from colorama import Fore
class Main():
    ctypes.windll.kernel32.SetConsoleTitleW("FNF Bot : Purple")
    def onStart():
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{Fore.MAGENTA}Purple{Fore.WHITE} Listening...")
        purpleX, purpleY = 728, 155
        purplePos = purpleX, purpleY
        OutX, OutY = 728, 2
        pyautogui.PAUSE = 0.0
        d.PAUSE = 0.0
        Missed = 0
        col1 = pyautogui.pixel(purpleX, purpleY)
        while True:
            if pyautogui.pixelMatchesColor(purpleX, purpleY, (194, 75, 153)):
                print(f'{Fore.GREEN}Missed{Fore.BLUE}:{Fore.LIGHTRED_EX} {Missed}{Fore.RESET}\n{Fore.LIGHTYELLOW_EX}Pressed {Fore.LIGHTMAGENTA_EX}Purple{Fore.LIGHTYELLOW_EX} at Position{Fore.CYAN}: {Fore.WHITE}{purplePos}!')
                d.keyDown('d')
                if col1 != pyautogui.pixelMatchesColor(purpleX, purpleY, (136, 165, 171)):
                    d.keyUp('d')
            #if pyautogui.pixelMatchesColor(OutX, OutY, (194, 75, 153)):
            #    print(f"\t{Fore.RED}Missed A Note!")
                #Missed = Missed+1
Main.onStart()