from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.humanize.templatetags.humanize import naturaltime
from .notification import Notification
from django.contrib.auth.models import User
from accounts.models import Profile
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
# from stock.models import *
from .models import Message
from django.db.models import Q
import json
from django.urls import reverse

def index(request):
    return render(request, 'chat/index.html')
@login_required(login_url='accounts/login.html')
def room(request):
    # other_user= get_object_or_404(User,pk=pk)
    manangers=Profile.objects.filter(manager=request.user.id)
    # last=Message.objects.filter(sender=other_user).last()
    last=[]
    for manage in manangers:

        message=Message.objects.filter(Q(sender  =manage.user , receiver=request.user)|Q(sender  =request.user , receiver=manage.user)).last()
        # print(message)
        if message:
         last.append(message)
    
    for m in last:
        print(m.message)
    if request.user.is_superuser==True:
     manangers=Profile.objects.filter(manager=request.user.id)
    else:
        if request.user.is_staff==True:
            manager=Profile.objects.get(user=request.user)
            manangers=Profile.objects.get(user=manager.manager)
        else:
            manangers= None
    # messages= Message.objects.filter(Q(receiver=other_user,sender=request.user)) | Q(receiver=request.user,sender=other_user)
    # messages.update(seen=True)
    # print(manangers)
    return render(request, 'chat/room.html', {
       'manangers': manangers,'other_user': 'other_user','last': last,
    })
@login_required(login_url='accounts/login.html')
def room_message(request,pk):

    other_user= get_object_or_404(User,pk=pk)
    manangers=Profile.objects.all()
    last=[]
    for manage in manangers:

        message=Message.objects.filter(Q(sender  =manage.user , receiver=request.user)|Q(sender  =request.user , receiver=manage.user)).last()
        # print(message)
        if message:
         last.append(message)
    
    for m in last:
        print(m.message)
    if request.user.is_superuser==True:
     manangers=Profile.objects.filter(manager=request.user.id)
    else:
        if request.user.is_staff==True:
            manager=Profile.objects.get(user=request.user)
            manangers=Profile.objects.get(user=manager.manager)
        else:
            manangers= None
    messages= Message.objects.filter(
        Q(receiver=other_user,sender=request.user) | Q(receiver=request.user,sender=other_user)
        )
    messages.update(seen=True)
    
    
    return render(request, 'chat/room_message.html', {
       'other_user': other_user,'messages': messages,'manangers':manangers,'last':last
    })
@login_required(login_url='accounts/login.html')
@login_required
def ajax_load_messages(request, pk):
    other_user = get_object_or_404(User, pk=pk)
    messages = Message.objects.filter(Q(seen=False, receiver=request.user))
    # notify=Message.objects.filter(seen=False| Q(receiver=other_user,sender=request.user) | Q(receiver=request.user,sender=other_user)).count()
    # notification=Message.objects.filter(Q(receiver=other_user,seen=False)).count(
    # print("messages")
    
    notification = Notification(request)
    for item in notification:
        print (item)
    # article_num=request.POST.get('numero')
    # article=get_object_or_404(Article,numero=article_num)
    # cart.add(article=article,quantity=cd['quantity'],override_quantity=cd['override'])
   
    message_list = [{
        "sender": message.sender.username,
        "message": message.message,
        "sent": message.sender == request.user,
        # "picture": other_user.profile.picture.url,
        'notification': messages.count(),
        "date_created": naturaltime(message.date_created),

    } for message in messages]
    print(message_list)
    messages.update(seen=True)
    
    # print(notification)
    if request.method == "POST":
        message = json.loads(request.body)
        # print (message)
        m = Message.objects.create(receiver=other_user, sender=request.user, message=message)
        notification = Notification(request)
        message_id=m.id
        message=get_object_or_404(Message,id=message_id)
        notification.add(message=message,receiver=other_user,sender=request.user,seen=False,number=1)
        message_list.append({
            "sender": request.user.username,
            "username": request.user.username,
            "message": m.message,
            "date_created": naturaltime(m.date_created),
            # "picture": other_user.profile.picture.url,
            'notification': 0,
            "sent": True,
        })
        # print (notification)
        # message_list[4]=notification
    # print(JsonResponse(message_list, safe=False))
    return JsonResponse(message_list, safe=False)
