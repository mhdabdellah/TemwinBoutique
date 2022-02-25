from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from django import template
from django.template.loader import get_template
from django.utils.html import format_html
import datetime
from django.contrib import messages
from django.urls import reverse
from .models import *
from .forms import *
from .filters import ArticleFilter
from django.contrib.auth.decorators import login_required
from django.db.models import Sum,Q
from accounts.models import *
from accounts.forms import SignupForm
from django.contrib.auth.models import User
from accounts.decorators import admin_only, in_fix, admin_and_manager_only
from chat.models import Message
from .cart import Cart
from django.views.decorators.http import require_POST

def get_notifications(request):
    message = Message.objects.filter(Q(seen=False, receiver=request.user))
    return message
@require_POST
def cart_add(request):
    cart = Cart(request)
    article_num=request.POST.get('numero')
    article=get_object_or_404(Article,numero=article_num)
    stck=get_object_or_404(Stock,article=article)
    if stck:
     form_cart=CartAddArticleForm(request.POST)
     if form_cart.is_valid():
        cd=form_cart.cleaned_data
        if article.quantity >= int(cd['quantity']) :
            cart.add(article=article,quantity=cd['quantity'],override_quantity=cd['override'])
        else :
            return HttpResponse('<style>'
                                +'.card{ box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2); transition: 0.3s; background-color:FFFFFF}'
                                +'.container{ padding: 50px 5px; margin: 50px 200px}'
                                +'.card:hover{ box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2); background-color:E0E0E0}'
                                +'#btn{ background-color:0000FF}'
                                +'#btn:hover{ background-color:6666FF}'
                                +'body{ background-color:C0C0C0; border-radius:20px; -moz-border-radius:20px}'
                                +'</style>'
                                +'<body>'
                                +'<div class="container" align="center">'
                                  +'<div class="card">'
                                    +'<div class="container">'
                                                        +'<h2>la quantité entreé n\'est pas disponible dans la table des articles saisir une quantité <='+ str(article.quantity)+'</h3>'
                                                        +'</div>'
                                                        +'<div aling="center">'
                                                        +'<a class="card" href="/sortir_article"><button class="card" id="btn" > <h1>OK</h1></button></a>'
                                                        +'</div></div></div></body>')
    print(cart)
    return redirect(reverse('stock:sortir_article'))
@require_POST
def update_item_from_cart(request, article_num):
    cart=Cart(request)
    article=get_object_or_404(Article,numero=article_num)
    form_cart = CartAddArticleForm(request.POST)
    if form_cart.is_valid():
        cd=form_cart.cleaned_data
        if str(cd['unite']) == 'individuel' :
            qt_disponible1 = int(cd['quantity'])
            if article.quantity >= qt_disponible1 :
                cart.add(article=article,quantity=cd['quantity'],override_quantity=cd['override'],unite=cd['unite'])
            else :
                return HttpResponse('<style>'
                                +'.card{ box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2); transition: 0.3s; background-color:FFFFFF}'
                                +'.container{ padding: 50px 5px; margin: 50px 200px}'
                                +'.card:hover{ box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2); background-color:E0E0E0}'
                                +'#btn{ background-color:0000FF}'
                                +'#btn:hover{ background-color:6666FF}'
                                +'body{ background-color:C0C0C0; border-radius:20px; -moz-border-radius:20px}'
                                +'</style>'
                                +'<body>'
                                +'<div class="container" align="center">'
                                  +'<div class="card">'
                                    +'<div class="container">'
                                                        +'<h2>la quantité entreé n\'est pas disponible dans la table des articles saisir une quantité <='+ str(article.quantity)+'</h3>'
                                                        +'</div>'
                                                        +'<div aling="center">'
                                                        +'<a class="card" href="/sortir_article"><button class="card" id="btn" > <h1>OK</h1></button></a>'
                                                        +'</div></div></div></body>')
        else :
            qt_disponible = int(cd['quantity']) * article.quantité_en_vrac
            if article.quantity >= qt_disponible :
                cart.add(article=article,quantity=cd['quantity'],override_quantity=cd['override'],unite=cd['unite'])
            else :
                return HttpResponse('<style>'
                                +'.card{ box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2); transition: 0.3s; background-color:FFFFFF}'
                                +'.container{ padding: 50px 5px; margin: 50px 200px}'
                                +'.card:hover{ box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2); background-color:E0E0E0}'
                                +'#btn{ background-color:0000FF}'
                                +'#btn:hover{ background-color:6666FF}'
                                +'body{ background-color:C0C0C0; border-radius:20px; -moz-border-radius:20px}'
                                +'</style>'
                                +'<body>'
                                +'<div class="container" align="center">'
                                  +'<div class="card">'
                                    +'<div class="container">'
                                                        +'<h2>la quantité entreé n\'est pas disponible dans la table des articles saisir une quantité <='+ str(article.quantity)+'</h3>'
                                                        +'</div>'
                                                        +'<div aling="center">'
                                                        +'<a class="card" href="/sortir_article"><button class="card" id="btn" > <h1>OK</h1></button></a>'
                                                        +'</div></div></div></body>')
    return redirect(reverse('stock:sortir_article'))

@require_POST
def cart_remove(request,numero):
    cart = Cart(request)
    article=get_object_or_404(Article,numero=numero)
    cart.remove(article)
    return redirect(reverse('stock:sortir_article'))
def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity']=CartAddArticleForm(initial={'quantity':item['quantity'],'override':True})
    return render(request,'stock/cart_detail.html',{'cart':cart})
def clear_cart(request):
    cart=Cart(request)
    cart.clear()
    return redirect(reverse('stock:sortir_article'))
@login_required(login_url='accounts/login')
def home(request):
    message = get_notifications(request)

    if request.user.is_staff == True and request.user.is_superuser == False :
        categorie=Categorie.objects.filter(user = request.user)
        article=Article.objects.filter(user = request.user)
        stock=Stock.objects.filter(user = request.user)
        user=User.objects.all()
        context={'user':user,'categorie':categorie,'article':article,'stock':stock,}
        return render(request,'stock/index.html',context)

    if request.user.is_staff == False and request.user.is_superuser == False:
        profiles = Profile.objects.all()
        for profile in profiles :
            if profile.user == request.user :
                article=Article.objects.filter(user = profile.manager)
                context={'article':article,}
                return render(request,'stock/index.html',context)
                break

    else :
        user=User.objects.all()
        categorie=Categorie.objects.all()
        article=Article.objects.all()
        stock=Stock.objects.all()
        sortir=Sortir.objects.all()
        context={'user':user,'categorie':categorie,'article':article,'stock':stock, 'sortir':sortir,'message': message}
        return render(request,'stock/index.html',context)

@login_required(login_url='accounts/login')
@admin_and_manager_only
def stockform(request):
    if request.method == 'POST':
        stock_Form = NewStock(request.user,request.POST)
        mes_article= request.POST.getlist('article')
        if stock_Form.is_valid():
            stock_Form= stock_Form.save(commit=False)
            stock_Form.user = User.objects.get(id=request.user.pk)
            quantity=0
            for expr in mes_article:
                print(expr)
                
                exp = Article.objects.get(id=expr)
                quantity=exp.quantity + quantity
            print(quantity)
            stock_Form.qtStock=quantity
            stock_Form.save()
            for expr in mes_article:
                exp = Article.objects.get(id=expr)
                stock_Form.article.add(exp)
                stock_Form.save()
            for art in mes_article: 
                artic=Article.objects.get(id=art)
                
                artic.statut='1'
                artic.save()

            messages.success(
                request, f"Felicitations la quantité  {stock_Form.qtStock} de stock est bien ajoute")
            return redirect(reverse('stock:stockform'))
    else:
    
        stock_Form = NewStock(request.user)
        context={
           
            'stock_Form' : stock_Form,

        }
        return render(request,'stock/stockform.html',context)

# Aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaajjjjjjjjjjjjjjjjjjjjjjaaaaaaaaaaaaaaaaaaaaaaaaaax  
def load_articles(request):
    categorie_id=request.GET.get('categorie')
    articles=Article.objects.filter(categorie=categorie_id).order_by('nom')

    return render(request,'stock/article_dropdown.html',{'articles':articles})
def load_articles_out(request):
    article_number=request.GET.get('article_number')
    print(article_number)
    article=Article.objects.get(numero=article_number)
    stock=Stock.objects.get(article=article.id)
    print (stock.id)
    print(article)
    article_out=NewSortir(
        initial={'qte':article.quantity,'stock':stock.id
    ,'categorie':article.categorie,'article': article.id,'prix_sortie':article.prix_achat,'date_sortie':article.date_entree}
    )
    
    return render(request,'stock/article_out.html',{'articles':article_out})
def load_stock_out(request):
    categorie=request.GET.get('categorie')

    stock=Stock.objects.filter(categorie=categorie).order_by('qtStock')
    
    for st in stock:
     print(st.qtStock)
    return render(request, 'stock/stock_out.html',{'stocks':stock})
def sortir_article(request):
   
    cart_article_form=CartAddArticleForm()
    cart=Cart(request)
    for item in cart:
        print (item)
        item['update_quantity']=CartAddArticleForm(initial={'quantity':item['quantity'],'override':True,'unite':'1'})
    if request.method == 'POST':
        articles=[]
        i=0
        for item in cart:
            id_article=item['article'].id
            article=Article.objects.get(id=int(id_article))
            article.quantity = article.quantity - int(item['quantity'])
            article.save()
            print (article.id)
            articles.append(id_article)
            stock_id=Stock.objects.get(article=article)
            Sortir.objects.create(categorie=item['article'].categorie,user=request.user,stock=stock_id,article=article,qte=item['quantity'],prix_sortie=item['prix_achat'])
            
        fac=Facture.objects.create(dateFacture=datetime.datetime.now().date(),User=request.user)
        for s in articles:
            fac.sorties.add(Sortir.objects.filter(article=s).last())
            fac.save()

    return render(request,'stock/sortir_article.html',{'cart_article_form':cart_article_form,'cart':cart})

def ajax_delete(request):
    id_user = request.GET.getlist('id_user[]')
    print(id_user)
    
    user = User.objects.get(id=id_user[0])
    return delete_user(request, user)
# eeeeeeeeeeeeeeeeeennnnnnnnnnnnnddddddddddddd AAAAAAAAAAAAAAAAAjjjjjjjjjjjjjjjjjjjaaaaaaaaaaaaaaaaaaxxxxxxxxxxxx

def delete_user(request,user):
    user.delete()
def ajax_update(request):
    if request.method == 'GET':
        id_user=request.GET.get('id_user')
        user=User.objects.get(id=id_user)
        print (user)
        print (user.password)
        form = SignupForm(instance=user)
        return render(request, 'registration/signup.html', {'form': form})
    else:
        form = SignupForm(request.POST)
        if form.is_valid():
            us = form.save()
            messages.success(
                request, f"Felicitation utilisateur bien ajoute")
        return redirect('accounts:signup')
    
def update_user(request, user):
    form = SignupForm(instance=user)
    return redirect(reverse('accounts:signup', kwargs={'form': form}))
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            us = form.save()

           
            messages.success(
                request, f"Felicitation utilisateur bien ajoute")

            return redirect('accounts:signup')

@login_required(login_url='accounts/login')
@admin_and_manager_only
def categorieform(request):
    message = get_notifications(request)
    if request.method == 'POST':
        categorie_Form = NewCategorie(request.POST)
        if categorie_Form.is_valid():
            categorie_Form= categorie_Form.save(commit=False)
            categorie_Form.user = User.objects.get(id=request.user.pk)
            myform=categorie_Form.save()
            messages.success(
                request, f"Felicitations la categorie  {categorie_Form.categorie}  est bien ajoute")
            return redirect(reverse('stock:categorieform'))
    else:
   
        categorie_Form = NewCategorie()
        context={
           
            'categorie_Form' : categorie_Form,
            'message': message

        }
        return render(request,'stock/categorieform.html',context)


@login_required(login_url='accounts/login') 
@admin_and_manager_only 
def articleform(request):
    message = get_notifications(request)
    if request.method == 'POST':
        article_Form = NewArticle(request.user,request.POST)
        if article_Form.is_valid():
            article_Form= article_Form.save(commit=False)
            article_Form.user = User.objects.get(id=request.user.pk)
            article_Form.save()
            url=article_Form.barcode.url
            msg=(f"""<p>Felicitations l'article  \'{article_Form.nom}\'  est bien ajoute vous pouvez imprimer le barcode <a href=\'{article_Form.barcode.url}\'>imprimer</a></p>""")
            messages.success(
                request,format_html(msg))
            return redirect(reverse('stock:articleform'))
    else:
    
        article_Form = NewArticle(request.user)
        context={ 
           
            'article_Form' : article_Form,
            'message': message

        }
        return render(request,'stock/articleform.html',context)


    


  
@login_required(login_url='accounts/login')
def sortirform(request):
    # qtStock=load_articles_out.qtStock
    if request.method == 'POST':
        sortir_Form = NewSortir(request.user, request.POST)
        if sortir_Form.is_valid():
            sortir_Form= sortir_Form.save(commit=False)
            sortir_Form.user = User.objects.get(id=request.user.pk)
            art = request.POST['article']
            artic=Article.objects.get(id=art)
            artic.quantity=artic.quantity-int(request.POST['qte'])
            artic.save()
            stock_id=request.POST['stock']
            stock=Stock.objects.get(id=stock_id)
            stock.qtStock=stock.qtStock-int(request.POST['qte'])
            stock.save()
            sortir_Form.save()
            messages.success(
                request, f"Felicitations {sortir_Form.stock}  est bien sortire de la stocke")
            return redirect(reverse('stock:sortirform'))
          
    else:
        sortir_Form = NewSortir(request.user)
        context={
           
            'sortir_Form' : sortir_Form,

        }
        return render(request,'stock/sortirform.html',context)

@login_required(login_url='accounts/login')
def factureform(request):
    if request.method == 'POST':
        facture_Form = NewFacture(request.POST)
        if facture_Form.is_valid():
            myform=facture_Form.save()
            messages.success(
                request, f"Felicitations la facture  {myform.totalprix}  est bien ajoute")
            return redirect(reverse('stock:factureform'))
    else:
        facture_Form = NewFacture()
        context={
           
            'facture_Form' : facture_Form,

        }
        return render(request,'stock/factureform.html',context)


@login_required(login_url='accounts/login')
@admin_and_manager_only 
def tableuser(request):
    message = get_notifications(request)
    profile = Profile.objects.all()
    user = User.objects.all()
    context={

        'profile': profile,
        'user': user,
        'message': message

    }
    return render(request,'stock/table_user.html',context)

# affichage de contenie de la table Entrer dans la page table_entrer
@login_required(login_url='accounts/login')
@in_fix
def tentrer(request):
    context={

        'title': 'les article entrer dans les stock' ,
        'tentrer': Entrer.objects.all()

    }
    return render(request,'stock/table_entrer.html',context)

@login_required(login_url='accounts/login')
def tarticle(request):
    message = get_notifications(request)
    article_manager = Article.objects.filter(user = request.user)
    article_admin = Article.objects.all()
    

    if request.user.is_staff == True and request.user.is_superuser == False :

        context={

            'title': 'les article',
            'tarticle':article_manager,
            'message': message

        }
        return render(request,'stock/table_article.html',context)

    if request.user.is_staff == False and request.user.is_superuser == False:

        profiles = Profile.objects.all()
        for profile in profiles :
            if profile.user == request.user :
                article_vendeure=Article.objects.filter(user = profile.manager)
                context={
                    'title': 'les article',
                    'tarticle':article_vendeure,
                }
                return render(request,'stock/table_article.html',context)
                break
        

    else :
        context={

            'title': 'les article',
            'tarticle':article_admin,

        }
        return render(request,'stock/table_article.html',context)

@login_required(login_url='accounts/login')
@admin_and_manager_only
def tcategorie(request):
    if request.user.is_staff == True and request.user.is_superuser == True :

        context={
        
            'title': 'les Categories' ,
            'tcategorie': Categorie.objects.all(),

        }
        return render(request,'stock/table_categorie.html',context)
    else :
        context={
        
            'title': 'les Categories' ,
            'tcategorie': Categorie.objects.filter(user = request.user)

        }
        return render(request,'stock/table_categorie.html',context)

@login_required(login_url='accounts/login')
@admin_and_manager_only
def tstock(request):
    context={

        'title': 'les article' ,
        'tstock': Stock.objects.all()

    }
    return render(request,'stock/table_stock.html',context)

@login_required(login_url='accounts/login')
@admin_and_manager_only
def tsortir(request):
    context={

        'title': 'les article' ,
        'tsortir': Sortir.objects.all()

    }
    return render(request,'stock/table_sortir.html',context)

@login_required(login_url='accounts/login')
@in_fix
def tcommande(request):
    context={

        'title': 'les article' ,
        'tcommande': Commande.objects.all()

    }
    return render(request,'stock/table_commande.html',context)

@login_required(login_url='accounts/login')
@in_fix
def tpanier(request):
    context={

        'title': 'les article' ,
        'tpanier': Panier.objects.all()

    }
    return render(request,'stock/table_panier.html',context)

@login_required(login_url='accounts/login')
@admin_and_manager_only
def tfacture(request):
    context={

        'title': 'les factures' ,
        'tfacture': Facture.objects.all()

    }
    return render(request,'stock/table_facture.html',context)

@login_required(login_url='accounts/login')
@in_fix
def results(request):
    search_text = request.GET.get('csrfmiddlewaretoken','')
    results = Article.objects.filter(nom=search_text)
    return render(request,'stock/results.html',{'results' : results})

@login_required(login_url='accounts/login')
def search(request):
    context={

        'title': 'la recherche' ,
        'body': 'body'

    }
    return render(request,'stock/search.html',context)

@login_required(login_url='accounts/login')
@admin_and_manager_only
def update_article(request, id):
    article = Article.objects.get(id=id)
    form = NewArticle(request.user,request.POST or None, instance=article )
    if form.is_valid():
        myform = form.save()
        return redirect(reverse('stock:table_article'))

    return render(request,'stock/update_article.html',{ 'form': form,  'article': article})

@login_required(login_url='accounts/login')
@admin_and_manager_only
def delete_article(request, id):
    article = Article.objects.get(id=id)
    if request.method == 'POST': 
        article.delete()
        return redirect(reverse('stock:table_article'))

    return render(request,'stock/delete_article.html',{'article': article})

@login_required(login_url='accounts/login')
@admin_and_manager_only
def update_categorie(request, id):
    categorie = Categorie.objects.get(id=id)
    form = NewCategorie(request.POST or None, instance=categorie )
    if form.is_valid():
        myform = form.save()
        return redirect(reverse('stock:table_categorie'))
    return render(request,'stock/update_categorie.html',{ 'form': form,  'categorie': categorie})

@login_required(login_url='accounts/login')
@admin_and_manager_only
def delete_categorie(request, id):
    categorie = Categorie.objects.get(id=id)
    if request.method == 'POST': 
        categorie.delete()
        return redirect(reverse('stock:table_categorie'))

    return render(request,'stock/delete_categorie.html', {'categorie': categorie})

@login_required(login_url='accounts/login')
@admin_and_manager_only
def update_stock(request, id):
    stock = Stock.objects.get(id=id)
    form = NewStock(request.user,request.POST or None, instance=stock )
    if form.is_valid():
        myform = form.save()
        return redirect(reverse('stock:table_stock'))

    return render(request,'stock/update_stock.html',{ 'form': form,  'stock': stock})

@login_required(login_url='accounts/login')
@admin_and_manager_only
def delete_stock(request, id):
    stock = Stock.objects.get(id=id)
    if request.method == 'POST': 
        stock.delete()
        return redirect(reverse('stock:table_stock'))

    return render(request,'stock/delete_stock.html',{'stock': stock}) 

@login_required(login_url='accounts/login')
@admin_and_manager_only
def delete_sortir(request, id):
    sortir = Sortir.objects.get(id=id)
    if request.method == 'POST': 
        sortir.delete()
        return redirect(reverse('stock:table_sortir'))

    return render(request,'stock/delete_sortir.html',{'sortir': sortir})

@login_required(login_url='accounts/login')
@admin_and_manager_only
def imprimer_facture(request, id):
    facture = Facture.objects.get(id=id)
   
    return render(request,'stock/imprimer_facture.html',{'facture':  facture})   

