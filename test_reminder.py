import unittest
import pandas as pd
from reminder import GroceryReminder


class TestGroceryReminder(unittest.TestCase):
    def setUp(self):
        self.prices = pd.DataFrame({"Item": ["Apple", "Banana"], "Price": [1.0, 0.5]})
        self.reminder = GroceryReminder(self.prices)

    def test_add_row(self):
        new_row = pd.DataFrame({"Item": ["Orange"], "Price": [0.75]})
        self.reminder.add_row(new_row)
        expected_prices = pd.DataFrame(
            {"Item": ["Apple", "Banana", "Orange"], "Price": [1.0, 0.5, 0.75]}
        )
        self.assertEqual(self.reminder.get_prices().equals(expected_prices), True)

    def test_get_prices(self):
        self.assertEqual(self.reminder.get_prices().equals(self.prices), True)


if __name__ == "__main__":
    unittest.main()
