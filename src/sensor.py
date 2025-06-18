class Sensor:
    def __init__(self, id_num, is_active, car_park):
        self.id_num = id_num
        self.is_active = is_active
        self.car_park = car_park

    def __str__(self):
        return f"Sensor {self.id_num} is active: {self.is_active}"

class EntrySensor(Sensor):
    pass

class ExitSensor(Sensor):
    pass