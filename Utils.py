import math

def forceOff(originObj, destinyObj, force):
    x = destinyObj.worldPosition.x - originObj.worldPosition.x
    y = destinyObj.worldPosition.y - originObj.worldPosition.y
    angle = math.atan(x / y)
    if y > 0:
        angle += math.pi
    destinyObj.applyForce([-math.sin(angle) * force, -math.cos(angle) * force, 0], False)