# zadanie
# napisz klase Calculator
# 2 atrybuty ( okreslane przy inicjacji) a i b
# 4 metody do obliczen - (ktore zwracaja wynik odpowiednio mnozenia, dzielenia, dodawania i odejmowania)

class Calculator:
    total_calculators = 0
    def __init__(self,a,b):
        self.a = a
        self.b = b
        Calculator.total_calculators += 1
        self.id = Calculator.total_calculators

    def mnozenie(self):
        return self.a * self.b

    def dzielenie(self):
        return self.a / self.b

    def dodawanie(self):
        return self.a + self.b

    def odejmowanie(self):
        return self.a - self.b

if __name__ == "__main__":
    calc1 = Calculator(6,6)
    print(calc1.dodawanie())
    print(calc1.odejmowanie())
    print(calc1.mnozenie())
    print(calc1.dzielenie())
    print(Calculator.total_calculators)

    calc2 = Calculator(12,6)
    print(calc2.dodawanie())
    print(calc2.odejmowanie())
    print(calc2.mnozenie())
    print(calc2.dzielenie())
    print(Calculator.total_calculators)

# upgrade - 1 - dodaj liczenie ile operacji juz bylo
#     - w danym kalkulatorze
# - we wszystkich kalkulatorach
