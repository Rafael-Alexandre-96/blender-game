import bge # type: ignore
from Player import Player
from WeaponManager import WeaponManager
from Mouse import Mouse

class Cursor:
    _instance = None

    def __init__(self):
        self._kxObj = None

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def getKxObject(self):
        return self._kxObj

    def setKxObject(self, kxObject):
        self._kxObj = kxObject

    def setFireCursor(self):
        if not(self._kxObj is None):
            self._kxObj.replaceMesh('Cursor_Fire')

    def setAimCursor(self):
        if not(self._kxObj is None):
            self._kxObj.replaceMesh('Cursor')

    def updatePosition(self):
        mouse = Mouse.instance()
        x = mouse.getX() * 15.8
        y = -mouse.getY() * 15.8
        self._kxObj.worldPosition = [x, y, 0]

def startCursor(controller):
    cursor = Cursor.instance()
    cursor.setKxObject(controller.owner)

def updateCursor():
    cursor = Cursor.instance()
    cursor.updatePosition()
    cursor.setAimCursor()
    try:
        if not(Mouse.instance().getKxOver() is None):
            if Mouse.instance().getKxOver() == Player.instance().getKxObject().rayCastTo(Mouse.instance().getKxOver(), 0):
                if 'Shootable' in Mouse.instance().getKxOver():
                    if Mouse.instance().getKxOver()['Shootable']:
                        cursor.setFireCursor()
    except:
        Mouse.instance().removeKxOver()
    
def updateHpText(controller):
    player = Player.instance()
    controller.owner['Text'] = str(player.getHp()) + "/" + str(player.getMaxHp())
    
def updateHpBar(controller):
    player = Player.instance()
    controller.owner.localScale = [player.getHp() / player.getMaxHp(), 1, 1]

def updateKvText(controller):
    player = Player.instance()
    controller.owner['Text'] = str(player.getKv()) + "/" + str(player.getMaxKv())
    
def updateKvBar(controller):
    player = Player.instance()
    controller.owner.localScale = [player.getKv() / player.getMaxKv(), 1, 1]
    
def updateBulletsText(controller):
    wm = WeaponManager.instance()
    controller.owner['Text'] = str(wm.getSelectedWeapon().getBullets()) + "/" + str(wm.getSelectedWeapon().getMaxBullets())

def updateGoldText(controller):
    player = Player.instance()
    controller.owner['Text'] = str(player.getGold())

def updateInDanger(controller):
    player = Player.instance()
    controller.owner.visible = player.getHp() <= 20