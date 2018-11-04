import subprocess
import time
import os.path

import colorama
from colorama import init, Fore, Back, Style

init(convert=True)

x = "Welcome to "
y = list(x)
i = 0
for each in y:
    print(y[i], end="")
    time.sleep(0.1)
    i += 1

x = "League Of Legends"
y = list(x)
i = 0
for each in y:
    print(Fore.LIGHTBLUE_EX+ y[i], end="")
    time.sleep(0.1)
    i += 1


print(Fore.WHITE+"\n")
x = "Trying to open... "
y = list(x)
i = 0
for each in y:
    print(Fore.GREEN+ y[i], end="")
    time.sleep(0.1)
    i += 1

path = "C:\\Riot Games\\League of Legends\\LeagueClient.exe"
if os.path.isfile(path):
    p = "exist"
else:
    p = "404"

if p == "exist":
    print(Fore.WHITE+"\n")
    x = "Found!  "
    y = list(x)
    i = 0
    for each in y:
        print(Fore.RED+ y[i], end="")
        time.sleep(0.1)
        i += 1

else:
    print(Fore.WHITE+"\n")
    x = "Cant Find League!"
    y = list(x)
    i = 0
    for each in y:
        print(Fore.RED+ y[i], end="")
        time.sleep(0.1)
        i += 1


# subprocess.call("cmd /c start explorer.exe \"C:\\Riot Games\\League of Legends\\ \"")