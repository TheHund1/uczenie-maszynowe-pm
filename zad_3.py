class Property:
    def __init__(self, area, rooms: int, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address
    
    def __str__(self):
        return f'{self.area}, {self.rooms}, {self.price}, {self.address}'
    

class House(Property):
    def __init__(self, area, rooms: int, price, address, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot
        
    def __str__(self):
        return super().__str__() + ', ' + f'{self.plot}'

class Flat(Property):
    def __init__(self, area, rooms: int, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor
        
    def __str__(self):
        return super().__str__() + ', ' + f'{self.floor}'
House1 = House("Old Hampton",8,"56969","Bogucicka 9",5)
Flat1 = Flat("Shire",7,"56969","Grabskiego 5b",6)
print(House1)
print(Flat1)