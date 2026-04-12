from django.db import models


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=80, default='Member')
    content = models.TextField()
    rating = models.PositiveSmallIntegerField(default=5)
    avatar_url = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} — {self.rating}★"

    class Meta:
        ordering = ['-created_at']


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    excerpt = models.TextField(max_length=300)
    content = models.TextField()
    cover_url = models.URLField(blank=True)
    category = models.CharField(max_length=60, default='Fitness')
    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.created_at.strftime('%d %b %Y')}"

    class Meta:
        ordering = ['-created_at']


class MembershipEnquiry(models.Model):
    PLAN_CHOICES = [
        ('starter', 'Starter'),
        ('pro', 'Pro'),
        ('elite', 'Elite'),
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    plan = models.CharField(max_length=20, choices=PLAN_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.get_plan_display()}"

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Membership Enquiries"
