class Player:
    count = 1
    def __init__(self,name,symbol):
        self.name = name
        self.symbol = symbol
        self.number = Player.count
        Player.count+=1

    def __repr__(self):
        print(f"This is Player {self.number} {self.name} playing with {self.symbol}")

    