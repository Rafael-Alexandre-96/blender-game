import Game

class Barril:

    def __init__(self):
        self._kxObj = None
        self._nearList = []
    
    def getKxObject(self):
        return self._kxObj

    def setKxObject(self, kxObject):
        self._kxObj = kxObject
        
    def setNearList(self, list):
        self._nearList = list

    def getNearList(self):
        return self._nearList

    def shooted(self, originBullet, weapon):
        for shootable in self.getNearList():
            shootable['instance'].damage(100 / self._kxObj.getDistanceTo(shootable))
        Game.addObject('Explosion_Sound', self.getKxObject())
        Game.addObject('Barril_Explosion', self.getKxObject())
        self._nearList = []
        self.getKxObject().endObject()

def start(controller):
    barril = Barril()
    barril.setKxObject(controller.owner)
    barril.getKxObject()['instance'] = barril

def update(controller):
    barril = controller.owner['instance']
    barril.setNearList([])

    if controller.sensors['NearExplosion'].positive:
        for shootable in controller.sensors['NearExplosion'].hitObjectList:
            if shootable == barril.getKxObject().rayCastTo(shootable):
                barril.getNearList().append(shootable)

    Game.print(barril.getNearList())

def explode(controller):
    scale = controller.owner.worldScale
    mult = 1.3
    controller.owner.worldScale = [scale.x * mult, scale.y * mult, scale.z * mult]
    if controller.owner.worldScale.z > 5:
        controller.owner.endObject()