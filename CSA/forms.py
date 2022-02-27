from django import forms
from django.contrib.auth.forms import User
 # forms here.

class ExpeditionForm(forms.Form):
    magazinier = forms.ModelChoiceField(queryset=User.objects.none(),widget=forms.Select({'class':"form-control"}))
    categorie = forms.TypedChoiceField(widget=forms.Select({'class':"form-control"}))
    produit = forms.MultipleChoiceField(widget=forms.SelectMultiple)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(ExpeditionForm, self).__init__(*args, **kwargs)
        if self.request.user.is_staff and  self.request.user.is_superuser:
            self.fields['magazinier'].queryset =  User.objects.all()
                                            #  empty_label="Choose a countries",)