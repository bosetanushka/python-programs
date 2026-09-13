class Transport:

    # Constructor
    def __init__(self, type):
        self.type = type

    # Show transport type
    def show(self):
        print("Transport Type:", self.type)


class Boat(Transport):

    # Constructor
    def __init__(self, type, capacity, source, destination):
        super().__init__(type)
        self.capacity = capacity
        self.source = source
        self.destination = destination

    # Show boat details
    def show(self):
        print("Transport Type:", self.type)
        print("Capacity:", self.capacity)
        print("Source:", self.source)
        print("Destination:", self.destination)
        print("------------------------")


class Bus(Transport):

    # Constructor
    def __init__(self, type, seat_no, source, destination):
        super().__init__(type)
        self.seat_no = seat_no
        self.source = source
        self.destination = destination

    # Show bus details
    def show(self):
        print("Transport Type:", self.type)
        print("Seat No:", self.seat_no)
        print("Source:", self.source)
        print("Destination:", self.destination)
        print("------------------------")


# Creating 2 Boat objects
boat1 = Boat("Boat", 100, "Kolkata", "Haldia")
boat2 = Boat("Boat", 150, "Mumbai", "Goa")

# Creating 2 Bus objects
bus1 = Bus("Bus", 25, "Kolkata", "Durgapur")
bus2 = Bus("Bus", 40, "Delhi", "Agra")


# Display boat records
print("BOAT DETAILS")
boat1.show()
boat2.show()

# Display bus records
print("BUS DETAILS")
bus1.show()
bus2.show()