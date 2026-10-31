import unittest

from py_pluralize import pluralize, is_plural


class PluralizeTests(unittest.TestCase):
    def test_regular_s(self):
        self.assertEqual(pluralize("cat"), "cats")
        self.assertEqual(pluralize("dog"), "dogs")

    def test_count_one_returns_singular(self):
        self.assertEqual(pluralize("cat", 1), "cat")
        self.assertEqual(pluralize("child", 1), "child")

    def test_count_zero_returns_plural(self):
        self.assertEqual(pluralize("cat", 0), "cats")

    def test_consonant_y(self):
        self.assertEqual(pluralize("city"), "cities")
        self.assertEqual(pluralize("baby"), "babies")

    def test_vowel_y(self):
        self.assertEqual(pluralize("boy"), "boys")
        self.assertEqual(pluralize("day"), "days")

    def test_sibilants(self):
        self.assertEqual(pluralize("bus"), "buses")
        self.assertEqual(pluralize("box"), "boxes")
        self.assertEqual(pluralize("church"), "churches")
        self.assertEqual(pluralize("dish"), "dishes")

    def test_irregular(self):
        self.assertEqual(pluralize("man"), "men")
        self.assertEqual(pluralize("woman"), "women")
        self.assertEqual(pluralize("child"), "children")
        self.assertEqual(pluralize("person"), "people")
        self.assertEqual(pluralize("foot"), "feet")
        self.assertEqual(pluralize("tooth"), "teeth")
        self.assertEqual(pluralize("mouse"), "mice")

    def test_irregular_f_and_fe(self):
        self.assertEqual(pluralize("leaf"), "leaves")
        self.assertEqual(pluralize("knife"), "knives")
        self.assertEqual(pluralize("wolf"), "wolves")

    def test_irregular_o(self):
        self.assertEqual(pluralize("potato"), "potatoes")
        self.assertEqual(pluralize("tomato"), "tomatoes")
        self.assertEqual(pluralize("hero"), "heroes")

    def test_uncountable(self):
        self.assertEqual(pluralize("sheep"), "sheep")
        self.assertEqual(pluralize("fish"), "fish")
        self.assertEqual(pluralize("deer"), "deer")
        self.assertEqual(pluralize("information"), "information")

    def test_case_preserved(self):
        self.assertEqual(pluralize("Cat"), "Cats")
        self.assertEqual(pluralize("MAN"), "men")

    def test_unknown_word_falls_back(self):
        self.assertEqual(pluralize("qux"), "quxes")
        self.assertEqual(pluralize("zzyzx"), "zzyzxes")


class IsPluralTests(unittest.TestCase):
    def test_regular_plural(self):
        self.assertTrue(is_plural("cats"))
        self.assertTrue(is_plural("dogs"))

    def test_irregular_plural(self):
        self.assertTrue(is_plural("men"))
        self.assertTrue(is_plural("children"))
        self.assertTrue(is_plural("mice"))

    def test_uncountable(self):
        self.assertTrue(is_plural("sheep"))
        self.assertTrue(is_plural("fish"))

    def test_singular_not_plural(self):
        self.assertFalse(is_plural("cat"))
        self.assertFalse(is_plural("child"))
        self.assertFalse(is_plural("man"))

    def test_ies(self):
        self.assertTrue(is_plural("cities"))
        self.assertTrue(is_plural("babies"))

    def test_es(self):
        self.assertTrue(is_plural("boxes"))
        self.assertTrue(is_plural("dishes"))

    def test_double_s_not_plural(self):
        self.assertFalse(is_plural("grass"))
        self.assertFalse(is_plural("class"))


if __name__ == "__main__":
    unittest.main()
