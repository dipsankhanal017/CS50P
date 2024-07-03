from pyfiglet import Figlet
import sys

figlet = Figlet()
a = figlet.getFonts()


if (sys.argv[1] == "-f" or sys.argv[1] == "--font") and (sys.argv[2] in a):
    text = input("Input: ")
else:
    print("Invalid usage")
    sys.exit(1)
figlet.setFont(font = sys.argv[2])
print("Output:", figlet.renderText(text))
