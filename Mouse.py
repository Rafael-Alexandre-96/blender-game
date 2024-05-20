import bge # type: ignore
import math
import Game

class Mouse:

    _instance = None

    def __init__(self):
        self._x = 0
        self._y = 0
        self._angle = 0
        self._kxObj = None
        self._bgeMouse = bge.logic.mouse
        self._kxOver = None

    def getKxObject(self):
        return self._kxObj

    def setKxObject(self, kxObject):
        self._kxObj = kxObject

    def getX(self):
        return (self._bgeMouse.position[0] - 0.5) * 16 / 9
    
    def getY(self):
        return self._bgeMouse.position[1] - 0.5
    
    def getAngle(self):
        if self.getY() != 0:
            tang = (self.getX() * 0.72) / self.getY()
            self._angle = math.atan(tang)
        
            if self.getY() > 0:
                self._angle += math.pi
        
        return self._angle

    def setKxOver(self, kxObject):
        self._kxOver = kxObject

    def getKxOver(self):
        return self._kxOver
    
    def removeKxOver(self):
        self._kxOver = None

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
def start(controller):
    mouse = Mouse.instance()
    mouse.setKxObject(controller.owner)

def update():
    pass

def setMouseOver(controller):
    if controller.sensors['MouseOver'].positive:
        Mouse.instance().setKxOver(controller.owner)
    else:
        Mouse.instance().setKxOver(None)