from django.urls import path
from . import views
app_name='stock'
urlpatterns=[
    path('',views.home,name='home'),
    path('stockform',views.stockform ,name='stockform'),
    path('categorieform',views.categorieform ,name='categorieform'),
    path('articleform',views.articleform ,name='articleform'),
    #vvvvvvv
    # path('sortirform',views.sortirform ,name='sortirform'),
    path('factureform',views.factureform ,name='factureform'),
    path('ajax/load-articles/',views.load_articles,name='load_articles'),
    path('ajax/load-articles_out/',views.load_articles_out,name='load_articles_out'),
    path('ajax/load_stock_out/',views.load_stock_out,name='load_stock_out'),
    path('table_users',views.tableuser,name='table_users'),
    path('table_article',views.tarticle,name='table_article'),
    path('table_categorie',views.tcategorie,name='table_categorie'),
    path('table_stock',views.tstock,name='table_stock'),
    path('table_sortir',views.tsortir,name='table_sortir'),
    path('table_facture',views.tfacture,name='table_facture'),
    #vvvvvv
    path('sortir_article/',views.sortir_article,name='sortir_article'),
    path('update_article/<int:id>',views.update_article,name='update_article'),
    path('delete_article/<int:id>',views.delete_article,name='delete_article'),
    path('update_categorie/<int:id>',views.update_categorie,name='update_categorie'),
    path('delete_categorie/<int:id>',views.delete_categorie,name='delete_categorie'),
    path('update_stock/<int:id>',views.update_stock,name='update_stock'),
    path('delete_stock/<int:id>',views.delete_stock,name='delete_stock'),
    path('delete_sortir/<int:id>',views.delete_sortir,name='delete_sortir'),

    path('ajax_delete',views.ajax_delete,name='ajax_delete'),
    path('ajax_update/',views.ajax_update,name='ajax_update'),
    
    path('imprimer_facture/<int:id>',views.imprimer_facture,name='imprimer_facture'),
    path('cart_detail',views.cart_detail,name='cart_detail'),
    path('cart_add/',views.cart_add,name='cart_add'),
    path('cart_remove/<slug:numero>',views.cart_remove,name='cart_remove'),
    path('clear_cart/',views.clear_cart,name='clear_cart'),
    path('update_item_from_cart/<int:article_num>',views.update_item_from_cart,name='update_item'),

    # path('update_item_from_cart/<int:article_num>',views.update_item_from_cart,name='update_item'),


]