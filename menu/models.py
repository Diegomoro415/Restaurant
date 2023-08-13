from django.db import models
from django.utils.text import slugify

class Menu(models.Model):
    """
    Model representing a menu item.
    """
    # Field to store the category of the menu item
    category = models.CharField(max_length=50, default='')

    # Field to store the name of the menu item
    name = models.CharField(max_length=50)

    # Field to store the description of the menu item
    description = models.TextField(max_length=500)

    # Field to store the price of the menu item
    price = models.DecimalField(max_digits=5, decimal_places=2)

    # Field to store the image of the menu item
    image = models.ImageField(upload_to="menu/")

    # Field to store the slug for the menu item
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        """
        Override the save method to automatically generate a slug from the name if it's not provided.
        """
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super(Menu, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'menu'
        verbose_name_plural = 'menu'

    def __str__(self):
        """
        Return the string representation of the menu item.
        """
        return self.name
