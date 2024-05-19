import bge  # type: ignore
import ItemFactory
import Game

def start(KxObject, item):
    KxObject['instance'] = item
    item.setKxObject(KxObject)
    KxObject['Item'] = True

def addSmallHp(controller):
    kxObject = Game.addObject('Item_HP', controller.owner)
    start(kxObject, ItemFactory.smallHp())
    
def addBulletsPistol(controller):
    kxObject = Game.addObject('Item_Bullets', controller.owner)
    start(kxObject, ItemFactory.bulletsPistol())