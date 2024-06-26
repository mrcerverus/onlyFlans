from django.utils.text import slugify
import uuid
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField



# Create your models here.

class Flan(models.Model):
    flan_uuid = models.UUIDField(default=uuid.uuid4 , editable=False, unique=True)
    name = models.CharField(max_length=64, blank=False, null=False) 
    description = models.TextField(blank=False, null=False)
    image_url = models.URLField(blank=False, null=False)
    slug = models.SlugField(unique=True, max_length=255, blank=True)
    is_private = models.BooleanField(default=False)
    precio = models.DecimalField(decimal_places=2, max_digits=10, default=1000, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name) # type: ignore
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    

class Contacto(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4 , editable=False, unique=True)
    customer_name = models.CharField(max_length=50, blank=False, null=False, verbose_name="Nombre Completo")
    customer_email = models.EmailField(blank=False, null=False, verbose_name="Correo electronico")
    message = models.TextField(blank=False, null=False, verbose_name="Mensaje")
    phone = PhoneNumberField(blank=False, null=False, default='',verbose_name="Telefono de contacto")

    def __str__(self):
        return self.customer_name