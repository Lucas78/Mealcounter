from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Student


@receiver(pre_save, sender=Student)
def define_password_student(sender, instance, *args, **kwargs):
    if not instance.pk:
        instance.username = instance.email
        instance.set_password(instance.cpf)
