import bge  # type: ignore
import Player
from Weapon import Weapon
from Mouse import Mouse
import Game

PISTOL_INDEX = 0
SUB_INDEX = 1
SHOTGUN_INDEX = 2
RIFLE_INDEX = 3
PLASMA_INDEX = 4

class WeaponManager:
    
    _instance = None

    def __init__(self):
        self._kxObj = None
        self._weapons = []
        self._selectedWeapon = None
        self.createWeapons()
        
    def createWeapons(self):
        pistol = Weapon('Pistol', 10, 40, 7, 1000, 2000, 100, False)
        self._weapons.append(pistol)
        self._weapons.append(Weapon('Sub', 7, 10, 5, 50, 50, 50, False))
        self._weapons.append(Weapon('Shotgun', 22, 60, 1, 7, 14, 230, False))
        self._weapons.append(Weapon('Rifle', 15, 13, 10, 25, 100, 70, False))
        self._weapons.append(Weapon('Plasma', 30, 10, 1, 50, 200, 10, False))
        self._selectedWeapon = pistol

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
    def getKxObject(self):
        return self._kxObj

    def setKxObject(self, kxObject):
        self._kxObj = kxObject
    
    def selectWeapon(self, index = 0):
        if not(self._weapons[index].isLocked()):
            self._selectedWeapon = self._weapons[index]
        
    def getSelectedWeapon(self):
        return self._selectedWeapon
    
    def updateTriggers(self):
        if self.getSelectedWeapon().getTriggerShootValue() != 0:
            self.getSelectedWeapon().updateTriggerShoot()

    def addBullets(self, index = 0, bullets = 0):
        weapon = self._weapons[index]
        if not(weapon.isFulled()):
            weapon.addBullets(bullets)
            return True
        return False
    
    def getBullets(self, index = 0):
        return self._weapons[index].getBullets()
    
def start(controller):
    wm = WeaponManager.instance()
    wm.setKxObject(controller.owner)
    
def update():
    wm = WeaponManager.instance()
    wm.updateTriggers()

def shoot(controller):
    if Player.Player.instance().getMode() != 'Run':
        wm = WeaponManager.instance()
        weapon = wm.getSelectedWeapon()
        if weapon.shoot():
            lampObj = 'Shoot_Lamp'
            if (weapon.getName() == 'Plasma'):
                lampObj = 'Plasma_Shoot_Lamp'
            bge.logic.getCurrentScene().addObject(lampObj, wm.getKxObject(), 5)
            bge.logic.getCurrentScene().addObject(wm.getSelectedWeapon().getName() + '_Shoot_Sound', wm.getKxObject())
            obj = Mouse.instance().getKxOver()
            if not(obj is None):
                if obj == Player.Player.instance().getKxObject().rayCastTo(obj, 0):
                    obj['instance'].shooted(controller.owner, weapon)
        
def changeWeapon(controller):
    wm = WeaponManager.instance()
    if controller.owner.sensors['Pistol'].positive:
        wm.selectWeapon(PISTOL_INDEX)
    if controller.owner.sensors['Sub'].positive:
        wm.selectWeapon(SUB_INDEX)
    if controller.owner.sensors['Shotgun'].positive:
        wm.selectWeapon(SHOTGUN_INDEX)
    if controller.owner.sensors['Rifle'].positive:
        wm.selectWeapon(RIFLE_INDEX)
    if controller.owner.sensors['Plasma'].positive:
        wm.selectWeapon(PLASMA_INDEX)