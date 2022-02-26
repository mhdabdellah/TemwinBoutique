from django.db import models
from django.contrib.auth.models import User
import qrcode
from io import StringIO
from io import BytesIO

from django.core.validators import MinLengthValidator, int_list_validator
# from django.core.urlresolvers import reverse
from django.urls import reverse
from django.core.files.uploadedfile import InMemoryUploadedFile

# Create your models here.
#models.IntegerField(blank=True)

class Client(models.Model):
     
    nni=models.CharField(unique=True,max_length=10,validators=[int_list_validator(sep=''),MinLengthValidator(10)])
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=20)
    email = models.CharField(max_length=255,null=True)
    adresse=models.CharField(max_length=255,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    tel = models.CharField(max_length=255,null=True)
    qrCode = models.ImageField(upload_to='client/qrcodes/',blank=True, null=True)
    # qrcode = models.ImageField(upload_to='qrcode', blank=True, null=True)

    def validate_digit_length(nni):
        if not (nni.isdigit() and len(nni)==10):
            raise ValueError('%(nni) must be a digits',params={'nni':nni},)

    def __str__(self):
        return f"le beneficiaires  {self.nom}/{self.prenom}"


    def save(self, *args, **kwargs):
        qrCode = self.qr_generate(self.nni)
        self.qrCode.save(str(self.nni)+'.png', BytesIO(qrCode), save=False)
        super(Client, self).save(*args, **kwargs)


    @staticmethod
    def qr_generate(nni):
        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data("somedata" + str(nni))
        qr.make(fit=True)

        qrCode = qr.make_image(fill_color="black", back_color="white")
        qrByte = BytesIO()
        qrCode.save(qrByte)
        return qrByte.getvalue()
    def delivrer_imprimer_carte():
        pass
    def verificationNni():
        pass