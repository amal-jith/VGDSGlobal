from django.db import models

# Create your models here.

class FAQ(models.Model):
    PAGE_CHOICES = [
        ('home', 'Home Page'),
        ('presentation_design', 'Presentation Design'),
        ('graphics', 'Graphics & Print Design'),
        ('other_services', 'Other Services'),
    ]
    page = models.CharField(max_length=50, choices=PAGE_CHOICES)
    question = models.CharField(max_length=255)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.question



class Testimonials(models.Model):
    name = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='testimonials/profile_images/', default='testimonials/profile_images/pro.png')
    date = models.DateField()
    content = models.TextField(max_length=400)
    trustpilot_url = models.URLField(blank=True, null=True)
    is_important = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.date.strftime('%d %b %Y')}"




class Order(models.Model):
    # Step 1 - Treatment
    treatment_name = models.CharField(max_length=100, blank=True, null=True)
    treatment_price = models.CharField(max_length=50, blank=True, null=True)

    # Step 2 - Style
    style_name = models.CharField(max_length=100, blank=True, null=True)
    style_file = models.FileField(upload_to="style_files/", blank=True, null=True)

    # Step 3 - Delivery
    delivery_date = models.CharField(max_length=20, blank=True, null=True)
    delivery_rate = models.CharField(max_length=100, blank=True, null=True)
    delivery_slides = models.IntegerField(default=1)
    delivery_option = models.CharField(max_length=100, blank=True, null=True)
    delivery_option_price = models.FloatField(default=0)
    estimated_price_range = models.CharField(max_length=100, blank=True, null=True)

    # Step 4 - Files
    google_checkbox = models.BooleanField(default=False)
    google_link = models.TextField(blank=True, null=True)
    presentation_file = models.FileField(upload_to="presentations/", blank=True, null=True)

    # Step 5 - Payment
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    promo_code = models.CharField(max_length=100, blank=True, null=True)
    agreed_to_terms = models.BooleanField(default=False)
    marketing_opt_in = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order by {self.full_name} - {self.created_at.strftime('%Y-%m-%d')}"





# Predefined categories to match your buttons
CATEGORY_CHOICES = [
    ('brandingTemplates', 'Branding Templates'),
    ('brochure', 'Brochure'),
    ('businessPresentation', 'Business Presentation'),
    ('companyProfile', 'Company Profile'),
    ('flyer', 'Flyer'),
    ('graphicDesign', 'Graphic Design'),
    ('pitchDeckDesign', 'Pitch Deck Design'),
    ('dataVisualization', 'Data Visualization'),
    ('salesDesign', 'Sales Design'),
    ('trainingDeck', 'Training Deck'),
    ('toolKit', 'Toolkit'),
    ('launchPlan', 'Launch Plan'),
    ('proposalDeck', 'Proposal Deck'),
    ('proficiencyDeck', 'Proficiency Deck'),
    ('growthProposal', 'Growth Proposal'),
    ('investorDeck', 'Investor Deck'),
    ('technicalDeck', 'Technical Deck'),
    ('rebranding', 'Rebranding'),
    ('corporate', 'Corporate'),
    ('strategyDeck', 'Strategy Deck'),

]


class Work(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='portfolio/')
    is_important = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class TeamMember(models.Model):
    ROLE_PRIORITY = [
        ('CEO', 'CEO'),
        ('COO', 'COO'),
        ('CTO', 'CTO'),
        ('DESIGNER', 'Designer'),
        ('PRESENTATION_EXPERT', 'Presentation Expert'),
        ('MEMBER', 'Team Member'),
        ('OTHER', 'Other'),
    ]

    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    image = models.ImageField(upload_to='team/images/')

    linkedin = models.URLField(blank=True, null=True)
    dribbble = models.URLField(blank=True, null=True)
    group = models.URLField(blank=True, null=True)

    role = models.CharField(max_length=50, choices=ROLE_PRIORITY, default='MEMBER')
    priority = models.PositiveIntegerField(default=100)  # Lower number = higher priority

    class Meta:
        ordering = ['priority', 'name']

    def __str__(self):
        return self.name


class Rating(models.Model):
    value = models.DecimalField(max_digits=3, decimal_places=1)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Rated {self.value}/5"


class Blog(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.TextField()
    image = models.ImageField(upload_to='blog_images/')
    date = models.DateField()
    link = models.URLField(blank=True)  # Optional external link

    def __str__(self):
        return self.title



class HeroImageSwiperOne(models.Model):
    image = models.ImageField(upload_to='hero/swiper1/')
    alt_text = models.CharField(max_length=100, blank=True)

class HeroImageSwiperTwo(models.Model):
    image = models.ImageField(upload_to='hero/swiper2/')
    alt_text = models.CharField(max_length=100, blank=True)

class HeroImageMobile(models.Model):
    image = models.ImageField(upload_to='hero/mobile/')
    alt_text = models.CharField(max_length=100, blank=True)
