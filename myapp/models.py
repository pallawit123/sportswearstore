from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

class MenNewArrival(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='men_new_arrivals/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class MenAutumnWinter(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='men_autumn_winter/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class MenTShirts(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='men_tshirts/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class MenPolos(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='men_polos/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class MenShorts(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='men_shorts/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class MenTrackpantsJoggers(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='men_trackpants_joggers/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class MenRunning(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='men_running/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class MenYoga(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='men_yoga/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class WomenNewArrival(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='women_new_arrivals/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class WomenAutumnWinter(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='women_autumn_winter/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class WomenTShirts(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='women_tshirts/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class WomenPolos(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='women_polos/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class WomenShorts(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='women_shorts/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class WomenTrackpantsJoggers(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='women_trackpants_joggers/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class WomenRunning(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='women_running/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class WomenYoga(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='women_yoga/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class KidsNewArrival(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='kids_new_arrivals/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class KidsAutumnWinter(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='kids_autumn_winter/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class KidsTShirts(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='kids_tshirts/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class KidsPolos(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='kids_polos/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class KidsShorts(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='kids_shorts/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class KidsTrackpantsJoggers(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='kids_trackpants_joggers/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class KidsRunning(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='kids_running/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class KidsYoga(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='kids_yoga/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.title} ({self.quantity})"

class WishlistItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.title