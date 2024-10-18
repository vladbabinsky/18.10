class Reservation:
    def __init__(self, customer, transport_or_hotel, price):
        self.customer = customer
        self.transport_or_hotel = transport_or_hotel
        self.price = price

    def __str__(self):
        return f"Бронювання для {self.customer.name} на {self.transport_or_hotel} - {self.price} грн"

def clear_reservations():
    with open("reservations.txt", "w") as file:
        file.write("")
    print("✅ Резервування очищено.")
