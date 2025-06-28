class Display:
    def __init__(self, id_num, message="", is_on=False):
        self.id_num = id_num
        self.message = message
        self.is_on = is_on

    def update(self, data):
        """
        Update the display
        """
        for key, value in data.items():
            if key == "message":
                self.message = value
            print(f"{key}: {value}")

    def __str__(self):
        return f"Display {self.id_num}: {self.message}"