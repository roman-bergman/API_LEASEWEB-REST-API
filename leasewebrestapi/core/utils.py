#  AUTHOR: Roman Bergman <roman.bergman@protonmail.com>
# RELEASE: 0.0.1
# LICENSE: AGPL3.0


import requests


class Utils():
    def httpGet(self, url, uri, query='', headers={}):
        try:
            req = requests.get('{}{}{}'.format(url, uri, query), headers=headers)
            return req
        except Exception as err:
            return err

    def httpPut(self, url, uri, query='', data={}, headers={}):
        try:
            req = requests.put('{}{}{}'.format(url, uri, query), json=data, headers=headers)
            return req
        except Exception as err:
            return err

    def httpPost(self, url, uri, data={}, headers={}):
        try:
            req = requests.post('{}{}'.format(url, uri), json=data, headers=headers)
            return req
        except Exception as err:
            return err

    def httpDelete(self, url, uri, headers={}):
        try:
            req = requests.delete('{}{}'.format(url, uri), headers=headers)
            return req
        except Exception as err:
            return err

    def query(self, query_params):
        if query_params:
            query = ''
            for elem in query_params:
                if query_params[elem]:
                    query += '&{}={}'.format(elem, query_params[elem])
            return query
        else:
            return ''

    def payload(self, payload_params):
        if payload_params:
            data = {}
            for elem in payload_params:
                if payload_params[elem]:
                    data.update({elem: payload_params[elem]})
            return data
        else:
            return {}

# INIT
utils = Utils()
