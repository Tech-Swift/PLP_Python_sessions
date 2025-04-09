# A program that displays the engine sounds of different types of vehicles

class Vehicle:
    def start_engine(self):
        pass
    
class Sedan(Vehicle):
    def start_engine(self):
        return "Sedan engine starting... Vroom... Vroom..."

class SUV(Vehicle):
    def start_engine(self):
        return "SUV engine starting... Rumble... Roar..."

class Pickup(Vehicle):
    def start_engine(self):
        return "Pickup engine starting... Grrr... Rrrr..."

class Truck(Vehicle):
    def start_engine(self):
        return "Truck engine starting... Grrrr... Grr... Rumble..."

class Tractor(Vehicle):
    def start_engine(self):
        return "Tractor engine starting... Chug... Chug... Vroom..."

# Create instances of each vehicle
sedan = Sedan()
suv = SUV()
pickup = Pickup()
truck = Truck()
tractor = Tractor()

# Store vehicles in a list
vehicles = [sedan, suv, pickup, truck, tractor]

# Return the engine sounds for each vehicle
engine_sounds = [vehicle.start_engine() for vehicle in vehicles]

# Display the engine sounds
for sound in engine_sounds:
    print(sound)
