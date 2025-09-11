import random
import os, os.path
import shutil
amtLoop = 3
weather = ["Flood", "Thunderstorm", "Rain", "English weather", "Cloudy", "Little clouds", "Sunny", "Saharan sun"]
curWeather = weather[random.randint(0, len(weather) - 1)]
windMax = 50
curWind = random.randint(0, windMax)
weatherAmt = {}
windAmt = {}
tempAmt = {}
informsCompilation = []

for x in weather:
    weatherAmt[x] = 0

for x in range(windMax + 1):
    windAmt[x] = 0

for x in range(-2, (len(weather) * 8) + 3):
    tempAmt[str(x) + "C"] = 0

def cleanTAmt(TAmt):
    removeT = []
    for x in TAmt:
        val = TAmt[x]
        if val == 0:
            removeT.append(x)
    for x in removeT:
        del TAmt[x]
    return TAmt

def getPrintT(WA, IA, TA, IC):
    printString = "Weather: \n"
    mostWA = {}
    mostIA = {}
    mostTA = {}
    for x in WA:
        val = None
        if mostWA != {}:
            for v in mostWA:
                val = mostWA[v]
        if mostWA == {} or WA[x] > val:
            mostWA = {}
            mostWA[x] = WA[x]
        elif WA[x] == val:
            mostWA[x] = WA[x]
        printString += "\n" + str(x) + " - " + str(WA[x]) + " times"
    if len(mostWA) == 1:
        val = None
        nam = None
        if mostWA != {}:
            for i, x in mostWA.items():
                val = x
                nam = i
        printString += "\n\nMost repeated is: " + str(nam) + " repeating " + str(val) + " times"
    elif len(mostWA) > 1:
        newString = "\n\nThe most repeated are: "
        endString = " repeating "
        lenght = len(mostWA)
        ciont = 1
        for key, val in mostWA.items():
            if ciont != lenght and ciont != lenght - 1:
                newString += str(key) + ", "
                endString += str(val) + ", "
            elif ciont == lenght - 1:
                newString += str(key) + " and "
                endString += str(val) + " and "
            elif ciont == lenght:
                newString += str(key)
                endString += str(val) + " times respectively."
            ciont += 1
        printString += newString + endString
    printString += "\n\nWind: \n"
    for x in IA:
        val = None
        if mostIA != {}:
            for v in mostIA:
                val = mostIA[v]
        if mostIA == {} or IA[x] > val:
            mostIA = {}
            mostIA[x] = IA[x]
        elif IA[x] == val:
            mostIA[x] = IA[x]
        printString += "\n" + str(x) + " - " + str(IA[x]) + " times"
    if len(mostIA) == 1:
        val = None
        nam = None
        if mostIA != {}:
            for i, x in mostIA.items():
                val = x
                nam = i
        printString += "\n\nMost repeated is: " + str(nam) + " knots repeating " + str(val) + " times"
    elif len(mostIA) > 1:
        newString = "\n\nThe most repeated are: "
        endString = " knots repeating "
        lenght = len(mostIA)
        ciont = 1
        for key, val in mostIA.items():
            if ciont != lenght and ciont != lenght - 1:
                newString += str(key) + ", "
                endString += str(val) + ", "
            elif ciont == lenght - 1:
                newString += str(key) + " and "
                endString += str(val) + " and "
            elif ciont == lenght:
                newString += str(key)
                endString += str(val) + " times respectively."
            ciont += 1
        printString += newString + endString
    printString += "\n \n Temperature: \n "
    for x in TA:
        val = None
        if mostTA != {}:
            for v in mostTA:
                val = mostTA[v]
        if mostTA == {} or TA[x] > val:
            mostTA = {}
            mostTA[x] = TA[x]
        elif TA[x] == val:
            mostTA[x] = TA[x]
        printString += "\n" + str(x) + " - " + str(TA[x]) + " times"
    if len(mostTA) == 1:
        val = None
        nam = None
        if mostTA != {}:
            for i, x in mostTA.items():
                val = x
                nam = i
        printString += "\n\nMost repeated is: " + str(nam) + " repeating " + str(val) + " times"
    elif len(mostTA) > 1:
        newString = "\n\nThe most repeated are: "
        endString = " repeating "
        lenght = len(mostTA)
        ciont = 1
        for key, val in mostTA.items():
            if ciont != lenght and ciont != lenght - 1:
                newString += str(key) + ", "
                endString += str(val) + ", "
            elif ciont == lenght - 1:
                newString += str(key) + " and "
                endString += str(val) + " and "
            elif ciont == lenght:
                newString += str(key)
                endString += str(val) + " respectively."
            ciont += 1
        printString += newString + endString
    printString += "\n \n Inform compilation: \n "
    coint = 1
    for x in IC:
        printString += "\n Day " + str(coint) + ": " + str(x)
        coint += 1
    return printString

def getWeather(coorWeather, coorWind, uindMax):
    startPos = weather.index(coorWeather)
    aindex = 0
    r = random.randint(1, 100)
    if r <= 47:
        if startPos != len(weather) - 1:
            coorWeather = weather[startPos + 1]
            aindex = weather.index(coorWeather)
        else:
            aindex = len(weather)
    elif r > 47 and r <= 94:
        if startPos != 0:
            coorWeather = weather[startPos - 1]
            aindex = weather.index(coorWeather)
    else:
        r2 = random.randint(1, 2)
        if r2 == 1:
            if startPos + 2 >= len(weather) - 1:
                coorWeather = weather[len(weather) - 1]
                aindex = weather.index(coorWeather)
            else:
                coorWeather = weather[startPos + 2]
                aindex = weather.index(coorWeather)
        elif r2 == 2:
            if startPos - 2 <= 0:
                coorWeather = weather[0]
                aindex = weather.index(coorWeather)
            else:
                coorWeather = weather[startPos - 2]
                aindex = weather.index(coorWeather)
    r3 = random.randint(1, 3)
    r4 = random.randint(1, 10)
    if r3 == 1:
        coorWind += r4
        if coorWind > uindMax:
            coorWind = uindMax
    elif r3 == 2:
        coorWind -= r4
        if coorWind < 0:
            coorWind = 0
    r5 = random.randint(-2, 2)
    temp = (aindex * 8) + r5
    return coorWeather, coorWind, temp

for x in range(amtLoop):
    curWeather, curWind, temperature = getWeather(curWeather, curWind, windMax)
    weatherAmt[curWeather] += 1
    windAmt[curWind] += 1
    tempAmt[str(temperature) + "C"] += 1
    inform = "The skies are: " + curWeather + ", we're rocking " + str(temperature) + "C and the wind looks like it's blowing at " + str(curWind) + " knots."
    informsCompilation.append(inform)

windAmt = cleanTAmt(windAmt)
tempAmt = cleanTAmt(tempAmt)

dir_path = os.path.join(os.getcwd(), "Results")
os.makedirs(dir_path, exist_ok=True)

count = len([f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))])
file_name = f"Results {amtLoop} rounds {count + 1}.txt"
file_path = os.path.join(dir_path, file_name)

with open(file_path, "x") as resultF:
    resultF.write(getPrintT(weatherAmt, windAmt, tempAmt, informsCompilation))