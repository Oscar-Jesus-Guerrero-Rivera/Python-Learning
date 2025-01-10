"""
Challenge
Complete the Siege, BatteringRam, and Catapult classes.

Siege Class
Constructor
Accepts two parameters (in order) and sets them as instance variables 
with the same name:

max_speed
efficiency
get_trip_cost()
Calculates the cost of a trip:

(distance / efficiency) * food_price

It costs food to move siege weapons, those things are heavy!

get_cargo_volume()
This method should be left empty. Use the pass keyword. Child classes 
will override this method.

Batteringram Class
Constructor
Calls the parent constructor, then sets the extra battering-ram-only 
instance variables as member variables.

get_trip_cost()
Uses the parent method to calculate the cost of food for a trip,
 plus the extra cost of carrying a load.

The formula for calculating the cost:

base_cost + (load_weight * 0.01)

get_cargo_volume()
Returns the cargo capacity in meters cubed. Get the volume of the 
battering-ram's "bed" (cargo area) by multiplying its area and depth. 
Every bed is 2 meters deep.

Catapult Class
Constructor
Calls the parent constructor, then sets the extra catapult-only 
instance variable as a member variable.

get_trip_cost()
Do not override this method.

get_cargo_volume()
Just returns the cargo capacity of the catapult. This is already set by the constructor.
"""

class Siege:
    def __init__(self, max_speed, efficiency):
        self.max_speed = max_speed
        self.efficiency = efficiency

    def get_trip_cost(self, distance, food_price):
        return (distance / self.efficiency) * food_price

    def get_cargo_volume(self):
        pass


class BatteringRam(Siege):
    def __init__(
        self,
        max_speed,
        efficiency,
        load_weight,
        bed_area,
    ):
        
        super().__init__(max_speed,efficiency)
        self.load_weight = load_weight
        self.bed_area = bed_area
        

    def get_trip_cost(self, distance, food_price):
        return (distance / self.efficiency) * food_price + (self.load_weight * 0.01)

    def get_cargo_volume(self):
        return self.bed_area * 2


class Catapult(Siege):
    def __init__(self, max_speed, efficiency, cargo_volume):
        super().__init__(max_speed,efficiency)
        self.cargo_volume = cargo_volume
        

    def get_cargo_volume(self):
        return self.cargo_volume






# Test Cases


run_cases = [
    (Siege(100, 10), 100, 4, 40, None),
    (BatteringRam(100, 10, 2000, 5), 100, 5, 70, 10),
    (Catapult(100, 10, 2), 100, 6, 60, 2),
]

submit_cases = run_cases + [
    (Siege(60, 5), 100, 2, 40, None),
    (BatteringRam(80, 5, 2000, 4), 100, 4, 100, 8),
    (Catapult(90, 4, 3), 100, 10, 250, 3),
]


def test(vehicle, distance, fuel_price, expected_cost, expected_cargo_volume):
    try:
        vehicle_type = vehicle.__class__.__name__
        print("---------------------------------")
        print(
            f"Testing {vehicle_type}: Max Speed {vehicle.max_speed} kph, Efficiency {vehicle.efficiency} km/food"
        )
        print(f"Distance: {distance} km, Price: {fuel_price} per food")
        print(
            f"Expected: Trip Cost: {expected_cost}, Cargo Volume: {expected_cargo_volume}"
        )
        actual_cost = int(vehicle.get_trip_cost(distance, fuel_price))
        actual_cargo_volume = vehicle.get_cargo_volume()
        if actual_cargo_volume is not None:
            actual_cargo_volume = int(actual_cargo_volume)
        print(
            f"  Actual: Trip Cost: {actual_cost}, Cargo Volume: {actual_cargo_volume}"
        )
        if (
            actual_cost == expected_cost
            and expected_cargo_volume == actual_cargo_volume
        ):
            print("Pass")
            return True
        else:
            print("Fail")
            return False
    except Exception as e:
        print(f"Error: {e}")
        print("Fail")
        return False


def main():
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
