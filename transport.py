class Transport:
    def __init__(self, origin, destination):
        self.origin = origin
        self.destination = destination

    def __str__(self):
        return f"{self.transport_type} з {self.origin} до {self.destination}"
