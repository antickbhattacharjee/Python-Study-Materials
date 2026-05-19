from colorama import Fore, Style, init

# Initialize Colorama to automatically reset styles after each print statement
init(autoreset=True)

print(Fore.GREEN + "Hello " + Fore.RED + "World" + Style.RESET_ALL)