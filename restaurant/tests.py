from django.test import TestCase
from .models import Category, MenuItem, Booking


class RestaurantModelTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(
            slug='salads',
            title='Salads'
        )

        self.menu_item = MenuItem.objects.create(
            title='Greek Salad',
            price='12.50',
            featured=True,
            category=self.category
        )

        self.booking = Booking.objects.create(
            first_name='Aditi',
            reservation_date='2026-10-10',
            reservation_slot=19
        )

    def test_category_created(self):
        self.assertEqual(self.category.title, 'Salads')

    def test_menu_item_created(self):
        self.assertEqual(self.menu_item.title, 'Greek Salad')
        self.assertEqual(str(self.menu_item.price), '12.50')

    def test_booking_created(self):
        self.assertEqual(self.booking.first_name, 'Aditi')
        self.assertEqual(self.booking.reservation_slot, 19)