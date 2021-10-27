import random
#####################
# Gridworld!

# The idea behind grid world is that we have a n x m grid where people can inhabit
# The Person and Grid class have been laid out for you, just fill in the functions!
# The tests below the classes should theoretically work without a problem so all you need to do is work with the classes


class Person:
    def __init__(self, name, age):
        print("New person created!")
        self.name = name
        self.age = age
        self.id = None
        self.address = tuple((None, None))

    def __del__(self):
        print("This function is called when del person_name is called")

    # hint, ID should be updated when creating a person
    def setID(self, id):
        self.id = id

    # hint, id should be updated when creating or moving a person
    def setAddress(self, address):
        self.address = address


class Grid:
    def __init__(self, rows, cols):
        print("The world has been created!")
        # The grid, this is where people live
        self.grid = [[None] * cols] * rows

        # for your convenience, a nested for loop that will run through all the squares in the grid:
        for row in self.grid:
            for col in row:
                print(col)

        # And again in a more traditional way, this may be easier to use as you can numerically index each square:
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                print(self.grid[i][j])

    def birth_person(self, person, gridx, gridy):
        print("Not implemented")
        # This function will take a person object and place them in the correct grid location
        # This function will also return the ID assigned to that person
        return 0  # placeholder return value

    def kill_person(self, id):
        print("Not implemented")
        # This function will find a person by ID and removed them from the grid

    def find_person(self, name):
        print("Not implemented")
        # This function will find a person by name and return their ID
        return 0  # placeholder return value

    def get_total_grid_population(self):
        print("Not implemented")
        # This function will return the total population of the grid

    def move_person(self, id, newx, newy):
        print("Not implemented")
        # This function will take a person ID, find that person, and move them to a new grid location

    def people_name_at_square(self, gridx, gridy):
        print("Not implemented")
        # this function will return a list of the names of people living in a grid square
        return ["Not a real person yet", "Also not a real person"] # placeholder return value

    def people_id_at_square(self, gridx, gridy):
        print("Not implemented")
        # this function will return a list of the id's of people living in a grid square
        return [6,8] # placeholder return value


# Tests run down here
utopia = Grid(5, 5)

# Create a person named Jeffward with age 46 at grid square (2,5)
utopia.birth_person(Person("Jeffward", 46), 2, 5)

jeffward_id = utopia.find_person("Jeffward")

kelvin = utopia.birth_person(Person("Kelvin", 25), 4, 1)

utopia.move_person(jeffward_id, 1, 1)

utopia.birth_person(Person("Elroy", 83), 1, 1)

print(utopia.people_name_at_square(1, 1))
print(utopia.get_total_grid_population())

# Commit genocide at grid square 1,1
for people in utopia.people_id_at_square(1, 1):
    utopia.kill_person(people)

print(utopia.people_name_at_square(1, 1))
print(utopia.get_total_grid_population())



