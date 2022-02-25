from .models import *
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver as receive

@receiver(m2m_changed,sender=Facture.sorties.through)
def calculate_total_price(sender, instance,action,**kwargs):
    print('action', action)


    totalprix = 0
    if  action == 'post_add' or action == 'post_remove':
      for item in instance.get_sorties():
          totalprix += item.prix_sortie

    instance.totalprix = totalprix
    instance.save()


# @receive(pre_delete,sender=Article)
# def delete_image(sender,instance,**kwargs):
#       instance.barcode.delete(False)