from django.db import models
import barcode
import random
import string

from django.dispatch import receiver
from client.models import Client
from django.contrib.auth.models import User
from barcode.writer import ImageWriter
from io import BytesIO
from django.db.models.signals import post_save
from django.core.files import File



class Categorie(models.Model):
    categorie=models.CharField(max_length=20,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    
    
    def __str__(self):
        return self.categorie



Status=(('0','Non'),('1','Oui'))
class Article(models.Model):

    user= models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE)
    numero=models.IntegerField(blank=True)
    # barcode=models.ImageField(upload_to='article/codes',blank=True)
    nom = models.CharField(max_length=20)
    quantity=models.IntegerField(null=True)
    categorie=models.ForeignKey(Categorie,on_delete=models.CASCADE)
    date_entree=models.DateField(null=True,auto_now_add=True)
    prix=models.IntegerField(null=True)
    # statut=models.CharField(max_length=2,null=True,default='0',choices=Status)
    # quantité_en_vrac =models.PositiveIntegerField(null=True)
    duree_conservation=models.DateTimeField(null=True)

    def __str__(self):
        return self.nom

    # def save(self,*args, **kwargs):
    #     if self._state.adding:
    #         EAN =barcode.get_barcode_class('upc')
    #         rend=str(random.randint(2055,99999))
    #         r=str(random.randint(20,1000))
    #         rr=self.categorie.id+self.prix_achat
    #         ean=EAN(str(self.categorie.id)+str(self.user.id)+r+rend+str(self.date_entree.year)+str(self.date_entree.month)+str(self.date_entree.day),writer=ImageWriter())
    #         buffer =BytesIO()
    #         ean.write(buffer)
    #         self.numero=ean.__str__()
    #         self.barcode.save(str({self.nom})+'.png',File(buffer),save=False)
    #     return super().save(*args, **kwargs)
        
class Stock(models.Model):
    qtStock=models.IntegerField()
    # user= models.ForeignKey(User,bla3nk=True,null=True,on_delete=models.CASCADE)
    categorie=models.ForeignKey(Categorie, blank=True,on_delete=models.CASCADE,null=True)
    Article=models.ManyToManyField(Article,blank=True,related_name="article") 
    
    def __str__(self):
        return f"la quantite de Stock: {self.qtStock}"
    
    def gererStock():
        pass
    
class Boutique(models.Model):
    lieu = models.CharField(max_length=32)
    moghataa = models.CharField(max_length=40)
    vendeur=models.OneToOneField(User,on_delete=models.CASCADE)
    # stock=models.OneToOneField(Stock,on_delete=models.CASCADE)
    def extraire_situation_boutique():
        pass
    def genererBel():
        pass

@receiver(post_save, sender=User)
def create_user_boutique(sender, instance, created, **kwargs):
    if created:
        if not instance.is_staff:
            boutique = Boutique.objects.create(vendeur=instance)

class Magazine(models.Model):
    lieu = models.CharField(max_length=32)
    magaziniere = models.ForeignKey(User, on_delete=models.CASCADE)
    # stock=models.OneToOneField(Stock, on_delete=models.CASCADE)
    wilaya = models.CharField(max_length=40)


def __str__(self):
        return f"la magazine gerer par l'utilisateur  {self.magaziniere}"
@receiver(post_save, sender=User)
def create_user_magasine(sender, instance, created, **kwargs):
    if created:
        if instance.is_staff:
                 if not instance.is_superuser:
                    magasine = Magazine.objects.create(magaziniere=instance)

class Entrer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    stock=models.ForeignKey(Stock,on_delete=models.CASCADE)
    article=models.ForeignKey(Article,on_delete=models.CASCADE)
    qte=models.IntegerField()
    prix_entree=models.IntegerField()
    date_entree=models.DateField()

    def __str__(self):
        return f"les articles entree dans la stock par l'utilisateur  {self.user}"

class Sortir(models.Model):
    categorie = models.ForeignKey(Categorie,on_delete=models.CASCADE,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    stock=models.ForeignKey(Stock,null=True,on_delete=models.CASCADE)
    article=models.ForeignKey(Article,on_delete=models.CASCADE)
    qte=models.PositiveIntegerField(null=True)
    prix_sortie=models.FloatField(null=True)
    date_sortie=models.DateField(blank=True,null=True)
    def __str__(self):
        return f"id:{self.id},article:{self.article},la quantité:{self.qte},la prix total:{self.prix_sortie},efectuer par:{self.user}"
    def save(self,*args,**kwargs):
        self.prix_sortie = self.article.prix_achat * self.qte
        return super().save(*args,**kwargs) 
 

class Facture(models.Model):
    dateFacture=models.DateField()
    sorties=models.ManyToManyField(Sortir,related_name='sorties',blank=True)
    User=models.ForeignKey(User,on_delete=models.CASCADE)
    totalprix=models.FloatField(null=True) 

    def __str__(self):
        return f"la prix total est {self.totalprix}"
    def get_sorties(self):
        return self.sorties.all()

class Vente(models.Model):
    date=models.DateTimeField(auto_now_add=True,null=True)
    quantite_vendu=models.PositiveIntegerField(verbose_name="quantite_vendu",null=True)
    client = models.ForeignKey(Client,on_delete=models.CASCADE,null=True)



    def sortir_Article(p):
        pass
    def ticket_de_vente(p):
        pass
    def verificationNni():
        pass
    def respetQuota():
        pass
