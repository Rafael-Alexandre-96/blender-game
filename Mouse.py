import bge # type: ignore
import math

class Mouse:

    _instance = None

    def __init__(self):
        self._x = 0
        self._y = 0
        self._angle = 0
        self._kxObj = None
        self._bgeMouse = bge.logic.mouse

    def getX(self):
        return (self._bgeMouse.position[0] - 0.5) * 16 / 9
    
    def getY(self):
        return self._bgeMouse.position[1] - 0.5
    
    def getAngle(self):
        if self.getY() != 0:
            tang = self.getX() / self.getY()
            self._angle = math.atan(tang)
        
            if self.getY() > 0:
                self._angle += math.pi
        
        return self._angle

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance