import bge # type: ignore
import mathutils # type: ignore
import random
from Mouse import Mouse
from Attribute import Attribute
import Game

class Player:

    _instance = None

    def __init__(self):
        self._velocity = 0.05
        self._kxObj = None
        self._hpAtr = Attribute(100, 100)
        self._kvAtr = Attribute(0, 100)
        self._goldAtr = Attribute(100, 999999)
        self._roofObj = None
        
    def getRoofObj(self):
        return self._roofObj
        
    def setRoofObj(self, kxObject):
        self._roofObj = kxObject
    
    def getKxObject(self):
        return self._kxObj

    def setKxObject(self, kxObject):
        self._kxObj = kxObject

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
    def heal(self, value):
        self._hpAtr.increase(value)

    def addKv(self, value):
        self._kvAtr.increase(value)

    def damage(self, value):
        if not(self._kvAtr.isEmpty()):
            self._hpAtr.decrease(int(value / 2))
            self._kvAtr.decrease(int(value * 0.667))
        else:
            self._hpAtr.decrease(value)

        if self._hpAtr.getValue() <= 0:
            Game.gameOver()
            
    def getHp(self):
        return self._hpAtr.getValue()
    
    def getMaxHp(self):
        return self._hpAtr.getMax()
    
    def hpIsFulled(self):
        return self._hpAtr.isFulled()
    
    def getKv(self):
        return self._kvAtr.getValue()
    
    def getMaxKv(self):
        return self._kvAtr.getMax()
    
    def kvIsFulled(self):
        return self._kvAtr.isFulled()
    
    def addGold(self, value):
        self._goldAtr.increase(value)

    def removeGold(self, value):
        self._goldAtr.decrease(value)

    def getGold(self):
        return self._goldAtr.getValue()
    
    def isRich(self):
        return self._goldAtr.isFulled()
    
    def move(self, vector):
        self._kxObj.applyMovement(vector.normalized() * self._velocity, False)

def start(controller):
    player = Player.instance()
    player.setKxObject(controller.owner)
    
def update():
    pass

def move():
    player = Player.instance()
    kxObj = player.getKxObject()
    moveVector = mathutils.Vector((0.0, 0.0, 0.0))
    
    if kxObj.sensors['F'].positive:
        moveVector.y += 1
    elif kxObj.sensors['B'].positive:
       moveVector.y -= 1
           
    if kxObj.sensors['L'].positive:
        moveVector.x -= 1
    elif kxObj.sensors['R'].positive:
        moveVector.x = 1
    
    player.move(moveVector)
        
def aim():
    mouse = Mouse.instance()
    player = Player.instance()
    kxObj = player.getKxObject()
    kxObj.orientation = mathutils.Matrix.Rotation(mouse.getAngle(), 4, 'Z').to_3x3()

def collision():
    player = Player.instance()
    kxObj = player.getKxObject()
    if kxObj.sensors['CollisionItem'].positive:
        item = kxObj.sensors['CollisionItem'].hitObject
        if item['Item']:
            item['instance'].consume()
            
def roof():
    player = Player.instance()
    kxObj = player.getKxObject()
    if kxObj.sensors['RayRoof'].positive:
        player.setRoofObj(kxObj.sensors['RayRoof'].hitObject)
        player.getRoofObj().visible = False
    else:
        player.getRoofObj().visible = True