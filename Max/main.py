import os
import random
import shutil
import time
amtOfImages = 5
curLoop = 1
loopAmt = 1000
WYLA = False
printIfFound = False
name = "VIVA_ESPAÑA"

def newRandom(curLup, name):
    if WYLA:
        shutil.copy("WYLA.jpg", name + str(curLup) + ".jpg")
        if os.path.exists(name + str(curLup) + ".jpg") and printIfFound:
            print("Found" + name + str(curLup) + ".jpg")
        else:
            if printIfFound == True:
                print("Couldn't find" + name + str(curLup - 1) + ".jpg")
        username = os.getlogin()
        first = "/Users/"
        middle = "/Downloads"
        name = name + str(curLup) + ".jpg"
        dir = first + username + middle
        shutil.move(name, dir)
    else:
        r = random.randint(1, amtOfImages)
        shutil.copy("meme" + str(r) + ".jpg", name + str(curLup) + ".jpg")
        if os.path.exists(name + str(curLup) + ".jpg") and printIfFound:
            print("Found" + name + str(curLup) + ".jpg")
        else:
            if not printIfFound == True:
                print("Couldn't find" + name + str(curLup - 1) + ".jpg")
        username = os.getlogin()
        first = "/Users/"
        middle = "/Downloads"
        name = name + str(curLup) + ".jpg"
        dir = first + username + middle
        shutil.move(name, dir)

for x  in range(loopAmt):
    newRandom(curLoop, name)
    curLoop += 1