from unittest import TestCase, main

from ..movie import Movie

class MovieTests(TestCase):


    def test_movie_init_create_correct_attributes(self):
        NAME = "Men in Black"
        YEAR = 1900
        RATING = 15

        movie = Movie(NAME, YEAR, RATING)
        self.assertEqual(NAME, movie.name)
        self.assertEqual(YEAR, movie.year)
        self.assertEqual(RATING, movie.rating)
        self.assertEqual([], movie.actors)

    def test_movie_init_raises_error(self):
        with self.assertRaises(ValueError) as contex:
            Movie('', 1900, 12)
        self.assertEqual('Name cannot be an empty string!', str(contex.exception))

        with self.assertRaises(ValueError) as contex:
            Movie('dsdsfg', 1560, 12)
        self.assertEqual('Year is not valid!', str(contex.exception))

    def test_add_actor(self):
        a = Movie("Dune", 2021, 8.5)
        a.add_actor("Zendaya")
        a.add_actor("Rebecca Ferguson")
        self.assertEqual(a.actors, ["Zendaya", "Rebecca Ferguson"])
        result = a.add_actor("Rebecca Ferguson")
        self.assertEqual(result, "Rebecca Ferguson is already added in the list of actors!")

    def test_gt_method(self):
        a = Movie("Dune", 2021, 8.5)
        b = Movie("Titanic", 1997, 7.8)
        result = str(a > b)
        self.assertEqual(result, '"Dune" is better than "Titanic"')
        c = Movie("The Shawshank Redemption", 1994, 9.2)
        second_result = str(a > c)
        self.assertEqual(second_result, '"The Shawshank Redemption" is better than "Dune"')

    def test_repr_method(self):
        a = Movie("Dune", 2021, 8.5)
        a.add_actor("Zendaya")
        a.add_actor("Rebecca Ferguson")
        self.assertEqual(str(a), "Name: Dune\nYear of Release: 2021\nRating: 8.50\nCast: Zendaya, Rebecca Ferguson")


if __name__ == '__main__':
    main()
