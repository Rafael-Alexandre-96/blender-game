class Attribute:

    def __init__(self, value = 0, max = 0):
        self._value = value
        self._max = max

    def getMax(self):
        return self._max

    def setMax(self, max):
        self._max = max

    def getValue(self):
        return self._value
    
    def setValue(self, value):
        self._value = value

    def decrease(self, value):
        if value > 0:
            if (self._value - value) < 0:
                self._value = 0
            else:
                self._value -= value

    def increase(self, value):
        if value > 0:
            if (self._value + value) > self._max:
                self._value = self._max
            else:
                self._value += value

    def isFulled(self):
        return self._value == self._max
    
    def isEmpty(self):
        return self._value == 0