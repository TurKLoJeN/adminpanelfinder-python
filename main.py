import pyfiglet
import requests

ascii_banner = pyfiglet.figlet_format("|| Welcome ||")

print(ascii_banner)

print("\033[1m \033[91m All responsibility belongs to the user \033[0m")

url = input("Please enter a url example (\033[92mhttps://google.com\033[0m): ")

while True:
    try:
        with open("list.txt", "r") as f:
                paneller = f.read().splitlines()

        for panel in paneller:
            test_url = f"{url}/{panel}/"
            response = requests.get(test_url)
            if response.status_code == 200:
                 print(f"\033[1m \033[92m{test_url} mevcut \033[0m")
            else:
                 print(f"\033[1m \033[91m{test_url} mevcut değil \033[0m")
    except ValueError:
        print("\033[33m Try again \033[0m")