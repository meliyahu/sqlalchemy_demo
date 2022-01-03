import math
import os
import sys

import requests

print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    """[summary]

    Args:
        who_to_greet ([type]): [description]

    Returns:
        [type]: [description]
    """
    greeting = f'Hello, {who_to_greet}'
    return greeting

req = requests.get(url='https://coreyms.com')
print(req.status_code)
