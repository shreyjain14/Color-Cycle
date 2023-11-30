def getNewVals(redVal, greenVal, blueVal, redValInc, greenValInc, blueValInc):
    colors = sorted([checkSteps(redVal, redValInc), checkSteps(redVal, redValInc), checkSteps(blueVal, blueValInc)])
    steps = colors[0]
    red = redVal + (steps * redValInc)
    green = greenVal + (steps * greenValInc)
    blue = blueVal + (steps * blueValInc)
    return red, green, blue


def checkSteps(val, valInc):
    if valInc == 0:
        return 999
    elif valInc < 0:
        return int((val / valInc) * -1)
    else:
        return int((256 - val) / valInc)
