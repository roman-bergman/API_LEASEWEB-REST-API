## INSTALL

For install module use pip package manager.
```python
pip3 install --upgrade leasewebrestapi
```


## AUTHENTICATION
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


## USAGE

To use the API, you need to generate an API key on the Leaseweb Customer Portal. See [Authentication section](#authentication).

API usage follows the pattern **api.<API_SERVICE>.<API_FUNCTION>**, where:
* **API_SERVICE** - API services offered by Leaseweb Services. For available services see [API SERVICES SUPPORT](#api-services-support).
* **API_FUNCTION** - Functions available for specific API_SERVICES. See [API FUNCTION SUPPORT](#api-function-support).

### Example:

Get Dedicated Servers List, single server info and hardware information for server.
```python
import leasewebrestapi

api = leasewebrestapi.API(API_KEY="<some_api_key>")

# get servers list
api.DedicatedServers.list_servers()

# get server info
api.DedicatedServers.get_server('<SERVER_ID>')

# get hardware info
api.DedicatedServers.show_hardware_information('<SERVER_ID>')
```

Get Invoice list and single invoice info.
```python
import leasewebrestapi

api = leasewebrestapi.API(API_KEY="<some_api_key>")

# get invoices list
api.Invoice.list_invoices()

# get single invoice info
api.Invoice.inspect_invoice('<INVOICE_ID>')
```


## API SERVICES SUPPORT

* DedicatedServers - Fully manage your dedicated servers.
* Invoice - Get your invoice data with this Invoice API.


## API FUNCTION SUPPORT

See the following sections to view the supported API functions:

- [DedicatedServers](./docs/DedicatedServersAPI.md) - Fully manage your dedicated servers.
- [Invoice](./docs/InvoicesAPI.md) - Get your invoice data with this Invoice API.

