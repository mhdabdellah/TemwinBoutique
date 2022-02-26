from django import forms
from .models import *
from client.models import Client
from crispy_forms.helper import FormHelper
from django import forms


ARTICLE_QUANTITY_CHOICES=[(i,str(i)) for i in range(1,21)]
UNITE=[('','---------'),('1','individuel'),('En bloc','En bloc')]
class CartAddArticleForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=ARTICLE_QUANTITY_CHOICES,widget=forms.Select({'class':"form-control"}))
    override =forms.BooleanField(required=False, initial=False,widget=forms.HiddenInput())
    unite = forms.TypedChoiceField(required=False, choices=UNITE,widget=forms.Select({'class':"form-control d-print-none"}))
   
class DateInput(forms.DateInput):
    input_type = 'date'
class NewStock(forms.ModelForm):
    class Meta:
        model = Stock
        fields ='__all__'
        exclude=['user','qtStock']
    def __init__(self,user, *args, **kwargs):
        super(NewStock, self).__init__(*args, **kwargs)
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

class ProductForm(forms.ModelForm):
    class Meta:
        model = Article
        fields ='__all__' 
        exclude=['user']
        widgets={
            "date_entree":DateInput()
        }
    def __init__(self,user, *args, **kwargs):
     
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['categorie'].queryset =Categorie.objects.filter(user=user)
        self.fields['categorie'].required=False 

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
            raise forms.ValidationError("la quantité n'est pas disponible dans le stock")
        # ValueError("la quantité n'est pas disponible dans le stock")
    def __init__(self, *args, **kwargs):
        super(NewSortir, self).__init__(*args, **kwargs)
        self.fields['qte']=forms.IntegerField(min_value=1)

 

class NewFacture(forms.ModelForm):
    class Meta:
        model = Facture
        fields ='__all__'  
        exclude =['totalprix'] 
        widgets={
            'dateFacture': DateInput()
        } 

