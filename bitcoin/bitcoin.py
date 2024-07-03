import requests
import json
import sys

data = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()

rate = data["bpi"]["USD"]["rate"].replace(",", "")
rate = float(rate)

if len(sys.argv) == 1:
    print("Missing command-line argument ")
    sys.exit(1)

x = sys.argv[1]

try:
    x = float(x)
    y = rate * x
    y = round(y, 4)
    print("$","{:,.4f}".format(y), sep ="")
except ValueError:
    print("Command-line argument is not a number")
    sys.exit(1)

