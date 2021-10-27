import random

name_list = ["Bob", "Wob", "Rob", "Sob", "Cob", "Tob"]
id_variable = 0


class Person:
    def __init__(self, name, age):
        print("A new being has been ejected from this digital womb")
        self.name = name
        self.age = age
        self.id = None
        self.address = tuple((None, None))

    def __del__(self):
        del Person

    def set_id(self, id_card):
        self.id = id_card

    def set_address(self, x, y):
        self.address = (x, y)


class Grid:
    def __init__(self, rows, columns, local_id):
        self.grid = [[[local_id] for i in range(columns)] for j in range(rows)]

    def give_birth(self, x, y, id_card):
        Person((name_list[random.randint(0, (len(name_list) - 1))]), random.randint(1, 100))
        Person.set_id(id_card)
        Person.set_address(x, y)

    def obliterate(self):

    def how_many_roaches(self, x, y):
        len(Grid[x][y])


    def relocate(self):

    def find_id(self):

    def who_lives_here_name(self, x, y):
        print(Grid[x][y])
    def who_lives_here_id(self):


def main():
    

if __name__ == "__main__":
    main()
