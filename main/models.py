from django.db import models
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator


class Category(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=100, unique=True)

    is_visible = models.BooleanField(default=False)
    sort = models.PositiveSmallIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __iter__(self):
        dishes = self.dishes.filter(is_visible=True)
        for dish in dishes:
            yield dish

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('sort', )
        db_table = 'main_categories'


class Dish(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_visible = models.BooleanField(default=True)
    description = models.TextField()
    photo = models.ImageField(upload_to='dishes/')

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='dishes')

    sort = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)\

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('sort', )
        db_table = 'main_dishes'


class SocialNetwork(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    phone_regex = RegexValidator(regex=r'^(\+?380)?\d{9}$',
                                 message="Phone number must be entered in the format: '+380XXXXXXXXX'")
    phone = models.CharField(validators=[phone_regex], max_length=13)
    date = models.DateField()
    time = models.TimeField()
    guests_number = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(10)])
    message = models.TextField(blank=True, null=True)

    is_processed = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)






