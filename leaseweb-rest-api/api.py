#  AUTHOR: Roman Bergman <roman.bergman@protonmail.com>
# RELEASE: 0.5.0
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
    def list_servers(self,
                     limit: int = 20,
                     offset: int = 0,
                     ip: str = None,
                     macAddress: str = None,
                     site: str = None,
                     privateRackId: str = None,
                     privateNetworkCapable: str = None,
                     privateNetworkEnabled: str = None) -> dict:
        """
        List your Dedicated Servers.

        This api call supports pagination. Use the `limit` and `offset` query string parameters to paginate through all your dedicated servers.
        Every server object in the json response lists a few properties of a server. Use the single resource api call to get more details for a single server.

        :param limit: Limit the number of results returned.
        :param offset: Return results starting from the given offset.
        :param ip: Filter the list of servers by ip address.
        :param macAddress: Filter the list of servers by mac address.
        :param site: Filter the list of servers by site (location).
        :param privateRackId: Filter the list of servers by private rack id.
        :param privateNetworkCapable: Filter the list for private network capable servers. Enum: "true" or "false".
        :param privateNetworkEnabled: Filter the list for private network enabled servers. Enum: "true" or "false".
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

    def get_server(self,
                   serverId: str) -> dict:
        """
        Use this API to get information about a single server.

        :param serverId: The ID of a server.
        :return: Standard HTTP status codes will be JSON.
        """
        headers = {'x-lsw-auth': self.config['API_KEY']}
        out = httpGet(self.config['API_URL'], '/bareMetals/v2/servers/{}'.format(serverId), headers=headers)
        return out.json()

    def update_server(self,
                      serverId: str,
                      reference: str) -> dict:
        """
        Update the reference for a server.

        :param serverId: The ID of a server.
        :param reference: The reference for this server.
        :return: Standard HTTP status codes will be JSON.
        """
        headers = {
            'x-lsw-auth': self.config['API_KEY'],
            'content-type': 'application/json'
        }
        data = {'reference': reference}
        out = httpPut(self.config['API_URL'], '/bareMetals/v2/servers/{}'.format(serverId), data=data, headers=headers)
        return True if out.status_code == 204 else out.json()

    def show_hardware_information(self,
                                  serverId: str) -> dict:
        """
        This information is generated when running a hardware scan for your server. A hardware scan collects hardware information about your system.

        :param serverId: The ID of a server.
        :return: Standard HTTP status codes will be JSON.
        """
        headers = {'x-lsw-auth': self.config['API_KEY']}
        out = httpGet(self.config['API_URL'], '/bareMetals/v2/servers/{}/hardwareInfo'.format(serverId), headers=headers)
        return out.json()

    def list_ips(self,
                 serverId: str,
                 networkType: str = None,
                 version: str = None,
                 nullRouted: str = None,
                 ips: str = None,
                 limit: int = 20,
                 offset: int = 0) -> dict:

        """
        List all IP Addresses associated with this server. Optionally filtered.

        :param serverId: The ID of a server.
        :param networkType: Filter the collection of ip addresses by network type.
        :param version: Filter the collection by ip version.
        :param nullRouted: Filter Ips by Nulled-Status.
        :param ips: Filter the collection of Ips for the comma separated list of Ips.
        :param limit: Limit the number of results returned.
        :param offset: Return results starting from the given offset.
        :return: Standard HTTP status codes will be JSON.
        """
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

    def show_ip(self,
                   serverId: str,
                   ip: str) -> dict:
        """
        Get a single IP address associated with this server.

        :param serverId: The ID of a server.
        :param ip: The IP Address.
        :return: Standard HTTP status codes will be JSON.
        """
        headers = {'x-lsw-auth': self.config['API_KEY']}
        out = httpGet(self.config['API_URL'], '/bareMetals/v2/servers/{}/ips/{}'.format(serverId, ip), headers=headers)
        return out.json()

    def update_ip(self,
                     serverId: str,
                     ip: str,
                     detectionProfile: str = None,
                     reverseLookup: str = None) -> dict:
        """
        Update the reverse lookup or DDoS detection profile for the ip address.

        :param serverId: The ID of a server.
        :param ip: The IP Address.
        :param detectionProfile: The detection profile value.  Enum: "ADVANCED_DEFAULT" "ADVANCED_LOW_UDP" "ADVANCED_MED_UDP".
        :param reverseLookup: The reverse lookup value.
        :return: Standard HTTP status codes will be JSON.
        """
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
            if _data[elem]:
                data.update({elem: _data[elem]})

        out = httpPut(self.config['API_URL'], '/bareMetals/v2/servers/{}/ips/{}'.format(serverId, ip), data=data, headers=headers)
        return out.json()

    def null_route_ip(self,
                         serverId: str,
                         ip: str) -> dict:
        """
        Null the given IP address. It might take a few minutes before the change is propagated across the network.

        :param serverId: The ID of a server.
        :param ip: The IP Address.
        :return: Standard HTTP status codes will be JSON.
        """
        headers = {
            'x-lsw-auth': self.config['API_KEY']
        }
        out = httpPost(self.config['API_URL'], '/bareMetals/v2/servers/{}/ips/{}/null'.format(serverId, ip), headers=headers)
        return out.json()

    def remove_null_route_ip(self,
                         serverId: str,
                         ip: str) -> dict:
        """
        Remove an existing null route for the given IP address. It might take a few minutes before the change is propagated across the network.

        :param serverId: The ID of a server.
        :param ip: The IP Address.
        :return: Standard HTTP status codes will be JSON.
        """
        headers = {
            'x-lsw-auth': self.config['API_KEY']
        }
        out = httpPost(self.config['API_URL'], '/bareMetals/v2/servers/{}/ips/{}/unnull'.format(serverId, ip), headers=headers)
        return out.json()

    def show_null_route_history(self,
                                serverId: str,
                                limit: int = 20,
                                offset: int = 0) -> dict:
        """
        Show all null route history for any ips associated with this server.

        :param serverId: The ID of a server.
        :param limit: Limit the number of results returned.
        :param offset: Return results starting from the given offset.
        :return: Standard HTTP status codes will be JSON.
        """
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

    def list_network_interfaces(self,
                                serverId: str) -> dict:
        """
        List all network interfaces for this server, including their current status.

        :param serverId: The ID of a server.
        :return: Standard HTTP status codes will be JSON.
        """
        headers = {'x-lsw-auth': self.config['API_KEY']}
        out = httpGet(self.config['API_URL'], '/bareMetals/v2/servers/{}/networkInterfaces'.format(serverId), headers=headers)
        return out.json()

    def close_all_network_interfaces(self,
                                     serverId: str) -> bool:
        """
        Close all network interfaces for this server.

        :param serverId: The ID of a server.
        :return: Bool.
        """
        headers = {
            'x-lsw-auth': self.config['API_KEY']
        }
        out = httpPost(self.config['API_URL'], '/bareMetals/v2/servers/{}/networkInterfaces/close'.format(serverId), headers=headers)
        return True if out.status_code == 204 else False

    def open_all_network_interfaces(self,
                                    serverId: str) -> bool:
        """
        Open all network interfaces of this server.

        :param serverId: The ID of a server.
        :return: Bool.
        """
        headers = {
            'x-lsw-auth': self.config['API_KEY']
        }
        out = httpPost(self.config['API_URL'], '/bareMetals/v2/servers/{}/networkInterfaces/open'.format(serverId), headers=headers)
        return True if out.status_code == 204 else False

    def show_network_interface_by_type(self,
                                 serverId: str,
                                 networkType: str) -> dict:
        """
        List the network interfaces of the given type of this server, including their status.

        :param serverId: The ID of a server.
        :param networkType: The network type.  Enum: "public" "internal" "remoteManagement".
        :return: Standard HTTP status codes will be JSON.
        """
        headers = {'x-lsw-auth': self.config['API_KEY']}
        out = httpGet(self.config['API_URL'], '/bareMetals/v2/servers/{}/networkInterfaces/{}'.format(serverId, networkType), headers=headers)
        return out.json()

    def close_network_interface_by_type(self,
                                serverId: str,
                                networkType: str) -> bool:
        """
        Close all network interfaces of this server by types.

        :param serverId: The ID of a server.
        :param networkType: The network type.  Enum: "public" "internal" "remoteManagement".
        :return: Bool.
        """
        headers = {
            'x-lsw-auth': self.config['API_KEY']
        }
        out = httpPost(self.config['API_URL'], '/bareMetals/v2/servers/{}/networkInterfaces/{}/close'.format(serverId, networkType), headers=headers)
        return True if out.status_code == 204 else False

    def open_network_interface(self,
                                serverId: str,
                                networkType: str) -> bool:
        """
        Open all network interfaces of this server by types.

        :param serverId: The ID of a server.
        :param networkType: The network type.  Enum: "public" "internal" "remoteManagement".
        :return: Bool.
        """
        headers = {
            'x-lsw-auth': self.config['API_KEY']
        }
        out = httpPost(self.config['API_URL'], '/bareMetals/v2/servers/{}/networkInterfaces/{}/open'.format(serverId, networkType), headers=headers)
        return True if out.status_code == 204 else False

    def delete_server_from_private_network(self,
                                           serverId: str,
                                           privateNetworkId: str) -> dict:
        """
        This API call will remove the dedicated server from the private network.

        It takes a few minutes before the server has been removed from the private network.
        To get the current status of the server you can call get_server({serverId}).
        While the server is being removed the status changes to `REMOVING`.

        :param serverId: The ID of a server.
        :param privateNetworkId: The ID of a Private Network.
        :return: Standard HTTP status codes will be JSON.
        """
        headers = {
            'x-lsw-auth': self.config['API_KEY']
        }
        out = httpDelete(self.config['API_URL'], '/bareMetals/v2/servers/{}/privateNetworks/{}'.format(serverId, privateNetworkId), headers=headers)
        return True if out.status_code == 204 else out.json()

    def add_server_to_private_network(self,
                                      serverId: str,
                                      privateNetworkId: str,
                                      linkSpeed: int) -> dict:
        """
        It takes a few minutes before the server has access to the private network.

        To get the current status of the server you can call get_server({serverId}).
        Once the server is added to the private network the status changes from CONFIGURING to CONFIGURED.


        :param serverId: The ID of a server.
        :param privateNetworkId: The ID of a Private Network.
        :param linkSpeed: The port speed in Mbps.  Enum: "100", "1000", "10000".
        :return: Standard HTTP status codes will be JSON.
        """
        headers = {
            'x-lsw-auth': self.config['API_KEY'],
            'content-type': 'application/json'
        }
        _data = {
            'linkSpeed': linkSpeed
        }
        data = {}
        for elem in _data:
            if _data[elem]:
                data.update({elem: _data[elem]})
        out = httpPut(self.config['API_URL'], '/bareMetals/v2/servers/{}/privateNetworks/{}'.format(serverId, privateNetworkId), data=data, headers=headers)
        return True if out.status_code == 204 else out.json()

    def delete_dhcp_reservation(self,
                                serverId: str) -> bool:
        """
        Delete a DHCP reservation for this server.

        :param serverId: The ID of a server.
        :return: Bool.
        """
        headers = {
            'x-lsw-auth': self.config['API_KEY'],
        }
        out = httpDelete(self.config['API_URL'], '/bareMetals/v2/servers/{}/leases'.format(serverId), headers=headers)
        return True if out.status_code == 204 else False

    def list_dhcp_reservation(self,
                              serverId: str) -> dict:
        """
        Please note that this will only show reservations for the public network interface.

        :param serverId: The ID of a server.
        :return: Standard HTTP status codes will be JSON.
        """
        headers = {'x-lsw-auth': self.config['API_KEY']}
        out = httpGet(self.config['API_URL'], '/bareMetals/v2/servers/{}/leases'.format(serverId), headers=headers)
        return out.json()

    def create_dhcp_reservation(self,
                                serverId: str,
                                bootfile: str,
                                hostname: str) -> dict:
        """
        After rebooting your server it will acquire this DHCP reservation and boot from the specified bootfile url.

        Please note that this API call will not reboot or power cycle your server.

        :param serverId: The ID of a server.
        :param bootfile: The URL of PXE boot you want your server to boot from. bootfile: http://example.com/bootme.ipxe
        :param hostname: The hostname for the server.
        :return: Standard HTTP status codes will be JSON.
        """
        headers = {
            'x-lsw-auth': self.config['API_KEY'],
            'content-type': 'application/json'
        }
        _data = {
            'bootfile': bootfile,
            'hostname': hostname
        }
        data = {}
        for elem in _data:
            if _data[elem]:
                data.update({elem: _data[elem]})
        out = httpPost(self.config['API_URL'], '/bareMetals/v2/servers/{}/leases'.format(serverId), data=data, headers=headers)
        return True if out.status_code == 204 else out.json()

    def cancel_active_job(self,
                          serverId: str) -> dict:
        """
        Canceling an active job will trigger the onfail flow of the current job often resulting in a server reboot. If you do not want the server state to change expire the active job instead.

        :param serverId: The ID of a server.
        :return: Standard HTTP status codes will be JSON.
        """
        headers = {'x-lsw-auth': self.config['API_KEY']}
        out = httpPost(self.config['API_URL'], '/bareMetals/v2/servers/{}/cancelActiveJob'.format(serverId), headers=headers)
        return out.json()

    def expire_active_job(self,
                          serverId: str) -> dict:
        """
        Expiring an active job will not have any influence on the current state of the server and is merely an administrative action.

        Often you want to cancel the job, resulting in a server reboot. In that case\nuse the /cancelActiveJob API call instead.

        :param serverId: The ID of a server.
        :return: Standard HTTP status codes will be JSON.
        """
        headers = {'x-lsw-auth': self.config['API_KEY']}
        out = httpPost(self.config['API_URL'], '/bareMetals/v2/servers/{}/expireActiveJob'.format(serverId), headers=headers)
        return out.json()

    def launch_hardware_scan(self,
                            serverId: str,
                            callbackUrl: str = None,
                            powerCycle: bool = True) -> dict:
        """
        A hardware scan collects hardware related information from your server.

        A hardware scan will require a reboot of your server. The contents of your hard drive won't be altered in any way. After a successful hardware scan your server is booted back into the original operating system.

        :param serverId: The ID of a server.
        :param callbackUrl: Url which will receive callbacks.
        :param powerCycle: If set to true, server will be power cycled in order to complete the operation.
        :return: Standard HTTP status codes will be JSON.
        """
        headers = {
            'x-lsw-auth': self.config['API_KEY'],
            'content-type': 'application/json'
        }
        data_payload = {
            'callbackUrl': callbackUrl,
            'powerCycle': powerCycle
        }
        data = {}
        for elem in data_payload:
            if data_payload[elem]:
                data.update({elem: data_payload[elem]})
        out = httpPost(self.config['API_URL'], '/bareMetals/v2/servers/{}/hardwareScan'.format(serverId), data=data, headers=headers)
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

    def rescue_images(self,
                      limit: int = 20,
                      offset: int = 0) -> dict:
        """
        Lists all Rescue Images which are available for launching a dedicated server into rescue mode.

        :param limit: Limit the number of results returned.
        :param offset: Return results starting from the given offset.
        :return: Standard HTTP status codes will be JSON.
        """
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


def httpPost(api_url, api_uri, data={}, headers={}):
    try:
        req = requests.post('{}{}'.format(api_url, api_uri), data=data, headers=headers)
        return req
    except Exception as err:
        return err


def httpDelete(api_url, api_uri, headers={}):
    try:
        req = requests.delete('{}{}'.format(api_url, api_uri), headers=headers)
        return req
    except Exception as err:
        return err