from django.db import models
import barcode
import random
import string
from django.contrib.auth.models import User
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File



class Categorie(models.Model):
    categorie=models.CharField(max_length=20)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    
    
    def __str__(self):
        return self.categorie



Status=(('0','Non'),('1','Oui'))
class Article(models.Model):

    user= models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE)
    numero=models.IntegerField(blank=True)
    barcode=models.ImageField(upload_to='article/codes',blank=True)
    nom = models.CharField(max_length=20)
    quantity=models.IntegerField(null=True)
    categorie=models.ForeignKey(Categorie,on_delete=models.CASCADE)
    date_entree=models.DateField(null=True)
    prix_achat=models.IntegerField(null=True)
    statut=models.CharField(max_length=2,null=True,default='0',choices=Status)
    quantité_en_vrac =models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.nom

    def save(self,*args, **kwargs):
        if self._state.adding:
            EAN =barcode.get_barcode_class('upc')
            rend=str(random.randint(2055,99999))
            r=str(random.randint(20,1000))
            rr=self.categorie.id+self.prix_achat
            ean=EAN(str(self.categorie.id)+str(self.user.id)+r+rend+str(self.date_entree.year)+str(self.date_entree.month)+str(self.date_entree.day),writer=ImageWriter())
            buffer =BytesIO()
            ean.write(buffer)
            self.numero=ean.__str__()
            self.barcode.save(str({self.nom})+'.png',File(buffer),save=False)
        return super().save(*args, **kwargs)
        

    


class Stock(models.Model):
    qtStock=models.IntegerField()
    user= models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE)
    categorie=models.ForeignKey(Categorie, blank=True,on_delete=models.CASCADE)
    article=models.ManyToManyField(Article,blank=True,related_name="article") 
    
    def __str__(self):
        return f"la quantite de Stock: {self.qtStock}"
    

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

