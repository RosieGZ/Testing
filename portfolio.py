
class Shares:
    def __init__(self, name, number, price):
        self.name = name
        self.number = number
        self.price = price

class Portfolio:
    def __init__(self):
        self._stocks = []

    def buy(self, shares):
        self._stocks.append(shares)
    
    def cost(self):
        return sum(shares.number * shares.price for shares in self._stocks)