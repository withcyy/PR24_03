class Stadium:
    def __init__(self, name, opening_date, country, city, capacity):
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity

    def __str__(self):
        return f"Стадіон: {self.name}, Місто: {self.city}, Країна: {self.country}, Відкриття: {self.opening_date}, Місткість: {self.capacity}"

    def input_stadium(self):
        self.name = input("Введіть назву стадіону: ")
        self.opening_date = input("Введіть дату відкриття: ")
        self.country = input("Введіть країну: ")
        self.city = input("Введіть місто: ")
        self.capacity = int(input("Введіть місткість: "))

    def display_stadium(self):
        print(self)

    def __eq__(self, other):
        return self.capacity == other.capacity

    def __lt__(self, other):
        return self.capacity < other.capacity

    def __gt__(self, other):
        return self.capacity > other.capacity

    def __le__(self, other):
        return self.capacity <= other.capacity

    def __ge__(self, other):
        return self.capacity >= other.capacity

stadium1 = Stadium("Camp Nou", "24.09.1957", "Іспанія", "Барселона", 99354)
stadium2 = Stadium("Wembley", "23.04.1923", "Велика Британія", "Лондон", 90000)
stadium1.display_stadium()
stadium2.display_stadium()
print("Стадіон 1 має ту ж місткість, що і стадіон 2:", stadium1 == stadium2)
print("Стадіон 1 має більшу місткість, ніж стадіон 2:", stadium1 > stadium2)
print("Стадіон 1 має меншу місткість, ніж стадіон 2:", stadium1 < stadium2)