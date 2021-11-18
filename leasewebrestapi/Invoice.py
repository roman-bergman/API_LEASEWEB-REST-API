#  AUTHOR: Roman Bergman <roman.bergman@protonmail.com>
# RELEASE: 0.3.1
# LICENSE: AGPL3.0

from .core.utils import utils


class Invoice():
    def __init__(self, config: dict):
        self.config = config

    def list_invoices(self,
                      limit: int = 20,
                      offset: int = 0) -> dict:
        """
        This endpoint will return an overview of all the invoices for the customer.

        :param limit: Limit the number of results returned.
        :param offset: Return results starting from the given offset.
        :return: Standard HTTP status codes will be JSON.
        """
        headers = {'x-lsw-auth': self.config['API_KEY']}
        query_params = {
            'limit': limit,
            'offset': offset
        }
        out = utils.httpGet(self.config['API_URL'], '/invoices/v1/invoices?', query=utils.query(query_params), headers=headers)
        return out.json()

    def pro_forma(self,
                  limit: int = 20,
                  offset: int = 0) -> dict:
        """
        This endpoint will return an overview of contract items that will be invoiced as of the 1st of the upcoming month.

        :param limit: Limit the number of results returned.
        :param offset: Return results starting from the given offset.
        :return: Standard HTTP status codes will be JSON.
        """
        headers = {'x-lsw-auth': self.config['API_KEY']}
        query_params = {
            'limit': limit,
            'offset': offset
        }
        out = utils.httpGet(self.config['API_URL'], '/invoices/v1/invoices/proforma?', query=utils.query(query_params), headers=headers)
        return out.json()

    def inspect_invoice(self,
                        invoiceId: str) -> dict:
        """
        This endpoint will return a single invoice for the customer.

        :param invoiceId: Invoice Id.
        :return: Standard HTTP status codes will be JSON.
        """
        headers = {'x-lsw-auth': self.config['API_KEY']}
        out = utils.httpGet(self.config['API_URL'], '/invoices/v1/invoices/{}'.format(invoiceId), headers=headers)
        return out.json()
