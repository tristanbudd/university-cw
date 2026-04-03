# --------------- Task #1 - Smart Plug Class ---------------
class SmartPlug:
    def __init__(self, consumption_rate=45):
        self.switched_on = False
        if 0 <= consumption_rate <= 150:
            self._consumption_rate = consumption_rate
        else:
            raise ValueError("Consumption rate must be more than 0 and less than 150 (inclusive)!")

    def toggle_switch(self):
        self.switched_on = not self.switched_on

    # Getter and setter for consumption_rate (Harder Task)
    @property
    def consumption_rate(self):
        return self._consumption_rate

    @consumption_rate.setter
    def consumption_rate(self, value):
        if 0 <= value <= 150:
            self._consumption_rate = value
        else:
            raise ValueError("Consumption rate must be more than 0 and less than 150 (inclusive)!")

    def get_attribute(self):
        return self._consumption_rate

    def __str__(self):
        if self.switched_on:
            return f"SmartPlug is on with a consumption rate of {self.consumption_rate}"
        else:
            return f"SmartPlug is off with a consumption rate of {self.consumption_rate}"


def test_smart_plug():
    # Task #1 - Create SmartPlug Class
    print("--------------- Task #1 - Smart Plug Test ---------------")
    smart_plug = SmartPlug(45)
    print(smart_plug)
    smart_plug.toggle_switch()
    print(smart_plug)
    smart_plug.consumption_rate = 75
    print(smart_plug)
    smart_plug.toggle_switch()
    print(smart_plug)

    # Testing disallowed consumption rate values. (Harder Task)
    try:
        smart_plug.consumption_rate = -10
    except ValueError as error:
        print(error)

    print(smart_plug)

    try:
        smart_plug.consumption_rate = 200
    except ValueError as error:
        print(error)

    print(smart_plug)

    # Attempting to create the plug with an invalid consumption rate. (Harder Task)
    try:
        smart_plug_2 = SmartPlug(-5)
        print(smart_plug_2)
    except ValueError as error:
        print(error)

    try:
        smart_plug_3 = SmartPlug(160)
        print(smart_plug_3)
    except ValueError as error:
        print(error)


# --------------- Task #2 - More Device Classes (Based on UP Number) ---------------
# Implementing (UP2271413): Task 1: Smart Fridge Class & Task 3: Smart TV Class
class SmartDevice:
    def __init__(self):
        self.switched_on = False

    def toggle_switch(self):
        self.switched_on = not self.switched_on


class SmartFridge(SmartDevice):
    def __init__(self, temperature=3):
        super().__init__()
        if temperature in [1, 3, 5]:
            self._temperature = temperature
        else:
            raise ValueError("Temperature must be 1, 3 or 5 degrees celsius!")

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value in [1, 3, 5]:
            self._temperature = value
        else:
            raise ValueError("Temperature must be 1, 3 or 5 degrees celsius!")

    def get_attribute(self):
        return self._temperature

    def __str__(self):
        if self.switched_on:
            return f"SmartFridge is on with a temperature of {self.temperature} degrees celsius"
        else:
            return f"SmartFridge is off with a temperature of {self.temperature} degrees celsius"


class SmartTV(SmartDevice):
    def __init__(self, channel=1):
        super().__init__()
        if 1 <= channel <= 734:
            self._channel = channel
        else:
            raise ValueError("Channel must be between 1 and 734!")

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        if 1 <= value <= 734:
            self._channel = value
        else:
            raise ValueError("Channel must be between 1 and 734!")

    def get_attribute(self):
        return self._channel

    def __str__(self):
        if self.switched_on:
            return f"SmartTV is on with channel {self.channel}"
        else:
            return f"SmartTV is off with channel {self.channel}"


def test_custom_device():
    # Task #2 - Create Custom Device Classes
    print("--------------- Task #2 - Custom Device Test ---------------")
    smart_fridge = SmartFridge()
    print(smart_fridge)
    smart_tv = SmartTV()
    print(smart_tv)
    smart_fridge.toggle_switch()
    print(smart_fridge)
    smart_tv.toggle_switch()
    print(smart_tv)
    smart_fridge.temperature = 5
    print(smart_fridge)
    smart_tv.channel = 512
    print(smart_tv)

    # Testing disallowed temperature values. (Harder Task)
    try:
        smart_fridge.temperature = 2
    except ValueError as error:
        print(error)

    print(smart_fridge)

    try:
        smart_fridge.temperature = 10
    except ValueError as error:
        print(error)

    print(smart_fridge)

    try:
        smart_tv.channel = -10
    except ValueError as error:
        print(error)

    print(smart_tv)

    try:
        smart_tv.channel = 1000
    except ValueError as error:
        print(error)

    print(smart_tv)


# --------------- Task #3 - SmartHome Class ---------------
class SmartHome:
    def __init__(self, max_devices=5):
        self.devices = []
        if max_devices > 0:
            self.max_devices = max_devices
        else:
            raise ValueError("SmartHome must have at least 1 device!")


    def add_device(self, device):
        if device in self.devices:
            raise ValueError("Device already in SmartHome!")
        elif len(self.devices) >= self.max_devices:
            raise ValueError("SmartHome device limit reached!")
        else:
            self.devices.append(device)

    def remove_device(self, index):
        if 0 <= index < len(self.devices):
            del self.devices[index]
        else:
            raise ValueError("Device not in SmartHome!")

    def update_option(self, index, value):
        if not (0 <= index < len(self.devices)):
            raise ValueError("Device not in SmartHome!")
        elif isinstance(self.devices[index], SmartPlug):
            self.devices[index].consumption_rate = value
        elif isinstance(self.devices[index], SmartFridge):
            self.devices[index].temperature = value
        elif isinstance(self.devices[index], SmartTV):
            self.devices[index].channel = value
        else:
            raise ValueError("Device type not recognised!")

    def get_device(self, index):
        return self.devices[index]

    def toggle_device(self, index):
        self.devices[index].toggle_switch()

    def switch_all_on(self):
        for device in self.devices:
            device.switched_on = True

    def switch_all_off(self):
        for device in self.devices:
            device.switched_on = False

    def __str__(self):
        output = f"SmartHome with {len(self.devices)} device(s):"
        for i, device in enumerate(self.devices):
            output += f"\n{i + 1} - {device}"
        return output


def test_smart_home():
    # Task #3 - Create SmartHome Class
    print("--------------- Task #3 - Smart Home Test ---------------")
    smart_home = SmartHome(3)
    smart_plug = SmartPlug(50)
    smart_fridge = SmartFridge()
    smart_tv = SmartTV()
    smart_home.add_device(smart_plug)
    smart_home.add_device(smart_fridge)
    smart_home.add_device(smart_tv)
    print(smart_home)
    print(smart_home.get_device(0))
    print(smart_home.get_device(1))
    print(smart_home.get_device(2))
    smart_home.toggle_device(0)
    smart_home.toggle_device(1)
    smart_home.toggle_device(2)
    print(smart_home)
    smart_home.switch_all_on()
    smart_home.switch_all_off()
    print(smart_home)

    # Testing device limit & additional functions. (Harder Task)
    smart_plug_2 = SmartPlug(75)
    try:
        smart_home.add_device(smart_plug_2)
    except ValueError as error:
        print(error)

    smart_home.update_option(0, 25)
    smart_home.update_option(1, 5)
    smart_home.update_option(2, 100)
    print(smart_home)

    try:
        smart_home.update_option(1, 5000)
    except ValueError as error:
        print(error)

    smart_home.remove_device(1)
    print(smart_home)

    try:
        smart_home.remove_device(-4321)
    except ValueError as error:
        print(error)

    try:
        smart_home.update_option(100, 50)
    except ValueError as error:
        print(error)

    print(smart_home)


def main():
    test_smart_plug()
    test_custom_device()
    test_smart_home()


if __name__ == "__main__":
    main()
