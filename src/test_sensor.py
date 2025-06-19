import unittest

from car_park import CarPark
from sensor import EntrySensor

class TestSensor(unittest.TestCase):
    def setUp(self):
        self.entry_sensor = EntrySensor(1, True, CarPark("123 Example Street", 100))

    def test_init(self):
        self.assertIsInstance(self.entry_sensor, EntrySensor)
        self.assertEqual(self.entry_sensor.id_num, 1)
        self.assertEqual(self.entry_sensor.is_active, True)
        self.assertIsInstance(CarPark("123 Example Street", 100), CarPark)

    def test_detect_vehicle(self):
        self.entry_sensor.detect_vehicle()
        self.assertEqual(len(self.entry_sensor.car_park.plates), 1)

