import bge  # type: ignore
from Player import Player
from WeaponManager import WeaponManager

class PrintAction:
    def execute(self):
        print('test')

class HealItemAction:
    def __init__(self, item):
        self._item = item

    def execute(self):
        if not(Player.instance().hpIsFulled()):
            self._item.getKxObject().endObject()
            Player.instance().heal(self._item.getValue())

class KvItemAction:
    def __init__(self, item):
        self._item = item

    def execute(self):
        if not(Player.instance().kvIsFulled()):
            self._item.getKxObject().endObject()
            Player.instance().addKv(self._item.getValue())

class GoldItemAction:
    def __init__(self, item):
        self._item = item

    def execute(self):
        if not(Player.instance().isRich()):
            self._item.getKxObject().endObject()
            Player.instance().addGold(self._item.getValue())

class BulletsItemAction:
    def __init__(self, item):
        self._item = item

    def execute(self):
        if WeaponManager.instance().addBullets(int(self._item.getSubType()), self._item.getValue()):
            self._item.getKxObject().endObject()
