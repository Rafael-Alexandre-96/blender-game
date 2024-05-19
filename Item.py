class Item:
    def __init__(self, type = '', subType = '', value = 0):
        self._type = type
        self._subType = subType
        self._value = value
        self._action = None
        self._kxObj = None

    def getKxObject(self):
        return self._kxObj

    def setKxObject(self, kxObject):
        self._kxObj = kxObject

    def getType(self):
        return self._type
    
    def getSubType(self):
        return self._subType
    
    def getValue(self):
        return self._value
    
    def setType(self, type):
        self._type = type
    
    def setSubType(self, subType):
        self._subType = subType
    
    def setValue(self, value):
        self._value = value

    def setAction(self, action):
        self._action = action

    def consume(self):
        self._action.execute()

TYPE_HP = 'hp'
TYPE_KV = 'kv'
TYPE_BULLETS = 'bullets'
TYPE_GOLD = 'gold'