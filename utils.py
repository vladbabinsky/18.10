def log_reservation(reservation):
    with open("reservations.txt", "a", encoding='utf-8') as file:
        file.write(
            f"\n----------------------------------------\n"
            f"📝 Бронювання:\n"
            f"Клієнт: {reservation.customer.name}\n"
            f"Телефон: {reservation.customer.phone}\n"
            f"Email: {reservation.customer.email}\n"
            f"Транспорт/Готель: {reservation.transport_or_hotel}\n"
            f"Ціна: {reservation.price} грн\n"
            f"----------------------------------------\n"
        )


def print_divider(message):
    print("\n" + "=" * (len(message) + 4))
    print("  " + message + "  ")
    print("=" * (len(message) + 4))


