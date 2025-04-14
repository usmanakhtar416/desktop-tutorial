class Device:
    """Base class for all electronic devices."""
    category = "Electronics"  

    def __init__(self, brand, model):
        self.brand = brand  
        self.model = model  

    def display_info(self):
        """Instance method to display device information."""
        print(f"Brand: {self.brand}, Model: {self.model}")

    @classmethod
    def category_info(cls):
        """Class method to display category information."""
        print(f"Device Category: {cls.category}")

    @staticmethod
    def power_source():
        """Static method to display common power source."""
        print("Devices typically use battery or direct power.")

# Single Inheritance
class Computer(Device):
    def __init__(self, brand, model, ram, storage):
        super().__init__(brand, model)
        self.ram = ram
        self.storage = storage

    def display_specs(self):
        print(f"RAM: {self.ram}GB, Storage: {self.storage}GB")

# Multiple Inheritance
class Phone(Device):
    def __init__(self, brand, model, sim_type):
        super().__init__(brand, model)
        self.sim_type = sim_type

    def phone_info(self):
        print(f"SIM Type: {self.sim_type}")

class Tablet(Device):
    def __init__(self, brand, model, screen_size):
        super().__init__(brand, model)
        self.screen_size = screen_size

    def tablet_info(self):
        print(f"Screen Size: {self.screen_size} inches")

# Multilevel Inheritance
class SmartPhone(Computer, Phone):
    def __init__(self, brand, model, ram, storage, sim_type, camera_quality):
        Computer.__init__(self, brand, model, ram, storage)
        Phone.__init__(self, brand, model, sim_type)
        self.camera_quality = camera_quality

    def smart_phone_info(self):
        self.display_info()
        self.display_specs()
        print(f"Camera Quality: {self.camera_quality}MP, SIM Type: {self.sim_type}")

# Hierarchical Inheritance
class FitnessBand(Device):
    def __init__(self, brand, model, heart_rate_monitor):
        super().__init__(brand, model)
        self.heart_rate_monitor = heart_rate_monitor

    def fitness_info(self):
        print(f"Heart Rate Monitor: {self.heart_rate_monitor}")

class SmartWatch(SmartPhone, FitnessBand):
    """Hybrid inheritance combining SmartPhone and FitnessBand"""
    def __init__(self, brand, model, ram, storage, sim_type, camera_quality, heart_rate_monitor, waterproof):
        SmartPhone.__init__(self, brand, model, ram, storage, sim_type, camera_quality)
        FitnessBand.__init__(self, brand, model, heart_rate_monitor)
        self.waterproof = waterproof

    def smartwatch_info(self):
        self.smart_phone_info()
        print(f"Waterproof: {self.waterproof}, Heart Rate Monitor: {self.heart_rate_monitor}")


print("\n--- Device Category ---")
Device.category_info()
Device.power_source()

print("\n--- Creating Instances ---")
smartphone = SmartPhone("Apple", "iPhone 15", 8, 256, "Nano-SIM", 48)
smartphone.smart_phone_info()

print("\n--- Smartwatch Details ---")
smartwatch = SmartWatch("Samsung", "Galaxy Watch 5", 4, 64, "eSIM", 12, "Active", True)
smartwatch.smartwatch_info()

print("\n--- Fitness Band Example ---")
fitness_band = FitnessBand("Fitbit", "Charge 5", "Enabled")
fitness_band.fitness_info()