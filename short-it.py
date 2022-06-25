import pyfiglet
import colorama
import pyshorteners
from colorama import Fore, Back, Style
result = pyfiglet.figlet_format("shortener", font = "3-d")
print(Fore.BLUE,result)
print(Fore.GREEN)
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("      \n about: Shortener \n:it is use for shortening URL         ")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
print("created by:iyanuhacks")
print("github:https://github.com/iyanuhacks.git")
print("whatsapp:07040435646")
print(Fore.RED)
input("enter [Y/N] for open console or back: ")
long_url = input("Enter the URL to shorten: ")

#TinyURL shortener service
type_tiny = pyshorteners.Shortener()
short_url = type_tiny.tinyurl.short(long_url)

print("The Shortened URL is: " + short_url)
