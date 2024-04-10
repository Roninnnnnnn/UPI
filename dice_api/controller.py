"""
controller.py
by Roninnnnnnn
Python code to make API connections.
"""

import requests as re

url = "https://api.dicebear.com/8.x/pixel-art/svg"

response = re.get(url)

if response.ok:
    print(response.text)
else:
    print(f"Error: {response.status_code}")