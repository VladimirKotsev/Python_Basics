import unittest
from unittest.mock import mock_open, patch
from secret import validate_recipe, RuinedNikuldenDinnerError


class TestNikuldenValidator(unittest.TestCase):

    def test_valid_recipe(self):
        #  Case containing 1/4 special words
        recipe_content = "Тази рецепта съдържа риба и зеленчуци."
        with patch("builtins.open", mock_open(read_data=recipe_content)):
            self.assertTrue(validate_recipe("valid_recipe.txt"))

        # Case containing 1/4 special words
        recipe_content = "Тази рецепта е с рибена глава."
        with patch("builtins.open", mock_open(read_data=recipe_content)):
            self.assertTrue(validate_recipe("valid_recipe.txt"))

        #  Case containing 1/4 special words
        recipe_content = "Тази рецепта съдържа сьонга."
        with patch("builtins.open", mock_open(read_data=recipe_content)):
            self.assertTrue(validate_recipe("valid_recipe.txt"))

        # Case containing 1/4 special words
        recipe_content = "Тази рецепта съдържа шаран."
        with patch("builtins.open", mock_open(read_data=recipe_content)):
            self.assertTrue(validate_recipe("valid_recipe.txt"))

        # Case-insensitive
        recipe_content = "Тази рецепта съдържа шАрАн."
        with patch("builtins.open", mock_open(read_data=recipe_content)):
            self.assertTrue(validate_recipe("valid_recipe.txt"))

    def test_invalid_recipe(self):
        recipe_content = "Тази рецепта съдържа човешко месо."
        with patch("builtins.open", mock_open(read_data=recipe_content)):
            self.assertFalse(validate_recipe("invalid_recipe.txt"))

        recipe_content = "Тази рецепта съдържа шараннннн."
        with patch("builtins.open", mock_open(read_data=recipe_content)):
            self.assertFalse(validate_recipe("invalid_recipe.txt"))

        recipe_content = "Тази рецепта съдържа сьомга."
        with patch("builtins.open", mock_open(read_data=recipe_content)):
            self.assertFalse(validate_recipe("invalid_recipe.txt"))

    def test_bad_recipe_file(self):
        with patch("builtins.open", side_effect=OSError):
            with self.assertRaises(RuinedNikuldenDinnerError):
                validate_recipe("bad_file.txt")

        with patch("builtins.open", side_effect=IOError):
            with self.assertRaises(RuinedNikuldenDinnerError):
                validate_recipe("bad_file.txt")
