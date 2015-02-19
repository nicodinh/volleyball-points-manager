import os

class Room(object):      # note: class name is Capitalized
    def __init__(self, number):
        self.number = number

    # get_ methods are non-Pythonic.
    # If you need to do some processing to retrieve room number,
    # make it a @property; otherwise, just use the field name

class House(object):
    def __init__(self, num_rooms):
        # I assume you don't want a room 0?
        #self.rooms = [Room(i) for i in range(1, num_rooms+1)]
        self.rooms = [Room(0)]
    def __iter__(self):
        return iter(self.rooms)

mansion = House(10)
for room in mansion:
    print (room.number)
	
os.system("pause")