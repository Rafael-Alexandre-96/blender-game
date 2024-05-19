import bge # type: ignore

class Game:

    _instance = None

    def __init__(self):
        self._kxObj = None
        self._cursorObj = None
        self._zoombies = []
        
    def getKxObject(self):
        return self._kxObj

    def setKxObject(self, kxObject):
        self._kxObj = kxObject

    def setCursorObj(self, kxObject):
        self._cursorObj = kxObject

    def setFireCursor(self):
        if not(self._cursorObj is None):
            self._cursorObj.replaceMesh('Cursor_Fire')

    def setAimCursor(self):
        if not(self._cursorObj is None):
            self._cursorObj.replaceMesh('Cursor')

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
    def print(self, value):
        Game.instance().getKxObject()['print'] = str(value)

###LIFECICLE
def start(controller):
    game = Game.instance()
    game.setKxObject(controller.owner)
    
def update():
    pass

def gameOver():
    bge.logic.endGame()

###HUD
def startCursor(controller):
    Game.instance().setCursorObj(controller.owner)

def setFireCursor():
    Game.instance().setFireCursor()
    
def setAimCursor():
    Game.instance().setAimCursor()

###UTILS
def addObject(kxObject, location, time = 0):
    scene = bge.logic.getCurrentScene()
    return scene.addObject(kxObject, location, time)

def print(value):
    Game.instance().print(value)

###LIMIT ENTITIES
def addZoombie(location):
    if len(Game.instance()._zoombies) < 2:
        zoombieObj = addObject('Zoombie_Obj', location)
        Game.instance()._zoombies.append(zoombieObj)

def removeZoombie(zoombieObj):
    zoombieObj.endObject()
    Game.instance()._zoombies.remove(zoombieObj)