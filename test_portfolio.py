import unittest
import os
import json
from services.portfolio_service import PortfolioService
from models.stock import Stock

class TestPortfolioTracker(unittest.TestCase):
    def setUp(self):
        # Create a test portfolio file
        self.test_data_file = "data/test_portfolio.json"
        if os.path.exists(self.test_data_file):
            os.remove(self.test_data_file)
        self.portfolio_service = PortfolioService(data_file=self.test_data_file)

    def tearDown(self):
        # Clean up test data file
        if os.path.exists(self.test_data_file):
            os.remove(self.test_data_file)

    def test_add_stock(self):
        self.portfolio_service.add_stock("AAPL", 10)
        self.assertEqual(len(self.portfolio_service.portfolio), 1)
        self.assertEqual(self.portfolio_service.portfolio[0].stock_symbol, "AAPL")
        self.assertEqual(self.portfolio_service.portfolio[0].quantity, 10)
        self.assertEqual(self.portfolio_service.portfolio[0].investment_value, 1800)

    def test_add_invalid_stock(self):
        self.portfolio_service.add_stock("INVALID", 10)
        self.assertEqual(len(self.portfolio_service.portfolio), 0)

    def test_update_stock(self):
        self.portfolio_service.add_stock("TSLA", 5)
        self.portfolio_service.update_stock("TSLA", 10)
        self.assertEqual(self.portfolio_service.portfolio[0].quantity, 10)
        self.assertEqual(self.portfolio_service.portfolio[0].investment_value, 2500)

    def test_delete_stock(self):
        self.portfolio_service.add_stock("MSFT", 2)
        self.assertEqual(len(self.portfolio_service.portfolio), 1)
        self.portfolio_service.delete_stock("MSFT")
        self.assertEqual(len(self.portfolio_service.portfolio), 0)

    def test_search_stock(self):
        self.portfolio_service.add_stock("AMZN", 5)
        found_stock = self.portfolio_service.search_stock("AMZN")
        self.assertIsNotNone(found_stock)
        self.assertEqual(found_stock.stock_symbol, "AMZN")

    def test_search_nonexistent_stock(self):
        found_stock = self.portfolio_service.search_stock("GOOGL")
        self.assertIsNone(found_stock)

if __name__ == '__main__':
    unittest.main()
