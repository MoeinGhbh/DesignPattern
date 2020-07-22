from abc import ABC, abstractclassmethod


class Abstracthandler(ABC):
    def __init__(self, successor):
        self._successor = successor

    def handle(self, request):
        handled = self.process_request(request)
        if not handled:
            self._successor.handle(request)

    @abstractclassmethod
    def process_request(self, request):
        pass
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


class HandlerOne(Abstracthandler):
    def process_request(self, request):
        if 0 < request <= 10:
            print(f'handler one is processing the request... {request}')
            return True


class HandlerTwo(Abstracthandler):
    def process_request(self, request):
        if 10 < request <= 20:
            print(f'handler two is processing the request... {request}')
            return True


class DefaultHandler(Abstracthandler):
    def process_request(self, request):
        print(
            f'request does not have handler so process by the default handler... {request}')
        return True
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


class client:
    def __init__(self):
        self.handler = HandlerOne(HandlerTwo(DefaultHandler(None)))

    def delegate(self, requests):
        for request in requests:
            self.handler.handle(request)


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
x = [5, 15, 30]
c1 = client()
c1.delegate(x)
