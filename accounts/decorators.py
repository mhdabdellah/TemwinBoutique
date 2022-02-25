from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse

def unauthenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('home')
		else:
			return view_func(request, *args, **kwargs)

	return wrapper_func

def allowed_users(allowed_roles=[]):
	def decorator(view_func):
		def wrapper_func(request, *args, **kwargs):

			group = None
			if request.user.groups.exists():
				group = request.user.groups.all()[0].name

			if group in allowed_roles:
				return view_func(request, *args, **kwargs)
			else:
					return HttpResponse('vous n\'avez pas l\'autorisation de faire cette action attention ne répéte pas cette opération ')
		return wrapper_func
	return decorator

# def admin_only(view_func):
# 	def wrapper_function(request, *args, **kwargs):
# 		group = None
# 		if request.user.groups.exists():
# 			group = request.user.groups.all()[0].name

# 		if group == 'shopkipper':
# 			return redirect('accounts/logout')

# 		if group == 'manager':
# 			return redirect('accounts/logout')

# 		if group == 'admin':
# 			return view_func(request, *args, **kwargs)

# 	return wrapper_function

def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'shopkipper' or 'manager':
            return redirect('accounts/logout')
        elif group == 'admin':
            return view_func(request, *args, **kwargs)
        else:
            return # <- return response here (possibly a redirect to login page?)

    return wrapper_function

def admin_and_manager_only(view_func):
	def wrapper_function(request, *args, **kwargs):
		group = None
		if request.user.groups.exists():
			group = request.user.groups.all()[0].name

		if group == 'shopkipper':
			return redirect('accounts/logout')

		if group == 'admin' or 'manager':
			return view_func(request, *args, **kwargs)

	return wrapper_function

def in_fix(view_func):
	def wrapper_function(request, *args, **kwargs):
		group = None
		if request.user.groups.exists():
			group = request.user.groups.all()[0].name
			return HttpResponse('Désolé, utilisateur, cette page est en cours de travaux et n\'est pas disponible pour le moment Merci de votre compréhention ')
	return wrapper_function

