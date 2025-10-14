import functools
import threading
#import time#more for logging what time that thread happened

def parallelise(func):#this wrapper does nothing, only for ThreadingManager to collect parallelisable methods of the class wrapped byb ThreadingManager
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper 

class ThreadingManager:
    current_ticket_number = -1
    pool = []
    ticketId__results = {}

    def __init__(self, cls):
        self.cls = cls
        # self.pool = []
        # self.ticketId__results = {}
        
        self.parallelisable_method_names = []
        self._collect_parallelisable_methods()
        # self.
        print('parallelisable_method_names:', self.parallelisable_method_names)
        self.parallelisedCls = self._parallelise_methods(self.cls)
        
    def __call__(self, *args, **kwargs):
        instance = self.parallelisedCls(*args, **kwargs)
        return instance
    
    @classmethod
    def _get_ticket_number(cls):
        cls.current_ticket_number += 1
        print('in Manager, ticket_number: ', cls.current_ticket_number)
        return cls.current_ticket_number

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
                    print('getting ticket')
                    _ticket_number = ThreadingManager._get_ticket_number()
                    print('creating hookedMethod')
                    hookedMethod = ThreadingManager._create_hooked_method(_method, _ticket_number)
                    print('starting thread')
                    threading.Thread(target=hookedMethod, args=args, kwargs=kwargs).start()
                    print('appending ticket_number')
                    ThreadingManager.pool.append(_ticket_number)
                    print('pool: ', ThreadingManager.pool)
                    return _ticket_number
                print('In manager, replaced method name: ', name)
                setattr(OGClass, name, parallelisedMethod) # replace the original method
        return OGClass
    
    @classmethod
    def _create_hooked_method(cls, method, ticket_number):
        def hooked_method(*args, **kwargs):
            cls.ticketId__results[ticket_number] = method(*args, **kwargs)
            cls.pool.remove(ticket_number)
        return hooked_method
                
    def getReturnOfTicketNumber(self, ticket_number):# a polling method, for user to get results
        if ticket_number in self.ticketId__results:
            result = self.ticketId__results.pop(ticket_number)
            return result #else(meaning that the thread has not completed yet) return None