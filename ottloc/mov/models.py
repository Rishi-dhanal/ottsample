from django.db import models

# Create your models here.
AGE_CHOICES = (
    ('All', 'All'),
    ('Kids', 'Kids'),
)

MOVIE_CHOICES = (
    ('seasonal', 'Seasonal'),
    ('single', 'Single'),
)
GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
)

ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
        ('child', 'Child'),
        # Add more roles as needed
    )

class Register(models.Model):


    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    age_limit = models.CharField(choices=AGE_CHOICES, max_length=10)  # Assuming AGE_CHOICES is defined somewhere
    date_joined = models.DateTimeField(auto_now_add=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1)  # Assuming GENDER_CHOICES is defined somewhere
    # role = models.CharField(max_length=10, choices=ROLE_CHOICES)  # Removed the default='user'

    def __str__(self):
        return self.username


class User(models.Model):
    register = models.OneToOneField(Register, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    def __str__(self):
        return self.full_name

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    genre = models.CharField(max_length=50)
    cover_image = models.ImageField(upload_to='movie_covers/', null=True, blank=True)
    age_limit = models.CharField(choices=AGE_CHOICES, max_length=10)  # Minimum age to watch the movie
    movie_type = models.CharField(choices=MOVIE_CHOICES, max_length=10)

    def __str__(self):
        return self.title

class Membership(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.user.full_name}'s Membership"

class PaymentOption(models.Model):
    membership_plan = models.ForeignKey(Membership, on_delete=models.CASCADE)
    method = models.CharField(max_length=100)  # Payment method (e.g., credit card, PayPal)
    duration = models.CharField(max_length=50)  # Duration of subscription (e.g., monthly, yearly)
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Payment amount

    def __str__(self):
        return f"{self.membership_plan.name} - {self.method} - {self.duration}"

class AdultAccount(models.Model):
    register = models.ForeignKey(Register, on_delete=models.CASCADE)
    # Add other fields for the adult account

class ChildAccount(models.Model):
    register = models.ForeignKey(Register, on_delete=models.CASCADE)
    # Add other fields for the child account