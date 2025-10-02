def calcs(iP, hP, points):
    play = None
    if iP == None:
        play = 1
    else:
        if iP == 1:
            play = 0
        elif iP == 0:
            play = 1
    return play
