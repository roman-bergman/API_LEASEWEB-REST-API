## Install

For install module use pip package manager.
```python
pip3 install --upgrade leasewebrestapi
```

## Usage

### Authentication
For authentication your need using parameter `API_KEY` in config or set the parameter when calling API() class.

You can generate API keys in the [Customer Portal](https://auth.leaseweb.com/loginCustomer).

#### Example

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







### API SUPPORT

See the following sections to view the supported API functions:

- [DedicatedServers](./docs/DedicatedServersAPI.md) - Fully manage your dedicated servers.
- [Invoices](./docs/InvoicesAPI.md) - Get your invoice data with this Invoice API.

