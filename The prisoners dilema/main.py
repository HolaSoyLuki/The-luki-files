import os
import importlib
import pathlib
import sys
curLoop = 1
rounds = 100
iterations = 4
prisoners = []
matches = {}
results = {}
pointDistribution = {
    "Win": 3,
    "2Silent": 2,
    "2Confess": 1,
    "Lose": 0,
}
totalString = "RESULTS:\n"

for name in os.listdir():
    if name != os.path.basename(__file__) and name != "Results" and name != "__pycache__":
        prisoners.append(name)

def resetT():
    matches = {}
    for x in prisoners:
        newT = {}
        for i in prisoners:
            if i == x: continue
            newT[i] = False
        matches[x] = newT
    return matches

def resetR():
    results = {}
    for i in prisoners:
        results[i] = {}
    return results

def write(text, totalStr):
    totalStr += text
    return totalStr

def resultsToText(reslts, tltstr):
    for i in reslts:
        amtWon = 0
        stri = "\n\n" + str(i.removesuffix(".py")) + "\n"
        for y, x in reslts[i].items():
            stri += "\n" + str(y) + " - "
            c = 1
            for w, z in x.items():
                if c == 1 or c == 2:
                    stri += str(w) + ": " + str(z) + " -- "
                elif c == 3:
                    stri += str(z)
                c += 1
        tltstr = write(stri, tltstr)
    return tltstr
        

def calculateResults(des1, des2): #passing 0 is cooperate and 1 is confess
    if des1 == 1:
        if des1 == des2:
            return pointDistribution["2Confess"], pointDistribution["2Confess"]
        if des1 > des2:
            return pointDistribution["Win"], pointDistribution["Lose"]
    if des1 == 0:
        if des1 == des2:
            return pointDistribution["2Silent"], pointDistribution["2Silent"]
        if des1 < des2:
            return pointDistribution["Lose"], pointDistribution["Win"]
        
matches = resetT()
results = resetR()

current_dir = pathlib.Path(__file__).parent.resolve()
sys.path.insert(0, str(current_dir))

for w in range(iterations):
    if w == 0:
        totalString = write("Iteration 1:", totalString)
    else:
        totalString = write("\n\n\nIteration" + str(w + 1), totalString)
    for i in prisoners:
        for y, x in matches[i].items():
            if x == True: continue
            plr1Play = None
            points1 = 0
            points1Total = 0
            plr2Play = None
            points2 = 0
            points2Total = 0
            name1 = i.removesuffix('.py')
            name2 = y.removesuffix('.py')
            module1 = importlib.import_module(name1)
            module2 = importlib.import_module(name2)
            calcsFunc1 = getattr(module1, 'calcs', None)
            calcsFunc2 = getattr(module2, 'calcs', None)
            for z in range(1, rounds + 1):
                plr1Play = calcsFunc1(plr1Play, plr2Play, points1)
                plr2Play = calcsFunc2(plr2Play, plr1Play, points2)
                points1, points2 = calculateResults(int(plr1Play), int(plr2Play))
                points1Total += points1
                points2Total += points2
            matches[y][i] = True
            matches[i][y] = True
            won = None
            if points1Total > points2Total:
                won = str(i) + " won."
            elif points2Total > points1Total:
                won = str(y) + " won."
            elif points1Total == points2Total:
                won = "Draw"
            newRT = {
                name1: points1Total,
                name2: points2Total,
                "Won": won,
            }
            newRT2 = {
                name2: points2Total,
                name1: points1Total,
                "Won": won,            
            }
            results[i]["Match" + str(curLoop)] = newRT
            results[y]["Match" + str(curLoop)] = newRT2
            curLoop += 1
    totalString = resultsToText(results, totalString)

dir_path = os.path.join(os.getcwd(), "Results")
os.makedirs(dir_path, exist_ok=True)

count = len([f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))])
file_name = f"Results {iterations} iterations and {rounds} rounds {count + 1}.txt"
file_path = os.path.join(dir_path, file_name)

with open(file_path, "x") as resultF:
    resultF.write(totalString)