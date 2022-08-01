from unittest import TestCase, main

from project.plantation import Plantation


class PlantationTests(TestCase):
    def test_init_method_work_properly(self):
        self.plantation = Plantation(1)
        self.assertEqual(1, self.plantation.size)

    def test_size_setter(self):
        with self.assertRaises(ValueError) as error:
            self.plantation = Plantation(-1)
        self.assertEqual("Size must be positive number!", str(error.exception))

    def test_hire_worker_when_worker_exists_raises(self):
        self.plantation = Plantation(1)
        self.plantation.hire_worker('Pesho')

        with self.assertRaises(ValueError) as error:
            self.plantation.hire_worker('Pesho')
        self.assertEqual("Worker already hired!", str(error.exception))

    def test_hire_worker_when_worker_not_exists(self):
        self.plantation = Plantation(1)
        worker1 = "Pesho"
        self.plantation.hire_worker(worker1)
        self.assertTrue(worker1 in self.plantation.workers)

    def test_hire_worker_returns_proper_message(self):
        self.plantation = Plantation(1)
        worker1 = "Pesho"
        result = self.plantation.hire_worker(worker1)
        self.assertEqual(f"{worker1} successfully hired.", result)

    def test__len__returns_proper_count(self):
        self.plantation = Plantation(1)
        worker1 = "Pesho"
        self.plantation.hire_worker(worker1)
        self.plantation.plants[worker1] = ['Tomatos']
        self.assertEqual(1, self.plantation.__len__())

    def test_len_not_addition(self):
        self.plantation = Plantation(1)
        self.plantation.hire_worker('Pesho')
        self.plantation.hire_worker('Alexandra')
        self.plantation.plants['Pesho'] = ['Tomatoes']
        self.plantation.plants['Alexandra'] = ['Potatoes']
        self.assertEqual(self.plantation.__len__(), 2)

    def test_planting_if_worker_not_in_workers_list_raises(self):
        self.plantation = Plantation(1)
        with self.assertRaises(ValueError) as error:
            self.plantation.planting('Pesho', "potatoes")
        self.assertEqual(f"Worker with name Pesho is not hired!", str(error.exception))

    def test_planting_wrong_error_message(self):
        self.plantation = Plantation(1)
        self.plantation.hire_worker('Pesho')
        self.plantation.planting('Pesho', 'carrots')
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting('Pesho', 'Tomatoes')
        self.assertEqual(str(ve.exception), 'The plantation is full!')

    def test_planting_wrong_dict_assigment(self):
        self.plantation = Plantation(2)
        self.plantation.hire_worker('Pesho')
        self.plantation.planting('Pesho', 'Radishes')
        self.plantation.planting('Pesho', 'carrots')
        self.assertEqual(len(self.plantation.plants['Pesho']), 2)

    def test_planting_wrong_message(self):
        self.plantation = Plantation(2)
        self.plantation.hire_worker('Pesho')
        self.plantation.planting('Pesho', 'Radishes')
        self.assertEqual(self.plantation.planting('Pesho', 'Radishes'), 'Pesho planted Radishes.')

    def test_planting_new_planting_not_added(self):
        self.plantation = Plantation(2)
        self.plantation.hire_worker('Pesho')
        self.plantation.planting('Pesho', 'Radishes')
        self.assertEqual(len(self.plantation.plants['Pesho']), 1)

    def test_planting_new_planting(self):
        self.plantation = Plantation(2)
        self.plantation.hire_worker('Pesho')
        self.assertEqual(self.plantation.planting('Pesho', 'Radishes'), 'Pesho planted it\'s first Radishes.')

    def test_str_return_wrong_output(self):
        self.assertEqual(Plantation(2).__str__().strip(), 'Plantation size: 2')
        self.plantation = Plantation(2)
        self.plantation.hire_worker('Pesho')
        self.plantation.planting('Pesho', 'Radishes')
        self.assertEqual(self.plantation.__str__().strip(), 'Plantation size: 2\nPesho\nPesho planted: Radishes')

    def test_repr_return_wrong_output(self):
        self.assertEqual(Plantation(2).__repr__().strip(), 'Size: 2\nWorkers:')
        self.plantation = Plantation(2)
        self.plantation.hire_worker('Pesho')
        self.plantation.planting('Pesho', 'Radishes')
        self.assertEqual(self.plantation.__repr__().strip(), 'Size: 2\nWorkers: Pesho')


if __name__ == "__main__":
    main()