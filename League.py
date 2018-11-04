import subprocess
import time
import sys
import os.path
import colorama
from colorama import init, Fore, Back, Style
init(convert=True)

try:
    if os.path.isfile("path.txt"):
        path_file = open("path.txt", "r")
        for line in path_file:
            print(Fore.YELLOW+"Found Custom Path! using: "+line)
    else:
        print(Fore.YELLOW+"No Custom Path found using Default")

    x = "\n \n \n \n \n \n \n \n \n \n \n \n \n"
    y = list(x)
    i = 0
    for each in y:
        print(y[i], end="")
        time.sleep(0.1)
        i += 1

    print(Fore.WHITE)
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
    
    time.sleep(1)

    print(Fore.WHITE+"\n")
    x = "Trying to open... "
    y = list(x)
    i = 0
    for each in y:
        print(Fore.GREEN+ y[i], end="")
        time.sleep(0.1)
        i += 1
    try:
        line
        path = line
        folder = line.replace("LeagueClient.exe", "")
    except NameError:
        path = "C:\\Riot Games\\League of Legends\\LeagueClient.exe"
        folder = path.replace("LeagueClient.exe", "")
    
    
    conf = folder+"Config\\LeagueClientSettings.yaml"
    
    # print("\nconf: "+conf)
    # print("path: "+path)
    # print("folder: "+folder)

    name = "user"
    with open(conf, 'r') as conf_file:
        line = conf_file.readline()
        cnt = 0
        for line in conf_file:
            if "username" in line:
                tmp, name = line.split(":")
                break
            cnt +=  1
    time.sleep(2)

    if os.path.isfile(path):
        print(Fore.WHITE+"\n")
        x = "Trying to load components!"
        y = list(x)
        i = 0
        for each in y:
            print(Fore.RED+ y[i], end="")
            time.sleep(0.1)
            i += 1
        time.sleep(3)
        print(Fore.WHITE+"\n")
        x = "Initiating..."
        y = list(x)
        i = 0
        for each in y:
            print(Fore.YELLOW+ y[i], end="")
            time.sleep(0.1)
            i += 1
        
        print(Fore.WHITE+"\n")
        x = ">>>Comepleted! Starting League with Profile "
        y = list(x)
        i = 0
        for each in y:
            print(Fore.GREEN+ y[i], end="")
            time.sleep(0.1)
            i += 1
            
        x = name
        y = list(x)
        i = 0
        for each in y:
            print(Fore.RED+ y[i], end="")
            time.sleep(0.1)
            i += 1

        print(Fore.WHITE+"\n")
        x = ". . . . . . . . . "
        y = list(x)
        i = 0
        for each in y:
            print(Fore.RED+ y[i], end="\r")
            time.sleep(0.5)
            i += 1
        
        subprocess.call("cmd /c \""+path+"\"")
        
        print(Fore.WHITE+"\n")
        x = ">>> Started!"
        y = list(x)
        i = 0
        for each in y:
            print(Fore.RED+ y[i], end="")
            time.sleep(0.5)
            i += 1
        time.sleep(3)
        sys.exit()

    else:
        print(Fore.WHITE+"\n")
        x = "Cant Find League!"
        y = list(x)
        i = 0
        for each in y:
            print(Fore.RED+ y[i], end="")
            time.sleep(0.1)
            i += 1
except KeyboardInterrupt:
    print("\n"*10)
    print(Fore.RED+"Exit")
    sys.exit()