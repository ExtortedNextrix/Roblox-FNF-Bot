#  Mouse Debugger by Extorted Nextrix

import pyautogui, os, time, keyboard as k, ctypes
from colorama import Fore


"""

███▄▄▄▄      ▄████████ ▀████    ▐████▀     ███        ▄████████  ▄█  ▀████    ▐████▀ 
███▀▀▀██▄   ███    ███   ███▌   ████▀  ▀█████████▄   ███    ███ ███    ███▌   ████▀  
███   ███   ███    █▀     ███  ▐███       ▀███▀▀██   ███    ███ ███▌    ███  ▐███    
███   ███  ▄███▄▄▄        ▀███▄███▀        ███   ▀  ▄███▄▄▄▄██▀ ███▌    ▀███▄███▀    
███   ███ ▀▀███▀▀▀        ████▀██▄         ███     ▀▀███▀▀▀▀▀   ███▌    ████▀██▄     
███   ███   ███    █▄    ▐███  ▀███        ███     ▀███████████ ███    ▐███  ▀███    
███   ███   ███    ███  ▄███     ███▄      ███       ███    ███ ███   ▄███     ███▄  
 ▀█   █▀    ██████████ ████       ███▄    ▄████▀     ███    ███ █▀   ████       ███▄ 
                                                     ███    ███                         #8446

"""


class Main:
    os.system('cls' if os.name == 'nt' else 'clear')
    ctypes.windll.kernel32.SetConsoleTitleW("Mouse Debugger by nextrix#8446")
    print(f"{Fore.BLUE}Mouse Debug Script by {Fore.LIGHTMAGENTA_EX}nextrix#8446\n")
    def mousePos():
        os.system('cls' if os.name == 'nt' else 'clear')
        while True:
            print(f"{Fore.MAGENTA}Press / Hold p to get Position Value {Fore.YELLOW}:: {Fore.RED}Press s to Stop the script")
            if k.read_key() == 's':
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"{Fore.RED}Stopped!{Fore.LIGHTWHITE_EX}")
                break
            elif k.read_key() == 'p':
                time.sleep(0.02)
                v, x = pyautogui.position()
                pos = v, x
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"{Fore.CYAN}X{Fore.BLACK}, {Fore.LIGHTBLUE_EX}Y{Fore.BLACK}: {Fore.GREEN}" + str(pos))

    def colorCode():
        os.system('cls' if os.name == 'nt' else 'clear')
        while True:
            print(f"{Fore.MAGENTA}Press / Hold c to get Color Value {Fore.YELLOW}:: {Fore.RED}Press s to Stop the script")
            if k.read_key() == 's':
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"{Fore.RED}Stopped!{Fore.LIGHTWHITE_EX}")
                break
            elif k.read_key() == 'c':
                time.sleep(0.2)
                x, y = pyautogui.position()
                col = pyautogui.pixel(x, y)
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"{Fore.RED}R{Fore.BLACK}, {Fore.GREEN}G{Fore.BLACK}, {Fore.BLUE}B{Fore.BLACK}: {Fore.GREEN}" + str(col))

    def both():
        os.system('cls' if os.name == 'nt' else 'clear')
        while True:
            print(f"{Fore.MAGENTA}Press / Hold b to get Color Value {Fore.YELLOW}:: {Fore.RED}Press s to Stop the script")
            if k.read_key() == 's':
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"{Fore.RED}Stopped!{Fore.LIGHTWHITE_EX}")
                break
            elif k.read_key() == 'b':
                time.sleep(0.02)
                z, r = pyautogui.position()
                pos = z, r
                col = pyautogui.pixel(z, r)
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"{Fore.CYAN}X{Fore.BLACK}, {Fore.LIGHTBLUE_EX}Y{Fore.BLACK}: {Fore.GREEN}" + str(pos) + "\n" + f"{Fore.RED}R{Fore.BLACK}, {Fore.GREEN}G{Fore.BLACK}, {Fore.BLUE}B{Fore.BLACK}: {Fore.GREEN}" + str(col))

selection = input(f"{Fore.CYAN}Check for Mouse Position [1] or Color Position [2] or Both Options [3]{Fore.LIGHTMAGENTA_EX} >>{Fore.GREEN}\t")
if selection == str('1'):
    os.system('cls' if os.name == 'nt' else 'clear')
    Main.mousePos()
elif selection == str('2'):
    os.system('cls' if os.name == 'nt' else 'clear')
    Main.colorCode()
elif selection == str('3'):
    os.system('cls' if os.name == 'nt' else 'clear')
    Main.both()
else:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{Fore.RED}Invalid Option!{Fore.LIGHTWHITE_EX}")
    exit()

"""

███████╗██╗  ██╗████████╗ ██████╗ ██████╗ ████████╗███████╗██████╗ 
██╔════╝╚██╗██╔╝╚══██╔══╝██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
█████╗   ╚███╔╝    ██║   ██║   ██║██████╔╝   ██║   █████╗  ██║  ██║
██╔══╝   ██╔██╗    ██║   ██║   ██║██╔══██╗   ██║   ██╔══╝  ██║  ██║
███████╗██╔╝ ██╗   ██║   ╚██████╔╝██║  ██║   ██║   ███████╗██████╔╝
╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═════╝   https://discord.gg/GX3dFpXxch

"""
