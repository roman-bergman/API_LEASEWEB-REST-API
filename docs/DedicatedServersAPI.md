Dedicated Servers API supports the following features.


### Servers
- `list_servers()` - List your Dedicated Servers.
- `get_server()` - Use this API to get information about a single server.
- `update_server()` - Update the reference for a server.
- `show_hardware_information()` - This information is generated when running a hardware scan for your server. A hardware scan collects hardware information about your system.


### IPs
- `list_ips()` - List all IP Addresses associated with this server. Optionally filtered.
- `show_an_ip()` - Get a single IP address associated with this server.
- `update_an_ip()` - Update the reverse lookup or DDoS detection profile for the ip address.
- `show_null_route_history()` - Null the given IP address. It might take a few minutes before the change is propagated across the network.


### Network Interfaces
- `list_network_interfaces()` - 
- `show_a_network_interface()` -


### Private Networks
- `list_dhcp_reservation()` - 
- `list_jobs()` - 
- `show_a_job()` - 
- `list_credentials()` - 
- `list_credentials_by_type()` - 
- `show_user_credentials()` - 
- `show_bandwidth_metrics()` - 
- `show_datatraffic_metrics()` - 
- `list_bandwidth_notification_settings()` - 
- `show_a_bandwidth_notification_setting()` -
- `list_datatraffic_notification_settings()` - 
- `show_a_datatraffic_notification_setting()` - 
- `inspect_ddos_notification_settings()` -
- `show_power_status()` - 
- `list_operating_system()` - 
- `show_an_operating_system()` - 
- `list_control_panels_an_os()` - 
- `list_control_panels()` - 
- `rescue_images()` - 
- ``
### 


### Rescue Images
- `rescue_images()` - Lists all Rescue Images which are available for launching a dedicated server into rescue mode.