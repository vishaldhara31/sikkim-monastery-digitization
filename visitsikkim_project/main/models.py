
from django.db import models

class Monastery(models.Model):
    name = models.CharField(max_length=200)  # ✅ allows spaces, must be unique
    description = models.TextField(blank=True)  # ✅ optional description
    image = models.ImageField(upload_to="monasteries/", blank=True, null=True)  # ✅ optional image
    google_map_embed_url = models.URLField(
        help_text="Paste the Google Maps Embed URL", blank=True, null=True
    )  # ✅ optional embed

    def __str__(self):
        return self.name

class map(models.Model):
    monastery_id = models.CharField(max_length=100, unique=True)  # to match 'id' from JS data
    name = models.CharField(max_length=255)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lng = models.DecimalField(max_digits=9, decimal_places=6)
    district = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    attractions = models.JSONField(blank=True, null=True)  # or TextField if storing as stringified JSON

    def __str__(self):
        return self.name