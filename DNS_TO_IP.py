import socket
from termcolor import colored
import pyfiglet


print(colored(pyfiglet.figlet_format("DNS TO IP"), 'red'))

print(colored("**********DNS TO IP CONVERTER**********", 'yellow'))
print(colored("*********Made by error75***************", 'cyan'))

domain = input(colored("Enter your Domain Name: ", 'green'))
ip = socket.gethostbyname(domain)

print(colored(f"IP of {domain}:", 'green'), colored(f"{ip}", 'red'))
