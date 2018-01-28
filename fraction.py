class Fraction:
    ''' represents a fraction in the calculator'''
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()

    def gcm(self, a, b):
        ''' calculate the gcm '''
        if b % a == 0:
            return a
        return self.gcm(b, b % a)

    def simplify(self):
        ''' simplify the fraction '''
        num = self.numerator
        den = self.denominator
        gcm = self.gcm(num, den)
        result = Fraction(num / gcm, den / gcm)
        return result

    def to_string(self):
        ''' print to console '''
        print('{} / {}'.format(self.numerator, self.denominator))
