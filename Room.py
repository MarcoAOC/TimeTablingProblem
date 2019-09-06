class Room:

    def __init__(self,idx,capacity,travel,unavailable):
        self.id = idx
        self.capacity = capacity
        self.travel = travel
        self.unavailable = unavailable