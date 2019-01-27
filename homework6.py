import json
from urllib import request


class Money(object):
    def __init__(self, amount=0.0, currency='USD'):
        self.amount = amount
        self.currency = currency
        self.rate = 2.43

    def convert(self, target):
        parameter = self.currency + '_' + target
        url = 'http://free.currencyconverterapi.com/api/v5/' \
              'convert?q={}&compact=y'.format(parameter)
        response = request.urlopen(url)
        data = json.load(response)
        rate = data[parameter]['val']
        return self.__class__(self.amount * rate, target)

    def __add__(self, other):
        if isinstance(other, Money):
            if other.currency != self.currency:
                other = other.convert(self.currency)
            other = other.amount
        return self.__class__(self.amount + other, self.currency)

    def __radd__(self, other):
        if isinstance(other, Money):
            if self.currency != other.currency:
                converted = self.convert(other.currency)
                self.amount = converted.amount
                self.currency = converted.currency
            other = other.amount
        return self.__class__(other + self.amount, self.currency)

    def __mul__(self, other):
        return self.__class__(self.amount * other, self.currency)

    def __rmul__(self, other):
        return self.__class__(other * self.amount, self.currency)

    def __repr__(self):
        return '{} {}'.format(self.amount, self.currency)


if __name__ == '__main__':
    x = Money(10, 'BYN')
    y = Money(11)
    z = Money(12.34, 'EUR')
    print(z + 3.11 * x + y * 0.8)

    lst = [Money(10, 'BYN'), Money(11), Money(12.01, 'JPY')]
    s = sum(lst)
    print(s)
