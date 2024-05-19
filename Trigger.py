class Trigger:
    
    def __init__(self, value = 0, max = 10):
        self._value = value
        self._max = max
        self._step = 1

    def getValue(self):
        return self._value
    
    def updateTrigger(self):
        self._value -= self._step
        if self._value < 0:
            self._value = self._max

    def reset(self):
        self._value = 0