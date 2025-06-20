from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display

car_park_moondalup = CarPark("Moondalup", 100, log_file="moondalup.txt",
                             config_file='moondalup.config.json')
car_park_moondalup.write_config()
car_park_moondalup = car_park_moondalup.from_config('moondalup.config.json')
exit_sensor_moondalup = ExitSensor(2, True, car_park_moondalup)
display_moondalup = Display(1, "Welcome to Moondalup", True)
entry_sensor_moondalup = EntrySensor(1, True, car_park_moondalup)
car_park_moondalup.register(entry_sensor_moondalup)
car_park_moondalup.register(display_moondalup)
car_park_moondalup.register(exit_sensor_moondalup)
entry_sensor_moondalup.detect_vehicle()
entry_sensor_moondalup.detect_vehicle()
entry_sensor_moondalup.detect_vehicle()
entry_sensor_moondalup.detect_vehicle()
entry_sensor_moondalup.detect_vehicle()
entry_sensor_moondalup.detect_vehicle()
entry_sensor_moondalup.detect_vehicle()
entry_sensor_moondalup.detect_vehicle()
entry_sensor_moondalup.detect_vehicle()
entry_sensor_moondalup.detect_vehicle()
exit_sensor_moondalup.detect_vehicle()
exit_sensor_moondalup.detect_vehicle()