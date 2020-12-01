import time
import clipboard
import webbrowser
import keyboard

with open('sites.txt', 'r') as file:
    sites = file.read().replace('\n', ' OR site:')
    sites = " site:"+sites
print(sites)

print("WHICH SEARCH ENGINE DO YOU USE?")
print("ENTER '0' FOR DUCK DUCK GO ")
print("OR ANY OTHER NUMBER FOR GOOGLE")
bchoice = int(input("BE QUICK \n"))

if bchoice == 0:
    print("SMORT!!! KEEP USING DUCKDUCKGO")
else:
    print("LEVEL UP DUDE AND START USING DUCK DUCK GO")
    time.sleep(3)
    print("")
    print("")
    print("ANYWAYS")

keyboard.add_hotkey('ctrl+shift+a', print, args=('triggered', 'hotkey'))

text = clipboard.paste()
print(text)

query = text + sites
query = query.replace(" ", "+")

if bchoice == 0:
    openbrow = "https://duckduckgo.com/?q=" + query
else:
    openbrow = "https://www.google.com/search?q=" + query

webbrowser.open(openbrow, new=2, autoraise=True)

