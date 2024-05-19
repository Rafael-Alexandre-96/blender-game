import bge # type: ignore
from Player import Player
from WeaponManager import WeaponManager
from Mouse import Mouse

def updateCursor(controller):
    mouse = Mouse.instance()
    x = mouse.getX() * 15.8
    y = -mouse.getY() * 15.8
    mult = 0.7
    controller.owner.worldPosition = [x / mult, y + mult, 0]
    
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