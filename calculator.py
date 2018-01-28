class Calculator:
    ''' represent a calculator that holds a collection of fractions that can be
    operated on (add/subtract/divide/multiply)'''

    def __init__(self, *args):
        # print(args)
        self.fractions = list(args)

    def add(self):
        all = self.fractions[0]
        for i in self.fractions[1:]:
            all = Fraction(i.denominator * all.numerator + all.denominator * i.numerator, i.denominator * all.denominator)
        return all

    def subtract(self):
        all = self.fractions[0]
        for i in self.fractions[1:]:
            all = Fraction(i.denominator * all.numerator - all.denominator * i.numerator, i.denominator * all.denominator)
        return all

    def multiply(self):
        all = self.fractions[0]
        for i in self.fractions[1:]:
            all = Fraction(all.numerator * i.numerator, i.denominator * all.denominator)
        return all

    def divide(self):
        all = self.fractions[0]
        for i in self.fractions[1:]:
            all = Fraction(all.numerator * i.denominator, i.numerator * all.denominator)
        return all

def gcm(a, b):
    ''' calculate the gcm '''
    if b % a == 0:
        return a
    return gcm(b, b % a)

if __name__ == "__main__":
    from fraction import Fraction

    fraction1 = Fraction(4, 5)
    fraction2 = Fraction(2, 3)
    calculator = Calculator(fraction1, fraction2)
