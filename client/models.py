from django.db import models
from django.contrib.auth.models import User
import qrcode
import io
from io import StringIO
from io import BytesIO


# from django.core.urlresolvers import reverse
from django.urls import reverse
from django.core.files.uploadedfile import InMemoryUploadedFile

# Create your models here.
#models.IntegerField(blank=True)
class Client(models.Model):
    nni=models.CharField(max_length=20)
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=20)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    img = models.ImageField(upload_to='client/qrcodes/',blank=True, null=True)
    # qrcode = models.ImageField(upload_to='qrcode', blank=True, null=True)


    def __str__(self):
        return f"le beneficiaires  {self.nom}/{self.prenom}"


    def save(self, *args, **kwargs):
        img = self.qr_generate(self.nni)
        self.img.save(self.nni+'.png', BytesIO(img), save=False)
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

        img = qr.make_image(fill_color="black", back_color="white")
        qrByte = BytesIO()
        img.save(qrByte)
        return qrByte.getvalue()
# def save(self,*args, **kwargs):
#     if self._state.adding:
#         # qr = qrcode.QRCode(
#         #     version=1,
#         #     error_correction=qrcode.constants.ERROR_CORRECT_L,
#         #     box_size=6,
#         #     border=0,
#         # )
#         # qr.add_data(self.nni)
#         qr.make(str(self.nni))

#         img = qr.make_image()

#         buffer = StringIO.StringIO()
#         img.save(buffer)
#         filename = 'client-%s.png' % (self.id)
#         filebuffer = InMemoryUploadedFile(
#             buffer, None, filename, 'image/png', buffer.len, None)
#         self.img.save(filename, filebuffer,save=False)
#     return super().save(*args, **kwargs)

    # def generate_qrcode(self):
    #     qr = qrcode.make('hello word')
    #     qr.save(self.img)