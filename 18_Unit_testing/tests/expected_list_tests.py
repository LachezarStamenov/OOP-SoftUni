# You are provided with a class IntegerList. It should only store integers. The initial integers should be set by the
# constructor. They are stored as a list. IntegerList has a functionality to add, remove_index, get, insert, get the
# biggest number, and get the index of an element. Your task is to test the class.
# Note: You are not allowed to change the structure of the provided code
# Constraints
# •	add operation, should add an element and returns the list.
# o	If the element is not an integer, a ValueError is thrown
# •	remove_index operation removes the element on that index and returns it.
# o	If the index is out of range, an IndexError is thrown
# •	__init__ should only take integers, and store them
# •	get should return the specific element
# o	If the index is out of range, an IndexError is thrown
# •	insert
# o	If the index is out of range, IndexError is thrown
# o	If the element is not an integer, ValueError is thrown
# •	get_biggest
# •	get_index
from lab.extended_list import IntegerList
from unittest import TestCase, main


class IntegerListTest(TestCase):
    def test_is_initialized_correctly_without_data(self):
        integer = IntegerList()
        self.assertEqual([], integer._IntegerList__data)

    def test_is_initialized_correctly_with_wrong_data(self):
        integer = IntegerList("asd", 5.6, 10.5)
        self.assertEqual([], integer._IntegerList__data)

    def test__is_initialized_correctly_with_integers_data(self):
        integer = IntegerList(5, "asd")
        self.assertEqual([5], integer._IntegerList__data)

    def test_get_data(self):
        integer = IntegerList(5, "asd")
        self.assertEqual([5], integer._IntegerList__data)

        result = integer.get_data()
        self.assertEqual([5], result)

    def test_add_method_incorrect_data_raises(self):
        integer = IntegerList(5)
        self.assertEqual([5], integer._IntegerList__data)

        with self.assertRaises(ValueError) as ex:
            integer.add("5")
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_add_method_correct_data(self):
        integer = IntegerList(5)
        self.assertEqual([5], integer._IntegerList__data)

        integer.add(10)
        self.assertEqual([5, 10], integer._IntegerList__data)

    def test_remove_el_removes_the_element(self):
        integer = IntegerList(5)
        integer.remove_index(0)
        self.assertEqual([], integer._IntegerList__data)

    def test_remove_invalid_index_raises(self):
        integer = IntegerList(5)

        with self.assertRaises(IndexError) as ex:
            integer.remove_index(2)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_remove_returns_element_at_the_removed_index(self):
        integer = IntegerList(5)
        result = integer.remove_index(0)
        self.assertEqual(5, result)

    def test_get_with_invalid_index_raises(self):
        integer = IntegerList(5)

        with self.assertRaises(IndexError) as ex:
            # Greater than the length of the index
            integer.get(2)
        self.assertEqual("Index is out of range", str(ex.exception))

        with self.assertRaises(IndexError) as ex:
            # Equal of the length of the index
            integer.get(1)
        self.assertEqual("Index is out of range", str(ex.exception))

    def tests_get_valid_index_return_element(self):
        integer = IntegerList(5)

        result = integer.get(0)
        self.assertEqual(5, result)

    def test_insert_with_invalid_index_raises(self):
        integer = IntegerList(5)

        with self.assertRaises(IndexError) as ex:
            integer.insert(2, 10)
        self.assertEqual("Index is out of range", str(ex.exception))


    def test_insert_with_invalid_data_type_raises(self):
        integer = IntegerList(5)

        with self.assertRaises(ValueError) as ex:
            integer.insert(0, "10")
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_insert_adds_elements(self):
        integer = IntegerList(5)
        integer.insert(0, 2)
        self.assertEqual([2, 5], integer._IntegerList__data)

    def tests_get_biggest(self):
        integer = IntegerList(5, -1, 0, 100, -400)
        result = integer.get_biggest()
        self.assertEqual(100, result)

    def test_get_index(self):
        integer = IntegerList(5, 2, 3)
        result = integer.get_index(3)
        self.assertEqual(2, result)


if __name__ == "__main__":
    main()
