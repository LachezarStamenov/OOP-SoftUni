from mammal.project.mammal import Mammal
from unittest import TestCase, main


class MammalTests(TestCase):
    def setUp(self):
        self.mammal = Mammal("name", "mammal_type", "sound")

    def test_mammal_init(self):
        name = "Test"
        mammal_type = "TestType"
        sound = "TestSound"

        mammal = Mammal(name, mammal_type, sound)

        self.assertEqual(name, mammal.name)
        self.assertEqual(mammal_type, mammal.type)
        self.assertEqual(sound, mammal.sound)
        self.assertEqual("animals", mammal._Mammal__kingdom)

    def test_make_sound(self):
        expected_result = f"{self.mammal.name} makes {self.mammal.sound}"
        actual_result = self.mammal.make_sound()
        self.assertEqual(expected_result, actual_result)

    def test_get_kingdom_returns_animals(self):
        self.assertEqual(self.mammal.get_kingdom(), "animals")

    def test_info_returns_proper_string(self):
        expected_result = f"{self.mammal.name} is of type {self.mammal.type}"
        actual_result = self.mammal.info()
        self.assertEqual(expected_result, actual_result)


if __name__ == "__main__":
    main()