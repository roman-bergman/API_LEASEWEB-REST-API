## Errors

The API uses standard HTTP status codes to indicate the success or failure of the API call. The response will be JSON. Most APIs use the following format:

```json
{
"errorCode" : "APP00800",
"errorMessage" : "The connection with the DB cannot be established.",
"correlationId" : "550e8400-e29b-41d4-a716-446655440000",
"userMessage" : "Cannot handle your request at the moment. Please try again later.",
"reference" : "http://developer.leaseweb.com/errors/APP00800"
}
```


## Authentication
For authentication your need using parameter `API_KEY` in config or set the parameter when calling API() class.

You can generate API keys in the [Customer Portal](https://auth.leaseweb.com/loginCustomer).

### Example

#### When calling API() class:
```python
import leasewebrestapi

api = leasewebrestapi.API(API_KEY='<some api key>')
```

#### In config:
```python
import leasewebrestapi

api = leasewebrestapi.API()
api.config['API_KEY'] = '<some api key>'
```


## Available functions

### Getting Started
- `list_servers()` - List your Dedicated Servers.
- `get_server()` - Use this API to get information about a single server.
- `update_server()` - Update the reference for a server.
- `show_hardware_information()` - This information is generated when running a hardware scan for your server. A hardware scan collects hardware information about your system.

### IPs
- `list_ips()` - List all IP Addresses associated with this server. Optionally filtered.
- `show_ip()` - Get a single IP address associated with this server.
- `update_ip()` - Update the reverse lookup or DDoS detection profile for the ip address.
- `null_route_ip()` - Null the given IP address. It might take a few minutes before the change is propagated across the network.
- `remove_null_route_ip()` - Remove an existing null route for the given IP address. It might take a few minutes before the change is propagated across the network.
- `show_null_route_history()` - Show all null route history for any ips associated with this server.

### Network Interfaces
- `list_network_interfaces()` - List all network interfaces for this server, including their current status.
- `close_all_network_interfaces()` - Close all network interfaces for this server.
- `open_all_network_interfaces()` - Open all network interfaces of this server.
- `show_network_interface_by_type()` - List the network interfaces of the given type of this server, including their status.
- `close_network_interface_by_type()` - Close all network interfaces of this server.
- `open_network_interface_by_type()` - Open all network interfaces of the given type for this server.

### Private Networks
- `delete_server_from_private_network()` - Delete a server from a private network.
- `add_server_to_private_network()` - Add a server to private network.

### DHCP Leases
- `delete_dhcp_reservation()` - Delete a DHCP reservation.
- `list_dhcp_reservation()` - Please note that this will only show reservations for the public network interface.
- `create_dhcp_reservation()` - Create a DHCP reservation.

### Jobs
- `cancel_active_job()` - Cancel active job.
- `expire_active_job()` - Expiring an active job will not have any influence on the current state of the server and is merely an administrative action.
- `launch_hardware_scan()` - A hardware scan collects hardware related information from your server.
- `launch_installation()` - Install your server with an Operating System and optional Control Panel.
- `launch_ipmi_reset()` - A reset makes sure that your IPMI interface of your server is compatible with Leaseweb automation.
- `list_jobs()` - List all jobs for this server.
- `show_job()` - Get a single job for this server. 
- `launch_resque_mode()` - Rescue mode allows you to trouble shoot your server in case your installed operating system is no longer reachable.

### Credentials
- `list_credentials()` - The credentials API allows you to store usernames and passwords securely.
- `create_credentials()` - Password will NOT be updated on the server. The ability to update credentials is for convenience only. It provides a secure way to communicate passwords with Leaseweb engineers in case support is required.
- `list_credentials_by_type()` - List all the credentials filtered by the specified type that are associated with this server.
- `delete_user_credentials()` - This action is purely administrative and will only remove the username and password associated with this resource from our database.
- `show_user_credentials()` - View the password for the given credential, identified by type and username. Auto generated credentials (during a re-install, rescue mode or ipmi reset can be found here).
- `update_user_credentials()` - The usernames or types cannot be changed. In order to change those remove this credentials and create a new one.

### Metrics
- `show_bandwidth_metrics()` - At this moment only bandwidth information for the public interface is supported.
- `show_datatraffic_metrics()` - At this moment only bandwidth information for the public interface is supported.

### Notification Settings
- `list_bandwidth_notification_settings()` - List all bandwidth notification settings for this server. 
- `create_bandwidth_notification_settings()` - Create a new bandwidth notification setting for this server.
- `delete_bandwidth_notification_setting()` - Remove a Bandwidth Notification setting for this server.
- `show_bandwidth_notification_setting()` - Get a bandwidth notification setting for this server.
- `update_bandwidth_notification_setting()` - Update a bandwidth notification setting.
- `list_datatraffic_notification_settings()` - List all datatraffic notification settings for this server.
- `create_datatraffic_notification_settings()` - Create a new datatraffic notification setting for this server.
- `delete_datatraffic_notification_setting()` - Delete the given datatraffic notification setting for this server.
- `show_datatraffic_notification_setting()` - Get a datatraffic notification setting for this server.
- `update_datatraffic_notification_setting()` - Update an existing datatraffic notification setting for this server.
- `inspect_ddos_notification_settings()` - Show all DDoS Protection related notification settings for this server. These settings control if you want to be notified via email in case a DDoS was mitigated.
- `update_ddos_notification_settings()` - Update your DDoS notification settings for this server.

### Power
- `power_cycle_server()` - Powercyle the server.
- `show_power_status()` - Show power status.
- `power_off_server()` - Power off the given server.
- `power_on_server()` - Power on the given server.

### Operating Systems
- `list_operating_system()` - An id of a operating system can be supplied when (re)installing a dedicated server (for more information on how to install dedicated servers via the API refer to the API documentation).
- `show_operating_system()` - This detailed information shows default options when installing the given operating system on a dedicated server.
- `list_control_panels_by_os()` - An id of a control panel can be supplied when (re)installing a dedicated server (for more information on how to install dedicated servers via the API refer to the API documentation).

### Control Panels
- `list_control_panels()` - An id of a control panel can be supplied when (re)installing a dedicated server (for more information on how to install dedicated servers via the API refer to the API documentation).

### Rescue Images
- `rescue_images()` - Lists all Rescue Images which are available for launching a dedicated server into rescue mode.