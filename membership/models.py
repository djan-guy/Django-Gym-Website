from django.db import models

class Membership(models.Model):
    DURATION_CHOICES = [
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly'),
    ]

    PRICING_CHOICES = [
        ('full', 'Full Price'),
        ('concession', 'Concession'),
    ]

    PAYMENT_CHOICES = [
        ('card', 'Credit/Debit Card'),
        ('paypal', 'PayPal'),
        ('simulated', 'Simulated Payment'),
    ]

    PLAN_CHOICES = [
        ('basic', 'Basic – £9.99/month'),
        ('pro', 'Pro – £19.99/month'),
        ('elite', 'Elite – £29.99/month'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    duration = models.CharField(max_length=20, choices=DURATION_CHOICES)
    pricing = models.CharField(max_length=20, choices=PRICING_CHOICES)
    payment = models.CharField(max_length=20, choices=PAYMENT_CHOICES)
    membership = models.CharField(max_length=20, choices=PLAN_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.membership}"
