import math
import os
import sys

import requests

print(sys.version)
print(sys.executable)

req = requests.get(url='https://coreyms.com')
print(req.status_code)
