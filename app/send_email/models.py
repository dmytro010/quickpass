from django.db import models

class Contact(models.Model):
    email = models.EmailField(max_length=50)
    date_created = models.DateField(auto_now=True)

    def str(self):
        return self.email