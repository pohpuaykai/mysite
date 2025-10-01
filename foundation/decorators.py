from functools import wraps
from json import loads
import threading

from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import redirect

from foundation.models import Ticket

def ticketable(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        dic = loads(request.body)
        # print('dic:<<<<<<<<<<<<<<<<<<<<')
        # print(dic)
        # print(dic); import pdb;pdb.set_trace()
        if dic.get('wantsTicket'):
            def runAndSave(request, ticketNum, args, kwargs):
                response = view_func(request, *args, **kwargs)
                print('runAndSave, ticketNum: ', ticketNum)
                ticket = Ticket.objects.get(id=ticketNum)
                ticket.responseContent=response.content
                ticket.save()
            # ticket = Ticket(responseContent=None)
            # ticket.save()
            ticket = Ticket.objects.create(responseContent=None)
            ticketNum = ticket.id
            thread = threading.Thread(target=runAndSave, args=(request, ticketNum, args, kwargs))
            thread.start()#thread might have started before ticket.save()<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            # print('returning ticketnumber: ', str(ticketNum)); import pdb;pdb.set_trace()
            return HttpResponse(str(ticket.id), content_type="text/plain")
        else:
            return view_func(request, *args, **kwargs)
    return wrapper
