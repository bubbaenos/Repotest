#! python3

import requests
import sys
import time
# This is a test for git.


r = requests.get('https://api.github.com/events')
print(r)

print(sys.version)
time.sleep(8)