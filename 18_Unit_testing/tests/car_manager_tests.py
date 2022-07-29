# You are provided with a simple project containing only one class - Car. The provided class is simple - its main
# point is to represent some of the functionality of a Car. Each car contains information about its make, model, fuel
# consumption, fuel amount, and fuel capacity. Also, each Car can add some fuel to its tank by refueling and can travel
# distance by driving. In order to be driven, our Car needs to have enough fuel. Everything in the provided skeleton is
# working perfectly fine, and you mustn't change it.
# Your job now is to write unit tests on the provided project and its functionality. You should test every part of the
# code inside the Car class:
# •	You should test the constructor
# •	You should test all the methods and validations inside the class
# Constraints
# •	Everything in the provided skeleton is working perfectly fine
# •	You must not change anything in the project structure
# •	Any part of validation should be tested
# •	There is no limit on the tests you can write but keep your attention on the main functionality
from lab.car_manager import Car
from unittest import TestCase, main


class CarTest(TestCase):
    def setUp(self) -> None:
        self.car = Car("Test", "TestModel", 10, 40)
        self.car.refuel(20)

    def test_init(self):
        self.assertEqual(self.car.make, 'Test')
        self.assertEqual(self.car.model, 'TestModel')
        self.assertEqual(self.car.fuel_capacity, 40)
        self.assertEqual(self.car.fuel_consumption, 10)
        self.assertEqual(self.car.fuel_amount, 20)

    def test_getters_and_setters(self):
        self.car.make = 'GAZ'
        self.car.model = 'Volga'
        self.car.fuel_capacity = 30
        self.car.fuel_consumption = 15
        self.car.fuel_amount = 23
        self.assertEqual(self.car.make, 'GAZ')
        self.assertEqual(self.car.model, 'Volga')
        self.assertEqual(self.car.fuel_capacity, 30)
        self.assertEqual(self.car.fuel_consumption, 15)
        self.assertEqual(self.car.fuel_amount, 23)

    def test_all_attributes_name_mangled(self):
        self.assertTrue(hasattr(self.car, f'_Car__make'))
        self.assertTrue(hasattr(self.car, f'_Car__model'))
        self.assertTrue(hasattr(self.car, f'_Car__fuel_consumption'))
        self.assertTrue(hasattr(self.car, f'_Car__fuel_capacity'))

    def test_make_cannot_be_null_or_empty(self):
        with self.assertRaises(Exception) as context:
            self.car.make = ''
        self.assertTrue("Make cannot be null or empty!" in str(context.exception))
        with self.assertRaises(Exception) as context:
            self.car.make = None
        self.assertTrue("Make cannot be null or empty!" in str(context.exception))

    def test_model_cannot_be_null_or_empty(self):
        with self.assertRaises(Exception) as context:
            self.car.model = ''
        self.assertTrue("Model cannot be null or empty!" in str(context.exception))
        with self.assertRaises(Exception) as context:
            self.car.model = None
        self.assertTrue("Model cannot be null or empty!" in str(context.exception))

    def test_fuel_consumption_setter_cannot_set_negative_or_zero(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_consumption = -10
        self.assertTrue("Fuel consumption cannot be zero or negative!" in str(context.exception))
        with self.assertRaises(Exception) as context:
            self.car.fuel_consumption = 0
        self.assertTrue("Fuel consumption cannot be zero or negative!" in str(context.exception))

    def test_fuel_capacity_setter_cannot_set_negative_or_zero(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_capacity = -10
        self.assertTrue("Fuel capacity cannot be zero or negative!" in str(context.exception))
        with self.assertRaises(Exception) as context:
            self.car.fuel_capacity = 0
        self.assertTrue("Fuel capacity cannot be zero or negative!" in str(context.exception))

    def test_fuel_setter_cannot_set_negative(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_amount = -10
        self.assertTrue("Fuel amount cannot be negative!" in str(context.exception))

    def test_fuel_correctly_top_up_on_refuel(self):
        self.car.refuel(self.car.fuel_capacity + 1)
        self.assertEqual(self.car.fuel_amount, self.car.fuel_capacity)
        self.car.fuel_amount = 10
        self.car.refuel(1)
        self.assertEqual(self.car.fuel_amount, 11)

    def test_exception_on_negative_refuel_amount(self):
        with self.assertRaises(Exception) as contex:
            self.car.refuel(-5)
        self.assertTrue("Fuel amount cannot be zero or negative!" in str(contex.exception))

    def test_exception_on_zero_refuel_amount(self):
        with self.assertRaises(Exception) as contex:
            self.car.refuel(0)
        self.assertTrue("Fuel amount cannot be zero or negative!" in str(contex.exception))

    def test_correct_remaining_fuel_after_drive(self):
        self.car.drive(100)
        self.assertEqual(self.car.fuel_amount, 10)

    def test_exception_on_not_enough_fuel_to_drive(self):
        with self.assertRaises(Exception) as contex:
            self.car.drive(201)
        self.assertTrue("You don't have enough fuel to drive!" in str(contex.exception))

if __name__ == "__main__":
    main()

