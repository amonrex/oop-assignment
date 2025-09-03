# Assignment 1: Design Your Own Class 🏗️

# Base class
class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.__battery = battery  # encapsulated attribute (private)

    def phone_info(self):
        return f"{self.brand} {self.model} with {self.storage}GB storage"

    def battery_status(self):
        return f"Battery: {self.__battery}%"

    def charge(self, amount):
        self.__battery = min(100, self.__battery + amount)
        print(f"🔋 Charging... Battery now at {self.__battery}%")

# Child class (Inheritance + Polymorphism)
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, battery, gpu):
        super().__init__(brand, model, storage, battery)
        self.gpu = gpu

    def phone_info(self):
        # Polymorphism: overrides parent method
        return f"{self.brand} {self.model} (Gaming Edition) with {self.storage}GB storage and {self.gpu} GPU"


# Activity 2: Polymorphism Challenge 🎭
class Vehicle:
    def move(self):
        raise NotImplementedError("This method should be overridden by subclasses")

class Car(Vehicle):
    def move(self):
        print("🚗 Driving on the road...")

class Plane(Vehicle):
    def move(self):
        print("✈️ Flying in the sky...")

class Boat(Vehicle):
    def move(self):
        print("🚤 Sailing on water...")

# Testing the code
if __name__ == "__main__":
    # Assignment 1
    phone1 = Smartphone("Samsung", "S24", 256, 80)
    phone2 = GamingPhone("Asus", "ROG 7", 512, 60, "Adreno X1")

    print(phone1.phone_info())
    print(phone1.battery_status())
    phone1.charge(15)

    print(phone2.phone_info())
    print(phone2.battery_status())
    phone2.charge(30)

    print("\n--- Polymorphism Challenge ---")
    vehicles = [Car(), Plane(), Boat()]
    for v in vehicles:
        v.move()

