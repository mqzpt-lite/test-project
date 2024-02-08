import pandas as pd

prices = pd.DataFrame(
    {
        "Apple": [1, 2, 3],
        "Banana": [4, 5, 6],
        "Cherry": [7, 8, 9],
        "Date": ["2018-01-01", "2018-01-02", "2018-01-03"],
    }
)


class GroceryReminder:
    def __init__(self, prices):
        self.prices = prices

    def add_row(self, row_df):
        self.prices = pd.concat([self.prices, row_df], ignore_index=True)

    def get_prices(self):
        return self.prices
