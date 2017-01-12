#! python3

import requests
import sys
import time


r = requests.get('https://api.github.com/events')
print(r)

print(sys.version)
time.sleep(7)