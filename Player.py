import bge # type: ignore
import mathutils # type: ignore
from Mouse import Mouse
from Attribute import Attribute
import Game

INITIAL_VEL = 0.05
IDLE = "Idle"
WALK = "Walk"
RUN = "Run"

class Player:

    _instance = None

    def __init__(self):
        self._velocity = INITIAL_VEL
        self._mode = IDLE
        self._kxObj = None
        self._hpAtr = Attribute(100, 100)
        self._kvAtr = Attribute(0, 100)
        self._goldAtr = Attribute(100, 999999)
        self._roofObj = None

    def getMode(self):
        return self._mode
    
    def setIdle(self):
        self._mode = IDLE

    def setWalk(self):
        self._mode = WALK

    def setRun(self):
        self._mode = RUN

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
        return int(self._hpAtr.getValue())
    
    def getMaxHp(self):
        return int(self._hpAtr.getMax())
    
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
        if self.getMode() == WALK:
            self._velocity = INITIAL_VEL
        elif self.getMode() == RUN:
            self._velocity = INITIAL_VEL * 1.5

        self._kxObj.applyMovement(vector.normalized() * self._velocity, False)

    def isRunning(self, running = True):
        if running:
            self.setRun()

    def shooted(self, originBullet, damage = 0, critical = 0, force = 0):
        pass

def start(controller):
    player = Player.instance()
    player.setKxObject(controller.owner)
    player.getKxObject()['instance'] = player
    
def update():
    player = Player.instance()
    kxObj = player.getKxObject()
    kxObj['mode'] = player.getMode()

    moveVector = mathutils.Vector((0.0, 0.0, 0.0))
    player.setIdle()
    
    if kxObj.sensors['F'].positive:
        player.setWalk()
        moveVector.y += 1
    elif kxObj.sensors['B'].positive:
       player.setWalk()
       moveVector.y -= 1
           
    if kxObj.sensors['L'].positive:
        player.setWalk()
        moveVector.x -= 1
    elif kxObj.sensors['R'].positive:
        player.setWalk()
        moveVector.x = 1

    player.isRunning(kxObj.sensors['Run'].positive)
    
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