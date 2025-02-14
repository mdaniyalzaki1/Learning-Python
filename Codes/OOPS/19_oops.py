class Car:
    total_cars = 0  # Class variable to track total number of cars

    def __init__(self, brand, model, year):
        """Initialize Car object with brand, model, and year."""
        self.__brand = brand  # Private attribute (Encapsulation)
        self.model = model
        self.year = year
        Car.total_cars += 1  # Increment car count when a new car is created

    def car_info(self):
        """Returns a formatted string with car details."""
        return f"Brand: {self.__brand}, Model: {self.model}, Year: {self.year}"

    def get_brand(self):
        """Getter method for private brand attribute."""
        return self.__brand

    def fuel_type(self):
        """Returns the fuel type of the car (default: Petrol)."""
        return "Petrol"


class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_size):
        """Initialize ElectricCar with additional battery_size attribute."""
        super().__init__(brand, model, year)
        self.battery_size = battery_size  # Unique attribute for electric cars

    def fuel_type(self):
        """Overrides the fuel_type method for electric cars."""
        return "Electric"

    def battery_info(self):
        """Returns battery size information."""
        return f"Battery Size: {self.battery_size} kWh"


# Display the total number of cars before adding any
print("Total Cars:", Car.total_cars)

# Creating multiple car instances
bmw = Car("BMW", "550i", 2019)
audi = Car("Audi", "A6", 2022)
toyota = Car("Toyota", "Corolla", 2020)

# Creating multiple electric car instances
tesla = ElectricCar("Tesla", "Model S", 2023, 100)
nissan = ElectricCar("Nissan", "Leaf", 2021, 40)

# Displaying information for all cars
print("\nCar Details:")
for car in [bmw, audi, toyota]:
    print(car.car_info(), "| Fuel Type:", car.fuel_type())

# Displaying information for all electric cars
print("\nElectric Car Details:")
for ecar in [tesla, nissan]:
    print(ecar.car_info(), "| Fuel Type:", ecar.fuel_type(), "|", ecar.battery_info())

# Display the total number of cars after adding them
print("\nTotal Cars:", Car.total_cars)
