## Errors

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

### Invoices
- `list_invoices()` - This endpoint will return an overview of all the invoices for the customer.
- `pro_forma()` - This endpoint will return an overview of contract items that will be invoiced as of the 1st of the upcoming month.
- `inspect_invoice()` - This endpoint will return a single invoice for the customer.

