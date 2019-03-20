class Die:

    def __init__(self):
        self.value = 0
        self.status = False   #False = unlocked, True = Locked

    def __eq__(self, other):
        return self.value == other.value and self.status == other.status