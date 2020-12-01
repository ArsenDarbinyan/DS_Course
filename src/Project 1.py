class Room:

    def __init__(self, type, count, ):

        self.type = type
        self.count = count
        self.reserved = 0



    def get_type(self):

        return self.type

    def get_count(self):
        return self.count

    def reserve(self):
        if self.count-1 >= self.reserved >= 0:
            self.count = self.count - 1
            self.reserved = self.reserved + 1
            print(f"{self.type} already reserve")
        else:
            print(f"{self.type} at the moment there are no vacant rooms of this type")

    def checkout(self):
        if self.reserved > 0:
            self.count = self.count + 1
            self.reserved = self.reserved - 1
            print(f"{self.type} already checkout")
        elif self.reserved == 0:
            print("you have not reserved a room")

    def __repr__(self):
        return f'{self.type} {self.count}'


class Hotel:

    def __init__(self, name=None):

        self.namber_list =[]
        self.reiting = 0
        self.rater_count = 0
        self.name = name
        self.room = ['penthause', "double", "single"]



    def rate(self):
        n = input("Rate it from 1/10:")
        if 0 < int(n) < 11:
            self.reiting = (self.reiting*self.rater_count + int(n))/(self.rater_count+1)
            self.rater_count += 1
        print('Thank you ')

    def get_Room(self):
        return self.room

    def get_rating(self):
        return self.reiting

    def reserve(self):
       a = Room("penthouse", 10)
       a.reserve()

    def checkout(self):
        a = Room("penthouse", 10)
        a.checkout()

def main():

    a = Room('penthouse',10)
    Hotel(a)


