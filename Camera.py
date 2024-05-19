import bge # type: ignore
from Player import Player

class Camera:

    _instance = None

    def __init__(self):
        self._kxObj = None
        self._zoom = 0
        self._followed = None
    
    def getKxObject(self):
        return self._kxObj

    def setKxObject(self, kxObject):
        self._kxObj = kxObject

    def setFollowed(self, followed):
        self._followed = followed

    def follow(self):
        if not(self._followed is None):
            self._kxObj.position.x = self._followed.position.x
            self._kxObj.position.y = self._followed.position.y - 13 - self._zoom
            self._kxObj.position.z = self._followed.position.z + 13 + self._zoom

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
    def zoomIn(self):
        if self._zoom > -5:
            self._zoom -= 1
        
    def zoomOut(self):
        if self._zoom < 5:
            self._zoom += 1

    def getZoom(self):
        return self._zoom

def start(controller):
    camera = Camera.instance()
    camera.setKxObject(controller.owner)
    camera.setFollowed(Player.instance().getKxObject())

def update():
    Camera.instance().follow()
    
def zoom():
    camera = Camera.instance()
    KxObj = camera.getKxObject()

    if KxObj.sensors['ZoomIn'].positive:
        camera.zoomIn()

    if KxObj.sensors['ZoomOut'].positive:
        camera.zoomOut()