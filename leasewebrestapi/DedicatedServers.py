#  AUTHOR: Roman Bergman <roman.bergman@protonmail.com>
# RELEASE: 0.5.4
# LICENSE: AGPL3.0

from .core.utils import utils


class DedicatedServers():
    def __init__(self, config: dict):
        self.config = config

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
        out = utils.httpGet(self.config['API_URL'], '/bareMetals/v2/servers?', query=utils.query(query_params), headers=headers)
        return out.json()

    def get_server(self,
                   serverId: str) -> dict:
        """
        Use this API to get information about a single server.

        :param serverId: The ID of a server.
        :return: Standard HTTP status codes will be JSON.
        """
        headers = {'x-lsw-auth': self.config['API_KEY']}
        out = utils.httpGet(self.config['API_URL'], '/bareMetals/v2/servers/{}'.format(serverId), headers=headers)
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
        payload_params = {'reference': reference}
        out = utils.httpPut(self.config['API_URL'], '/bareMetals/v2/servers/{}'.format(serverId), data=utils.payload(payload_params), headers=headers)
        return True if out.status_code == 204 else out.json()

    def show_hardware_information(self,
                                  serverId: str) -> dict:
        """
        This information is generated when running a hardware scan for your server. A hardware scan collects hardware information about your system.

        :param serverId: The ID of a server.
        :return: Standard HTTP status codes will be JSON.
        """
        headers = {'x-lsw-auth': self.config['API_KEY']}
        out = utils.httpGet(self.config['API_URL'], '/bareMetals/v2/servers/{}/hardwareInfo'.format(serverId), headers=headers)
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
        out = utils.httpGet(self.config['API_URL'], '/bareMetals/v2/servers/{}/ips?'.format(serverId), query=utils.query(query_params), headers=headers)
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
        out = utils.httpGet(self.config['API_URL'], '/bareMetals/v2/servers/{}/ips/{}'.format(serverId, ip), headers=headers)
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
        payload_params = {
            'detectionProfile': detectionProfile,
            'reverseLookup': reverseLookup
        }
        out = utils.httpPut(self.config['API_URL'], '/bareMetals/v2/servers/{}/ips/{}'.format(serverId, ip), data=utils.payload(payload_params), headers=headers)
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
        headers = {'x-lsw-auth': self.config['API_KEY']}
        out = utils.httpPost(self.config['API_URL'], '/bareMetals/v2/servers/{}/ips/{}/null'.format(serverId, ip), headers=headers)
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
        headers = {'x-lsw-auth': self.config['API_KEY']}
        out = utils.httpPost(self.config['API_URL'], '/bareMetals/v2/servers/{}/ips/{}/unnull'.format(serverId, ip), headers=headers)
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
        out = utils.httpGet(self.config['API_URL'], '/bareMetals/v2/servers/{}/nullRouteHistory?'.format(serverId), query=utils.query(query_params), headers=headers)
        return out.json()

    def list_network_interfaces(self,
                                serverId: str) -> dict:
        """
        List all network interfaces for this server, including their current status.

        :param serverId: The ID of a server.
        :return: Standard HTTP status codes will be JSON.
        """
        headers = {'x-lsw-auth': self.config['API_KEY']}
        out = utils.httpGet(self.config['API_URL'], '/bareMetals/v2/servers/{}/networkInterfaces'.format(serverId), headers=headers)
        return out.json()

    def close_all_network_interfaces(self,
                                     serverId: str) -> bool:
        """
        Close all network interfaces for this server.

        :param serverId: The ID of a server.
        :return: Bool.
        """
        headers = {'x-lsw-auth': self.config['API_KEY']}
        out = utils.httpPost(self.config['API_URL'], '/bareMetals/v2/servers/{}/networkInterfaces/close'.format(serverId), headers=headers)
        return True if out.status_code == 204 else False

    def open_all_network_interfaces(self,
                                    serverId: str) -> bool:
        """
        Open all network interfaces of this server.

        :param serverId: The ID of a server.
        :return: Bool.
        """
        headers = {'x-lsw-auth': self.config['API_KEY']}
        out = utils.httpPost(self.config['API_URL'], '/bareMetals/v2/servers/{}/networkInterfaces/open'.format(serverId), headers=headers)
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
        out = utils.httpGet(self.config['API_URL'], '/bareMetals/v2/servers/{}/networkInterfaces/{}'.format(serverId, networkType), headers=headers)
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
        headers = {'x-lsw-auth': self.config['API_KEY']}
        out = utils.httpPost(self.config['API_URL'], '/bareMetals/v2/servers/{}/networkInterfaces/{}/close'.format(serverId, networkType), headers=headers)
        return True if out.status_code == 204 else False

    def open_network_interface_by_type(self,
                                       serverId: str,
                                       networkType: str) -> bool:
        """
        Open all network interfaces of this server by types.

        :param serverId: The ID of a server.
        :param networkType: The network type.  Enum: "public" "internal" "remoteManagement".
        :return: Bool.
        """
        headers = {'x-lsw-auth': self.config['API_KEY']}
        out = utils.httpPost(self.config['API_URL'], '/bareMetals/v2/servers/{}/networkInterfaces/{}/open'.format(serverId, networkType), headers=headers)
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
        headers = {'x-lsw-auth': self.config['API_KEY']}
        out = utils.httpDelete(self.config['API_URL'], '/bareMetals/v2/servers/{}/privateNetworks/{}'.format(serverId, privateNetworkId), headers=headers)
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
        payload_params = {
            'linkSpeed': linkSpeed
        }
        out = utils.httpPut(self.config['API_URL'], '/bareMetals/v2/servers/{}/privateNetworks/{}'.format(serverId, privateNetworkId), data=utils.payload(payload_params), headers=headers)
        return True if out.status_code == 204 else out.json()

    def delete_dhcp_reservation(self,
                                serverId: str) -> bool:
        """
        Delete a DHCP reservation for this server.

        :param serverId: The ID of a server.
        :return: Bool.
        """
        headers = {'x-lsw-auth': self.config['API_KEY']}
        out = utils.httpDelete(self.config['API_URL'], '/bareMetals/v2/servers/{}/leases'.format(serverId), headers=headers)
        return True if out.status_code == 204 else False

    def list_dhcp_reservation(self,
                              serverId: str) -> dict:
        """
        Please note that this will only show reservations for the public network interface.

        :param serverId: The ID of a server.
        :return: Standard HTTP status codes will be JSON.
        """
        headers = {'x-lsw-auth': self.config['API_KEY']}
        out = utils.httpGet(self.config['API_URL'], '/bareMetals/v2/servers/{}/leases'.format(serverId), headers=headers)
        return out.json()

    def create_dhcp_reservation(self,
                                serverId: str,
                                bootfile: str,
                                hostname: str = None) -> dict:
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
        data_params = {
            'bootfile': bootfile,
            'hostname': hostname
        }
        out = utils.httpPost(self.config['API_URL'], '/bareMetals/v2/servers/{}/leases'.format(serverId), data=utils.payload(data_params), headers=headers)
        return True if out.status_code == 204 else out.json()

    def cancel_active_job(self,
                          serverId: str) -> dict:
        """
        Canceling an active job will trigger the onfail flow of the current job often resulting in a server reboot. If you do not want the server state to change expire the active job instead.

        :param serverId: The ID of a server.
        :return: Standard HTTP status codes will be JSON.
        """
        headers = {'x-lsw-auth': self.config['API_KEY']}
        out = utils.httpPost(self.config['API_URL'], '/bareMetals/v2/servers/{}/cancelActiveJob'.format(serverId), headers=headers)
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
        out = utils.httpPost(self.config['API_URL'], '/bareMetals/v2/servers/{}/expireActiveJob'.format(serverId), headers=headers)
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
        data_params = {
            'callbackUrl': callbackUrl,
            'powerCycle': powerCycle
        }
        out = utils.httpPost(self.config['API_URL'], '/bareMetals/v2/servers/{}/hardwareScan'.format(serverId), data=utils.payload(data_params), headers=headers)
        return out.json()

    def launch_installation(self,
                            serverId: str,
                            operatingSystemId: str,
                            callbackUrl: str = None,
                            controlPanelId: str = None,
                            device: str = None,
                            hostname: str = None,
                            partitions: list = None,
                            password: str = None,
                            postInstallScript: str = None,
                            powerCycle: bool = False,
                            raid: str = None,
                            sshKeys: str = None,
                            timezone: str = None) -> dict:
        """
        Install your server with an Operating System and optional Control Panel.

        To retrieve a list of available operating systems use the /v2/operatingSystems endpoint.
        To retrieve a list of available control panels use the /v2/controlPanels endpoint.
        The default device / partitions to be used are operating system depended and can be retrieved via the /v2/operatingSystems/{operatingSystemId} endpoint.
        For more information about Dedicated Server installation, click here for our related Knowledge Base article.

        :param serverId: The ID of a server.
        :param operatingSystemId: Operating system identifier.
        :param callbackUrl: Url which will receive callbacks when the installation is finished or failed.
        :param controlPanelId: Control panel identifier.
        :param device: Block device in which the partitions would be installed.  Enum: "SATA_SAS" "NVME".
        :param hostname: Hostname to be used in your installation.
        :param partitions: Array of partition objects that should be installed per partition.
        :param password: Server root password. If not provided, it would be automatically generated.
        :param postInstallScript: Base64 Encoded string containing a valid bash script to be run right after the installation.
        :param powerCycle: If true, allows system reboots to happen automatically within the process. Otherwise, you should do them manually.
        :param raid: Contains RAID related information about the installation request.
        :param sshKeys: List of public sshKeys to be setup in your installation, separated by new lines.
        :param timezone: Timezone represented as Geographical_Area/City.
        :return: Standard HTTP status codes will be JSON.
        """
        headers = {
            'x-lsw-auth': self.config['API_KEY'],
            'content-type': 'application/json'
        }
        data_params = {
            "operatingSystemId": operatingSystemId,
            "callbackUrl": callbackUrl,
            "controlPanelId": controlPanelId,
            "device": device,
            "hostname": hostname,
            "partitions": partitions,
            "password": password,
            "postInstallScript": postInstallScript,
            "powerCycle": powerCycle,
            "raid": raid,
            "sshKeys": sshKeys,
            "timezone": timezone
        }
        out = utils.httpPost(self.config['API_URL'], '/bareMetals/v2/servers/{}/install'.format(serverId), data=utils.payload(data_params), headers=headers)
        return out.json()

    def launch_ipmi_reset(self,
                          serverId: str,
                          callbackUrl: str = None,
                          powerCycle: bool = True) -> dict:
        """
        A reset makes sure that your IPMI interface of your server is compatible with Leaseweb automation.

        An IPMI reset will require a reboot of your server. The contents of your hard drive won't be altered in any way. After a successful IPMI reset your server is booted back into the original operating system.",

        :param serverId: The ID of a server.
        :param callbackUrl: Url which will receive callbacks.
        :param powerCycle: If set to true, server will be power cycled in order to complete the operation.
        :return: Standard HTTP status codes will be JSON.
        """
        headers = {
            'x-lsw-auth': self.config['API_KEY'],
            'content-type': 'application/json'
        }
        data_params = {
            "callbackUrl": callbackUrl,
            "powerCycle": powerCycle
        }
        out = utils.httpPost(self.config['API_URL'], '/bareMetals/v2/servers/{}/ipmiReset'.format(serverId), data=utils.payload(data_params), headers=headers)
        return out.json()

    def list_jobs(self,
                  serverId: str) -> dict:
        """
        List all jobs for this server.

        :param serverId: The ID of a server.
        :return: Standard HTTP status codes will be JSON.
        """
        headers = {'x-lsw-auth': self.config['API_KEY']}
        out = utils.httpGet(self.config['API_URL'], '/bareMetals/v2/servers/{}/jobs'.format(serverId), headers=headers)
        return out.json()

    def show_job(self,
                 serverId: str,
                 jobId: str) -> dict:
        """
        Get a single job for this server.

        :param serverId: The ID of a server.
        :param jobId: The ID of a Job.
        :return: Standard HTTP status codes will be JSON.
        """
        headers = {'x-lsw-auth': self.config['API_KEY']}
        out = utils.httpGet(self.config['API_URL'], '/bareMetals/v2/servers/{}/jobs/{}'.format(serverId, jobId), headers=headers)
        return out.json()

    def launch_resque_mode(self,
                           serverId: str,
                           rescueImageId: str,
                           callbackUrl: str =None,
                           password: str = None,
                           postInstallScript: str = None,
                           powerCycle: bool = True,
                           sshKeys: str = None) -> dict:
        """
        Rescue mode allows you to trouble shoot your server in case your installed operating system is no longer reachable.

        You can supply a postInstallScript key in the body of the request which should contain a base64 encoded string with a valid script. This script will be executed as soon as rescue mode is launched and can be used to further automate the process. A requirement for the post install script is that it starts with a shebang line like #!/usr/bin/env bash.
        After a rescue mode is launched you can manually reboot the server. After this reboot the server will boot into the existing operating system.
        To get a list of available rescue images, you could do so by sending a GET request to /bareMetals/v2/rescueImages.

        :param serverId: The ID of a server.
        :param rescueImageId: Rescue image identifier.
        :param callbackUrl: Url which will receive callbacks.
        :param password: Rescue mode password. If not provided, it would be automatically generated.
        :param postInstallScript: Base64 Encoded string containing a valid bash script to be run right after rescue mode is launched.
        :param powerCycle: If set to true, server will be power cycled in order to complete the operation.
        :param sshKeys: User ssh keys.
        :return: Standard HTTP status codes will be JSON.
        """
        headers = {
            'x-lsw-auth': self.config['API_KEY'],
            'content-type': 'application/json'
        }
        data_params = {
            "rescueImageId": rescueImageId,
            "callbackUrl": callbackUrl,
            "password": password,
            "postInstallScript": postInstallScript,
            "powerCycle": powerCycle,
            "sshKeys": sshKeys
        }
        out = utils.httpPost(self.config['API_URL'], '/bareMetals/v2/servers/12345/rescueMode'.format(serverId), data=utils.payload(data_params), headers=headers)
        return out.json()

    def list_credentials(self,
                         serverId: str,
                         limit: int = 20,
                         offset: int = 0) -> dict:
        """
        The credentials API allows you to store usernames and passwords securely.

        During (re)installations, rescue modes and ipmi resets the newly generated passwords are stored and can be retrieved using this API.

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
        out = utils.httpGet(self.config['API_URL'], '/bareMetals/v2/servers/{}/credentials?'.format(serverId), query=utils.query(query_params), headers=headers)
        return out.json()

    def create_credentials(self,
                           serverId: str,
                           password: str,
                           type: str,
                           username: str) -> dict:
        """
        Password will NOT be updated on the server. The ability to update credentials is for convenience only. It provides a secure way to communicate passwords with Leaseweb engineers in case support is required.

        :param serverId: The ID of a server.
        :param password: The password for the credentials.
        :param type: The type of the credential.  Enum: "OPERATING_SYSTEM" "CONTROL_PANEL" "REMOTE_MANAGEMENT" "RESCUE_MODE" "SWITCH" "PDU" "FIREWALL" "LOAD_BALANCER".
        :param username: The username for the credentials.
        :return: Standard HTTP status codes will be JSON.
        """
        headers = {
            'x-lsw-auth': self.config['API_KEY'],
            'content-type': 'application/json'
        }
        data_params = {
            "password": password,
            "type": type,
            "username": username
        }
        out = utils.httpPost(self.config['API_URL'], '/bareMetals/v2/servers/{}/credentials'.format(serverId), data=utils.payload(data_params), headers=headers)
        return out.json()

    def list_credentials_by_type(self,
                                 serverId: str,
                                 type: str,
                                 limit: int = 20,
                                 offset: int = 0) -> dict:
        """
        List all the credentials filtered by the specified type that are associated with this server.

        :param serverId: The ID of a server.
        :param type: Credential type.
        :param limit: Limit the number of results returned.
        :param offset: Return results starting from the given offset.
        :return: Standard HTTP status codes will be JSON.
        """
        headers = {'x-lsw-auth': self.config['API_KEY']}
        query_params = {
            'limit': limit,
            'offset': offset
        }
        out = utils.httpGet(self.config['API_URL'], '/bareMetals/v2/servers/{}/credentials/{}?'.format(serverId, type), query=utils.query(query_params), headers=headers)
        return out.json()

    def delete_user_credentials(self,
                                serverId: str,
                                type: str,
                                username: str) -> bool:
        """
        This action is purely administrative and will only remove the username and password associated with this resource from our database.

        :param serverId: The ID of a server.
        :param type: Credential type.
        :param username: Username.
        :return: Bool.
        """
        headers = {'x-lsw-auth': self.config['API_KEY']}
        out = utils.httpDelete(self.config['API_URL'], '/bareMetals/v2/servers/{}/credentials/{}/{}'.format(serverId, type, username), headers=headers)
        return True if out.status_code == 204 else False

    def show_user_credentials(self,
                              serverId: str,
                              type: str,
                              username: str) -> dict:
        """
        View the password for the given credential, identified by type and username. Auto generated credentials (during a re-install, rescue mode or ipmi reset can be found here).

        :param serverId: The ID of a server.
        :param type: Credential type.
        :param username: Username.
        :return: Standard HTTP status codes will be JSON.
        """
        headers = {'x-lsw-auth': self.config['API_KEY']}
        out = utils.httpGet(self.config['API_URL'], '/bareMetals/v2/servers/{}/credentials/{}/{}'.format(serverId, type, username), headers=headers)
        return out.json()

    def update_user_credentials(self,
                                serverId: str,
                                type: str,
                                username: str,
                                password: str) -> dict:
        """
        The usernames or types cannot be changed. In order to change those remove this credentials and create a new one.

        This action is purely administrative and will only update the password associated with this resource in our database.

        :param serverId: The ID of a server.
        :param type: Credential type.
        :param username: Username.
        :param password: The password for the credentials.
        :return: Standard HTTP status codes will be JSON.
        """
        headers = {
            'x-lsw-auth': self.config['API_KEY'],
            'content-type': 'application/json'
        }
        data_params = {
            "password": password
        }
        out = utils.httpPut(self.config['API_URL'], '/bareMetals/v2/servers/{}/credentials/{}/{}'.format(serverId, type, username), query=utils.query(data_params), headers=headers)
        return out.json()

    def show_bandwidth_metrics(self,
                               serverId: str,
                               date_from: str,
                               date_to: str,
                               aggregation: str = 'AVG',
                               granularity: str = None) -> dict:
        """
        At this moment only bandwidth information for the public interface is supported.

        :param serverId: The ID of a server.
        :param date_from: Start of date interval in ISO-8601 format. The returned data will include everything up from - and including - the specified date time. Example: from=2019-06-01T00:00:00Z
        :param date_to: End of date interval in ISO-8601 format. The returned data will include everything up until - but not including - the specified date time. Example: to=2019-06-05T00:00:00Z
        :param aggregation: Aggregate each metric using the given aggregation function. When the aggregation type 95TH is specified the granularity parameter should be omitted from the request.  Enum: "AVG" "95TH"
        :param granularity: Specify the preferred interval for each metric. If granularity is omitted from the request, only one metric is returned.  Enum: "5MIN" "HOUR" "DAY" "WEEK" "MONTH" "YEAR"
        :return: Standard HTTP status codes will be JSON.
        """
        headers = {'x-lsw-auth': self.config['API_KEY']}
        query_params = {
            'granularity': granularity,
            'aggregation': aggregation
        }
        out = utils.httpGet(self.config['API_URL'], '/bareMetals/v2/servers/{}/metrics/bandwidth?from={}&to={}'.format(serverId, date_from, date_to), query=utils.query(query_params), headers=headers)
        return out.json()

    def show_datatraffic_metrics(self,
                                 serverId: str,
                                 date_from: str,
                                 date_to: str,
                                 aggregation: str = 'SUM',
                                 granularity: str = None) -> dict:
        """
        At this moment only bandwidth information for the public interface is supported.

        :param serverId: The ID of a server.
        :param date_from: Start of date interval in ISO-8601 format. The returned data will include everything up from - and including - the specified date time. Example: from=2019-06-01T00:00:00Z
        :param date_to: End of date interval in ISO-8601 format. The returned data will include everything up until - but not including - the specified date time. Example: to=2019-06-05T00:00:00Z
        :param aggregation: Aggregate each metric using the given aggregation function. When the aggregation type 95TH is specified the granularity parameter should be omitted from the request.  Enum: "AVG" "95TH"
        :param granularity: Specify the preferred interval for each metric. If granularity is omitted from the request, only one metric is returned.  Enum: "5MIN" "HOUR" "DAY" "WEEK" "MONTH" "YEAR"
        :return: Standard HTTP status codes will be JSON.
        """
        headers = {'x-lsw-auth': self.config['API_KEY']}
        query_params = {
            'granularity': granularity,
            'aggregation': aggregation
        }
        out = utils.httpGet(self.config['API_URL'], '/bareMetals/v2/servers/{}/metrics/datatraffic?from={}&to={}'.format(serverId, date_from, date_to), query=utils.query(query_params), headers=headers)
        return out.json()

    def list_bandwidth_notification_settings(self,
                                             serverId: str,
                                             limit: int = 20,
                                             offset: int = 0) -> dict:
        """
        List all bandwith notification settings for this server.

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
        out = utils.httpGet(self.config['API_URL'], '/bareMetals/v2/servers/{}/notificationSettings/bandwidth?'.format(serverId), query=utils.query(query_params), headers=headers)
        return out.json()

    def create_bandwidth_notification_settings(self,
                                               serverId: str,
                                               frequency: str,
                                               threshold: str,
                                               unit: str) -> dict:
        """
        Create a new bandwidth notification setting for this server.

        :param serverId: The ID of a server.
        :param frequency: Frequency for the Bandwidth Notification.  Enum: "DAILY" "WEEKLY" "MONTHLY"
        :param threshold: Threshold Value for the Bandwidth Notification.
        :param unit: Unit for the Bandwidth Notification.  Enum: "Gbps" "Mbps"
        :return: Standard HTTP status codes will be JSON.
        """
        headers = {
            'x-lsw-auth': self.config['API_KEY'],
            'content-type': 'application/json'
        }
        data_params = {
            'frequency': frequency,
            'threshold': threshold,
            'unit': unit
        }
        out = utils.httpGet(self.config['API_URL'], '/bareMetals/v2/servers/{}/notificationSettings/bandwidth'.format(serverId), data=utils.query(data_params), headers=headers)
        return out.json()

    def delete_bandwidth_notification_setting(self,
                                              serverId: str,
                                              notificationSettingId: str) -> bool:
        """
        Remove a Bandwidth Notification setting for this server.

        :param serverId: The ID of a server.
        :param notificationSettingId: The ID of a notification setting.
        :return: Bool.
        """
        headers = {'x-lsw-auth': self.config['API_KEY']}
        out = utils.httpDelete(self.config['API_URL'], '/bareMetals/v2/servers/{}/notificationSettings/bandwidth/{}'.format(serverId, notificationSettingId), headers=headers)
        return True if out.status_code == 204 else False

    def show_bandwidth_notification_setting(self,
                                            serverId: str,
                                            notificationSettingId: str) -> dict:
        """
        Get a bandwidth notification setting for this server.

        :param serverId: The ID of a server.
        :param notificationSettingId: The ID of a notification setting.
        :return: Standard HTTP status codes will be JSON.
        """
        headers = {'x-lsw-auth': self.config['API_KEY']}
        out = utils.httpGet(self.config['API_URL'], '/bareMetals/v2/servers/{}/notificationSettings/bandwidth/{}'.format(serverId, notificationSettingId), headers=headers)
        return out.json()

    def update_bandwidth_notification_setting(self,
                                              serverId: str,
                                              notificationSettingId: str,
                                              frequency: str,
                                              threshold: str,
                                              unit: str) -> dict:
        """
        Update an existing bandwidth notification setting for this server.

        :param serverId: The ID of a server.
        :param notificationSettingId: The ID of a notification setting.
        :param frequency: Frequency for the Bandwidth Notification.  Enum: "DAILY" "WEEKLY" "MONTHLY"
        :param threshold: Threshold Value for the Bandwidth Notification.
        :param unit: Unit for the Bandwidth Notification.  Enum: "Gbps" "Mbps"
        :return: Standard HTTP status codes will be JSON.
        """
        headers = {
            'x-lsw-auth': self.config['API_KEY'],
            'content-type': 'application/json'
        }
        data_params = {
            'frequency': frequency,
            'threshold': threshold,
            'unit': unit
        }
        out = utils.httpPut(self.config['API_URL'], '/bareMetals/v2/servers/{}/notificationSettings/bandwidth/{}'.format(serverId, notificationSettingId), query=utils.query(data_params), headers=headers)
        return out.json()

    def list_datatraffic_notification_settings(self,
                                               serverId: str,
                                               limit: int = 20,
                                               offset: int = 0) -> dict:
        """
        List all datatraffic notification settings for this server.

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
        out = utils.httpGet(self.config['API_URL'], '/bareMetals/v2/servers/{}/notificationSettings/datatraffic?'.format(serverId), query=utils.query(query_params), headers=headers)
        return out.json()

    def create_datatraffic_notification_settings(self,
                                                 serverId: str,
                                                 frequency: str,
                                                 threshold: str,
                                                 unit: str) -> dict:
        """
        Create a new datatraffic notification setting for this server.

        :param serverId: The ID of a server.
        :param frequency: Frequency for the Datatraffic Notification. Enum: "DAILY" "WEEKLY" "MONTHLY"
        :param threshold: Threshold Value for the Datatraffic Notification.
        :param unit: Unit for the Datatraffic Notification. Enum: "MB" "GB" "TB"
        :return: Standard HTTP status codes will be JSON.
        """
        headers = {
            'x-lsw-auth': self.config['API_KEY'],
            'content-type': 'application/json'
        }
        data_params = {
            'frequency': frequency,
            'threshold': threshold,
            'unit': unit
        }
        out = utils.httpPost(self.config['API_URL'], '/bareMetals/v2/servers/{}/notificationSettings/datatraffic'.format(serverId), data=utils.payload(data_params), headers=headers)
        return out.json()

    def delete_datatraffic_notification_setting(self,
                                                serverId: str,
                                                notificationSettingId: str) -> bool:
        """
        Delete the given datatraffic notification setting for this server.

        :param serverId: The ID of a server.
        :param notificationSettingId: The ID of a notification setting.
        :return: Bool.
        """
        headers = {'x-lsw-auth': self.config['API_KEY']}
        out = utils.httpDelete(self.config['API_URL'], '/bareMetals/v2/servers/{}/notificationSettings/datatraffic/{}'.format(serverId, notificationSettingId), headers=headers)
        return True if out.status_code == 204 else False

    def show_datatraffic_notification_setting(self,
                                              serverId: str,
                                              notificationSettingId: str) -> dict:
        """
        Get a datatraffic notification setting for this server.

        :param serverId: The ID of a server.
        :param notificationSettingId: The ID of a notification setting.
        :return: Standard HTTP status codes will be JSON.
        """
        headers = {'x-lsw-auth': self.config['API_KEY']}
        out = utils.httpGet(self.config['API_URL'], '/bareMetals/v2/servers/{}/notificationSettings/datatraffic/{}'.format(serverId, notificationSettingId), headers=headers)
        return out.json()

    def update_datatraffic_notification_setting(self,
                                                serverId: str,
                                                notificationSettingId: str,
                                                frequency: str,
                                                threshold: str,
                                                unit: str) -> dict:
        """
        Update an existing datatraffic notification setting for this server.

        :param serverId: The ID of a server.
        :param notificationSettingId: The ID of a notification setting.
        :param frequency: Frequency for the Datatraffic Notification.  Enum: "DAILY" "WEEKLY" "MONTHLY"
        :param threshold: Threshold Value for the Datatraffic Notification.
        :param unit: Unit for the Datatraffic Notification.  Enum: "MB" "GB" "TB"
        :return: Standard HTTP status codes will be JSON.
        """
        headers = {
            'x-lsw-auth': self.config['API_KEY'],
            'content-type': 'application/json'
        }
        data_params = {
            'frequency': frequency,
            'threshold': threshold,
            'unit': unit
        }
        out = utils.httpPut(self.config['API_URL'], '/bareMetals/v2/servers/{}/notificationSettings/datatraffic/{}'.format(serverId, notificationSettingId), data=utils.payload(data_params), headers=headers)
        return out.json()

    def inspect_ddos_notification_settings(self,
                                           serverId: str) -> dict:
        """
        Show all DDoS Protection related notification settings for this server. These settings control if you want to be notified via email in case a DDoS was mitigated.

        :param serverId: The ID of a server.
        :return: Standard HTTP status codes will be JSON.
        """
        headers = {'x-lsw-auth': self.config['API_KEY']}
        out = utils.httpGet(self.config['API_URL'], '/bareMetals/v2/servers/{}/notificationSettings/ddos'.format(serverId), headers=headers)
        return out.json()

    def update_ddos_notification_settings(self,
                                          serverId: str,
                                          nulling: str = None,
                                          scrubbing: str = None) -> bool:
        """
        Update your DDoS notification settings for this server.

        :param serverId: The ID of a server.
        :param nulling: Enable or disable email notifications for nulling events.  Enum: "ENABLED" "DISABLED"
        :param scrubbing: Enable or disable email notifications for nulling events. Enum: "ENABLED" "DISABLED"
        :return: Bool.
        """
        headers = {
            'x-lsw-auth': self.config['API_KEY'],
            'content-type': 'application/json'
        }
        data_params = {
            'nulling': nulling,
            'scrubbing': scrubbing
        }
        out = utils.httpPut(self.config['API_URL'], '/bareMetals/v2/servers/{}/notificationSettings/ddos'.format(serverId), data=utils.payload(data_params), headers=headers)
        return True if out.status_code == 204 else False

    def power_cycle_server(self,
                           serverId: str) -> bool:
        """
        Powercyle the server.

        :param serverId: The ID of a server.
        :return: Bool.
        """
        headers = {'x-lsw-auth': self.config['API_KEY']}
        out = utils.httpPost(self.config['API_URL'], '/bareMetals/v2/servers/{}/powerCycle'.format(serverId), headers=headers)
        return True if out.status_code == 204 else False

    def show_power_status(self,
                          serverId: str) -> dict:
        """
        The server can either be ON or OFF. Servers can be powered on or off by using the respective /powerOn and /powerOff API calls. In addition servers can also be rebooted using the /powerCycle API call.

        The pdu object describes the power status from the power distribution unit (PDU) point of view. If your server is connected to multiple PDU ports the status property will report on if at least one PDU port has power.
        The ipmi object describes the power status by quering the remote management interface of your server.
        Note that pdu.status can report on but your server can still be powered off if it was shutdown via IPMI for example.

        :param serverId: The ID of a server.
        :return: Standard HTTP status codes will be JSON.
        """
        headers = {'x-lsw-auth': self.config['API_KEY']}
        out = utils.httpGet(self.config['API_URL'], '/bareMetals/v2/servers/{}/powerInfo'.format(serverId), headers=headers)
        return out.json()

    def power_off_server(self,
                         serverId: str) -> bool:
        """
        Power off the given server.

        :param serverId: The ID of a server.
        :return: Bool.
        """
        headers = {'x-lsw-auth': self.config['API_KEY']}
        out = utils.httpPost(self.config['API_URL'], '/bareMetals/v2/servers/{}/powerOff'.format(serverId), headers=headers)
        return True if out.status_code == 204 else False

    def power_on_server(self,
                        serverId: str) -> bool:
        """
        Power on the given server.

        :param serverId: The ID of a server.
        :return: Bool.
        """
        headers = {'x-lsw-auth': self.config['API_KEY']}
        out = utils.httpPost(self.config['API_URL'], '/bareMetals/v2/servers/{}/powerOn'.format(serverId), headers=headers)
        return True if out.status_code == 204 else False

    def list_operating_system(self,
                              limit: int = 20,
                              offset: int = 0,
                              controlPanelId: str = None) -> dict:
        """
        An id of a operating system can be supplied when (re)installing a dedicated server (for more information on how to install dedicated servers via the API refer to the API documentation).

        :param limit: Limit the number of results returned.
        :param offset: Return results starting from the given offset.
        :param controlPanelId: Filter operating systems by control panel id.
        :return: Standard HTTP status codes will be JSON.
        """
        headers = {'x-lsw-auth': self.config['API_KEY']}
        query_params = {
            'limit': limit,
            'offset': offset,
            'controlPanelId': controlPanelId
        }
        out = utils.httpGet(self.config['API_URL'], '/bareMetals/v2/operatingSystems?', query=utils.query(query_params), headers=headers)
        return out.json()

    def show_operating_system(self,
                              operatingSystemId: str,
                              controlPanelId: str) -> dict:
        """
        This detailed information shows default options when installing the given operating system on a dedicated server.

        For some operating systems these defaults can be adjusted when making the POST request to /install. If the configurable parameter is true these defaults can be adjusted by the client.

        :param operatingSystemId: Credential type.
        :param controlPanelId: The Control Panel ID
        :return: Standard HTTP status codes will be JSON.
        """
        headers = {'x-lsw-auth': self.config['API_KEY']}
        out = utils.httpGet(self.config['API_URL'], '/bareMetals/v2/operatingSystems/{}?operatingSystemId={}'.format(operatingSystemId, controlPanelId), headers=headers)
        return out.json()

    def list_control_panels_by_os(self,
                                  operatingSystemId: str,
                                  limit: int = 20,
                                  offset: int = 0) -> dict:
        """
        An id of a control panel can be supplied when (re)installing a dedicated server (for more information on how to install dedicated servers via the API refer to the API documentation).

        :param operatingSystemId: Credential type
        :param limit: Limit the number of results returned.
        :param offset: Return results starting from the given offset.
        :return: Standard HTTP status codes will be JSON.
        """
        headers = {'x-lsw-auth': self.config['API_KEY']}
        query_params = {
            'limit': limit,
            'offset': offset
        }
        out = utils.httpGet(self.config['API_URL'], '/bareMetals/v2/operatingSystems/{}/controlPanels?'.format(operatingSystemId), query=utils.query(query_params), headers=headers)
        return out.json()

    def list_control_panels(self,
                            limit: int = 20,
                            offset: int = 0,
                            operatingSystemId: str = None) -> dict:
        """
        An id of a control panel can be supplied when (re)installing a dedicated server (for more information on how to install dedicated servers via the API refer to the API documentation).

        Not all operating systems support all control panels. Some operating systems do not allow for installation of a control panel. To filter the list of control panels which are supported for an operating system use the operatingSystemId query string parameter to filter this list.

        :param limit: Limit the number of results returned.
        :param offset: Return results starting from the given offset.
        :param operatingSystemId: Filter control panels by operating system id.
        :return: Standard HTTP status codes will be JSON.
        """
        headers = {'x-lsw-auth': self.config['API_KEY']}
        query_params = {
            'limit': limit,
            'offset': offset,
            'operatingSystemId': operatingSystemId
        }
        out = utils.httpGet(self.config['API_URL'], '/bareMetals/v2/controlPanels?'.format(operatingSystemId), query=utils.query(query_params), headers=headers)
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
        out = utils.httpGet(self.config['API_URL'], '/bareMetals/v2/rescueImages?', query=utils.query(query_params), headers=headers)
        return out.json()
