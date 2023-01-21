import pyautogui, os, pydirectinput as d, keyboard as k, ctypes
from colorama import Fore
class Main():
    ctypes.windll.kernel32.SetConsoleTitleW("FNF Bot : Blue")
    def onStart():
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{Fore.CYAN}BLUE{Fore.WHITE} Listening...")
        blueX, blueY = 880, 155
        bluePos = blueX, blueY
        OutX, OutY = 880, 2
        pyautogui.PAUSE = 0.0
        d.PAUSE = 0.0
        Missed = 0
        col2 = pyautogui.pixel(blueX, blueY)
        while True:
            if pyautogui.pixelMatchesColor(blueX, blueY, (0, 255, 255)):
                print(f'{Fore.GREEN}Missed{Fore.BLUE}:{Fore.LIGHTRED_EX} {Missed}{Fore.RESET}\n{Fore.LIGHTYELLOW_EX}Pressed {Fore.LIGHTCYAN_EX}Blue{Fore.LIGHTYELLOW_EX} at Position{Fore.CYAN}: {Fore.WHITE}{bluePos}!')
                d.keyDown('f')
                if col2 != pyautogui.pixelMatchesColor(blueX, blueY, (136, 165, 171)):
                    d.keyUp('f')
            #if pyautogui.pixelMatchesColor(OutX, OutY, (0, 255, 255)):
                #print(f"\t{Fore.RED}Missed A Note!")
                #Missed = Missed+1
Main.onStart()
        
