from __future__ import print_function

from pprint import pformat

from twisted.internet import reactor
from twisted.internet.defer import Deferred
from twisted.internet.protocol import Protocol
from twisted.web.client import Agent
from twisted.web.http_headers import Headers
from datetime import datetime 

class BeginningPrinter(Protocol):
    def __init__(self, finished):
        self.finished = finished
        self.remaining = 1024 * 10

    def dataReceived(self, bytes):
        if self.remaining:
            display = bytes[:self.remaining]
            print('Some data received:')
            print(display)
            self.remaining -= len(display)

    def connectionLost(self, reason):
        print('Finished receiving body:', reason.getErrorMessage())
        self.finished.callback(None)

agent = Agent(reactor)

currenttime = datetime.utcnow()
cutctm = str(currenttime)
print (cutctm)

# server 1 request
d = agent.request(
    'GET',
    'http://127.0.0.1:4000/checkcrime?lat=37.334164&longi=-121.884301&radius=0.02',
    Headers({'User-Agent': ['My Twisted client request #1'], 'Date':[cutctm]}),
    None)

# server 1 request
d2 = agent.request(
    'GET',
    'http://www.youtube.com',
    Headers({'User-Agent': ['My request #2'], 'Date':[cutctm]}),
    None)

# server 1 request
d3 = agent.request(
    'GET',
    'http://www.facebook.com',
    Headers({'User-Agent': ['My request #3'], 'Date':[cutctm]}),
    None)

def cbRequest(response):
    print('Response version:', response.version)
    print('Response code:', response.code)
    print('Response phrase:', response.phrase)
    print('Response headers:')
    print(pformat(list(response.headers.getAllRawHeaders())))
    finished = Deferred()
    response.deliverBody(BeginningPrinter(finished))
    return finished

d.addCallback(cbRequest)
d2.addCallback(cbRequest)
d3.addCallback(cbRequest) 

def cbShutdown(ignored):
    reactor.stop()

d.addBoth(cbShutdown)


reactor.run()