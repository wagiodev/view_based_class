from django.db import models
from django.utils import timezone
from django.urls import reverse

class New(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    city = models.CharField(max_length=200)
    topic = models.CharField(max_length=200)
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def get_absolute_url(self):
        return reverse('new_detail', kwargs={'pk': self.pk})

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title



