from django.db import models
from django.utils.translation import ugettext_lazy as _

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(_("Name"), max_length=20, blank=False)
    sid = models.CharField(_("Student ID"), max_length=8, blank=False)
    dob = models.CharField(_("Date of birth"), max_length=10, blank=False)
    gender = models.CharField(_("Gender"), max_length=8, blank=False)

class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    contact_name = models.CharField(_("Contact name"), max_length=50, blank=False)
    contact_addr = models.CharField(_("Contact address"), max_length=100, blank=False)
    student = models.ForeignKey("Student", verbose_name=_(
        "Student"), related_name="contacts", on_delete=models.CASCADE)

class Email(models.Model):
    email_id = models.AutoField(primary_key=True)
    vnu_email = models.CharField(_("VNU email"), max_length=50, blank=False)
    other_email = models.CharField(_("Other email"), max_length=50, blank=False)
    student = models.OneToOneField(Student, related_name='email', on_delete=models.CASCADE)

