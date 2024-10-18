from utils import log_reservation

def process_payment(cart, database):
    print("\nОформлення оплати...")
    card_number = input("Введіть номер картки: ").strip().replace(" ", "")
    
    if len(card_number) == 16 and card_number.isdigit():
        total_amount = 0
        for reservation in cart.view_cart():
            total_amount += reservation.price

        print(f"✅ Оплата успішна за допомогою картки {card_number}.")
        print(f"💳 З вашої карти списано: {total_amount} грн.")
        
        for reservation in cart.view_cart():
            database.save_reservation(reservation)
            log_reservation(reservation) 
            
        cart.clear_cart()
        print("✅ Ваше бронювання підтверджено!")
        print("🔗 Для отримання детальної інформації відвідайте наш сайт: https://vladbabinsky.github.io/exam/")
    
    else:
        print("❌ Неправильний формат номера картки. Спробуйте ще раз.")

