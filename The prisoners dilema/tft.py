import random

def calcs(iP, hP, points):
  play = None
  if hP == None:
    play = 0
  else:
    play = abs(int(hP) - 1)

  return play
