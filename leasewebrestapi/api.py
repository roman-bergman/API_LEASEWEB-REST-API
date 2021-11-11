#  AUTHOR: Roman Bergman <roman.bergman@protonmail.com>
# RELEASE: 0.6.0
# LICENSE: AGPL3.0


from .Invoice import Invoice
from .DedicatedServers import DedicatedServers


class API():
    def __init__(self, API_KEY=None):
        self.config = {
            'API_URL': 'https://api.leaseweb.com',
            'API_KEY': API_KEY
        }
        self.DedicatedServers = DedicatedServers(self.config)
        self.Invoice = Invoice(self.config)
