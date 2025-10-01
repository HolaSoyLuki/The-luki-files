import random

def calcs(iP, hP, points):
  play = None
  if hP == None:
    play = random.randint(0,1)
  else:
    play = abs(int(hP) - 1)
  return play