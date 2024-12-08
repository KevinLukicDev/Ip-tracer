import requests
import pyfiglet
from termcolor import colored
import random
import json
from datetime import datetime

while True:
    def save_to_json(ip_data):
        ip_data['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        try:
            # Try to load existing data
            with open('ip_history.json', 'r') as f:
                try:
                    history = json.load(f)
                except json.JSONDecodeError:
                    history = []
        except FileNotFoundError:
            history = []
        
        # Add new data
        history.append(ip_data)
        
        # Save updated data
        with open('ip_history.json', 'w') as f:
            json.dump(history, f, indent=4)

    random_color = random.choice(["red", "green", "yellow", "blue", "magenta", "cyan", "white"])
    welcome = pyfiglet.figlet_format("IP-TRACER", font="slant")
    colored_welcome = colored(welcome, random_color)
    print(colored_welcome)

    print(colored("made by Kevin Lukic", "blue"))

    ip = input(colored("Enter an IP address: ", "yellow"))

    response = requests.get(f"https://ipinfo.io/{ip}/json")

    if response.status_code == 200:
        data = response.json()
        print(f"Country: {data['country']}")
        print(f"City: {data['city']}")
        print(f"Region: {data['region']}")
        print(f"Organization: {data['org']}")
        print(f"Postal: {data['postal']}")
        print(f"Timezone: {data['timezone']}")
        
        # Save the data to JSON file
        save_to_json(data)
        print("\nData has been saved to ip_history.json")
    else:
        print("Invalid IP address")
