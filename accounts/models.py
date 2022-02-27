from PIL import Image
from django.db import models
from django.contrib.auth.models import AbstractUser, Permission,User
from django.db.models.signals import post_save
from django.dispatch import receiver



# Create your models here.

# Role=(('0','admin'),('1','manager'),('2','vendeure'))
    # statut=models.CharField(max_length=2,null=True,default='2',choices=Status)
# class User(AbstractUser):
    
#     role = models.CharField(max_length=2,choices=Role,verbose_name='role')
    

#     def save(self, *args, **kwargs):
#         super(User, self).save(*args, **kwargs)
#         permission=Permission.objects.get(codename="Ajout_client")
#         self.user_permissions.add(permission)
#         permission=Permission.objects.get(codename="change_client")
#         self.user_permissions.add(permission)
#         permission=Permission.objects.get(codename="Ajout_stock")
#         self.user_permissions.add(permission)
#         permission=Permission.objects.get(codename="change_stock")
#         self.user_permissions.add(permission)
#         permission=Permission.objects.get(codename="Ajout_Boutique")
#         self.user_permissions.add(permission)
#         permission=Permission.objects.get(codename="change_Boutique")
#         self.user_permissions.add(permission)
#         return super(User,self).save(*args, **kwargs)

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=12)
    image = models.ImageField(default='avatar.png',null=True)
    manager = models.CharField(max_length=50,null=True)
    def __str__(self):
        return str(self.user)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.width > 300 or img.height > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)



##create new user --->create new  empty profile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.create(user=instance)