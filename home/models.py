from django.db import models

class Document(models.Model):
    document_name = models.CharField(max_length=255)
    owner_name = models.CharField(max_length=255)
    certificate_number = models.CharField(max_length=100)
    completion_date = models.DateField()

    def __str__(self):
        return f"{self.owner_name} - {self.completion_date}"

