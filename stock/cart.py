from decimal import Decimal 
from django.conf import settings
from .models import *
class Cart(object):
    def __init__(self,request):
        self.session=request.session
        cart =self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart=self.session[settings.CART_SESSION_ID]={}
        self.cart=cart
    def add(self,article,quantity=1,unite='1',override_quantity=False):
        article_num=str(article.numero)
        if article_num not in self.cart: 
            self.cart[article_num]={
                'quantity':0,'prix_achat':str(article.prix_achat),
                'unite':str(article.quantité_en_vrac),
            }
            print (self.cart[article_num]['unite'])
        if override_quantity:
            self.cart[article_num]['quantity']=quantity
            if unite == 'En bloc':
                self.cart[article_num]['unite']=article.quantité_en_vrac
            else:
                self.cart[article_num]['unite']=1
        else:
            self.cart[article_num]['quantity']+=int(quantity)
            self.cart[article_num]['unite']=int(unite)
        self.save()
    def save(self):
        self.session.modified = True
    def remove(self,article):
        article_num = str(article.numero)
        if article_num in self.cart:
            del self.cart[article_num]
            self.save()
    def __iter__(self):
        article_nums=self.cart.keys()
        articles=Article.objects.filter(numero__in=article_nums)

        cart = self.cart.copy()
        for article in articles:
            cart[str(article.numero)]['article']=article
        for item in cart.values():
            item['prix_achat']=Decimal(item['prix_achat'])
            item['total_prix']=item['prix_achat']*Decimal(item['quantity'])*int(item['unite'])
            yield item
    def __len__(self):
        for item in self.cart.values():
            print (item)
        return sum(int(item['quantity']) for item in self.cart.values())

    def get_total_prix(self):
        return sum(Decimal(item['prix_achat']*Decimal(item['quantity'])*int(item['unite'])) for item in self.cart.values())
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()