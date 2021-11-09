#  AUTHOR: Roman Bergman <roman.bergman@protonmail.com>
# RELEASE: 0.1.12
# LICENSE: AGPL3.0


import json
import requests


class LeasewebRestAPI():
    def __init__(self, API_KEY=None):
        self.config = {
            'API_URL': 'https://api.leaseweb.com',
            'API_KEY': API_KEY
        }


class DedicatedServers(LeasewebRestAPI):
    def list_servers(self, limit=20, offset=0, ip=None, macAddress=None, site=None, privateRackId=None, privateNetworkCapable=None, privateNetworkEnabled=None):
        """
        List your Dedicated Servers.

        This api call supports pagination. Use the `limit` and `offset` query string parameters to paginate through all your dedicated servers.
        Every server object in the json response lists a few properties of a server. Use the single resouce api call to get more details for a single server.

        :param limit: int - Limit the number of results returned.
        :param offset: int - Return results starting from the given offset.
        :param ip: string - Filter the list of servers by ip address.
        :param macAddress: string - Filter the list of servers by mac address.
        :param site: string - Filter the list of servers by site (location).
        :param privateRackId: string - Filter the list of servers by private rack id.
        :param privateNetworkCapable: string - Filter the list for private network capable servers. Enum: "true" or "false".
        :param privateNetworkEnabled: string - Filter the list for private network enabled servers. Enum: "true" or "false".
        :return: Standard HTTP status codes will be JSON.
        """
        headers = {'x-lsw-auth': self.config['API_KEY']}
        query_params = {
            'limit': limit,
            'offset': offset,
            'ip': ip,
            'macAddress': macAddress,
            'site': site,
            'privateRackId': privateRackId,
            'privateNetworkCapable': privateNetworkCapable,
            'privateNetworkEnabled': privateNetworkEnabled
        }
        query_added = ''
        for elem in query_params:
            if query_params[elem]:
                query_added += '?{}={}'.format(elem, query_params[elem])
        out = httpGet(self.config['API_URL'], '/bareMetals/v2/servers', api_query=query_added, headers=headers)
        return out.json()

    def get_server(self, serverId):
        """
        Use this API to get information about a single server.

        :param serverId: - string - The ID of a server
        :return: Standard HTTP status codes will be JSON.
        """
        headers = {'x-lsw-auth': self.config['API_KEY']}
        out = httpGet(self.config['API_URL'], '/bareMetals/v2/servers/{}'.format(serverId), headers=headers)
        return out.json()

    def update_server(self, serverId, reference):
        """
        Update the reference for a server.

        :param serverId: - string - The ID of a server
        :param reference: - string - The reference for this server
        :return: Standard HTTP status codes will be JSON.
        """
        headers = {
            'x-lsw-auth': self.config['API_KEY'],
            'content-type': 'application/json'
        }
        data = {'reference': reference}
        out = httpPut(self.config['API_URL'], '/bareMetals/v2/servers/{}'.format(serverId), data=data, headers=headers)
        return True if out.status_code == 204 else out.json()

    def show_hardware_information(self, serverId):
        headers = {'x-lsw-auth': self.config['API_KEY']}
        out = httpGet(self.config['API_URL'], '/bareMetals/v2/servers/{}/hardwareInfo'.format(serverId), headers=headers)
        return out.json()

    def list_ips(self, serverId, networkType=None, version=None, nullRouted=None, ips=None, limit=20, offset=0):
        headers = {'x-lsw-auth': self.config['API_KEY']}
        query_params = {
            'networkType': networkType,
            'version': version,
            'nullRouted': nullRouted,
            'ips': ips,
            'limit': limit,
            'offset': offset
        }
        query_added = ''
        for elem in query_params:
            if query_params[elem]:
                query_added += '?{}={}'.format(elem, query_params[elem])
        out = httpGet(self.config['API_URL'], '/bareMetals/v2/servers/{}/ips'.format(serverId), api_query=query_added, headers=headers)
        return out.json()

    def show_an_ip(self, serverId, ip):
        headers = {'x-lsw-auth': self.config['API_KEY']}
        out = httpGet(self.config['API_URL'], '/bareMetals/v2/servers/{}/ips/{}'.format(serverId, ip), headers=headers)
        return out.json()

    def update_an_ip(self, serverId, ip, detectionProfile=None, reverseLookup=None):
        headers = {
            'x-lsw-auth': self.config['API_KEY'],
            'content-type': 'application/json'
        }
        _data = {
            'detectionProfile': detectionProfile,
            'reverseLookup': reverseLookup
        }
        data = {}
        for elem in _data:
            if data[elem]:
                data.update({elem: _data[elem]})

        out = httpPut(self.config['API_URL'], '/bareMetals/v2/servers/{}'.format(serverId), data=data, headers=headers)
        return True if out.status_code == 204 else out.json()

    def show_null_route_history(self, serverId, limit=20, offset=0):
        headers = {'x-lsw-auth': self.config['API_KEY']}
        query_params = {
            'limit': limit,
            'offset': offset
        }
        query_added = ''
        for elem in query_params:
            if query_params[elem]:
                query_added += '?{}={}'.format(elem, query_params[elem])
        out = httpGet(self.config['API_URL'], '/bareMetals/v2/servers/{}/nullRouteHistory'.format(serverId), api_query=query_added, headers=headers)
        return out.json()

    def list_network_interfaces(self, serverId):
        headers = {'x-lsw-auth': self.config['API_KEY']}
        out = httpGet(self.config['API_URL'], '/bareMetals/v2/servers/{}/networkInterfaces'.format(serverId), headers=headers)
        return out.json()

    def show_a_network_interface(self, serverId, networkType):
        headers = {'x-lsw-auth': self.config['API_KEY']}
        out = httpGet(self.config['API_URL'], '/bareMetals/v2/servers/{}/networkInterfaces/{}'.format(serverId, networkType), headers=headers)
        return out.json()

    def list_dhcp_reservation(self, serverId):
        headers = {'x-lsw-auth': self.config['API_KEY']}
        out = httpGet(self.config['API_URL'], '/bareMetals/v2/servers/{}/leases'.format(serverId), headers=headers)
        return out.json()

    def list_jobs(self, serverId):
        headers = {'x-lsw-auth': self.config['API_KEY']}
        out = httpGet(self.config['API_URL'], '/bareMetals/v2/servers/{}/jobs'.format(serverId), headers=headers)
        return out.json()

    def show_a_job(self, serverId, jobId):
        headers = {'x-lsw-auth': self.config['API_KEY']}
        out = httpGet(self.config['API_URL'], '/bareMetals/v2/servers/{}/jobs/{}'.format(serverId, jobId), headers=headers)
        return out.json()

    def list_credentials(self, serverId, limit=20, offset=0):
        headers = {'x-lsw-auth': self.config['API_KEY']}
        query_params = {
            'limit': limit,
            'offset': offset
        }
        query_added = ''
        for elem in query_params:
            if query_params[elem]:
                query_added += '&{}={}'.format(elem, query_params[elem])
        out = httpGet(self.config['API_URL'], '/bareMetals/v2/servers/{}/credentials?'.format(serverId), api_query=query_added, headers=headers)
        return out.json()

    def list_credentials_by_type(self, serverId, type, limit=20, offset=0):
        headers = {'x-lsw-auth': self.config['API_KEY']}
        query_params = {
            'limit': limit,
            'offset': offset
        }
        query_added = ''
        for elem in query_params:
            if query_params[elem]:
                query_added += '?{}={}'.format(elem, query_params[elem])
        out = httpGet(self.config['API_URL'], '/bareMetals/v2/servers/{}/credentials/{}'.format(serverId, type), api_query=query_added, headers=headers)
        return out.json()

    def show_user_credentials(self, serverId, type, username):
        headers = {'x-lsw-auth': self.config['API_KEY']}
        out = httpGet(self.config['API_URL'], '/bareMetals/v2/servers/{}/credentials/{}/{}'.format(serverId, type, username), headers=headers)
        return out.json()

    def show_bandwidth_metrics(self, serverId, date_from, date_to, granularity=None, aggregation='AVG'):
        headers = {'x-lsw-auth': self.config['API_KEY']}
        query_params = {
            'granularity': granularity,
            'aggregation': aggregation
        }
        query_added = ''
        for elem in query_params:
            if query_params[elem]:
                query_added += '&{}={}'.format(elem, query_params[elem])
        out = httpGet(self.config['API_URL'], '/bareMetals/v2/servers/{}/metrics/bandwidth?from={}&to={}'.format(serverId, date_from, date_to), api_query=query_added, headers=headers)
        return out.json()

    def show_datatraffic_metrics(self, serverId, date_from, date_to, granularity=None, aggregation='SUM'):
        headers = {'x-lsw-auth': self.config['API_KEY']}
        query_params = {
            'granularity': granularity,
            'aggregation': aggregation
        }
        query_added = ''
        for elem in query_params:
            if query_params[elem]:
                query_added += '&{}={}'.format(elem, query_params[elem])
        out = httpGet(self.config['API_URL'], '/bareMetals/v2/servers/{}/metrics/datatraffic?from={}&to={}'.format(serverId, date_from, date_to), api_query=query_added, headers=headers)
        return out.json()

    def list_bandwidth_notification_settings(self, serverId, limit=20, offset=0):
        headers = {'x-lsw-auth': self.config['API_KEY']}
        query_params = {
            'limit': limit,
            'offset': offset
        }
        query_added = ''
        for elem in query_params:
            if query_params[elem]:
                query_added += '&{}={}'.format(elem, query_params[elem])
        out = httpGet(self.config['API_URL'], '/bareMetals/v2/servers/{}/notificationSettings/bandwidth?'.format(serverId), api_query=query_added, headers=headers)
        return out.json()

    def show_a_bandwidth_notification_setting(self, serverId, notificationSettingId):
        headers = {'x-lsw-auth': self.config['API_KEY']}
        out = httpGet(self.config['API_URL'], '/bareMetals/v2/servers/{}/notificationSettings/bandwidth{}?'.format(serverId, notificationSettingId), headers=headers)
        return out.json()

    def list_datatraffic_notification_settings(self, serverId, limit=20, offset=0):
        headers = {'x-lsw-auth': self.config['API_KEY']}
        query_params = {
            'limit': limit,
            'offset': offset
        }
        query_added = ''
        for elem in query_params:
            if query_params[elem]:
                query_added += '&{}={}'.format(elem, query_params[elem])
        out = httpGet(self.config['API_URL'], '/bareMetals/v2/servers/{}/notificationSettings/datatraffic?'.format(serverId), api_query=query_added, headers=headers)
        return out.json()


    def show_a_datatraffic_notification_setting(self, serverId, notificationSettingId):
        headers = {'x-lsw-auth': self.config['API_KEY']}
        out = httpGet(self.config['API_URL'],
                      '/bareMetals/v2/servers/{}/notificationSettings/bandwidth{}?'.format(serverId, notificationSettingId), headers=headers)
        return out.json()

    def inspect_ddos_notification_settings(self, serverId):
        headers = {'x-lsw-auth': self.config['API_KEY']}
        out = httpGet(self.config['API_URL'], '/bareMetals/v2/servers/{}/notificationSettings/ddos'.format(serverId), headers=headers)
        return out.json()

    def show_power_status(self, serverId):
        headers = {'x-lsw-auth': self.config['API_KEY']}
        out = httpGet(self.config['API_URL'], '/bareMetals/v2/servers/{}/powerInfo'.format(serverId), headers=headers)
        return out.json()

    def list_operating_system(self, limit=20, offset=0, controlPanelId=None):
        headers = {'x-lsw-auth': self.config['API_KEY']}
        query_params = {
            'limit': limit,
            'offset': offset,
            'controlPanelId': controlPanelId
        }
        query_added = ''
        for elem in query_params:
            if query_params[elem]:
                query_added += '&{}={}'.format(elem, query_params[elem])
        out = httpGet(self.config['API_URL'], '/bareMetals/v2/operatingSystems?', api_query=query_added, headers=headers)
        return out.json()

    def show_an_operating_system(self, operatingSystemId, controlPanelId):
        headers = {'x-lsw-auth': self.config['API_KEY']}
        out = httpGet(self.config['API_URL'], '/bareMetals/v2/operatingSystems/{}?operatingSystemId={}'.format(operatingSystemId, controlPanelId), headers=headers)
        return out.json()

    def list_control_panels_an_os(self, operatingSystemId, limit=20, offset=0):
        headers = {'x-lsw-auth': self.config['API_KEY']}
        query_params = {
            'limit': limit,
            'offset': offset
        }
        query_added = ''
        for elem in query_params:
            if query_params[elem]:
                query_added += '&{}={}'.format(elem, query_params[elem])
        out = httpGet(self.config['API_URL'], '/bareMetals/v2/operatingSystems/{}/controlPanels?'.format(operatingSystemId), api_query=query_added, headers=headers)
        return out.json()

    def list_control_panels(self, limit=20, offset=0, operatingSystemId=None):
        headers = {'x-lsw-auth': self.config['API_KEY']}
        query_params = {
            'limit': limit,
            'offset': offset,
            'operatingSystemId': operatingSystemId
        }
        query_added = ''
        for elem in query_params:
            if query_params[elem]:
                query_added += '&{}={}'.format(elem, query_params[elem])
        out = httpGet(self.config['API_URL'], '/bareMetals/v2/controlPanels?'.format(operatingSystemId), api_query=query_added, headers=headers)
        return out.json()


    def rescue_images(self, limit=20, offset=0):
        headers = {'x-lsw-auth': self.config['API_KEY']}
        query_params = {
            'limit': limit,
            'offset': offset
        }
        query_added = ''
        for elem in query_params:
            if query_params[elem]:
                query_added += '&{}={}'.format(elem, query_params[elem])
        out = httpGet(self.config['API_URL'], '/bareMetals/v2/rescueImages?', api_query=query_added, headers=headers)
        return out.json()





def httpGet(api_url, api_uri, api_query='', headers={}):
    try:
        req = requests.get('{}{}{}'.format(api_url, api_uri, api_query), headers=headers)
        return req
    except Exception as err:
        return err


def httpPut(api_url, api_uri, api_query='', data={}, headers={}):
    try:
        req = requests.put('{}{}{}'.format(api_url, api_uri, api_query), json=data, headers=headers)
        return req
    except Exception as err:
        return err


if __name__ == '__main__':
    api = DedicatedServers()
    api.config['API_KEY'] = 'c51dd46f-265e-44a5-a864-8fad0618d617'
    print(api.update_server("103060", reference='OLOLO'))
