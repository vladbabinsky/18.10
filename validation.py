def validate_phone(cart):
    while True:
        phone = input("Введіть ваш телефон (формат: +380XXXXXXXXX, 380XXXXXXXXX або 098XXXXXXXX): ").strip().replace(" ", "")
        
        # Формат: +380XXXXXXXXX
        if len(phone) == 13 and phone[0:4] == '+380':
            return phone
        
        # Формат: 380XXXXXXXX
        elif len(phone) == 12 and phone[0:3] == '380':
            return '+' + phone
        
        # Формат: 098XXXXXXXX
        elif len(phone) == 10 and phone[0:3] == '098':
            return phone
        
        print("❌ Неправильний формат телефону. Спробуйте ще раз.")

def validate_email(cart):
    email = input("Введіть вашу електронну пошту (має закінчуватися на @gmail.com): ").strip()
    
    while email[-10:] != '@gmail.com':
        print("❌ Неправильний формат електронної пошти. Спробуйте ще раз.")
        email = input("Введіть вашу електронну пошту (має закінчуватися на @gmail.com): ").strip()
    
    return email
