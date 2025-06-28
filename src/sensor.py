from abc import ABC, abstractmethod
import random

class Sensor:
    def __init__(self, id_num, is_active, car_park):
        self.id_num = id_num
        self.is_active = is_active
        self.car_park = car_park

    @abstractmethod
    def update_car_park(self, plate):
        pass

    def _scan_plate(self):
        """
        Returns a randomly created licence plate
        """
        return 'FAKE-' + format(random.randint(0, 999), "03d")

    def detect_vehicle(self):
        """
        Adds
        """
        plate = self._scan_plate()
        self.update_car_park(plate)

    def __str__(self):
        return f"Sensor {self.id_num} is active: {self.is_active}"

class EntrySensor(Sensor):
    def update_car_park(self, plate):
        """
        Informs car park of when a car enters car park
        """
        self.car_park.add_car(plate)
        print(f"Incoming 🚘 vehicle detected. Plate: {plate}")

class ExitSensor(Sensor):
    def update_car_park(self, plate):
        """
        Informs car park of when a car leaves car park
        """
        self.car_park.remove_car(plate)
        print(f"Outgoing 🚗 vehicle detected. Plate: {plate}")

    def _scan_plate(self):
        """
        Chooses a random plate from teh car park's plate list
        """
        return random.choice(self.car_park.plates)