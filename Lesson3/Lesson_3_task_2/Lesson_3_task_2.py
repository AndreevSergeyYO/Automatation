from smartphone import Smartphone

catalog = []

phone1 = Smartphone("Samsung", "Galaxy S21", "+70987654")
phone2 = Smartphone("Apple", "iPhone 12", "+7093232654")
phone3 = Smartphone("Xiaomi", "Mi 11", "+702332987654")
phone4 = Smartphone("Google", "Pixel 5", "+77890987654")
phone5 = Smartphone("OnePlus", "9 Pro", "+709876645654")

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f"{phone.brand} - {phone.model}, {phone.phone_namber}")