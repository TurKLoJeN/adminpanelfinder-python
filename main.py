import pyfiglet
import requests
from termcolor import colored

ascii_banner = pyfiglet.figlet_format("|| Welcome ||")

print(ascii_banner)

print(colored("All responsibility belongs to the user","red"))

url = input("Please enter a url example "+colored("(https://google.com): ","green"))

while True:
    try:
        with open("list.txt", "r") as f:
                paneller = f.read().splitlines()

        for panel in paneller:
            test_url = f"{url}/{panel}/"
            response = requests.get(test_url)
            if response.status_code == 200:
                 print(colored(f"{test_url} OK","green"))
            else:
                 print(colored(f"{test_url} NOT WORKING","red"))
    except ValueError:
        print(colored("Try Again.","yellow"))
