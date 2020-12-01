from pynput import keyboard
import time
import clipboard
import webbrowser

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


def function_1():
    text = clipboard.paste()
    print(text)

    query = text + sites
    query = query.replace(" ", "+")

    if bchoice == 0:
        openbrow = "https://duckduckgo.com/?q=" + query
    else:
        openbrow = "https://www.google.com/search?q=" + query

    webbrowser.open(openbrow, new=2, autoraise=True)


def function_2():
    print('Function 2 activated')


with keyboard.GlobalHotKeys({
    '<ctrl>+c': function_1,
    '<alt>+<ctrl>+y': function_2}) as h:
    h.join()
