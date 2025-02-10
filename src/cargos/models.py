from django.db import models
from django.utils.text import slugify
from unidecode import unidecode

from addons.utils.constants import HELP_TEXT_STATUS, Statuses


class Cargo(models.Model):
    title =  models.CharField(max_length=100, null=True)
    description = models.TextField(max_length=500, null=True)
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        null=True,
        default=None,
        related_name="owner",
    )
    location = models.CharField(max_length=100, null=True)
    destination = models.CharField(max_length=100, null=True)
    weight = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    status = models.SmallIntegerField(null=True, help_text=HELP_TEXT_STATUS, default=Statuses.PENDING)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True, default=None)
    is_published = models.BooleanField(null=True, default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        db_table = "cargos"
        ordering = ["-id"]

    def __str__(self):
        return f"{self.title} - {self.location} -> {self.destination}"

    def save(self, *args, **kwargs):
        if self.id is None:
            super().save(*args, **kwargs)

        if not self.slug or not self.slug.startswith(f"{self.id}-"):
            base_slug = slugify(unidecode(self.title))
            self.slug = f"{self.id}-{base_slug}"

        kwargs["force_insert"] = False
        super().save(*args, **kwargs)