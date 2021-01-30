import math

class PiggyBank:
    # create __init__ and add_money methods
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def add_money(self, deposit_dollars, deposit_cents):
        if self.cents + deposit_cents >= 99:
            self.dollars = self.dollars + deposit_dollars + ((self.cents + deposit_cents) / 100)
            self.cents = math.ceil(self.dollars % 1)
        else:
            self.dollars += deposit_dollars
            self.cents += deposit_cents

        self.dollars = int(self.dollars)

        return self.dollars, int(self.cents)