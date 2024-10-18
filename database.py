class Database:
    def __init__(self):
        self.reservations = []

    def save_reservation(self, reservation):
        self.reservations.append(reservation)

    def get_reservations(self):
        return self.reservations
