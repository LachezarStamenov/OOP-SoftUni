# Create the following tests:
# •	Cat's size is increased after eating
# •	Cat is fed after eating
# •	Cat cannot eat if already fed, raises an error
# •	Cat cannot fall asleep if not fed, raises an error
# •	Cat is not sleepy after sleeping
from lab.cat import Cat

import unittest

class CatTests(unittest.TestCase):
    def test_cat_size_is_increased_after_eating(self):
        cat = Cat("TestCat")

        self.assertEqual(0, cat.size)

        cat.eat()

        self.assertEqual(1, cat.size)

    def test_cat_is_fed_after_eating(self):
        cat = Cat("TestCat")
        self.assertFalse(cat.fed)

        cat.eat()

        self.assertTrue(cat.fed)

    def test_cat_is_fed_raises_if_eat_again(self):
        cat = Cat("TestCat")
        cat.eat()

        with self.assertRaises(Exception) as ex:
            cat.eat()
        self.assertEqual("Already fed.", str(ex.exception))

    def test_cat_can_not_sleep_if_not_fed_raises(self):
        cat = Cat("TestCat")
        self.assertFalse(cat.fed)

        with self.assertRaises(Exception) as ex:
            cat.sleep()
        self.assertEqual("Cannot sleep while hungry", str(ex.exception))

    def test_cat_is_not_sleepy_after_sleeping(self):
        cat = Cat("TestCat")
        self.assertFalse(cat.fed)
        self.assertFalse(cat.sleepy)

        cat.eat()
        self.assertTrue(cat.sleepy)

        cat.sleep()
        self.assertFalse(cat.sleepy)

if __name__ == '__main__':
    unittest.main()



