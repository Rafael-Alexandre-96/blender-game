import bge  # type: ignore
import random

def randomLight(controller):
    controller.owner.energy = random.randint(80, 120) * 0.01