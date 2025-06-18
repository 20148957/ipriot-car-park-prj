class CarPark:
    def __init__(self, location, capacity, plates=None, displays=None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or None
        self.displays = displays or None

    def __str__(self):
        return f"{self.location} {self.capacity}"