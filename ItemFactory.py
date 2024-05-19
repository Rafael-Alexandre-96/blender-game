import random
import Item
import WeaponManager
import Actions

def smallHp() -> Item.Item:
    item = Item.Item()
    item.setType(Item.TYPE_HP)
    item.setValue(15)
    item.setAction(Actions.HealItemAction(item))
    return item

def mediumHp() -> Item.Item:
    item = Item.Item()
    item.setType(Item.TYPE_HP)
    item.setValue(25)
    item.setAction(Actions.HealItemAction(item))
    return item

def bigHp() -> Item.Item:
    item = Item.Item()
    item.setType(Item.TYPE_HP)
    item.setValue(50)
    item.setAction(Actions.HealItemAction(item))
    return item

def smallKv() -> Item.Item:
    item = Item.Item()
    item.setType(Item.TYPE_KV)
    item.setValue(15)
    item.setAction(Actions.KvItemAction(item))
    return item

def bulletsPistol() -> Item.Item:
    item = Item.Item()
    item.setType(Item.TYPE_BULLETS)
    item.setSubType(str(WeaponManager.PISTOL_INDEX))
    item.setValue(10)
    item.setAction(Actions.BulletsItemAction(item))
    return item

def bulletsSub() -> Item.Item:
    item = Item.Item()
    item.setType(Item.TYPE_BULLETS)
    item.setSubType(str(WeaponManager.SUB_INDEX))
    item.setValue(20)
    item.setAction(Actions.BulletsItemAction(item))
    return item

def bulletsShotgun() -> Item.Item:
    item = Item.Item()
    item.setType(Item.TYPE_BULLETS)
    item.setSubType(str(WeaponManager.SHOTGUN_INDEX))
    item.setValue(7)
    item.setAction(Actions.BulletsItemAction(item))
    return item

def bulletsRifle() -> Item.Item:
    item = Item.Item()
    item.setType(Item.TYPE_BULLETS)
    item.setSubType(str(WeaponManager.RIFLE_INDEX))
    item.setValue(15)
    item.setAction(Actions.BulletsItemAction(item))
    return item

def randomSmallGold() -> Item.Item:
    item = Item.Item()
    item.setType(Item.TYPE_GOLD)
    item.setValue(random.randint(1, 5) * 50)
    item.setAction(Actions.GoldItemAction(item))
    return item