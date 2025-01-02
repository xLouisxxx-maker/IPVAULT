from django.db import models

# Create your models here.


# class Patent(models.Model):
#     # Basic patent information
#     title = models.CharField(max_length=255, help_text="Titel des Patents")
#     abstract = models.TextField(help_text="Kurzbeschreibung des Patents")
#     application_number = models.CharField(max_length=100, unique=True, help_text="Antragsnummer")
#     publication_number = models.CharField(max_length=100, unique=True, help_text="Veröffentlichungsnummer")
#     filing_date = models.DateField(help_text="Einreichungsdatum")
#     publication_date = models.DateField(help_text="Veröffentlichungsdatum")

#     # Applicant and inventor information
#     applicant = models.CharField(max_length=255, help_text="Antragsteller")
#     inventor = models.CharField(max_length=255, help_text="Erfinder")

#     # Classification
#     ipc_classification = models.CharField(max_length=255, help_text="IPC-Klassifikation")
#     cpc_classification = models.CharField(max_length=255, blank=True, null=True, help_text="CPC-Klassifikation")

#     # Status and legal information
#     status = models.CharField(max_length=100, choices=[
#         ('pending', 'Ausstehend'),
#         ('granted', 'Erteilt'),
#         ('rejected', 'Abgelehnt'),
#         ('expired', 'Abgelaufen')
#     ], default='pending', help_text="Status des Patents")
#     expiry_date = models.DateField(blank=True, null=True, help_text="Ablaufdatum")

#     # Optional fields
#     priority_date = models.DateField(blank=True, null=True, help_text="Prioritätsdatum")
#     related_patents = models.ManyToManyField('self', blank=True, help_text="Verwandte Patente")

#     # Full text
#     full_text = models.TextField(blank=True, null=True, help_text="Volltext des Patents")

#     # Administrative fields
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


class Patent(models.Model):
   
    title = models.CharField(max_length=400)
    valid = models.BooleanField(default=False)
    application_number = models.CharField(max_length=100, null=True, blank=True)  # Optionales Feld für die Antragsnummer
    description = models.TextField(null=True, blank=True)  # Optionales Textfeld für die Beschreibung des Patents

    def __str__(self):
        return self.title
    