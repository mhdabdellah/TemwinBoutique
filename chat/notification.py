from django.conf import settings
from .models import Message
class Notification(object):
    def __init__(self,request):
        self.session=request.session
        notification =self.session.get(settings.NOTIFICATION_SESSION_KEY)
        if not notification:
            notification=self.session[settings.NOTIFICATION_SESSION_KEY]={}
        self.notification=notification
    def add(self,message,receiver,sender,seen=False,number=0):
        message_id=str(message.id)
        if message_id not in self.notification: 
            self.notification[message_id]={
                'message':str(message.message),
                'receiver':str(receiver.id),
                'sender':str(sender.id),
                'number':number
            }
            if seen:
                self.notification[message_id]['number']=number
            else:
                self.notification[message_id]['number']+=int(number)

        self.save()
    def save(self):
        self.session.modified = True
    def remove(self,message):
        message_id = str(message.id)
        if message_id in self.notification:
            del self.notification[message_id]
            self.save()
    def __iter__(self):
        message_ids=self.notification.keys()
        messages=Message.objects.filter(id__in=message_ids)

        notification = self.notification.copy()
        for message in messages:
            notification[str(message.id)]['message']=message
        for item in notification.values():
            item['message']=str(item['message'])
            yield item
    def __len__(self):
        return sum(int(item['number']) for item in self.notification.values())
    def clear(self):
        del self.session[settings.NOTIFICATION_SESSION_KEY]
        self.save()
