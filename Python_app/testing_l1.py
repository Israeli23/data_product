import unittest
import pandas as pd
from cleaningdata import dataEnrichment 

class testOperations(unittest.TestCase):

    def setUp(self):
        self.enricher = dataEnrichment()
        self.book = pd.DataFrame({
            "Book checkout": ["2023-01-01", "2023-05-10", "2023-06-01"],
            "Book Returned": ["2023-01-05", "2023-05-20", "2023-06-03"]
        })

        self.book["Book checkout"] = pd.to_datetime(self.book["Book checkout"])
        self.book["Book Returned"] = pd.to_datetime(self.book["Book Returned"])

    def test_data_enrichment(self):
        result = self.enricher.enrichData(
            self.book,
            "Book checkout",
            "Book Returned",
            "daysTakenToReturn"
        )
        self.assertTrue((result["daysTakenToReturn"] >= 0).all())


    def test_negative_days_filtered(self):
        book = pd.DataFrame({
            "Book checkout": ["2023-06-10", "2023-06-01"],
            "Book Returned": ["2023-06-05", "2023-06-07"]
        })
        book["Book checkout"] = pd.to_datetime(book["Book checkout"])
        book["Book Returned"] = pd.to_datetime(book["Book Returned"])

        result = self.enricher.enrichData(book, "Book checkout", "Book Returned", "daysTakenToReturn")

        self.assertTrue((result["daysTakenToReturn"] >= 0).all())
        # Confirm the row with negative days is dropped
        self.assertLess(len(result), len(book))


if __name__ == '__main__':
    unittest.main()