from customer import Customer
from reservation import Reservation
from database import Database
from cart import Cart
from utils import log_reservation, print_divider
from data import transports, hotels
from validation import validate_phone, validate_email
from payment import process_payment
from reservation import clear_reservations

class TravelBookingSystem:
    def __init__(self):
        self.database = Database()
        self.cart = Cart()
        self.hotels = hotels
        self.last_customer = None 

    def start(self):
        print_divider("🏖️ Система бронювання подорожей 🏖️")
        while True:
            print("1. Бронювати квиток")
            print("2. Замовити готель")
            print("3. Переглянути кошик")
            print("4. Оформити замовлення")
            print("5. Очистити резервування")
            print("6. Вийти")

            choice = input("Оберіть опцію: ")
            try:
                if choice == '1':
                    self.book_ticket()
                elif choice == '2':
                    self.book_hotel()
                elif choice == '3':
                    self.view_cart()
                elif choice == '4':
                    self.checkout()
                elif choice == '5':
                    clear_reservations()
                elif choice == '6':
                    print("Вихід...")
                    break
                else:
                    raise ValueError("Неправильний вибір.")
            except Exception as e:
                print(f"❌ Помилка: {e}")

    def book_ticket(self):
        customer = self.get_customer_data()
        print("\nДоступний транспорт:")
        for idx in range(len(transports)):
            transport, price = transports[idx]
            print(f"{idx + 1}. {transport} - {price} грн")

        try:
            transport_choice = int(input("Оберіть транспорт (номер): ")) - 1
            if transport_choice < 0 or transport_choice >= len(transports):
                raise IndexError("Неправильний номер транспорту.")
            transport, price = transports[transport_choice]
            reservation = Reservation(customer, transport, price)
            self.cart.add_to_cart(reservation)

            # Запис в файл
            log_reservation(reservation)

            print(f"\n✅ {customer.name}, ви додали квиток на {transport} до кошика.")
        except ValueError as e:
            print(f"❌ Помилка: {e}")
        except IndexError as e:
            print(f"❌ Помилка: {e}")

    def book_hotel(self):
        customer = self.get_customer_data()
        print("\nДоступні готелі:")
        for i in range(len(self.hotels)):
            hotel, price = self.hotels[i]
            print(f"{i + 1}. {hotel} - {price} грн за ніч")
        try:
            hotel_choice = int(input("Оберіть готель (номер): ")) - 1
            if hotel_choice < 0 or hotel_choice >= len(self.hotels):
                raise IndexError("Неправильний номер готелю.")
            hotel, price = self.hotels[hotel_choice]
            reservation = Reservation(customer, hotel, price)
            self.cart.add_to_cart(reservation)

            # Запис в файл
            log_reservation(reservation)

            print(f"\n✅ {customer.name}, ви замовили готель {hotel}.")
        except (ValueError, IndexError) as e:
            print(f"❌ Помилка: {e}")

    def get_customer_data(self):
        while True:
            if self.last_customer:
                use_last = input("Використати попередні дані клієнта? (так/ні): ").strip().lower()
                if use_last == "так":
                    return self.last_customer
                elif use_last == "ні":
                    break
                else:
                    print("❌ Неправильний вибір. Спробуйте ще раз.")
                    continue
            
            name = input("Введіть ваше ім'я: ").strip().capitalize()
            phone = validate_phone(self.cart)
            email = validate_email(self.cart)
            customer = Customer(name, phone, email)
            self.last_customer = customer
            return customer

    def view_cart(self):
        reservations = self.cart.view_cart()
        if not reservations:
            print("Ваш кошик порожній.")
        else:
            print("\nВаш кошик:")
            for reservation in reservations:
                print(f"- {reservation.transport_or_hotel} - {reservation.price} грн")

    def checkout(self):
        reservations = self.cart.view_cart()
        if not reservations:
            print("Ваш кошик порожній. Додайте щось у кошик перед оформленням.")
            return
        print("\nВаш кошик:")
        for idx, reservation in enumerate(reservations):
            print(f"{idx}. {reservation.transport_or_hotel} - {reservation.price} грн")

        while True:
            confirm = input("Ви впевнені, що хочете оформити замовлення? (так/ні): ").strip().lower()
            if confirm == "так":
                process_payment(self.cart, self.database)
                break
            elif confirm == "ні":
                print("❌ Оформлення скасовано.")
                return
            else:
                print("❌ Неправильний вибір. Спробуйте ще раз.")

system = TravelBookingSystem()
system.start()
