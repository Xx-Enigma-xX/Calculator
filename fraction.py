

class Fraction:
    ''' represents a fraction in the calculator'''
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        # self.simplify()

    def simplify(self):
        ''' simplify the fraction '''
        num = self.numerator
        den = self.denominator
        gcm = calculator.gcm(num, den)
        result = Fraction(num / gcm, den / gcm)
        return result

    def to_string(self):
        ''' print to console '''
        print('{} / {}'.format(self.numerator, self.denominator))

if __name__ == "__main__":
    pass
