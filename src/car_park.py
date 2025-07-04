from sensor import Sensor
from display import Display
from pathlib import Path
from datetime import datetime
import json

class CarPark:
    def __init__(self, location, capacity, plates=None, displays=None, sensors=None, log_file=Path("log.txt"),
                 config_file=None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.displays = displays or []
        self.sensors = sensors or []
        self.log_file = log_file if isinstance(log_file, Path) else Path(log_file)
        self.log_file.touch(exist_ok=True)
        self.config_file = config_file or "config.json"

    def register(self, component):
        """
        Add Sensors and Displays to self.displays or self.sensors list
        """
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display")
        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)

    def add_car(self, plate):
        """
        Add a car's plate to the self.plates list
        """
        self.plates.append(plate)
        self.update_displays()
        self._log_car_activity(plate, "entered")

    def remove_car(self, plate):
        """
        Remove a car from the self.plates list
        """
        self.plates.remove(plate)
        self.update_displays()
        self._log_car_activity(plate, "exited")

    @property
    def available_bays(self):
        """
        Return number of available bays
        """
        if self.capacity > len(self.plates):
            return self.capacity - len(self.plates)
        else:
            return 0

    def update_displays(self):
        """
        Call all car park's display to update displays
        """
        data = {"available_bays": self.available_bays, "temperature": 25}
        for display in self.displays: display.update(data)

    def _log_car_activity(self, plate, action):
        """
        Write in log file the action of a car at what time
        """
        with self.log_file.open("a") as f:
            f.write(f"{plate} {action} at {datetime.now():%Y-%m-%d %H:%M:%S}\n")

    def write_config(self):
        """
        Write config file
        """
        with open(self.config_file, "w") as f:
            json.dump({"location": self.location,
                       "capacity": self.capacity,
                       "log_file": str(self.log_file)}, f)

    @classmethod
    def from_config(cls, config_file=Path("config.json")):
        config_file = config_file if isinstance(config_file, Path) else Path(config_file)
        with config_file.open() as f:
            config = json.load(f)
        return cls(config["location"], config["capacity"], log_file=config["log_file"])

    def __str__(self):
        return f"{self.location} {self.capacity}"