# Create a class WorkerTests
# Create the following tests:
# •	Test if the worker is initialized with the correct name, salary, and energy
# •	Test if the worker's energy is incremented after the rest method is called
# •	Test if an error is raised if the worker tries to work with negative energy or equal to 0
# •	Test if the worker's money is increased by his salary correctly after the work method is called
# •	Test if the worker's energy is decreased after the work method is called
# •	Test if the get_info method returns the proper string with correct values


class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


import unittest


class WorkerTest(unittest.TestCase):
    def test_worker_is_initialized_correctly(self):
        # Arrange, Act
        worker = Worker("Test", 100, 10)
        # Assert
        self.assertEqual("Test", worker.name)
        self.assertEqual(100, worker.salary)
        self.assertEqual(10, worker.energy)
        self.assertEqual(0, worker.money)

    def test_energy_is_increased_after_rest(self):
        # Arrange
        worker = Worker("Test", 100, 10)
        self.assertEqual(10, worker.energy)
        # Act
        worker.rest()
        # Assert
        self.assertEqual(11, worker.energy)

    def test_worker_work_with_zero_energy_raises(self):
        # Arrange
        worker = Worker("Test", 100, 0)

        # Assert, Act
        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_worker_work_with_negative_energy_raises(self):
        # Arrange
        worker = Worker("Test", 100, -1)

        # Assert, Act
        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_worker_is_payed_after_work(self):
        # Arrange
        worker = Worker('Test', 100, 10)
        self.assertEqual(0, worker.money)

        # Act
        worker.work()
        # Assert
        self.assertEqual(100, worker.money)
        # Act
        worker.work()
        # Assert
        self.assertEqual(200, worker.money)

    def test_energy_is_decreased_after_work(self):
        # Arrange
        worker = Worker('Test', 100, 10)
        self.assertEqual(10, worker.energy)

        # Act
        worker.work()

        # Assert
        self.assertEqual(9, worker.energy)

        # Act
        worker.work()

        # Assert
        self.assertEqual(8, worker.energy)

    def test_get_info(self):
        # Arrange
        worker = Worker('Test', 100, 10)

        result = worker.get_info()
        expected = "Test has saved 0 money."

        self.assertEqual(expected, result)

        worker.work()
        result = worker.get_info()
        expected = "Test has saved 100 money."

        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()



















