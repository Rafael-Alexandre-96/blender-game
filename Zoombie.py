import bge # type: ignore
import mathutils # type: ignore
import math
import Utils
import random
import Game
from Attribute import Attribute
from Trigger import Trigger
from Player import Player

IDLE = 'Idle'
WALK = 'Walk'
FOLLOW = 'Follow'
DEAD = 'Dead'
ATK = 'Atk'

class Zoombie:

    def __init__(self):
        self._velocity = 0.0250
        self._kxObj = None
        self._hpAtr = Attribute(50, 50)
        self._rotTrigger = Trigger(0, random.randint(180, 240))
        self._movTrigger = Trigger(0, random.randint(100, 140))
        self._atkTrigger = Trigger(0, 80)
        self._endObjTrigger = Trigger(-1, 300)
        self._damage = 10
        self._hpBar = None
        self._dropZoombie = None
        self._bloodZoombie = None
        self._armatureZoombie = None
        self._mode = WALK
    
    def getKxObject(self):
        return self._kxObj

    def setKxObject(self, kxObject):
        self._kxObj = kxObject
        for children in kxObject.childrenRecursive:
            if children.name == "Drop_Zoombie":
                self._dropZoombie = children
            if children.name == "Blood_Zoombie":
                self._bloodZoombie = children
            if children.name == "Zoombie_Armature":
                self._armatureZoombie = children
            if children.name == "Zoombie_HP":
                self._hpBar = children

    def getHp(self):
        return self._hpAtr.getValue()
    
    def getMaxHp(self):
        return self._hpAtr.getMax()

    def damage(self, value):
        beforeLife = self.getHp()
        self._hpAtr.decrease(value)
        self._hpBar.localScale = [self.getHp() / self.getMaxHp(), 1, 1]
        blood = Game.addObject('Blood', self._bloodZoombie, 300)
        scale = ((beforeLife - self.getHp()) / self.getMaxHp())
        blood.localScale = [scale, scale, scale]
        if self._hpAtr.getValue() <= 0:
            #if random.randint(1,2) == 1:
            #    Game.instance().addDrop(self._dropZoombie)
            self._kxObj['Shootable'] = False
            self._kxObj.suspendDynamics(True)
            Game.print("Morreu")
            self._mode = DEAD
    
    def updateTriggers(self):
        self._rotTrigger.updateTrigger()
        self._movTrigger.updateTrigger()
        
        if self._atkTrigger.getValue() != 0:
            self._atkTrigger.updateTrigger()
        
        if self._mode == DEAD:
            self._endObjTrigger.updateTrigger()
            if self._endObjTrigger.getValue() == 0:
                Game.removeZoombie(self._kxObj)

    def resetAtkTrigger(self):
        self._atkTrigger.reset()
    
    def getMode(self):
        return self._mode
    
    def shooted(self, originBullet, weapon):
        if not(self._mode == DEAD):
            damage = weapon.getDamage()
            damage += random.randint(int(-damage / 2), int(damage / 2))
            if random.randint(1, 100) <= weapon.getCritical():
                    damage *= 3
            Utils.forceOff(originBullet, self.getKxObject(), weapon.getForce())
            self.setFollow()
            self.damage(damage)

    def setIdle(self):
        self._mode = IDLE

    def idle(self):
        if (self._movTrigger.getValue() == 0):
            if random.randint(0, 3) == 2:
                self.setWalk()

    def move(self, vector = mathutils.Vector((0.0, 1.0, 0.0))):
        frame = self._armatureZoombie.getActionFrame(0)

        if (frame < 16 or (frame > 40 and frame < 60) or frame > 110):
            self._kxObj.applyMovement(vector.normalized() * self._velocity, True)
        else:
           self._kxObj.applyMovement(vector.normalized() * self._velocity / 2, True)
    
    def setWalk(self):
        self._mode = WALK

    def walk(self, sensorCollision = False): #OUTRO
        if (self._rotTrigger.getValue() == 0):
            self._kxObj.applyRotation([0, 0, (math.pi / 2) * random.randint(0, 3)], True)

        if (self._movTrigger.getValue() == 0):
            if random.randint(0, 3) == 2:
                self.setIdle()
            
        if sensorCollision: #BUG
            self._kxObj.applyRotation([0, 0, math.pi / 2], True)

        self.move()

    def setFollow(self):
        if self._kxObj.rayCastTo(Player.instance().getKxObject()) == Player.instance().getKxObject():
            self._mode = FOLLOW

    def follow(self):
        if self._kxObj.rayCastTo(Player.instance().getKxObject()) == Player.instance().getKxObject():
            self.move()
        else:
            self.setIdle()

    def setAtk(self):
        if self._kxObj.rayCastTo(Player.instance().getKxObject()) == Player.instance().getKxObject():
            self._mode = ATK

    def atk(self):
        if self._kxObj.rayCastTo(Player.instance().getKxObject()) == Player.instance().getKxObject():
            if self._atkTrigger.getValue() == 0:
                self._atkTrigger.updateTrigger()

            if self._atkTrigger.getValue() == 46:
                player = Player.instance()
                player.damage(self._damage)
        else:
            self.setIdle()
        
def start(controller):
    zoombie = Zoombie()
    zoombie.setKxObject(controller.owner)
    zoombie.getKxObject()['instance'] = zoombie
    zoombie.getKxObject()['Zoombie'] = True

def update(controller):
    zoombieObj = controller.owner
    if zoombieObj['Zoombie']:
        zoombie = zoombieObj['instance']
        zoombie.updateTriggers()
        zoombieObj = zoombie.getKxObject()
        zoombieObj['mode'] = zoombie.getMode()
        controller.deactivate(zoombieObj.actuators['Track'])

    if zoombie.getMode() != DEAD:
        if zoombie.getMode() == IDLE:
            zoombie.idle()
        elif zoombie.getMode() == WALK:
            zoombie.walk(zoombieObj.sensors['RadarCollision'].positive)
        elif zoombie.getMode() == FOLLOW:
            controller.activate(zoombieObj.actuators['Track'])
            zoombie.follow()
        elif zoombie.getMode() == ATK:
            zoombie.atk()

        if (zoombieObj.sensors['RadarPlayer'].positive or zoombieObj.sensors['NearPlayer'].positive):
            zoombie.setFollow()

        if zoombieObj.sensors['AtkPlayer'].positive:
            zoombie.setAtk()
        else:
            zoombie.resetAtkTrigger()