from Trigger import Trigger
from Attribute import Attribute

class Weapon:
    
    def __init__(self, name = None, damage = 0, triggerShoot = 5, critical = 0, bullets = 0, maxBullets = 0, force = 100, locked = True):
        self._name = name
        self._damage = damage
        self._triggerShoot = Trigger(0, triggerShoot)
        self._critical = critical
        self._atrBullets = Attribute(bullets, maxBullets)
        self._force = force
        self._locked = locked

    def getName(self):
        return self._name
        
    def getDamage(self):
        return self._damage
    
    def getCritical(self):
        return self._critical
    
    def getTriggerShootValue(self):
        return self._triggerShoot.getValue()
    
    def updateTriggerShoot(self):
        self._triggerShoot.updateTrigger()
        
    def getBullets(self):
        return self._atrBullets.getValue()
    
    def getMaxBullets(self):
        return self._atrBullets.getMax()
    
    def getForce(self):
        return self._force
    
    def isLocked(self):
        return self._locked

    def addBullets(self, value):
        self._atrBullets.increase(value)

    def isFulled(self):
        return self._atrBullets.isFulled()
        
    def shoot(self):
        if self.getTriggerShootValue() == 0 and self.getBullets() > 0:
            self.updateTriggerShoot()
            self._atrBullets.decrease(1)
            return True
        return False