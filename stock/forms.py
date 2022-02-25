from django import forms
from .models import *
from client.models import Client
# from django.contrib.auth import User
from crispy_forms.helper import FormHelper
from django import forms


ARTICLE_QUANTITY_CHOICES=[(i,str(i)) for i in range(1,21)]
UNITE=[('','---------'),('1','individuel'),('En bloc','En bloc')]
class CartAddArticleForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=ARTICLE_QUANTITY_CHOICES,widget=forms.Select({'class':"form-control"}))
    override =forms.BooleanField(required=False, initial=False,widget=forms.HiddenInput())
    unite = forms.TypedChoiceField(required=False, choices=UNITE,widget=forms.Select({'class':"form-control d-print-none"}))
    # def __init__(self,*args, **kwargs):
    #     super(CartAddArticleForm(), self).__init__(*args, **kwargs)
    #     self.fields.label=False
class DateInput(forms.DateInput):
    input_type = 'date'
class NewStock(forms.ModelForm):
    class Meta:
        model = Stock
        fields ='__all__'
        exclude=['user','qtStock']
    def __init__(self,user, *args, **kwargs):
        super(NewStock, self).__init__(*args, **kwargs)
        # self.fields['qtStock'].label= "Quantité de stock"
        self.fields['categorie'].required = True
        self.fields['categorie'].queryset =Categorie.objects.filter(user=user)
        self.fields['article'].queryset=Article.objects.none()
        if 'categorie' in self.data:
            try:
                categorie_id=int(self.data.get('categorie'))
                self.fields['article'].queryset=Article.objects.filter(categorie=categorie_id).order_by('nom')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['article'].queryset=self.instance.categorie.article_set.order_by('nom')
        


class NewCategorie(forms.ModelForm):
    class Meta:
        model = Categorie
        fields =['categorie']

class NewArticle(forms.ModelForm):
    class Meta:
        model = Article
        fields ='__all__' 
        exclude=['user','numero','barcode']
        widgets={
            "date_entree":DateInput()
        }
    def __init__(self,user, *args, **kwargs):
     
        super(NewArticle, self).__init__(*args, **kwargs)
        self.fields['categorie'].queryset =Categorie.objects.filter(user=user)
        self.fields['categorie'].required=False
        # for key in self.fields:
        # self.fields['description'].required = False 

class NewEntrer(forms.ModelForm):
    class Meta:
        model = Entrer
        fields =['stock', 'article', 'qte', 'prix_entree', 'date_entree']
        exclude =['user']
        widgets = {
            'date_entree': DateInput(),
        }
    def __init__(self, user, *args, **kwargs):
        super(NewEntrer, self).__init__(*args, **kwargs)
        self.fields['stock'].queryset =Entrer.objects.filter(user=user)
 

class NewSortir(forms.ModelForm):
    class Meta:
        model = Sortir
        fields ='__all__'
        exclude = ['user', 'prix_sortie']
        widgets={
            'date_sortie':DateInput()
        }
    def clean(self):
        article = self.cleaned_data['article']
        qte = self.cleaned_data['qte']
        if (qte > article.quantity):
            raise ValueError("la quantité n'est pas disponible dans le stock")
    def __init__(self, *args, **kwargs):
        super(NewSortir, self).__init__(*args, **kwargs)
        self.fields['qte']=forms.IntegerField(min_value=1)
        # self.fields['categorie'].queryset =Categorie.objects.filter(user=user)
        
        # self.fields['article'].queryset=Article.objects.none()
        # self.fields['stock'].queryset=Stock.objects.none()
        # if 'categorie' in self.data:
        #     try:
        #         categorie_id=int(self.data.get('categorie'))
        #         self.fields['stock'].queryset=Stock.objects.filter(categorie=categorie_id).order_by('qtStock')
        #     except (ValueError, TypeError):
        #         pass
        # elif self.instance.pk:
        #     self.fields['stock'].queryset=self.instance.categorie.article_set.order_by('qtStock')
        # if 'stock' in self.data:
        #     # stock_id=int(self.data.get('stock'))
        #     # st=stock.objects.get(id=stock_id)
        #     # qtStock= st.qtStock
        #     # self.fields['qte']=forms.IntegerField(max_value=int(qtStock),min_value=1)
        #     try:
        #         stock_id=int(self.data.get('stock'))
        #         self.fields['article'].queryset=Article.objects.filter(stock=stock_id).order_by('nom')
               

        #     except (ValueError, TypeError):
        #         pass
        # elif self.instance.pk:
        #     self.fields['article'].queryset=self.instance.stock.article_set.order_by('nom')
class NewCommande(forms.ModelForm):
    class Meta:
        model = Commande
        fields =['date', 'user']          

class NewPanier(forms.ModelForm):
    class Meta:
        model = Panier
        fields =['commande', 'article', 'qte']  

class NewFacture(forms.ModelForm):
    class Meta:
        model = Facture
        fields ='__all__'  
        exclude =['totalprix'] 
        widgets={
            'dateFacture': DateInput()
        } 

class NewClient(forms.ModelForm):
    class Meta:
        model = Client
        fields ='__all__'  
        exclude =['user']