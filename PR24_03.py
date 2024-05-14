class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def input_fraction(self):
        self.numerator = int(input("Введіть чисельник: "))
        self.denominator = int(input("Введіть знаменник: "))

    def display_fraction(self):
        print(f"Дріб: {self}")

    def add(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def subtract(self, other):
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def multiply(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def divide(self, other):
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    def __add__(self, other):
        return self.add(other)

    def __sub__(self, other):
        return self.subtract(other)

    def __mul__(self, other):
        return self.multiply(other)

    def __truediv__(self, other):
        return self.divide(other)

fraction1 = Fraction(1, 2)
fraction2 = Fraction(3, 4)

print("Додавання:", fraction1 + fraction2)
print("Віднімання:", fraction1 - fraction2) 
print("Множення:", fraction1 * fraction2)
print("Ділення:", fraction1 / fraction2)

fraction1.display_fraction()
fraction2.display_fraction()