from django.db import models


class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    featured = models.BooleanField(default=False)
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='menu_items'
    )

    def __str__(self):
        return self.title


class Booking(models.Model):
    first_name = models.CharField(max_length=100)
    reservation_date = models.DateField()
    reservation_slot = models.IntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['reservation_date', 'reservation_slot'],
                name='unique_booking_slot'
            )
        ]

    def __str__(self):
        return (
            f"{self.first_name} - "
            f"{self.reservation_date} - "
            f"{self.reservation_slot}"
        )