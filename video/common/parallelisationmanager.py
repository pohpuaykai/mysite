import functools
import pickle
import json
import threading
import time

from foundation.models import Ticket
#import time#more for logging what time that thread happened

def parallelise(func):#this wrapper does nothing, only for ThreadingManager to collect parallelisable methods of the class wrapped byb ThreadingManager
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper 

class ThreadingManager:
    STRFORMAT = 'utf-8'

    current_ticket_number = -1
    pool = []
    ticketId__results = {} # write results to database so that people can come and collect
    ready_method_names_parameters = []
    #manages the maximum number of runnable_thread
    maximum_number_of_running_threads = None
    waitingPollingTimeInSeconds = None
    saveRequestInDatabase = None
    poolLock = threading.Lock()
    databaseLock = threading.Lock()

    def __init__(self, maximum_number_of_running_threads, waitingPollingTimeInSeconds, saveRequestInDatabase, storageType):
        # self.cls = cls
        ThreadingManager.maximum_number_of_running_threads = maximum_number_of_running_threads
        ThreadingManager.waitingPollingTimeInSeconds = waitingPollingTimeInSeconds
        ThreadingManager.saveRequestInDatabase = saveRequestInDatabase
        if storageType not in ['json', 'pickle']:
            raise Exception()
        ThreadingManager.storageType = storageType
        # self.pool = []
        # self.ticketId__results = {}
        

    def __call__(self, cls):
        self.cls = cls

        self.parallelisable_method_names = []
        self._collect_parallelisable_methods()
        # self.
        self.parallelisedCls = self._parallelise_methods(self.cls)
        self.parallelisedCls = self.giveMethodToWrapped(self.getReturnOfTicketNumber, 'getReturnOfTicketNumber') # beware of name collision!<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        self.parallelisedCls = self.giveMethodToWrapped(self.getReturnOfDatabaseTicket, 'getReturnOfDatabaseTicket') # beware of name collision!<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        
        print('parallelisable_method_names:', self.parallelisable_method_names)
        return self.parallelisedCls
        
    
    @classmethod
    def _get_ticket_number(cls):
        if ThreadingManager.saveRequestInDatabase:
            ticket = Ticket.objects.create(responseContent=None)
            ticketNumber = ticket.id
        else:
            cls.current_ticket_number += 1
            ticketNumber = cls.current_ticket_number
        # print('in Manager, ticket_number: ', cls.current_ticket_number)
        return ticketNumber

    def _collect_parallelisable_methods(self):
        for name in dir(self.cls):
            method = getattr(self.cls, name)
            if callable(method) and hasattr(method, '__wrapped__'):
                self.parallelisable_method_names.append(name)

    def _parallelise_methods(self, OGClass):
        """This method looks for methods that with a parallelise decorator and turns it into a thread that will be executed immediately
        
        gives a ticket for the user, to retrieve the results later
        """
        for name in dir(OGClass):
            if name in self.parallelisable_method_names:
                method = getattr(OGClass, name)
                # ticket_number = self._get_ticket_number()
                # def parallelisedMethod(*args, _method=method, _ticket_number=ticket_number, **kwargs):
                def parallelisedMethod(*args, _method=method, **kwargs):
                    # print('getting ticket')
                    _ticket_number = ThreadingManager._get_ticket_number()
                    # print('creating hookedMethod')
                    hookedMethod = ThreadingManager._create_hooked_method(_method, _ticket_number)
                    # print('appending ticket_number')
                    def attemptToAddToPool():
                        try:
                            ThreadingManager.poolLock.acquire()
                            #with
                            ThreadingManager.pool.append(_ticket_number)
                            if len(ThreadingManager.pool)-1 >= ThreadingManager.maximum_number_of_running_threads:
                                #what if 2 threads are here? not possible because of ThreadingManager.poolLock LongJohnSilver
                                ThreadingManager.pool.remove(_ticket_number)
                                ThreadingManager.poolLock.release()
                                # print('toomanyinpool, removed: ', ThreadingManager.pool, 'waiting ')
                                time.sleep(ThreadingManager.waitingPollingTimeInSeconds) # wait a second...
                                # print('woke, calling attemptToAddToPool')
                                attemptToAddToPool()
                            else:
                                print('starting thread')
                                threading.Thread(target=hookedMethod, args=args, kwargs=kwargs).start()
                            #
                            ThreadingManager.poolLock.release()
                        except:
                            if ThreadingManager.poolLock.locked():
                                ThreadingManager.poolLock.release()
                    attemptToAddToPool()
                    return _ticket_number
                # print('In manager, replaced method name: ', name)
                setattr(OGClass, name, parallelisedMethod) # replace the original method
        return OGClass


    @classmethod
    def _create_hooked_method(cls, method, ticket_number):
        def hooked_method(*args, **kwargs):
            print('running hooked_method')
            cls.ticketId__results[ticket_number] = method(*args, **kwargs)
            print('ran hooked_method')
            if ThreadingManager.saveRequestInDatabase:
                ticket = Ticket.objects.get(id=ticket_number)
                if ThreadingManager.storageType == 'pickle':
                    ticket.responseContent = pickle.dumps(cls.ticketId__results[ticket_number])
                elif ThreadingManager.storageType == 'json':
                    ticket.responseContent = json.dumps(cls.ticketId__results[ticket_number]).encode(ThreadingManager.STRFORMAT)
                ticket.save()
            cls.pool.remove(ticket_number)
            print('inhookedMethod, removed ticket_number', ticket_number, 'from pool: ', cls.pool)
        return hooked_method

    def giveMethodToWrapped(self, method, methodName):
        setattr(self.cls, methodName, method) # replace the original method
        return self.cls

    def getReturnOfTicketNumber(self, ticket_number):# a polling method, for user to get results
        if ticket_number in self.ticketId__results:
            result = self.ticketId__results.pop(ticket_number)
            return result #else(meaning that the thread has not completed yet) return None

    def getReturnOfDatabaseTicket(self, ticket_number):
        with ThreadingManager.databaseLock:
            try:
                ticket = Ticket.objects.get(id=str(ticket_number))
            except:
                return 
            if ticket.responseContent is None:
                return None
            if ThreadingManager.storageType == 'pickle':
                answer = pickle.loads(ticket.responseContent)
            elif ThreadingManager.storageType == 'json':
                answer = json.loads(ticket.responseContent.decode(ThreadingManager.STRFORMAT))
            ticket.delete()
        return answer
