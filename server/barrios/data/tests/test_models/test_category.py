from django.test import TestCase
from data.models import Category


class CategoryTests(TestCase):
    """
    Test the Category model.
    It's a simple little entity made for mapping different
    category representations across the datasets, so we
    shouldn't need many.
    """

    def setUp(self):
        Category.objects.create(
            category_id=8,
            category_name="Dummy Test Category",
            rate_category="Dummy Test Category",
        )

    def test_category_id(self):
        """Check that a new Category object has the expected category_id"""
        test_cat = Category.objects.get(category_id=8)
        self.assertEqual(test_cat.category_id, 8)

    def test_category_name(self):
        """Check that a new Category object has the expected category_name"""
        test_cat = Category.objects.get(category_name="Dummy Test Category")
        self.assertEqual(test_cat.category_name, "Dummy Test Category")

    def test_category_rate_category(self):
        """Check that a new Category object has the expected rate_category"""
        test_cat = Category.objects.get(rate_category="Dummy Test Category")
        self.assertEqual(test_cat.rate_category, "Dummy Test Category")
