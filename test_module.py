import unittest
from budget import Category, create_spend_chart

class TestBudgetApp(unittest.TestCase):
    def test_category_methods(self):
        food = Category("Food")
        clothing = Category("Clothing")

        food.deposit(1000, "initial deposit")
        clothing.deposit(500, "initial deposit")

        self.assertEqual(food.get_balance(), 1000)
        self.assertEqual(clothing.get_balance(), 500)

        food.withdraw(10, "groceries")
        clothing.transfer(50, food)

        self.assertEqual(food.get_balance(), 990)
        self.assertEqual(clothing.get_balance(), 450)

        self.assertFalse(food.withdraw(1000, "overspending"))
        self.assertTrue(food.transfer(100, clothing))
        self.assertEqual(food.get_balance(), 890)
        self.assertEqual(clothing.get_balance(), 550)

    def test_create_spend_chart(self):
        food = Category("Food")
        clothing = Category("Clothing")
        auto = Category("Auto")

        categories = [food, clothing, auto]
        chart = create_spend_chart(categories)

        self.assertIn("Food", chart)
        self.assertIn("Clothing", chart)
        self.assertIn("Auto", chart)

if __name__ == '__main__':
    unittest.main()
