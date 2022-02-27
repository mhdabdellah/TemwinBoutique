from django.shortcuts import render
from .forms import ExpeditionForm

# Create your views here.
def expediton(request):
   expedition_Form= ExpeditionForm(request=request)
   if request.method =="POST":
      redirect(reverse('csa:expediton'))
   else:
      context={'expedition_Form' : expedition_Form}
      return render(request,'CSA/expedition.html',context)
