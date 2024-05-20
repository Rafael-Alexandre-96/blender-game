import bge # type: ignore
import Game
from Mouse import Mouse

def addZoombie(controller):
    Game.addZoombie(controller.owner)